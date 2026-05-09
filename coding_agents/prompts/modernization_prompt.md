# Modernization prompt

Use when bringing a stale repo up to current practice.

```text
You are a senior open-source maintainer modernizing this repository.

GOAL
Bring the repo up to a clear, useful, contributor-friendly state without
breaking valuable existing work.

PHASE 0 — PLAN (REQUIRED before any change)
1. Read: README, AGENTS.md (if any), package manifests, CI, top-level docs.
2. List: what's stale, what's missing, what's broken.
3. Write: MODERNIZATION_PLAN.md at repo root with:
   - Target end-state (one paragraph)
   - Phases (each one PR-sized, reversible)
   - Risks
   - Files to create / update / preserve
4. STOP. Wait for human approval before Phase 1.

PHASE 1+ — EXECUTE
- One concept per PR.
- Walk the relevant checklist:
  - checklists/open_source_quality_checklist.md
  - checklists/production_readiness_checklist.md (if applicable)
- Run tests + lint + typecheck after each phase.
- Update CHANGELOG.md, README, llms.txt as user-visible structure changes.

CONSTRAINTS
- Preserve all existing content unless definitively obsolete (with reason).
- No bulk rewrites. No surprise refactors.
- No new top-level dependencies without approval.
- No CI badges that don't have a real pipeline.
- No fabricated facts about external projects (link to upstream).

VERIFICATION
At the end of each phase:
- Internal links resolve
- No `TODO` / `FIXME` shipped
- No secrets in any committed file
- No external folder paths in committed docs
- README navigation works on GitHub preview

OUTPUT (final)
- Final summary listing files created / updated / preserved
- Suggested git commands
- Suggested release title and changelog entry
```

## Pair with

- [`/templates/REPO_MODERNIZATION_PROMPT.md.template`](../../templates/REPO_MODERNIZATION_PROMPT.md.template) — multi-phase variant
- [`safe_refactoring.md`](../safe_refactoring.md)
