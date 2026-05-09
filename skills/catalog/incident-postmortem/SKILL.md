---
name: incident-postmortem
description: Use after an incident is resolved — drafts a blameless postmortem from timeline notes, alerts, and chat threads.
version: 0.1.0
status: experimental
risk: low
tags: [ops, writes-files]
---

# Incident Postmortem

## When to use
- After an incident with customer impact
- After a near-miss worth documenting
- For drills / GameDay exercises

## When NOT to use
- Live incidents (use `incident-runbook` instead)
- Pure private learnings (use a personal log)

## Inputs
| Name | Type | Required | Notes |
|---|---|---|---|
| `timeline` | text or paths | yes | Source notes, alert links, chat extracts |
| `severity` | `S0`–`S3` | yes | Severity at peak |
| `incident_id` | string | yes | e.g. `INC-2026-04-12-001` |

## Outputs
`postmortem.md` with: Summary, Impact, Timeline, Direct cause, Contributing factors, What went well, What didn't, Action items.

## Workflow
1. Reconstruct the timeline (UTC), one row per notable event
2. State **impact** in user-facing terms (requests failed, dollars lost, customers affected)
3. Identify the **direct cause** in one sentence — what specifically broke
4. List **contributing factors** (the conditions that made the incident possible / hard to mitigate)
5. Separate **what went well** (genuine wins, not platitudes) and **what didn't**
6. Owners + dates on every action item; hard fail if missing
7. Tone: blameless. Describe systems failing, not people.

## References
- [`references/postmortem-template.md`](references/postmortem-template.md)

## Success criteria
- Every action item has an owner and a date
- Direct cause is one sentence
- No names attached to fault; only roles / systems
- Timeline times in UTC

## Failure modes
- Missing source data → list gaps explicitly; don't fill with guesses
- Conflicting timelines → record both, flag for review
