# Bug fix prompt

```text
You are a senior software engineer fixing a bug.

BUG
{{One paragraph describing the symptom and how to reproduce.}}

WORKFLOW (failing-test-first)
1. Reproduce the bug locally. Confirm you can see the failure.
2. Write a failing test that captures the bug. Run tests; confirm it fails.
3. Commit the failing test (or include it in the same commit as the fix).
4. Fix the bug. Run tests; confirm everything passes.
5. Search for similar bugs (grep for the bad pattern). Fix or note them.
6. Open a PR with: reproduction, root cause, fix, similar-bug audit.

CONSTRAINTS
- Smallest diff that fixes the bug. Resist the urge to refactor.
- If the bug requires architectural change to fix properly, surface that —
  don't paper over with a workaround silently.
- The PR must include the failing test BEFORE the fix in the diff history.

OUTPUT IN PR
- Reproduction steps
- Root cause (one paragraph)
- Fix description (one paragraph)
- Similar-bug check: list of greps run + results
- Risk: what tests don't cover
```

## Why "failing test first"

Without it, you've fixed *a* bug but you don't know if it was *the* bug. The failing test pins the exact behavior. After the fix it passes; if it ever fails again, the regression is named.
