# Evals

Evaluations turn "the agent works" into "the agent works *and didn't regress*."

## What's here

- [eval_design.md](eval_design.md) — designing a useful eval suite
- [regression_evals.md](regression_evals.md) — pinning yesterday's wins
- [tool_call_evals.md](tool_call_evals.md) — does it pick + use tools correctly
- [memory_evals.md](memory_evals.md) — recall, no-fab, isolation
- [mcp_evals.md](mcp_evals.md) — integration tests for MCP
- [safety_evals.md](safety_evals.md) — refusals, approvals, injection resistance
- [examples/eval_dataset.jsonl](examples/eval_dataset.jsonl) — minimal dataset format
- [examples/eval_rubric.md](examples/eval_rubric.md) — LLM-as-judge rubric
- [examples/regression_eval_plan.md](examples/regression_eval_plan.md) — concrete plan

## Suites you should run

| Suite | Purpose | Cadence | Block release? |
|---|---|---|---|
| Regression | Yesterday's tasks still pass | Per-PR + nightly | Yes |
| Tool call | Right tool, right args, right order | Per-PR | Yes |
| Memory | Recall, no fabrication, isolation | Nightly | Yes |
| MCP | Integration determinism | Per server bump | Yes |
| Safety | Refuse, approve, resist injection | Per-PR | Yes (criticals = 100%) |
| Quality (LLM-judge) | Subjective quality | Nightly | Soft (trend-based) |

## Tooling

- Promptfoo, DeepEval, RAGAs, TruLens — popular harnesses
- LangSmith, Langfuse, Phoenix — managed eval + tracing
- DIY: a `pytest` runner over a JSONL dataset and a rubric — works fine for many teams

## Dataset hygiene

- Keep golden datasets versioned in git
- Tag every case (category, difficulty, source)
- Avoid contaminating the dataset with model output (model marks its own homework)
- Refresh quarterly

## Reporting

- Per-release: pass/fail per suite, deltas vs last release
- Failures triaged within 2 business days
- Regressions block the release

📖 [eval_design.md](eval_design.md)
