# Providers

LLM provider documentation, capability matrix, abstraction guide, and runnable examples for **24+ providers** across six families: frontier APIs, fast inference, marketplaces, enterprise clouds, specialty APIs, and local runtimes.

## What's here

- [provider_matrix.md](provider_matrix.md) — capability comparison
- [provider_abstraction.md](provider_abstraction.md) — `LLMProvider` interface, design rationale
- [model_selection_guide.md](model_selection_guide.md) — pick a model, not a brand
- [router_patterns.md](router_patterns.md) — fallback chains, task-class routing
- [cost_latency_matrix.md](cost_latency_matrix.md) — rough comparison (with caveats)
- [local_models.md](local_models.md) — Ollama, LM Studio, vLLM, llama.cpp, generic OpenAI-compatible
- [env_vars.md](env_vars.md) — every env var the abstraction reads
- [examples/](examples/) — minimal-runnable adapter examples per provider

## Provider families

| Family | Examples | Best for |
|---|---|---|
| **Frontier APIs** | OpenAI, Anthropic, Google Gemini | Reasoning, tool use, production agents |
| **Fast inference** | Groq, Cerebras, SambaNova | Low-latency, high-volume workloads |
| **Marketplaces** | OpenRouter, Together, Fireworks, DeepInfra | Model choice + routing |
| **Enterprise clouds** | Azure OpenAI, AWS Bedrock, Vertex AI | Compliance, governance |
| **Specialty** | xAI, Perplexity, Mistral, Cohere, DeepSeek, Hugging Face, Replicate, NVIDIA NIM, MiniMax | Domain or feature specialization |
| **Local runtimes** | Ollama, LM Studio, vLLM, llama.cpp, generic OpenAI-compatible | Privacy, cost, offline |

Most providers expose an OpenAI-compatible API. Installing the `openai` Python SDK is enough to reach **most** of them — you only switch the `base_url`. Anthropic and (stub) Bedrock / Replicate use their own paths.

## Quick start

```python
from utilities import get_provider, list_providers

# What's available?
for p in list_providers(family="fast"):
    print(p["name"], p["default_model"])

# Use a specific provider:
groq = get_provider("groq")
out = groq.chat(
    [{"role": "user", "content": "Summarize MCP in one sentence."}],
    model="llama-3.1-8b-instant",
)
print(out["text"])
```

Set `LLM_PROVIDER=groq` in your env to make it the default.

## Routing

```python
from utilities.provider_router import ProviderRouter

router = ProviderRouter()  # uses DEFAULT_CHAINS, env-overridable
out = router.chat(
    [{"role": "user", "content": "Summarize this PR in 3 bullets."}],
    task_class="cheap",      # tries: groq → deepseek → together → openrouter
)
print(out["_router"]["provider_used"])
```

📖 [router_patterns.md](router_patterns.md)

## Adding a new provider

1. Add a `ProviderInfo(...)` entry to [`utilities/provider_config.py`](../utilities/provider_config.py)
2. If it speaks OpenAI-compatible JSON, you're done — `chat()` works
3. If it has a unique API, add an adapter branch in [`utilities/llm_provider.py`](../utilities/llm_provider.py)
4. Add an env var to [.env.example](../.env.example) and [env_vars.md](env_vars.md)
5. Drop a minimal example in [examples/](examples/)
6. Update [provider_matrix.md](provider_matrix.md)

## What this layer doesn't do

- Track real-time pricing (use the providers' own pricing pages)
- Forward tool-call protocols across providers without conversion (each provider's tool format is canonical for that provider)
- Manage spend budgets (build that in [`safety/`](../safety/) or your runtime)

## Caveats

The provider landscape moves fast. Capability tags here are best-effort. Verify against current upstream docs before betting production traffic on any one tag.
