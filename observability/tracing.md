# Tracing

A trace captures one agent run as a tree of spans. Without traces, debugging an agent is guessing.

## What to capture per run

| Field | Why |
|---|---|
| `run_id` | Stable correlation across logs / metrics / approvals |
| `agent` + `version` | Reproduce later |
| `user_id` (if any) | Per-user investigation |
| `task` (input summary) | Group similar runs |
| `started_at` / `ended_at` | Latency |
| `total_cost`, `total_tokens` | Cost analysis |
| `outcome` (success / refused / error) | Funnel analysis |
| Tree of spans | The actual debugging surface |

## What to capture per span

| Field | Why |
|---|---|
| `name` | Conventional naming (`tool.<name>`, `model.complete`, `skill.<name>`) |
| `inputs` | Reproduce step |
| `outputs` | Compare across runs |
| `duration_ms` | Latency hotspots |
| `cost` | Per-call accounting |
| `error` | Where it broke |
| `parent_id` | Tree structure |

## Span shapes (suggested)

```
run
├── plan
├── skill.research-summarizer
│   ├── tool.web_search
│   ├── tool.fetch_url
│   ├── tool.fetch_url
│   └── model.complete (draft)
├── guardrail.output (passed)
└── tool.write_file
```

## Sampling

- 100% sample for medium+ tools
- 100% for any guardrail trip or error
- Lower sampling acceptable for high-volume Low-risk steps

## Backends

OpenTelemetry has become the lingua franca. Most agent frameworks emit OTEL traces; pipe to whatever backend you already use (Langfuse, Phoenix, Honeycomb, Tempo, Datadog, …).

## Anti-patterns

- ❌ Capturing the whole prompt + whole completion in plaintext when there's PII — redact
- ❌ Async fire-and-forget — drop traces on shutdown
- ❌ Local-only traces in production — they vanish on restart
