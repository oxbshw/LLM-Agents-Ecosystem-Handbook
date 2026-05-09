# Project memory

What the agent knows about *this project / repo*, across sessions.

## Where it lives

- `MEMORY.md#project` — index of project facts
- `memory/semantic/<topic>.md` — per-topic deep dives
- Decision records (ADR-style): `memory/decisions/` or `logs/decisions/`

## What to store

- Architecture facts not visible from the code (ownership, contracts, runtime quirks)
- Decisions and their rationale (alternatives, trade-offs)
- Conventions (testing, deploy, on-call)
- Known fragile areas
- External dependencies and their quirks

## What NOT to store

- Anything trivially derivable from `git log` / `git blame` / current code
- Ephemeral build state
- Per-session task tracking (use a TODO file or issue tracker)

## Decision records

For non-trivial decisions, write a short ADR:

```markdown
# ADR-0042: Use pnpm for the monorepo
Date: 2026-03-15
Status: accepted

## Context
{{What problem are we solving}}

## Decision
{{What we chose}}

## Alternatives considered
- npm — {{why not}}
- yarn — {{why not}}

## Consequences
- {{positive}}
- {{negative or risks}}
```

Index it in `MEMORY.md#decisions`:
```
- ADR-0042: pnpm over npm/yarn (2026-03-15) — see memory/decisions/0042-pnpm.md
```

## Cross-references

Project memory should link to:

- `AGENTS.md` for the *operational* version of conventions (the parts an agent enforces)
- ADRs for the *historical* version (why those conventions exist)

This split keeps `AGENTS.md` short.
