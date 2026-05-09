# Rollout plan

Shipping a design without surprises.

## Stages

| Stage | Audience | Goal | Exit criterion |
|---|---|---|---|
| **1. Internal** | Devs only | Smoke test, fix obvious bugs | No P0 issues for 2 days |
| **2. Dogfood** | Internal users | Edge cases, perf | No P1 issues for 5 days |
| **3. Small users** | 5–10% of traffic | Real-world signal | Quality + cost within budget |
| **4. Broad** | 50% | Scale signal | Same as 3, at scale |
| **5. Default** | 100% | Done | Old path deprecated |

For agents: each stage gets eval gates ([evals/regression_evals.md](../evals/regression_evals.md)).

## Kill switch

A *single config flip* that returns to the prior path. Test it before stage 1.

- Feature flag, env var, traffic-routing rule — pick one and document it
- The flip must be reversible without a deploy
- Document **who** can flip and **how** (chat command, dashboard, etc.)

## Rollback playbook

Document explicitly:

1. What signals trigger rollback (error rate, cost spike, customer reports)
2. Who decides
3. How (the kill-switch mechanism)
4. What to communicate (status page, internal channel)
5. Postmortem timeline

## Metrics to watch per stage

- Error rate (and which classes)
- p50 / p95 latency
- Cost per run / per user
- Approval-grant ratio (for agents — too many approvals = friction problem)
- Refusal rate (sudden change → policy regression)
- Eval suite scores

## Communication

- Internal: status updates on a fixed cadence (daily during stage 3+)
- External: changelog + status page
- Post-rollout: 1-page retro filed as an ADR (see [`adr_guide.md`](adr_guide.md))

## Anti-patterns

- ❌ "Just turn it on for everyone" — even small features can have weird interactions
- ❌ No kill switch — "we'll figure it out if we need it" rarely ends well
- ❌ Stage 3 with no eval gate — flying blind
- ❌ Letting a new path ride alongside the old forever — cleanup debt
- ❌ "Soft" rollback that requires a deploy — too slow

## Pair with

- [`/checklists/production_readiness_checklist.md`](../checklists/production_readiness_checklist.md)
- [`/observability/dashboards.md`](../observability/dashboards.md)
