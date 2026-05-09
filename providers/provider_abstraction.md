# Provider abstraction — design

The `LLMProvider` interface is intentionally small. The hard work is in the *capability registry* and the *router*, not the adapters.

## Interface

```python
class LLMProvider:
    def chat(
        self,
        messages: list[dict],
        *,
        model: Optional[str] = None,
        temperature: float = 0.2,
        max_tokens: int = 1024,
        tools: Optional[list[dict]] = None,
        response_format: Optional[dict] = None,
        stream: bool = False,
        **kwargs,
    ) -> dict:
        """Returns: {text, tool_calls, usage, raw}."""

    def complete_text(self, prompt: str, *, system: str = "...", ...) -> str: ...
```

That's it. Streaming returns the raw provider iterator wrapped in the dict.

## Why messages-style as the canonical input

- Every modern provider speaks messages
- It maps 1:1 to OpenAI Chat Completions and to Anthropic's Messages API (with a small system-extraction step)
- It carries enough structure for tool calls and multimodal content blocks

## Why one `chat()` and not separate methods per family

- Adapters are picked by `info.name` inside `chat()` — no inheritance hierarchy to maintain
- New providers = a registry entry; no class to subclass

## Why `info.openai_compatible` matters

The OpenAI Chat Completions wire format is the **lingua franca** of the ecosystem. Most provider docs explicitly publish a "use the OpenAI SDK with our base URL" path. This means:

- Installing `openai` reaches ~17 of the 24 providers in this repo
- Capability tags carry the differences (tool calling, JSON mode, structured outputs)

## Why temperature is clamped

- MiniMax requires `temperature > 0`
- Some local servers reject `> 1.0`
- We normalize to `[0.0, 2.0]` then provider-specific ceilings in `_clamp_temperature`

## Errors

Typed in [`utilities/provider_errors.py`](../utilities/provider_errors.py):

- `ProviderNotConfigured` — env var missing
- `ProviderSDKMissing` — SDK not installed
- `ProviderUnsupportedCapability` — capability tag absent
- `ProviderRateLimited` — 429
- `ProviderAuth` — 401/403
- `ProviderTransient` — timeouts, 5xx
- `ProviderError` — base
- `ProviderRouterExhausted` — all chain entries failed

The router treats Configured/Auth/Capability/RateLimited/Transient as fall-throughable; everything else propagates.

## What this layer does not do

- **No prompt templating.** That's the agent's job. We pass `messages` through.
- **No retry beyond the router's first-success-wins.** Real retry policies (jittered backoff, deadline budgets) belong above this layer.
- **No streaming UI.** We return the raw stream when `stream=True`; you iterate.
- **No tool-protocol translation.** OpenAI tool schemas don't auto-convert to Anthropic's. If you need cross-provider tools, normalize in your agent code.
- **No spend tracking.** See [observability/cost_tracking.md](../observability/cost_tracking.md).

## Extending

To add a provider with a non-OpenAI-compatible API:

1. Add a `ProviderInfo(..., openai_compatible=False)` entry
2. Add a branch in `LLMProvider.chat()` that dispatches to a new `_chat_<name>(...)` adapter
3. Map provider exceptions in a `_map_<name>_exc(...)` helper
4. Document in [provider_matrix.md](provider_matrix.md), add `.env.example`, drop an example
