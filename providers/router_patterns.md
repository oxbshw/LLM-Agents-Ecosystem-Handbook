# Router patterns

Routing turns "use Provider X" into "use the right provider for this task, with fallbacks."

## Default chains

From [`utilities/provider_router.py`](../utilities/provider_router.py):

| Task class | Default chain |
|---|---|
| `default` | `openai → anthropic → openrouter` |
| `cheap` | `groq → deepseek → together → openrouter` |
| `fast` | `groq → cerebras → fireworks` |
| `reasoning` | `anthropic → openai → google → deepseek` |
| `long_context` | `google → anthropic → minimax → openai` |
| `vision` | `openai → google → anthropic → xai` |
| `local` | `ollama → lmstudio → vllm → llamacpp` |
| `research` | `perplexity → openai → anthropic` |

Override per task via env (`ROUTER_CHEAP="groq,deepseek"`) or constructor.

## Common patterns

### Pattern 1: cheap-first with hosted fallback
```python
from utilities.provider_router import ProviderRouter
router = ProviderRouter()
out = router.chat(messages, task_class="cheap")
# Tries Groq first; falls back if rate-limited or key missing.
```

### Pattern 2: local-first for privacy
```python
router = ProviderRouter(chains={
    "default": ["ollama", "lmstudio", "openai"],  # only fall back if local is down
})
out = router.chat(messages)
```

### Pattern 3: capability-filtered
```python
out = router.chat(
    messages,
    task_class="reasoning",
    constraints=["tool_calling", "vision"],   # drop providers missing either
)
```

### Pattern 4: per-step routing
Different steps of an agent often have different needs:

```python
plan      = router.chat(plan_msgs,    task_class="reasoning")
extract   = router.chat(extract_msgs, task_class="cheap")
summarize = router.chat(sum_msgs,     task_class="fast")
```

### Pattern 5: shadow / A-B
For evals, run two providers and diff:

```python
a = get_provider("openai").chat(msgs)
b = get_provider("anthropic").chat(msgs)
diff = compare(a["text"], b["text"])
```

### Pattern 6: budget-bounded
Wrap the router with a cost cap:

```python
spend = 0
def safe_chat(msgs, cap=0.05):
    global spend
    if spend > cap:
        return {"text": "[budget exceeded]"}
    out = router.chat(msgs, task_class="cheap")
    spend += estimate_cost(out)
    return out
```

The router *itself* doesn't enforce budgets — that belongs above it. See [observability/cost_tracking.md](../observability/cost_tracking.md).

## What the router is NOT

- It is **not** a load balancer. First-success-wins; no round-robin.
- It is **not** a circuit breaker. Add one in front if you need flap protection.
- It is **not** smart about cost or latency. It honors **chain order**. Order your chain by what you actually want.

## Failure handling

The router falls through on:

- `ProviderNotConfigured` (missing key)
- `ProviderAuth` (bad key)
- `ProviderUnsupportedCapability` (wrong tool for the job)
- `ProviderRateLimited` (429)
- `ProviderTransient` (timeouts, 5xx)

Everything else propagates — bugs in your code shouldn't be hidden behind a fallback.

## Inspecting decisions

```python
out = router.chat(messages, task_class="cheap")
print(out["_router"])            # {"provider_used": "...", "task_class": "...", "attempts": N}
print(router.last_attempts)      # [RouteAttempt(provider, success, error?), ...]
```

Pipe `last_attempts` into your traces ([observability/tracing.md](../observability/tracing.md)) so you can answer "why did this run pick provider X?" three months later.
