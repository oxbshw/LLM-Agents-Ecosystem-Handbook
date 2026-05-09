# MEMORY.md — Coding agent

## Project
- Monorepo: backend (FastAPI) + frontend (Next.js); shared types in `packages/types` (2026-04-09)
- CI runs on every push to PR branches; tests must be green pre-merge
- Default branch: `main`; releases via tags `vX.Y.Z`

## User
- Prefers minimal diffs and explicit migration steps when schemas change

## Decisions
- We use `pnpm`, not npm or yarn (2026-03-15)
- DB migrations via `alembic`; never modify `versions/` history (2026-02-04)

## Open
- Switch to Bun for the TS workspace? — under evaluation (2026-04-20)
