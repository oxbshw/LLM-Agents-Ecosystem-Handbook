# Skills

A **Skill** is a reusable, model-loaded workflow defined by a `SKILL.md` plus optional `references/` and `scripts/`. Skills make repeatable tasks consistent across runs.

## What's here

### Concepts
- [skill_design_guide.md](skill_design_guide.md) — write a skill the model actually picks up
- [skill_vs_tool_vs_mcp.md](skill_vs_tool_vs_mcp.md) — when to use which
- [skill_taxonomy.md](skill_taxonomy.md) — domains, tags, risk axes
- [skill_maturity_model.md](skill_maturity_model.md) — experimental → beta → production
- [skill_packaging.md](skill_packaging.md) — ship a portable skill
- [skill_validation.md](skill_validation.md) — lint / smoke / eval

### Catalog
- [catalog/](catalog/) — handbook's curated catalog
  - [catalog/index.md](catalog/index.md) — every skill, one line each
  - [catalog/categories.md](catalog/categories.md) — by domain
- [examples/](examples/) — fully-built reference skills
- [awesome_skills_catalog.md](awesome_skills_catalog.md) — broader ecosystem map

### Quality + safety
- [security_checklist.md](security_checklist.md)
- [`/checklists/skill_quality_checklist.md`](../checklists/skill_quality_checklist.md)

## The core six (build into your agent first)

| Skill | Purpose |
|---|---|
| [research-summarizer](examples/research-summarizer/) | Sourced multi-source briefings |
| [repo-auditor](examples/repo-auditor/) | Pre-PR audit of changed code |
| [mcp-security-reviewer](examples/mcp-security-reviewer/) | Review an MCP server before wiring |
| [agent-memory-curator](examples/agent-memory-curator/) | Promote episodic → semantic memory |
| [pr-summarizer](catalog/pr-summarizer/) | Generate clean PR descriptions |
| [adr-writer](catalog/adr-writer/) | Capture architecture decisions |

## Why Skills (vs more prompting)

| You can put it in… | Why a Skill is better |
|---|---|
| The system prompt | Bloats every run; doesn't load progressively |
| A README | The model isn't guaranteed to read it |
| Code | Can't be loaded by tools that don't run code |

Skills are the smallest unit of *modular, model-readable workflow*. They scale because the agent only loads the ones whose `description` matches the current task.

## Anatomy

```
skills/<scope>/<skill-name>/
├── SKILL.md          ← frontmatter + workflow
├── references/       ← loaded only when needed
└── scripts/          ← optional helpers
```

Frontmatter (required):

```yaml
---
name: research-summarizer
description: Use when ...   # this line decides whether the model loads the skill
version: 0.1.0
status: beta                # experimental | beta | production | deprecated
risk: low                   # low | medium | high | critical
tags: [research, read-only, network-required]
---
```

📖 Field reference: [skill_taxonomy.md](skill_taxonomy.md). Maturity rules: [skill_maturity_model.md](skill_maturity_model.md). Quality bar: [`/checklists/skill_quality_checklist.md`](../checklists/skill_quality_checklist.md).

## Designing well — five rules

1. **Specific triggers.** "Use when X" beats "useful for research."
2. **Progressive disclosure.** Don't put 30 pages in `SKILL.md`. Put them in `references/` and reference them from the workflow steps.
3. **Validate output.** Define what success looks like inside the skill.
4. **Fail loudly.** Bad inputs → clear error, not silent degradation.
5. **Compose.** A complex task = several small Skills, not one giant one.

📖 [skill_design_guide.md](skill_design_guide.md)
