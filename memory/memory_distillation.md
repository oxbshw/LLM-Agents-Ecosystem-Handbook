# Memory distillation

Turning runs into durable facts. The single most important practice for keeping memory useful.

## The protocol

1. **Collect** — at end of run, gather episodic notes worth promoting
2. **Filter** — apply the [promotion threshold](#promotion-threshold)
3. **Distill** — one line per fact, with date and category
4. **Reconcile** — update or supersede existing entries; never dual-state
5. **Verify** — no PII / secrets, no contradictions
6. **Write** — to `MEMORY.md` (index) and/or `memory/semantic/<topic>.md`

## Promotion threshold

Promote only if the fact is:

- **General** — applies beyond one session
- **Confident** — observed twice OR explicitly user-stated
- **Stable** — unlikely to flip next week
- **Useful** — would change a future decision

Otherwise leave it in episodic logs (or drop).

## Format

```
- {{fact in one line}} ({{YYYY-MM-DD}})
```

Optional tags after the fact (`#user`, `#decision`) to make grep/index easier.

## Examples

| ✅ Good | ❌ Bad |
|---|---|
| `- Use pnpm not npm (2026-03-15)` | `- npm/pnpm decision discussion happened` |
| `- Merge freeze starts Thursdays 5pm PT (2026-04-01)` | `- there was talk of merge freezes` |
| `- User prefers terse, diff-first responses (2026-04-15)` | `- user might be impatient` |

## Reconciliation rules

When a new entry would contradict an existing one:

1. *Update* the existing entry rather than appending
2. Move the old fact to "Outdated" with `superseded by …`
3. If unresolved, demote both to "Open questions"

```
## Outdated
- Use yarn (2025-09-01) — superseded by "Use pnpm" (2026-03-15)
```

## Cadence

- Distillation runs at the end of every session (manual or via [`agent-memory-curator`](../skills/examples/agent-memory-curator/SKILL.md))
- Quarterly review of all entries; expire stale ones

## What distillation must NOT do

- Don't compress secrets / PII into "anonymized" memory — drop them
- Don't promote facts from low-trust sources (web fetch, untrusted MCP) without human confirmation
- Don't summarize transcripts — distill *learnings*, not events
