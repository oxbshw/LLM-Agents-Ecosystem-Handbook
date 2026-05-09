# Observability

You cannot ship what you cannot see. Three dimensions: **traces**, **metrics**, **evals**.

## What's here

- [tracing.md](tracing.md) — what to capture per run
- [spans.md](spans.md) — span model and naming
- [logging.md](logging.md) — structured logs that survive
- [cost_tracking.md](cost_tracking.md) — per-run, per-tool, per-task
- [latency_tracking.md](latency_tracking.md) — p50/p95/p99 + tail analysis
- [failure_analysis.md](failure_analysis.md) — debugging bad runs
- [dashboards.md](dashboards.md) — what to put on the wall

For evals, see [/evals](../evals/).

## Minimum bar before shipping

- [ ] Every run emits a trace
- [ ] Every tool call is a span with inputs, outputs, duration, cost
- [ ] Cost / latency / error dashboards exist
- [ ] Alerts on cost spike, error rate spike, repeated guardrail trips
- [ ] Traces survive process restart (durable backend)

## Tooling (vendor-neutral)

| Need | Options |
|---|---|
| Trace storage + UI | Langfuse, Arize Phoenix, LangSmith, Logfire, Honeycomb (via OTEL) |
| Standard | OpenTelemetry — most frameworks emit it now |
| Evals | Promptfoo, DeepEval, RAGAs, TruLens |
| Cost | Most managed observability tools track this; or roll your own from token counts |

The right answer is "instrument something" — the wrong answer is "we'll add it later."
