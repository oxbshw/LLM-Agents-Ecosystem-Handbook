# Eval design

How to design an eval suite that's actually useful.

## Three questions before you write a case

1. **What decision does this eval inform?** ("Should we ship?", "Did this prompt change help?", "Is this tool used correctly?")
2. **What's the ground truth?** Exact match, schema, rubric score, structured tool-call trace?
3. **Will this case still mean the same thing in 6 months?** Brittle cases churn the suite.

## Case shape

```jsonl
{"id":"reg-2026-04-12-001","input":{"task":"Summarize PR #312"},"expected":{"min_score":0.8,"must_cite":["#312"],"forbidden_tools":["gh.pr.merge"]},"tags":["regression","pr_summary"]}
```

Stick to JSONL — works with everything, diffs cleanly.

## Pass criteria

Three styles, pick per case:

| Style | When |
|---|---|
| **Exact / regex** | Structured outputs (JSON, tool-call sequences) |
| **Schema** | Outputs must conform to a Pydantic / JSON schema |
| **Rubric (LLM judge)** | Subjective quality (briefings, code review comments) |
| **Trace assertion** | "Called X before Y", "Never called Z" |

For LLM-judge: pin the judge model, version the rubric, sample-grade with humans periodically to detect judge drift.

## Coverage

A useful suite covers:

- The **golden path** (it must always work)
- The **edge cases** that broke things in the past (regression)
- The **adversarial cases** (injection, ambiguity, missing data)
- The **negative cases** (the agent should *refuse* / *ask*)

## Anti-patterns

- ❌ Cases written by the model being evaluated
- ❌ Suites with 1000 trivial cases and 0 hard ones
- ❌ Brittle string matches that change with model upgrades
- ❌ Using the production prompt as the eval prompt — judges contamination

## Workflow

1. Add cases when you fix a bug → regression case
2. Add cases when you spec a new feature → acceptance cases
3. Run on every PR → block on regression
4. Review the suite quarterly → kill dead cases
