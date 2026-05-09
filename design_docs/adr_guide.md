# ADR guide

ADR = Architecture Decision Record. Short, dated, irreversible-by-design. The thing future-you will thank you for.

## When to write one

- A non-trivial architecture decision was made
- A *choice* was made between alternatives that informed people will revisit
- A constraint was accepted (compliance, cost, deadline)
- A bug fix required a structural change worth remembering

## When NOT to write one

- Naming / formatting decisions
- Operational tweaks
- Per-project conventions (those go in `AGENTS.md` / `MEMORY.md`)

## Structure (≤ 1 page)

```markdown
# ADR-NNNN: <Title>

Date: YYYY-MM-DD
Status: proposed | accepted | superseded by ADR-XXXX | deprecated

## Context
{{What problem are we solving? What constraints apply?}}

## Decision
{{What we chose, in one paragraph.}}

## Alternatives considered
- {{Alt 1}} — {{why not}}
- {{Alt 2}} — {{why not}}

## Consequences
- ✅ {{positive}}
- ❗ {{negative or risk}}
```

## Naming and storage

- File: `memory/decisions/ADR-NNNN-short-slug.md`
- ID is monotonic (next number)
- Index in `MEMORY.md#decisions` with one-line entry

## Status lifecycle

```
proposed → accepted → superseded
                    ↓
                deprecated
```

- A superseded ADR is *not* deleted; it's marked and points at its replacement
- A deprecated ADR is no longer in force but the history is preserved

## Anti-patterns

- ❌ ADRs longer than a page (you've conflated decision + design)
- ❌ ADRs without alternatives (looks like the only choice was the chosen one)
- ❌ ADRs without negative consequences (no decision is consequence-free)
- ❌ Mass-writing ADRs after the fact ("ADR backfill weeks") — usually low quality
- ❌ Renaming / renumbering ADRs after creation — breaks references

## Pair with

- [`/templates/ADR.md.template`](../templates/ADR.md.template)
- [`/skills/catalog/adr-writer/SKILL.md`](../skills/catalog/adr-writer/SKILL.md)
- [`/memory/examples/decision_log.md.example`](../memory/examples/decision_log.md.example)
