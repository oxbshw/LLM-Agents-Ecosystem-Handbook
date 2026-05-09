---
name: repo-auditor
description: Use before opening a PR to audit the changes for stale comments, unused imports, missing tests, and inconsistencies with neighboring code.
version: 0.1.0
---

# Repo Auditor

## When to use
- After making code edits, before `git commit` or PR open
- After resolving merge conflicts
- When the user asks "is this PR ready?"

## When NOT to use
- During exploration / read-only work
- For purely formatting changes (lint/format already covers it)

## Inputs
| Name | Type | Required | Notes |
|---|---|---|---|
| `base` | string | no | base ref (default `origin/main`) |
| `paths` | list | no | restrict to specific paths |

## Workflow
1. **Diff**: `git diff <base>...HEAD --name-only` and `git diff <base>...HEAD`
2. **For each changed file**: load `references/audit-checklist.md` and walk it
3. **Check tests**: any new public function without a corresponding test → flag
4. **Check imports**: unused imports / missing imports → flag
5. **Check style fit**: does the new code match neighboring code's idioms?
6. **Check docs**: did this change require an `AGENTS.md` / `MEMORY.md` / README update? → flag if missed
7. **Produce report**: structured output (see Outputs)

## References
- [`references/audit-checklist.md`](references/audit-checklist.md)

## Outputs
```markdown
## Audit report
- ✅ {{N}} files reviewed
- 🟡 {{N}} warnings
- 🔴 {{N}} blockers

### Blockers
- {{file:line}} — {{issue}}

### Warnings
- {{file:line}} — {{issue}}
```

## Success criteria
- 0 blockers (PR can open) OR
- All blockers explicitly acknowledged by user

## Failure modes
- Diff too large (> 1k lines) → ask user to scope
- Cannot read base ref → fail with instructions
