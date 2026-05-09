# Skill validation

A skill that isn't validated isn't a skill — it's a guess. Three layers: **lint**, **smoke**, **eval**.

## Lint — the cheap pass

Run on every PR that touches a skill. Checks:

- Frontmatter present and well-formed (`name`, `description`, `version`, `status`, `risk`, `tags`)
- `description` starts with "Use when "
- Required sections exist: `When to use`, `When NOT to use`, `Workflow`, `Success criteria`, `Failure modes`
- All referenced files in `references/` actually exist
- No absolute paths
- No `TODO` / `FIXME` strings
- `version:` bumped if the file changed

A 30-line script can do this; gate it in CI.

## Smoke — does it run?

For each skill, at least one canned input → expected-shape output. Goals:

- Skill loads without error
- Workflow completes
- Output matches the documented schema (e.g., briefing produces `briefing.md`)

Smoke runs are cheap. Run on every PR.

## Eval — does it work *well*?

Production skills get a regression eval row in [`evals/`](../evals/):

```jsonl
{"id":"skill-research-1",
 "skill":"research-summarizer",
 "input":{"topic":"MCP adoption 2026","depth":"shallow"},
 "expected":{"min_sources":5,"distinct_domains":3,"all_claims_cited":true},
 "tags":["regression","skill"]}
```

Pass criteria are skill-specific. The skill itself defines them in "Success criteria"; the eval *enforces* them.

## What "good validation" looks like

| Stage | Lint | Smoke | Eval |
|---|---|---|---|
| Experimental | required | optional | optional |
| Beta | required | required | partial |
| Production | required | required | required + reg-tracked |

## Validation tooling sketch (Python)

```python
import yaml, pathlib

REQUIRED = {"name", "description", "version", "status", "risk"}

def lint_skill(path: pathlib.Path) -> list[str]:
    text = path.read_text("utf-8")
    if not text.startswith("---"):
        return ["missing frontmatter"]
    head, body = text.split("---", 2)[1:]
    fm = yaml.safe_load(head)
    errors = []
    missing = REQUIRED - set(fm)
    if missing:
        errors.append(f"missing keys: {missing}")
    if not str(fm.get("description", "")).lower().startswith("use when"):
        errors.append("description must start with 'Use when'")
    for section in ["When to use", "When NOT to use", "Workflow", "Success criteria", "Failure modes"]:
        if f"## {section}" not in body:
            errors.append(f"missing section: {section}")
    return errors
```

Drop this in `scripts/lint_skills.py` and wire to CI. (Not shipped here to avoid a runtime dep on PyYAML — copy if useful.)

## Failing loudly

A skill should *fail noisily* when:

- Required input is missing
- A reference can't be loaded
- Success criteria can't be met (e.g., "couldn't find ≥ 5 sources")
- A tool call returns an error

Silent fallback to a degraded answer is the worst failure mode — the user accepts a wrong answer because nothing flagged.
