# Blueprint: Customer support agent

## Use case
Tier-1 support: answer common questions, look up account state, escalate when needed.

## Non-goals
- Refunds / billing actions without human approval
- Account changes (passwords, ownership, plan downgrades) without auth
- Legal/compliance commitments

## Architecture

```
user message
    │
    ▼
[classifier]  ── intent, sentiment, account?
    │
    ▼
[retriever]   ── docs MCP / KB
    │
    ▼
[responder]   ── grounded answer
    │
    ▼  (if action requested)
[actuator]    ── account-read tools, ticket create
    │
    ▼  (if escalation)
[escalator]   ── handoff with summary
```

## Tools

| Tool | Risk |
|---|---|
| `docs.search`, `docs.get` (internal MCP) | Low |
| `account.read(user_id)` | Medium (auth required) |
| `ticket.create` | Medium |
| `ticket.assign(team)` | Medium |
| `email.send` (canned) | High (template allow-list) |
| `refund.issue` | Critical (always handoff) |

## Memory
- `USER.md`: tone preferences, language
- Per-user memory: prior tickets, plan, known issues — strict isolation
- `MEMORY.md#project`: known incidents, current outages

## Skills
- A custom `escalation-summarizer` (write a clean handoff)
- `agent-memory-curator` for end-of-shift distillation

## Safety
- Per-user isolation eval (no cross-tenant)
- Refusal style for OOS asks ("I can't process refunds — let me get a human")
- PII redaction in logs and traces
- Output filter against secret patterns

## Evals
- Intent classification accuracy
- Grounding (every fact cited to a doc)
- Escalation correctness (escalates when it should, doesn't otherwise)
- Refusal style adherence
- Per-tenant isolation

## Deployment
- Behind your existing auth; agent never sees raw credentials
- Streaming responses for conversational latency
- Daily quality review on a sampled trace set

## Extensions
- Voice channel
- Outbound proactive notifications (gated)
- Team-coach mode: summarize trends to product team
