# Safety

Practical controls that keep an agent useful *and* harmless. This section is opinionated.

## What's here

- [guardrails.md](guardrails.md) — programmatic checks around the loop
- [human_approval.md](human_approval.md) — when to ask, how to ask
- [tool_risk_levels.md](tool_risk_levels.md) — the canonical risk table
- [prompt_injection.md](prompt_injection.md) — direct + indirect, patterns + mitigations
- [data_exfiltration.md](data_exfiltration.md) — preventing leaks via tools/output
- [secure_agent_checklist.md](secure_agent_checklist.md) — the pre-ship gate
- [examples/guarded_tool_agent](examples/guarded_tool_agent/) — agent with risk-gated tools
- [examples/human_approval_agent](examples/human_approval_agent/) — agent with explicit approval flow

## Pillars

1. **Least privilege** — smallest scope for the job
2. **Risk tiering** — every tool labelled
3. **Human approval** — High/Critical actions are gated
4. **Audit logging** — every medium+ tool call recorded

## Risk levels (canonical)

| Risk | Examples | Approval |
|---|---|---|
| Low | read-only search, summarization | none |
| Medium | drafting files, creating tickets | sometimes |
| High | sending email, modifying repos, running shell | required |
| Critical | deleting data, spending money, changing permissions | always + 2nd reviewer |

📖 [tool_risk_levels.md](tool_risk_levels.md)

## What good looks like

A safe-by-default agent has:

- ✅ `GUARDRAILS.md` and `HUMAN_APPROVAL_POLICY.md` filled in
- ✅ Every tool risk-labelled in `TOOLS.md`
- ✅ Tracing on for every run; audit log for High/Critical
- ✅ A safety eval suite that runs pre-release
- ✅ A documented kill switch / rollback

📖 [secure_agent_checklist.md](secure_agent_checklist.md)
