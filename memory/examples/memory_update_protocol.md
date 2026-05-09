# Memory update protocol (example)

A concrete, copy-able protocol for keeping memory healthy.

## When
- End of every working session
- After resolving an incident worth remembering
- Quarterly review for staleness

## Steps

1. **Collect candidates** from today's `logs/episodic/` (entries tagged `decision`, `feedback`, or `#promote`)
2. **Filter** through the [promotion threshold](../memory_distillation.md#promotion-threshold):
   - General? Confident? Stable? Useful? — all four = yes
3. **Distill** — one line per fact, with date, in the right `MEMORY.md` section
4. **Reconcile** existing entries:
   - If new contradicts old → update old, move old to "Outdated"
   - If new restates old → drop new
5. **Verify**:
   - No PII / secrets
   - No fabricated content
   - No content from low-trust sources without confirmation
6. **Commit** the diff to git with message `memory: distil 2026-04-12 session`

## Example diff

```diff
 ## Project
 - Monorepo: backend (FastAPI) + frontend (Next.js); shared types in `packages/types` (2026-04-09)
 - We use pnpm, not npm or yarn (2026-03-15)
 - DB migrations via alembic; never modify `versions/` history (2026-02-04)
+- NOT NULL backfills must include a default in the same migration (2026-04-12)

 ## User
 - Prefers terse responses with diffs over prose (2026-04-15)
+- Always show migration diffs before applying (2026-04-12)
```

## Anti-patterns

- ❌ Pasting raw transcript chunks
- ❌ Adding "user might prefer" without confirmation
- ❌ Storing API keys "just in case"
- ❌ Letting `MEMORY.md` exceed ~200 lines — split into per-topic files first
