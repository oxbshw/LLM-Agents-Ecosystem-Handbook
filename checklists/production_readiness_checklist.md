# Production readiness checklist

Walk this. All boxes ticked → ship. Otherwise, fix.

## Identity & instructions
- [ ] `SOUL.md`, `AGENTS.md`, `USER.md` current
- [ ] System prompt explicitly treats tool output as data, not instruction

## Tools
- [ ] Every tool listed in `TOOLS.md`
- [ ] Every tool has a risk level
- [ ] Every High/Critical tool has an approval gate
- [ ] Argument schemas validated
- [ ] Dangerous patterns blocked

## MCP (if used)
- [ ] Each server reviewed via [`mcp-security-reviewer`](../skills/examples/mcp-security-reviewer/SKILL.md)
- [ ] Versions pinned
- [ ] Tokens minimum-scope
- [ ] Allow-lists configured

## Memory
- [ ] No PII / secrets in any memory file
- [ ] Promotion is gated, not automatic
- [ ] Per-user / per-project isolation verified
- [ ] Memory eval passes

## Guardrails
- [ ] Input / output / tool-call / loop guardrails wired
- [ ] Cost ceiling per run
- [ ] Iteration cap, wallclock timeout

## Approvals
- [ ] `HUMAN_APPROVAL_POLICY.md` filled
- [ ] Approval mechanism out-of-band
- [ ] No auto-approve on timeout
- [ ] Audit log append-only + durable

## Observability
- [ ] Traces emit per run
- [ ] Cost / latency / error dashboards reachable
- [ ] Alerts: cost spike, error spike, repeated guardrail trips
- [ ] On-call knows where to look

## Evals
- [ ] Regression eval ≥ baseline
- [ ] Tool-call eval ≥ baseline
- [ ] Memory eval ≥ baseline
- [ ] Safety eval = 100% on criticals
- [ ] Reports archived

## Ops
- [ ] Rollback plan documented
- [ ] Kill switch tested
- [ ] Incident runbook
- [ ] Privacy / retention policy documented
- [ ] CHANGELOG updated
