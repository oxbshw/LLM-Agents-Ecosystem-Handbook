# Coding agent review checklist

What a *human* should check on a coding-agent PR. Cheap, repeatable, catches most issues.

## Did the agent follow the rules?
- [ ] Stayed within the task scope (no surprise refactors)
- [ ] Smallest diff that solves the problem
- [ ] Followed `AGENTS.md` conventions (style, naming, commits)
- [ ] Walked the test commands; tests pass

## Is the change correct?
- [ ] No off-by-one / null-handling regressions
- [ ] Error handling preserved
- [ ] Behavior changes are intentional and documented
- [ ] Backwards-compat preserved (or break is documented)

## Tests
- [ ] Every new public function has a test
- [ ] Every changed branch has at least one covering test
- [ ] Tests are deterministic (no time / network without mocking)
- [ ] Failing-test-first commit present for bug fixes

## Docs
- [ ] Public API change → docstring updated
- [ ] Behavior change → CHANGELOG entry
- [ ] Workflow change → `AGENTS.md` updated
- [ ] If memory was promoted → `MEMORY.md` diff sensible

## Security
- [ ] No new dependency without review
- [ ] No secrets / tokens / `.env*` in the diff
- [ ] Input validation on new boundaries
- [ ] No new High/Critical tool calls without approval gates

## Hygiene
- [ ] No `TODO` / `FIXME` left without an issue
- [ ] No debug prints / stack traces
- [ ] No commented-out code
- [ ] No surprise file moves

## Style fit
- [ ] Imports in project order
- [ ] Logging via project logger
- [ ] Error types match conventions
- [ ] Doesn't introduce a new pattern when an old one exists

## PR description
- [ ] Title concise
- [ ] Description explains *why*, not just what
- [ ] Risks called out honestly
- [ ] Test plan present

## Trace + evals (if applicable)
- [ ] Trace exists for any agent-driven multi-step run
- [ ] Eval suites green (regression, tool-call, safety)

## Stop signs
- 🛑 PR mixes concerns → ask for a split
- 🛑 PR removes a test "to make CI pass" → reject
- 🛑 PR force-pushes over base → reject
- 🛑 PR touches `.env*` or `*credentials*` → security review
