# Design: Provider Router (example, filled — meta)

**Author:** handbook
**Date:** 2026-05-09
**Status:** accepted (shipped in this handbook v1.0.1)

## Background
Originally the abstraction supported 3 providers (OpenAI, Anthropic, MiniMax). The 2026 ecosystem is much larger — frontier APIs, fast inference, marketplaces, enterprise clouds, specialty providers, and local runtimes — and users want both *vendor neutrality* and *per-task routing*.

## Goals
- Support 24+ providers via a single `LLMProvider` interface
- Route by task class (cheap / fast / reasoning / vision / long-context / local)
- Fall back when a provider is unavailable
- Avoid forcing every provider's SDK as a hard dependency
- Preserve the existing `complete()` API for backwards compatibility

## Non-goals
- Tracking real-time pricing
- Cross-provider tool-protocol translation
- Spend budgeting (lives above this layer)

## Proposed design

### Layers
```
utilities/
├── provider_config.py     # capability registry (data)
├── llm_provider.py        # LLMProvider interface + adapters
├── provider_router.py     # task-class routing + fallback
└── provider_errors.py     # typed error hierarchy
```

### Capability model
Each provider has a `ProviderInfo(name, family, capabilities, openai_compatible, ...)`. Capabilities are tags: `chat`, `streaming`, `tool_calling`, `structured_outputs`, `json_mode`, `vision`, `embeddings`, `rerank`, `long_context`, `local`.

### Adapters
- OpenAI-compatible HTTP path covers ~17 providers (set `base_url`, ship the `openai` SDK)
- Anthropic uses its own SDK + Messages API
- Bedrock / Replicate documented as stubs (not auto-implemented)

### Router
`DEFAULT_CHAINS` for `default / cheap / fast / reasoning / long_context / vision / local / research`. Env-overridable (`ROUTER_CHEAP=...`). Falls through on `ProviderNotConfigured`, `ProviderAuth`, `ProviderUnsupportedCapability`, `ProviderRateLimited`, `ProviderTransient`. Other errors propagate.

## Alternatives considered
- **One adapter per provider with an inheritance hierarchy** — too much code for what the registry achieves; rejected.
- **Single hosted gateway** (LiteLLM-style) — adds a dependency + opinion; we wanted the lightest possible surface that works locally.
- **Forcing all SDKs in `requirements.txt`** — bloated; we use lazy imports.

## API
```python
from utilities import get_provider
from utilities.provider_router import ProviderRouter

p = get_provider("groq")
out = p.chat([...], model="llama-3.1-8b-instant")

r = ProviderRouter()
out = r.chat([...], task_class="cheap")
```

## Failure modes
- Provider missing key → `ProviderNotConfigured`; router skips
- Provider rate-limited → `ProviderRateLimited`; router falls through
- Provider 5xx / timeout → `ProviderTransient`; router falls through
- Capability missing → `ProviderUnsupportedCapability`; router falls through
- All chain entries fail → `ProviderRouterExhausted`

## Performance
- Startup: lazy SDK imports; no overhead for unused providers
- Routing decision: O(N) over chain; trivial
- Latency dominated by network, not abstraction

## Security
- No keys in code; all via env
- No per-call telemetry to external services
- Errors include status hints but not credentials

## Rollout
Already shipped (v1.0.1). Provider docs in [`/providers`](../../providers/), examples per provider, ecosystem-wide adoption guidance in `provider_matrix.md`.

## Risks
- Capability tags drift with the ecosystem → marked as best-effort, hedged in docs
- Router decisions hidden from traces → mitigated by `_router` debug field on every response
- Cost runaway in fallback storms → budget caps belong above this layer

## Open questions
- Should we ship a `LiteLLM` adapter as one of the providers? (post-1.0.1, low priority)
- Streaming response shape — current API returns dict with `stream=True` flag; consider an iterator wrapper
