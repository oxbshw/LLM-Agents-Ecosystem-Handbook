# Prompt evals

A focused eval suite for *prompt changes* — separate from the broader regression suite.

## Why a dedicated suite

Prompt changes touch every agent run. A poor change can quietly regress quality, cost, or safety. The signal/noise on a generic eval is too low to catch small but real shifts.

## Structure

```
evals/datasets/prompt_evals.jsonl
evals/rubrics/prompt_eval_rubric.md
```

## Cases to keep

| Class | Why |
|---|---|
| Golden 5 | The five tasks the agent must always do well |
| Style adherence | Output matches the documented voice / format |
| Refusal correctness | Refuses what it should + accepts what it should |
| Tool selection under noise | With distractor tools present, picks the right one |
| Adversarial input | Treats tool/RAG output as data, not instruction |
| Ambiguity handling | Asks for clarification rather than guessing |
| Brevity / length compliance | Honors the contract's length cap |

10–30 cases is enough to start; grow with each prompt iteration.

## Workflow on a prompt change

1. Run the suite on the current prompt — record baseline
2. Apply the prompt change
3. Re-run the suite
4. Diff per-case results
5. Promote the change if:
   - Quality wins on aggregate AND no critical refusal regresses
   - Cost stays within budget (allow ±10% by default)
   - Latency stays within budget

## Pass thresholds

- Critical refusals: 100% (no tolerance)
- Style adherence: ≥ 90% (style failures don't block, but track)
- Tool selection under noise: ≥ 95%
- Adversarial: 100% on documented vectors
- Brevity: contract met on ≥ 90% of cases

## What "the same case" means

Pin:
- Provider + model id
- Sampling parameters (temperature, max_tokens, etc.)
- Random seed if available

Compare prompts by changing **one variable**. If you bump the model AND change the prompt, you can't tell which won.

## Cross-references

- [eval_design.md](eval_design.md) — overall eval design
- [examples/eval_rubric.md](examples/eval_rubric.md) — rubric template
- [`prompt_engineering/prompt_eval_methods.md`](../prompt_engineering/prompt_eval_methods.md) — methods + pitfalls
