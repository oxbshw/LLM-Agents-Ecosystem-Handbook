# Semantic memory

Distilled, generalized facts that survive runs and inform future decisions.

## Where it lives

- **`MEMORY.md`** — the index, one line per entry, scannable
- **`memory/semantic/<topic>.md`** — when a topic outgrows one line

Use the index for breadth (every fact is reachable), per-topic files for depth.

## What goes here

| Category | Example |
|---|---|
| Project | "We use pnpm, not npm" |
| Architecture | "Auth is owned by team Iris; their on-call is X" |
| Decision | "We chose alembic over raw SQL for migrations because rollback matters" |
| Convention | "Tests must be deterministic — no time/network without mocks" |
| User preference | "Terse responses, diffs over prose" |
| Domain knowledge | "Customer tier 'pro' includes the X feature" |

## What does NOT go here

- Transcripts (→ `logs/`)
- Single-session state (→ working memory)
- Unverified claims (→ "Open questions")
- Anything in `git log` or current code (don't duplicate)

## Per-topic files

When entries on a topic exceed ~5 lines, extract to `memory/semantic/<topic>.md`:

```
memory/semantic/
├── auth_service.md
├── data_pipeline.md
├── deploy_workflow.md
└── customer_tiers.md
```

`MEMORY.md` then has a one-line pointer:

```
## Architecture
- Auth service: see `memory/semantic/auth_service.md`
```

## Quality bar

A good semantic memory entry is:

- ≤ 1 line in the index
- Dated
- Sourced (where it came from is obvious from the file or tag)
- Verifiable (someone could confirm it)

## Maintenance

- Quarterly review for staleness
- Curator skill runs after every session
- Conflicts force an update (not an append)
