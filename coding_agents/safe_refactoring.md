# Safe refactoring with coding agents

Refactors fail when they're too big, too fast, and too entangled. The fix is process, not cleverness.

## The four-phase pattern

### Phase 1 — Characterize
Write tests that pin current behavior **before** changing anything. If the area lacks tests, the agent's first job is to add them. No tests → no refactor.

### Phase 2 — Wrap
Introduce the new abstraction **alongside** the old. Both call sites coexist. Add adapters where needed.

### Phase 3 — Migrate
Move call sites one at a time. Each commit:
- Targets a small set of call sites
- Keeps tests green
- Is independently revert-able

### Phase 4 — Remove
Once all call sites are migrated and stable, delete the old.

## What an agent should NOT do unattended

- Rename APIs across many call sites in one go
- Restructure tests at the same time as code
- Touch infra and code in one PR
- Convert formatting alongside semantic changes
- Apply automated codemods without a plan

Each of these mixes signals — when something breaks, you don't know what.

## Smallest-diff bias

If a change can be expressed in 50 lines, a 500-line agent diff is failing. Counter-measures:

- "Smallest diff that solves the problem" rule in `SOUL.md`
- One concept per PR
- "Show me what you'll touch before you touch it" gate

## Tests as the contract

Coding agents trust the test suite. If your tests are flaky, slow, or under-covering the area being refactored, fix them *first*. A confident agent on a weak test suite is a recipe for silent regressions.

## Reversibility checklist

For each refactor:

- [ ] Old and new coexist for the migration window
- [ ] One commit per call-site batch
- [ ] Tests green at every commit
- [ ] Feature flag if behavior shifts (even subtly)
- [ ] Rollback path documented in the PR

## Anti-patterns

- ❌ "Modernize the codebase" as a single task
- ❌ Mixing rename + behavior change
- ❌ Touching `main` without a feature branch
- ❌ Waiting until the end to run tests
- ❌ Letting the agent decide unilaterally to rewrite a module

## Cross-references

- [`prompts/modernization_prompt.md`](prompts/modernization_prompt.md)
- [`/templates/REPO_MODERNIZATION_PROMPT.md.template`](../templates/REPO_MODERNIZATION_PROMPT.md.template)
- [skills/examples/repo-auditor](../skills/examples/repo-auditor/SKILL.md)
