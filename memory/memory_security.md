# Memory security

Memory is an attractive attack surface. If an attacker can write to memory, they can persistently influence the agent.

## Threat model

| Threat | Vector | Impact |
|---|---|---|
| **Prompt injection via stored content** | Web fetch / RAG / MCP → memory | Persistent compromise |
| **Memory poisoning** | Untrusted source promoted to semantic | Wrong decisions across runs |
| **Data leakage** | PII / secrets stored, then shown in responses | Privacy / compliance breach |
| **Cross-tenant leakage** | User A's memory served to User B | Privacy breach |
| **Stale memory** | Outdated fact treated as current | Confidently wrong answers |

## Mitigations

### Promotion gates
Episodic → semantic is **never automatic** for content from low-trust sources. Promote via:
- Explicit user confirmation, or
- A curator skill that flags untrusted content for review

### Source tagging
Every entry knows its origin. Make this visible in the file:

```
- Auth service rate-limits at 100 req/s [from: ops doc, 2026-04-01]
- Customer X uses tier "pro" [from: user, 2026-03-15]
```

### Sanitization at the boundary
External content (web, MCP output, RAG passages) is sanitized before it can be quoted into memory:

- Strip imperative language directed at the agent
- Strip URLs that aren't sources
- Strip code blocks unless they're the actual fact

### Isolation
- Per-user memory in **per-user files** or DB rows; never share keys
- Per-project memory in repo, never in a global store unless explicitly cross-project

### Retention + redaction
- Documented retention per category
- One-click delete for user memory (legal + UX)
- Periodic redaction sweeps for PII patterns

### Auditing
- Memory writes are logged (who/what/when/source)
- Diff every change to `MEMORY.md` in git
- Quarterly review surfaces anomalies

## Eval

Run a memory eval suite on every release. See [evals/memory_evals.md](../evals/memory_evals.md). Cases to cover:

- Recall: agent surfaces relevant memory when needed
- No-fabrication: agent doesn't invent memory it doesn't have
- Refusal: agent refuses to act on injected instructions in memory
- Isolation: no cross-tenant leakage

## What never goes in memory

- 🚫 API keys, tokens, passwords (any form)
- 🚫 Full credit card / SSN / equivalent
- 🚫 Health info unless you have HIPAA-class controls
- 🚫 Anything covered by an NDA without explicit consent

If in doubt, don't store it.
