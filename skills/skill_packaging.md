# Skill packaging

How to ship a skill so it works across coding-agent harnesses (Claude Code, Cursor, Codex, Aider, Cline, custom agent runtimes).

## Layout

```
<skill-name>/
├── SKILL.md              ← the spec (YAML frontmatter + workflow)
├── references/           ← loaded only when steps need them
│   ├── *.md
│   └── *.json | *.yaml   ← optional structured refs
└── scripts/              ← optional helpers
    └── *.py | *.sh
```

`SKILL.md` MUST be the only required file.

## Frontmatter (required)

```yaml
---
name: research-summarizer
description: Use when ...
version: 0.3.1
status: beta
risk: low
tags: [research, read-only]
---
```

See [skill_taxonomy.md](skill_taxonomy.md) and [skill_maturity_model.md](skill_maturity_model.md) for the field vocab.

## Body (required sections)

```markdown
## When to use
## When NOT to use
## Inputs        (table)
## Outputs       (spec)
## Workflow      (numbered steps)
## References    (link to references/*.md)
## Success criteria
## Failure modes
## Examples
```

If you skip "When NOT to use" or "Failure modes", the model will be over-eager.

## Portability rules

1. **No absolute paths.** `references/foo.md` is correct; `/Users/me/skills/...` is not.
2. **No tool-specific syntax** in the spec. If you need a Claude Code hook, document it as a *hook* in [coding_agents/](../coding_agents/), not inside the skill.
3. **Inputs as data, not assumptions.** "The user will pass `topic`" beats "the user means topic when they say research."
4. **Reference loading on demand.** Mention the reference in the step that uses it: "Step 3: load `references/clustering-rules.md`."
5. **Scripts are optional.** If a Python helper makes sense, include it; document `python --version` and dependencies. Don't require a paid service.

## Distributing a skill

| Channel | When |
|---|---|
| In-repo (this handbook) | Reusable across this project's agents |
| Per-project `.agent/skills/<name>/` | Project-specific |
| Shared registry (internal) | Org-wide skill library |
| Open-source repo | External community |

When sharing across orgs, version-pin (`version:`) and changelog. A skill that mutates is harder to trust than a frozen one.

## Anti-patterns

- ❌ Skill description that doesn't say *when* to use
- ❌ Hard-coded URLs to internal services
- ❌ Side effects buried in references
- ❌ A skill that bundles five purposes
- ❌ Skills that invoke high-risk tools without explicit approval handling
