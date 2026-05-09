# Awesome skills — ecosystem map

Where skills come from, where they're going, and how to harvest patterns from the wider community without bulk-copying.

> The skill ecosystem is large and inconsistent. Some collections list thousands of skills with little quality control; others are highly curated. This page catalogs the *kinds* of collections, what each is good for, and how to extract patterns into your own catalog.

## Collection types

| Type | Examples | Use it for |
|---|---|---|
| **Federated author collections** | One repo aggregating many authors' personal skill folders | Spotting domain-expert patterns; copy carefully — quality varies |
| **Mega-catalogs** | Repos with 1000+ skills, broad categorization | Inspiration + taxonomy; not a direct dependency |
| **Curated lists** | Smaller "awesome-*" repos with editorial bar | Higher signal; still verify each skill before adoption |
| **Production harnesses** | Tooling that ships pre-bundled skills with a config system | Patterns for skill loading, hooks, eval discovery |
| **Vendor docs** | Anthropic / OpenAI / Cursor "best practices" guides | Authoritative on the tool you're targeting |

## How to harvest

1. **Skim by domain.** If you need a "code-review" skill, look for it in 3–5 collections.
2. **Look for the description.** A skill whose `description:` is generic is rarely picked up cleanly by the model.
3. **Check the references.** A SKILL.md with no progressive disclosure (no `references/`) is usually a long monolithic prompt — extract the *workflow*, drop the prose.
4. **Ignore the prose, keep the structure.** Many skills repeat the same shape: trigger / inputs / steps / examples. Adopt the shape; rewrite the content for your project.
5. **Re-test.** External skills almost never pass your evals on the first try. Tag them `experimental` until they do.

## Domains worth seeking patterns for

- **Code review & repo audit** — many strong examples; pick the one with explicit success criteria
- **API design** — usually best when paired with concrete style references
- **Security review** — must include "what NOT to do" cases
- **Sprint / PRD writing** — domain-specific; avoid one-size templates
- **Test scaffolding** — varies by language; collect per-stack
- **Memory curation** — see [agent-memory-curator](examples/agent-memory-curator/SKILL.md)

## What to NOT bulk-copy

- Skills with vague triggers ("helps with research")
- Skills with hard-coded user paths or repo names
- Skills that bundle five workflows
- Skills with executable scripts but no security review
- Skills authored by anonymous accounts on read-only mirrors

## Curation philosophy

This handbook ships a **small** catalog of high-quality skills (in [`examples/`](examples/) and [`catalog/`](catalog/)) and *describes* the ecosystem rather than mirroring it. The goal is a reference you can actually trust — not a search index of unknown content.

If you want to harvest at scale:

1. Mirror only the SKILL.md files (cheap)
2. Run lint on every file (most fail)
3. Group by domain, sort by description-quality heuristics
4. Manual review the top 5 per domain
5. Add the survivors to `catalog/` with a short curator's note

That's a weekend's work for a careful person, vs. a year-long maintenance treadmill.

## Building your own internal catalog

Most teams want a *private* catalog tuned to their stack. The pattern:

1. Start by copying [`templates/SKILL.md.template`](../templates/SKILL.md.template)
2. Adopt the [taxonomy](skill_taxonomy.md) and [maturity model](skill_maturity_model.md)
3. Wire validation ([skill_validation.md](skill_validation.md)) into CI
4. Promote skills experimental → beta → production based on real use
5. Keep the catalog small. A trusted 20 beats a sprawling 500.
