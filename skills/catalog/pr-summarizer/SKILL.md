---
name: pr-summarizer
description: Use when opening a PR — produces a clean PR description (what / why / how to verify / risks) from a branch diff against base.
version: 0.1.0
status: experimental
risk: low
tags: [engineering, read-only, writes-files]
---

# PR Summarizer

## When to use
- Just before opening a PR
- After force-pushing a substantive update to an existing PR (refresh description)

## When NOT to use
- Drafts the user is still iterating on (the summary will go stale immediately)
- Massive diffs (> 1000 lines) — ask the user to scope first

## Inputs
| Name | Type | Required | Notes |
|---|---|---|---|
| `base` | string | no | default `origin/main` |
| `branch` | string | no | default current `HEAD` |

## Outputs
A markdown PR body with sections: **Summary**, **Why**, **How tested**, **Risks**, **Linked**.

## Workflow
1. `git diff <base>...HEAD --stat` and `git log <base>..HEAD --oneline` to see scope
2. `git diff <base>...HEAD` for content
3. Group changes by area (one bullet per logical concern, not per file)
4. Pull "why" from commit messages + linked tickets if mentioned
5. Identify test artifacts touched; surface as **How tested** (or flag if none)
6. Risks: any High-risk paths touched? auth, billing, migrations? mention.
7. Linked: parse `Fixes #` / `Refs #` from commits

## References
- [`references/pr-template.md`](references/pr-template.md)

## Success criteria
- Description ≤ 25 lines
- Every "why" claim is supported by a commit message or visible in the diff
- Risks section honest about unknowns ("untested in production data shape")

## Failure modes
- No commit messages worth quoting → "Why" sourced from diff only; flag this
- Diff touches secrets / `.env*` → STOP and surface; PR shouldn't include them
