# Observability Layer

You cannot ship what you cannot see. Observability for agents has three dimensions: **traces**, **metrics**, and **evals**.

## Traces — what happened

A trace captures one agent run as a tree of spans:

```
run/
├── plan
├── tool: web_search (320ms, $0.0002)
├── tool: fetch_page (1.2s)
├── reasoning_step
├── tool: write_file (10ms)
└── final_answer
```

Each span has: name, inputs, outputs, duration, cost, errors. With this, you can answer:

- Why did the agent call this tool?
- Where did the run spend its time / tokens?
- Did it loop? Did it retry?
- What was the model's reasoning before the bad action?

📖 [observability/tracing.md](../observability/tracing.md), [observability/spans.md](../observability/spans.md)

## Metrics — how it's doing

Track and dashboard:

- **Cost per run** (and per task type)
- **Latency** (p50, p95, p99)
- **Tool-call rate** (calls per run, error rate per tool)
- **Loop length** (steps per run, capped vs natural)
- **Failure modes** (timeouts, refusals, guardrail trips)
- **Approval rate** (how often humans say no — a lagging signal of agent quality)

📖 [observability/cost_tracking.md](../observability/cost_tracking.md), [observability/dashboards.md](../observability/dashboards.md)

## Evals — does it still work

Tracing tells you what *happened*; evals tell you whether the agent is *good*. The handbook's eval section ([evals/](../evals/)) covers:

- **Regression evals** — does the agent still pass yesterday's tasks?
- **Tool-call evals** — does it pick the right tool with the right args?
- **Memory evals** — does it remember and not hallucinate?
- **MCP evals** — do integrations behave as expected?
- **Safety evals** — does it refuse / approve correctly?

## Tooling

Vendor-neutral options worth evaluating:

- **OpenTelemetry** — standard for traces, integrates with most frameworks
- **Langfuse, Arize Phoenix, LangSmith, Logfire** — managed agent observability
- **Promptfoo, DeepEval, RAGAs, TruLens** — eval harnesses

The point is *not* picking a tool — it's instrumenting *something* before you ship.
