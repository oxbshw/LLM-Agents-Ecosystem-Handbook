# Regression eval plan (example)

Concrete plan for an agent in production. Adapt the numbers.

## Goal
Catch regressions before they reach users. Pin yesterday's wins.

## Suites
| Suite | Cases | Cadence | Block? |
|---|---|---|---|
| `regression.jsonl` | 60 | Per PR + nightly | Yes |
| `tool_calls.jsonl` | 25 | Per PR | Yes |
| `memory.jsonl` | 20 | Nightly | Yes |
| `safety.jsonl` | 30 (incl. injection) | Per PR | Yes (criticals 100%) |
| Quality (LLM-judge) | 40 | Nightly | Soft |

## Dataset growth
- Every fixed bug → 1 case
- Every new feature → 1–3 acceptance cases
- Every red-team finding → 1 case

## Pass thresholds
- Regression: 100% on golden-path subset; ≥ 95% overall
- Tool-call: ≥ 95%
- Memory: recall ≥ 95%, no-fab 100%, isolation 100%
- Safety: criticals 100%, overall ≥ 95%
- Quality: rolling avg score not down > 5% week-over-week

## On failure
- Hard fail (block release): regression, safety criticals, memory isolation
- Soft fail (file issue, ship anyway with sign-off): quality dip, single new tool-call edge

## Reporting
- Per run: report at `evals/runs/<release>/report.md`
- Include: pass rate per suite, deltas vs last release, per-case failure detail
- Archive forever; cheap and useful for trends
