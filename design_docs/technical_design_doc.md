# Technical design doc

For non-agent technical work, the classic shape still applies. We don't reinvent it; we add the "AI-shaped" considerations that often go missing.

## Sections

### 1. Background
What we're solving and why now.

### 2. Goals + Non-goals
Both.

### 3. Proposed design
Diagram + prose.

### 4. Alternatives considered
At least two. Each with one-line "why not."

### 5. API / Interface
Surfaces — RPC, REST, library, CLI, SDK.

### 6. Data model
Schema, retention, isolation.

### 7. Failure modes
What happens when things go wrong.

### 8. Performance
Latency, throughput, cost.

### 9. Security
Threat model, AuthN/AuthZ, secrets, PII.

### 10. Observability
Traces, metrics, logs, alerts.

### 11. Rollout
Stages, kill switch, rollback.

### 12. Open questions
Honest list.

## AI-shaped additions

When the system uses or is used by LLMs, also include:

- **Provider strategy**: which provider(s), which fallbacks, why
- **Cost ceilings**: per-request, per-user, daily total
- **Prompt versioning**: where prompts live, who can change them, eval gates
- **Memory model**: where it lives, how it's curated, isolation
- **Eval plan**: regression / safety / quality thresholds
- **Injection surface**: where untrusted content enters, how it's sanitized

If you skip any of these, expect to retrofit them after an incident.

## Length

Aim for 2–6 pages. Longer = the design probably needs to be smaller.

## Pair with

- [`/templates/DESIGN_DOC.md.template`](../templates/DESIGN_DOC.md.template)
- [`adr_guide.md`](adr_guide.md) — record the *decisions* the design produces
