# Blueprint: Secure-action agent

## Use case
An agent that takes high-impact actions on behalf of a user — payments, deploys, IAM changes, customer comms — without disasters.

## Non-goals
- Convenience over safety (this is the wrong agent for that)
- Removing the human from Critical actions (they stay)

## Architecture

```
user request
    │
    ▼
[interpreter]  ── what action, what scope
    │
    ▼
[risk classifier]  ── Low | Medium | High | Critical
    │
    ▼
[dry-run] (for Medium+) ── preview the change
    │
    ▼
[approval gate] (for High/Critical) ── out-of-band
    │
    ▼
[executor]  ── tools/call
    │
    ▼
[verifier + audit]  ── post-action check, immutable log
```

## Tools

| Tool | Risk |
|---|---|
| Read state | Low |
| Draft action | Medium |
| Execute action | High–Critical |
| Rollback | High (often pre-approved) |

## Memory
- Audit-log centric; the *audit log* is the memory of record
- `MEMORY.md` only for non-sensitive policy / convention context

## Safety controls (everything together)

- **Risk classifier** with a pinned, eval'd model (or rules + model fallback)
- **Dry-run mandatory** for Medium+
- **Out-of-band approvals** with signed decision records
- **Second reviewer** for Critical actions
- **Budget caps** per tool / per user / per day
- **Reversibility-first**: prefer the reversible variant when one exists
- **Kill switch** at the gateway

## Evals (extra weight here)

- Risk classification accuracy (especially false-low; never under-classify Critical)
- Approval flow correctness (always requested, never bypassed)
- Adversarial: prompt injection trying to coerce action — must refuse / approval-block
- Drill: simulate a Critical attempt with the kill switch off — confirm gates hold

## Deployment

- Sit behind your real auth; no agent-held privileges
- Action gateway runs as its own service, separate from the model loop
- Audit log → durable, append-only storage (write-once if possible)
- On-call rotation has eyes on the agent's first weeks

## What "good" looks like

You can answer "what did this agent do, by whom, with whose approval, on what data, in what time window?" in seconds. If you can't, this agent isn't ready for the actions it's taking.
