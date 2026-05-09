# Audit checklist

Walked per-file by the Repo Auditor skill.

## Correctness
- [ ] No obvious off-by-one or null-handling regressions
- [ ] Error handling preserved (no swallowed exceptions)
- [ ] Time-zones / encodings / locales handled like neighbors

## Tests
- [ ] Every new public function has a test
- [ ] Every changed branch has at least one covering test
- [ ] Tests are deterministic (no time/network without mocking)

## Style fit
- [ ] Imports match project order/grouping
- [ ] Logging uses project's logger, not bare `print`
- [ ] Error types match project conventions

## Hygiene
- [ ] No `TODO` / `FIXME` left without a tracked issue
- [ ] No `console.log` / `pdb.set_trace` / debug prints
- [ ] No commented-out code blocks

## Docs
- [ ] Public API change → docstring updated
- [ ] Behavior change → CHANGELOG entry
- [ ] Workflow change → `AGENTS.md` updated

## Security
- [ ] No new dependency without review
- [ ] No secrets in code or fixtures
- [ ] Input validation on new boundaries
