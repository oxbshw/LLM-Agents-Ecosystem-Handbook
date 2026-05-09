# Safety matrix

Risk → controls → eval, in one view.

| Risk | Examples | Approval | Logging | Eval | Where |
|---|---|---|---|---|---|
| Low | search, summarize, read | none | sampled | smoke | [tool_risk_levels.md](../safety/tool_risk_levels.md) |
| Medium | drafting, ticket create | first-time | full | tool-call eval | [guardrails.md](../safety/guardrails.md) |
| High | email send, repo modify, shell | required | full + alert | safety eval | [human_approval.md](../safety/human_approval.md) |
| Critical | delete, transfer, IAM | always + 2nd | immutable | safety eval (100% on criticals) | [human_approval.md](../safety/human_approval.md) |

## Threats by source

| Threat | Source | Mitigation |
|---|---|---|
| Direct injection | user prompt | system-prompt rules + safety eval |
| Indirect injection | tool output / RAG / web | sanitize + treat as data + approval gates |
| Memory poisoning | episodic from external | curator gate + source-tag |
| Data exfiltration | tool args / output / logs | output filter + egress allow-list |
| Tool over-reach | broad permissions | least-privilege + risk gates |
| Cost runaway | bad loop | iteration cap + cost ceiling |
| Cross-tenant leak | shared memory | per-user isolation + isolation eval |

## Pre-ship safety gate

Walk [safety/secure_agent_checklist.md](../safety/secure_agent_checklist.md). Don't skip the audit log + alert rows.
