# Prompt eval methods

Treat prompt changes like code changes: measure before merge.

## What to measure

| Dimension | How |
|---|---|
| **Task quality** | Rubric / LLM-judge / golden examples |
| **Tool-call correctness** | Trace assertions on tool selection + args |
| **Refusal correctness** | Did it refuse what it should + accept what it should? |
| **Format compliance** | Schema validation on output |
| **Cost** | Tokens × price per case |
| **Latency** | Wall time per case |
| **Robustness** | Same task with adversarial paraphrase / injection variants |

## A minimal eval loop

1. **Dataset** of N labelled cases (start with 30, grow to 200)
2. **Pinned model** + **pinned old prompt** (baseline)
3. **New prompt** under test
4. Run both; compare per-case scores
5. Promote new prompt only if it wins on quality without regressing safety / cost beyond a budget

## Datasets — keep three kinds

| Kind | Purpose |
|---|---|
| **Golden path** | Tasks the agent must always solve |
| **Edge cases** | Past bugs / hairy inputs |
| **Adversarial** | Injection, ambiguity, missing data |

## Judge selection

| Method | Best for | Caveat |
|---|---|---|
| Exact / regex / schema | Structured outputs | Brittle to harmless variation |
| LLM judge | Subjective quality | Drifts; sample-grade with humans monthly |
| Trace assertion | Tool calls / step shapes | Requires instrumentation |

When using an LLM judge:

- Pin its model + prompt version
- Don't use the same model that's being judged (collusion bias)
- Keep the judge prompt small + the rubric explicit ([evals/examples/eval_rubric.md](../evals/examples/eval_rubric.md))

## Reading the results

- **Single-case win/loss** is noise. Aggregate.
- **5–10% delta** is usually the signal threshold; below that, save it for cheaper changes.
- **Watch the tails.** A change that improves p50 but tanks p95 may be net-bad in production.
- **Cost-quality tradeoff** is real — track both.

## Common eval pitfalls

- ❌ Cases written by the model being evaluated (contamination)
- ❌ Re-using your production prompt as the judge prompt
- ❌ Tiny eval sets that miss the regression
- ❌ Judges drifting silently — re-grade humans periodically
- ❌ Letting "feels better" override numbers

## Versioning prompts

- Files in repo, diffable, dated
- Bump version on substantive change
- Tag the model + prompt version on every run trace
- Keep one rollback prompt around

## Cross-references

- [evals/eval_design.md](../evals/eval_design.md)
- [evals/examples/eval_rubric.md](../evals/examples/eval_rubric.md)
- [evals/regression_evals.md](../evals/regression_evals.md)
