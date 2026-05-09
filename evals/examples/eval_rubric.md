# Eval rubric (LLM-as-judge example)

For subjective outputs (briefings, code-review comments, summaries) where exact match doesn't apply.

## Judge model

- Model: pin a specific version (e.g., `claude-haiku-4-5-20251001`)
- Sample-grade with humans monthly to detect drift

## Dimensions (0–3 each)

| Dimension | 0 (bad) | 1 | 2 | 3 (excellent) |
|---|---|---|---|---|
| Correctness | Wrong / fabricated | Mostly right with errors | Right with minor issues | Fully correct |
| Coverage | Misses key points | Some key points | Most key points | All key points |
| Sources | Unsourced | Some sourced | Most sourced | All claims sourced + verified |
| Style fit | Off-tone | Wrong format | Mostly right | Matches voice + format perfectly |
| Brevity | Wall of text | Verbose | Reasonable | Tight |

## Total

Sum (0–15). Pass threshold per case (e.g., 12/15).

## Judge prompt template

```
You are evaluating an agent output. Be strict but fair.

Task: {{task}}
Output to evaluate:
---
{{output}}
---

Reference (if any): {{reference}}

Score each dimension 0–3, then total. Output JSON:
{
  "correctness": int, "coverage": int, "sources": int,
  "style": int, "brevity": int, "total": int,
  "notes": "one sentence on the biggest gap"
}
```

## Anti-bias

- Never put the model's own ID into the judge prompt
- Randomize order if comparing two outputs
- Re-run with a different judge model on disagreements > N points
