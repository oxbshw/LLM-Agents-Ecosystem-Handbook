# Agent design doc

A short, opinionated structure for designing one agent. Different from a generic technical design doc because agents have unique surfaces (identity, memory, tools, skills, MCP, safety, evals).

## Sections

### 1. Use case (1 paragraph)
What the agent does and for whom. Concrete enough that "would this user be happy?" has a yes/no answer.

### 2. Non-goals (3–7 bullets)
What the agent will NOT do. This is more important than the goals.

### 3. Architecture (diagram + paragraph)
High-level component diagram. Inputs, outputs, internal flow.

### 4. Components

| Layer | Choice | Why |
|---|---|---|
| Identity | `SOUL.md` voice / values | … |
| Memory | per-user / per-project / vector / etc. | … |
| Skills | which Skills load | … |
| Tools | risk-tiered list | … |
| MCP | which servers | … |
| Provider | default + fallback chain | … |

### 5. Tools — risk table
The full `TOOLS.md`-style table for this agent: tool, purpose, risk, approval.

### 6. Safety controls
Guardrails (input / output / tool-call / loop), approval gates, audit logging, kill switch.

### 7. Eval plan
Suites that will run before each release: regression, tool-call, memory, MCP, safety. Pass thresholds.

### 8. Cost / latency budget
Per-run target. Cost ceiling. Latency p95.

### 9. Rollout plan
Stages (internal → small users → all). Kill switch. Rollback.

### 10. Risks + mitigations
Top 5 risks with concrete mitigations.

### 11. Open questions
Things to decide before launch.

## Tips

- Lead with non-goals — that's where most over-promising shows up
- The architecture diagram is one square per major component, not one per class
- Risk tables are non-optional for High/Critical-tool agents
- An "open questions" section is honest. Empty open-questions = optimistic doc

## Pair with

- [`agent_os/`](../agent_os/) for layer concepts
- [`/templates/DESIGN_DOC.md.template`](../templates/DESIGN_DOC.md.template) for the file shape
- [`examples/`](examples/) for filled examples
