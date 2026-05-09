---
name: agent-memory-curator
description: Use after a session to promote useful episodic notes from logs/episodic/ into distilled, dated entries in MEMORY.md and memory/semantic/.
version: 0.1.0
---

# Agent Memory Curator

## When to use
- End of a working session
- After resolving an incident worth remembering
- When `MEMORY.md` has grown stale or contradictory

## When NOT to use
- During a session (don't write memory mid-flight from low-confidence signals)
- For raw transcripts (those stay in `logs/`)

## Inputs
| Name | Type | Required | Notes |
|---|---|---|---|
| `since` | date | no | default: last curation time |
| `categories` | list | no | restrict to e.g. `[user, project, decision]` |

## Workflow
1. **Read** new episodic logs in `logs/episodic/` since `since`
2. **Distill** each notable event into a one-line dated entry
3. **Categorize** into: user / project / decision / feedback / open question
4. **Reconcile**: if a new entry contradicts an existing one, *update* the existing one rather than appending; move the old fact to "Outdated"
5. **Apply rules** from `references/memory-distillation-rules.md`
6. **Write** to `MEMORY.md` (index) and `memory/semantic/<topic>.md` (details)
7. **Verify** no PII / secrets leaked into memory
8. **Report** summary of additions / updates / deletions

## References
- [`references/memory-distillation-rules.md`](references/memory-distillation-rules.md)

## Success criteria
- Every new entry is dated
- No duplicate entries (search before adding)
- No PII / secret values
- Outdated entries moved, not deleted in-place

## Failure modes
- Conflicting evidence → mark as "Open question" rather than guessing
- Source untrusted (e.g., from MCP/web fetch) → require human confirm before promotion
