---
name: sprint-planner
description: Use when planning the next sprint — turns ticket intake + team capacity into a planned sprint with explicit non-goals.
version: 0.1.0
status: experimental
risk: low
tags: [product, writes-files]
---

# Sprint Planner

## When to use
- Start of a sprint cycle
- After a re-prioritization mid-cycle
- When intake outpaces capacity and you need a defendable plan

## When NOT to use
- Daily standup (different cadence)
- Annual planning (different scope; use `roadmap-synthesizer`)

## Inputs
| Name | Type | Required | Notes |
|---|---|---|---|
| `tickets` | list / path | yes | candidate work items with priority + estimates |
| `capacity` | object | yes | per-engineer days available |
| `previous_carry` | list | no | items rolling over from last sprint |
| `commitments` | list | no | OKR / stakeholder commitments that must land |

## Outputs
`sprint-plan.md` with: Sprint goal, Committed, Stretch, Non-goals, Risks.

## Workflow
1. Compute total capacity (days × team)
2. Sort candidates: committed → carry → stretch
3. Pack to ~85% of capacity (leave room for support / interrupts)
4. Identify dependencies between items; surface blockers
5. Surface **explicit non-goals** — what we are *not* doing this sprint and why
6. Risks: anything that would cause spillover

## References
- [`references/sprint-plan-template.md`](references/sprint-plan-template.md)

## Success criteria
- Committed work ≤ 85% of capacity
- Every committed item has an owner and an estimate
- Non-goals section is non-empty
- Risks include at least one "what could derail us"

## Failure modes
- Capacity unknown → ask, don't guess
- Tickets without estimates → flag and exclude from "committed"
