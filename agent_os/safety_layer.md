# Safety Layer

Safety is not a switch — it is a *layered* set of policies, gates, and audit trails. A production agent without an explicit safety layer is an incident waiting to happen.

## The four pillars

1. **Least privilege** — the agent gets the smallest scope that lets it do the job
2. **Risk tiering** — every tool is labelled low / medium / high / critical
3. **Human approval** — high and critical actions require explicit human sign-off
4. **Audit logging** — every tool call, decision, and approval is recorded

## Tool risk levels

| Level | Examples | Approval | Logging |
|---|---|---|---|
| Low | Read-only search, summarization, format conversion | Not required | sampled |
| Medium | Drafting files, creating tickets, posting to staging | Sometimes | full |
| High | Sending email, modifying repos, running shell, calling production APIs | Required | full + alert |
| Critical | Deleting data, spending money, changing permissions, force-pushing | Always + 2nd reviewer | full + immutable |

📖 Detailed table: [safety/tool_risk_levels.md](../safety/tool_risk_levels.md)

## Guardrails

Guardrails are programmatic checks that run *around* the agent loop:

- **Input guardrails** — sanitize untrusted text (RAG, MCP outputs, web fetches)
- **Output guardrails** — block PII leaks, secrets, policy violations
- **Tool-call guardrails** — argument validation, dry-run checks, dangerous-pattern detection
- **Loop guardrails** — max iterations, timeouts, cost ceilings

📖 [safety/guardrails.md](../safety/guardrails.md)

## Human approval

When the agent proposes a high-risk action, pause and emit a structured **approval request** containing:

- The action and arguments
- The reasoning
- Reversibility / blast radius
- A confirmation token

Approvals must be **explicit** — auto-approving on timeout is the opposite of safety. See [templates/HUMAN_APPROVAL_POLICY.md.template](../templates/HUMAN_APPROVAL_POLICY.md.template).

## What a secure agent looks like

A secure-by-default agent has:

- ✅ A `GUARDRAILS.md` and a `HUMAN_APPROVAL_POLICY.md`
- ✅ Tools labelled by risk in `TOOLS.md`
- ✅ Read-only mode for any new tool until tested
- ✅ Audit log of all medium+ tool calls
- ✅ A safety eval suite that runs before each release
- ✅ A clear rollback / kill-switch

Checklist: [checklists/mcp_security_checklist.md](../checklists/mcp_security_checklist.md), [safety/secure_agent_checklist.md](../safety/secure_agent_checklist.md).
