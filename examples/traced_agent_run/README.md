# Traced agent run (example)

What a real trace looks like, in human-readable form. Use this as a mental model for what your tracing backend should show.

## Sample run

```
run  id=r-2026-04-12-001  agent=research-agent v0.4.2  outcome=ok
duration=18.4s  cost=$0.043  tokens_in=12,310  tokens_out=2,940
└── plan                          0.9s   $0.002
└── skill.research-summarizer    16.8s   $0.040
    ├── tool.web_search           0.4s   $0.000  q="MCP adoption 2026"
    ├── tool.web_search           0.5s   $0.000  q="MCP server catalog"
    ├── tool.fetch_url            1.2s   $0.000  url=https://… (allow-listed)
    ├── tool.fetch_url            0.9s   $0.000  url=https://…
    ├── tool.fetch_url            1.1s   $0.000  url=https://…
    ├── model.complete (cluster)  3.4s   $0.012  in=4.8k out=0.8k
    ├── model.complete (draft)    7.9s   $0.026  in=6.2k out=2.1k
    └── guardrail.output         0.05s   passed
└── tool.write_file              0.06s          path=briefing.md
```

## What's debuggable from this trace

- **Latency** — model.complete (draft) is half the run. Could try a smaller drafting model.
- **Cost** — same span dominates cost. Token budget is reasonable.
- **Quality signal** — three fetches, all allow-listed, no guardrail trips
- **Reproducibility** — the searches and URLs are captured

## What you'd add for production

- Per-span error / retry detail
- Prompt + completion (redacted) for the model spans, behind an "expand" affordance
- Cost / latency dashboards aggregating across many runs
- Alerting on outliers

## Sample as JSON

```json
{
  "run_id": "r-2026-04-12-001",
  "agent": {"name": "research-agent", "version": "0.4.2"},
  "outcome": "ok",
  "duration_ms": 18400,
  "cost_usd": 0.043,
  "spans": [
    {"name": "plan", "duration_ms": 900, "cost_usd": 0.002},
    {"name": "skill.research-summarizer", "children": [
      {"name": "tool.web_search", "args": {"q": "MCP adoption 2026"}},
      {"name": "tool.fetch_url", "args": {"url": "https://…"}, "outcome": "ok"},
      {"name": "model.complete", "label": "draft", "tokens_in": 6200, "tokens_out": 2100, "cost_usd": 0.026}
    ]},
    {"name": "guardrail.output", "outcome": "passed"},
    {"name": "tool.write_file", "args": {"path": "briefing.md"}}
  ]
}
```
