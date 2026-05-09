# Design: Memory-Enabled Assistant (example, filled)

**Author:** handbook
**Date:** 2026-05-09
**Status:** accepted

## Use case
A persistent personal assistant whose behavior changes based on what it remembers about the user and the user's projects. Multi-session continuity is the headline feature.

## Non-goals
- Sharing memory across users
- Sending email / spending money without approval
- Inferring private data the user hasn't explicitly shared

## Architecture

```
session start
   │
   ▼
[load USER.md + relevant MEMORY.md slices]
   │
   ▼
session loop:  user → agent ↔ tools / memory reads / writes
   │
   ▼
session end
   │
   ▼
[agent-memory-curator promotes episodic → semantic]
   │
   ▼
diff committed; user approves changes
```

## Components

| Layer | Choice |
|---|---|
| Identity | concise, asks before assuming |
| Memory | `USER.md`, `MEMORY.md`, `memory/semantic/<topic>.md`, `logs/episodic/<date>.md` |
| Skills | `agent-memory-curator`, `meeting-prep`, `inbox-triage` |
| Tools | calendar, email, tasks, web_search |
| Provider | default chain; local fallback for privacy mode |

## Memory model

- `USER.md`: stable profile + preferences
- `MEMORY.md#user`: dynamic user facts (dated)
- `MEMORY.md#project`: per-project conventions
- `memory/semantic/<topic>.md`: deep per-topic
- `logs/episodic/<date>.md`: append-only daily

Promotion gated by `agent-memory-curator` skill + user approval on USER.md changes.

## Safety
- Strict per-user isolation
- Email send always gated (no exceptions)
- Approval shows full draft + recipients
- One-click "forget me" wipes user memory + traces
- Encrypted at rest

## Eval plan
- Recall: ≥ 95% on golden cases
- No-fab: 100% (zero tolerance for invented memory)
- Isolation: 100% (no cross-tenant leakage — non-negotiable)
- Memory injection resistance ([memory_evals.md](../../evals/memory_evals.md))

## Cost / latency budget
- Interactive p95 ≤ 3s
- Per-session cost ≤ $0.30

## Rollout
- Single-user (author) for 2 weeks
- Internal alpha with 5 users
- Beta with explicit privacy disclosure

## Risks
- Memory poisoning via fetched content → curator gate, source-tagging
- Stale memory → quarterly review + expiry
- Privacy regression → audit log of every memory read/write
- Over-confident assistant → "what I remember about you" recap UI

## Open questions
- Voice channel (post-1.0)
- Cross-device sync (requires server; deferred)
