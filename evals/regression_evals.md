# Regression evals

Pin the wins. The single highest-ROI eval suite.

## What's a regression case?

A task the agent solved correctly that you don't want to break. Each one becomes one row.

## Source them from real life

- Bugs you fixed → regression case for the bug
- Features you shipped → one case per acceptance criterion
- User-flagged failures → case after fix
- Incidents → case as part of postmortem

## Structure

```jsonl
{"id":"reg-2026-04-12-001",
 "input":{"task":"Summarize PR #312, link to base ref"},
 "expected":{"must_include":["#312","base ref"],"forbidden_tools":["gh.pr.merge"],"max_steps":12},
 "tags":["pr_summary","golden_path"]}
```

## Run

- On every PR, in CI
- Nightly against `main`
- Per-release on the candidate

## Pass policy

- Hard fail: any regression case that previously passed
- Soft fail: rubric score down by > X%

A regression on the golden-path set blocks release. Period.

## Maintenance

- Cases with 100% pass for 6 months → keep but de-prioritize in CI runtime
- Cases that flake → fix the flake, don't ignore
- Quarterly review: prune duplicates, re-tag

## Folder layout

```
evals/
├── datasets/
│   ├── regression.jsonl
│   ├── tool_calls.jsonl
│   ├── memory.jsonl
│   └── safety.jsonl
├── rubrics/
│   └── briefing.md
└── runs/
    └── 2026-04-12/
        └── report.md
```
