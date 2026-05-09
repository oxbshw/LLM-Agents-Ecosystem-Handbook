# Blueprint: Data analysis agent

## Use case
Given a dataset (CSV, parquet, SQL view), produce reproducible analyses, charts, and a written summary.

## Non-goals
- Owning a data pipeline (this agent reads, doesn't ingest)
- Free-text "vibes" answers — every chart must be reproducible

## Architecture

```
dataset + question
    │
    ▼
[scout]    ── schema, sample, missingness
    │
    ▼
[planner]  ── analysis plan with steps
    │
    ▼
[runner]   ── exec sandboxed Python (pandas/polars), chart writes
    │
    ▼
[narrator] ── summary linked to charts + script
```

## Tools

| Tool | Risk |
|---|---|
| `read_dataset` | Low |
| `run_python` (sandboxed, no network) | Medium |
| `write_chart` | Medium |
| `sql.query` (read-only DSN) | Medium |
| `sql.exec` (write) | High (approval) |

## Memory
- `MEMORY.md`: schema gotchas, dirty columns, agreed dimensions
- `memory/semantic/datasets/<name>.md`: per-dataset learnings

## Skills
- `dataset-profiler` (custom) — schema + missingness + outliers
- `report-writer` — narrate against a template

## Safety
- Sandbox the Python runner (no network, restricted FS)
- Read-only DB by default; writes require approval
- Don't echo PII in summaries

## Evals
- Reproducibility: re-run produces same charts
- Correctness: golden Q→A pairs on fixture datasets
- Refusal: when data is insufficient, says so
- Performance: large dataset within time/cost budget

## Deployment
- Worker with the runner sandbox (e.g., Firecracker / gVisor / restricted container)
- Outputs: HTML report, optionally Notion / S3

## Extensions
- Anomaly watch (scheduled, alert on deviation)
- Auto-doc datasets it's seen
- Hand-off to a viz-only agent for dashboards
