# Skill taxonomy

Skills are easier to find — and easier to design — when they share a vocabulary. This taxonomy is the one we use across the catalog.

## Top-level domains

| Domain | Examples |
|---|---|
| **Engineering** | repo audits, code review, test scaffolding, refactor planning |
| **Research** | sourced briefings, comparative analysis, literature scans |
| **Product / PM** | PRD writing, sprint planning, roadmap synthesis |
| **Data** | dataset profiling, ad-hoc analysis, dashboards |
| **Ops / SRE** | incident triage, postmortems, runbook creation |
| **Security** | threat modeling, secure-coding review, vuln triage |
| **Design / UX** | spec writing, design-review notes, copy iteration |
| **Memory & knowledge** | curators, summarizers, ADR writers |
| **Agent ops** | MCP review, prompt review, eval design |

## Cross-cutting tags

Apply on top of the domain.

| Tag | Meaning |
|---|---|
| `read-only` | No external writes (search, summarize) |
| `writes-files` | Produces or modifies files |
| `writes-external` | Posts to GitHub, Slack, Notion, etc. |
| `agentic` | Drives a multi-step loop with tools |
| `interactive` | Expects user dialogue |
| `progressive` | Loads references on demand |
| `network-required` | Hits the internet |
| `local-only` | Runs offline |

## Risk axes

Skills inherit risk from the *tools they call*, not from the workflow itself. The taxonomy maps cleanly to [safety/tool_risk_levels.md](../safety/tool_risk_levels.md):

| Risk | Typical skill shapes |
|---|---|
| Low | research-summarizer, dataset-profiler |
| Medium | repo-auditor (writes a report), prd-writer |
| High | release-cutter, deploy-reviewer, secret-rotator |
| Critical | infra-applier, billing-action, prod-data-mutator |

## Maturity

| Stage | Meaning | Loaded by default? |
|---|---|---|
| `experimental` | New, behavior may change, tests light | only if explicitly enabled |
| `beta` | Stable enough to use; eval coverage partial | yes, with caveats |
| `production` | Regression-eval'd, security-reviewed | yes |
| `deprecated` | Superseded; kept for compatibility | no |

See [skill_maturity_model.md](skill_maturity_model.md).

## Naming conventions

- kebab-case folder names: `research-summarizer`, not `Research Summarizer`
- Verb-first or descriptive: `audit-`, `summarize-`, `triage-`, `generate-`
- One purpose per skill — if you need `... and ...`, split.

## Description shape

YAML frontmatter `description:` follows the form:

> **Use when** *<specific trigger>*. Produces *<output>*. Best with *<tool / context>*. Skip when *<anti-trigger>*.

Specific triggers beat generic ones. Example:

✅ "Use when the user asks for a sourced briefing on a topic that spans multiple web sources and requires citations."
❌ "Use when the user wants research."

## Inheritance from open ecosystems

The catalog is informed by patterns observed across community skill collections. We do not bulk-import other catalogs — we curate. See [awesome_skills_catalog.md](awesome_skills_catalog.md) for ecosystem links.
