# Logging

Logs complement traces — they're better for free-form investigation.

## Structured, always

JSON lines or another structured format. Plain text logs from agents become unsearchable in a week.

```json
{"ts":"2026-04-12T15:08:11Z","level":"info","run_id":"r-...","span":"tool.write_file","path":"src/api/orders.py","bytes":2840}
```

## Levels

- `debug` — everything; off by default in prod
- `info` — every tool call, every guardrail check
- `warn` — guardrail trips, retries, recoverable errors
- `error` — failed runs, unrecoverable errors

## Redact

Run a redactor at log boundary:

- Secret formats (PEM, JWT, common API key shapes)
- PII (when policy requires)
- Anything from a field marked `secret: true` in the tool schema

## Correlation

Every log line has `run_id`. Log lines from the same run group cleanly when grepping.

## Retention

- 30 days hot, 1 year cold for medium-volume agents
- Decision/incident logs: indefinitely
- Approval audit log: indefinitely + immutable storage
