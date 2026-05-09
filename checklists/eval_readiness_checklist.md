# Eval readiness checklist

Before running evals as a release gate, confirm the suite is actually meaningful.

## Coverage
- [ ] Golden path covered
- [ ] Edge cases (past bugs) covered
- [ ] Adversarial cases (injection, ambiguity) covered
- [ ] Negative cases (refusal / clarification) covered

## Hygiene
- [ ] Cases tagged (suite, category, difficulty)
- [ ] Cases versioned in git
- [ ] No model-generated cases that the model is then evaluated on
- [ ] Stale / always-passing cases pruned periodically

## Pass criteria
- [ ] Per-case pass rule explicit (exact / schema / rubric / trace)
- [ ] Suite-level thresholds documented
- [ ] Critical safety cases require 100% pass

## Judge (if used)
- [ ] LLM judge model + version pinned
- [ ] Rubric versioned
- [ ] Sample-graded by humans periodically

## Reporting
- [ ] Output report includes pass rate, deltas vs last release, per-case detail
- [ ] Reports archived per release

## Release gate
- [ ] Hard fails defined (regression, safety criticals)
- [ ] Soft fails defined with sign-off path
- [ ] Triage SLA documented
