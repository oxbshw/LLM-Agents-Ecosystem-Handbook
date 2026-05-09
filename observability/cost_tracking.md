# Cost tracking

Agents are easy to make expensive. Treat cost as a first-class metric.

## What to track

| Granularity | Purpose |
|---|---|
| Per call (model + tool) | Find expensive steps |
| Per run | Per-task economics |
| Per task type | Compare workflows |
| Per user / tenant | Budget enforcement |
| Per agent / version | Regression detection on releases |

## Compute it

Cost per model span = tokens × per-token price (varies by model + tier). Most agent observability tools do this for you; if rolling your own, store the per-model price table in code, version it, and compute on ingest.

## Set ceilings

- **Per-run** ceiling — break the loop if exceeded
- **Per-user-day** ceiling — refuse politely once hit
- **Per-tenant-month** budget — alert before exceed

A cost ceiling is a guardrail. Wire it into the loop:

```python
if run.cost_usd > MAX_PER_RUN:
    raise GuardrailTrip("cost_ceiling")
```

## Dashboards

Useful charts:

- Cost per run, p50/p95/max, last 7d
- Cost per task type
- Cost per tool (which tools are expensive vs frequent vs both)
- Cost vs success rate (overpriced failures)
- Top 10 most expensive runs in last 24h (debug surface)

## Alerts

- Daily cost > N× 7-day average → page
- Single run > Mx normal max → page
- Token usage spike on a specific model (potential loop) → page

## Common surprises

- Long-context calls cost ~2-10× short-context (input tokens are not free)
- Tool retries multiply cost — guardrail loops save real money
- Vector retrieval embeddings add up; cache aggressively
- "Reasoning" / extended-thinking tokens count toward cost on most providers
