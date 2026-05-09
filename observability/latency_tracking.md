# Latency tracking

Latency budget = user patience. Track p50, p95, p99 — and look at the tail.

## Measure

Per-span and per-run:

- `time_to_first_token` (model spans)
- `total_duration` (run)
- `tool_wait` (sum of tool durations)
- `model_wait` (sum of model durations)

## Where time goes (typical agent run)

```
total
├── model wait        ~30–60%
├── tool wait         ~30–60%
└── overhead           ~5%
```

If overhead exceeds 10%, look at: trace export, guardrail compute, retry backoff.

## Tail analysis

p99 hides the worst cases. Always:

- Look at the slowest 10 runs in the last day
- Group by error / refusal / success — slow refusals are a UX bug

## Speedups (in order of typical payoff)

1. **Don't make the call** — caching, smarter loop control
2. **Parallelize independent tool calls** — most frameworks support it
3. **Use a smaller model** for the easy steps (planning, classification)
4. **Stream** to the user when possible
5. **Cache** retrieval / embeddings
6. **Pre-warm** any cold paths

## Dashboards

- Latency p50/p95/p99 over time
- Latency per task type
- Latency vs success
- Slowest tool calls in last 24h
