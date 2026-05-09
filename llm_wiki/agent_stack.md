# Agent stack

The modern agent in one page.

```
┌────────────────────────────────────────────────────────┐
│ Deployment   Docker / serverless / workers / web       │
├────────────────────────────────────────────────────────┤
│ Observability  traces · spans · cost · latency · evals │
├────────────────────────────────────────────────────────┤
│ Safety       guardrails · approvals · policies         │
├────────────────────────────────────────────────────────┤
│ Identity     SOUL.md · AGENTS.md · USER.md             │
├────────────────────────────────────────────────────────┤
│ Skills       SKILL.md (+ references, scripts)          │
├────────────────────────────────────────────────────────┤
│ Memory       MEMORY.md · semantic · episodic · user    │
├────────────────────────────────────────────────────────┤
│ MCP          standardized external tools + context     │
├────────────────────────────────────────────────────────┤
│ Tools        function calling                          │
├────────────────────────────────────────────────────────┤
│ Orchestration agent loops · planning · handoffs        │
├────────────────────────────────────────────────────────┤
│ Model        provider + model + caching                │
└────────────────────────────────────────────────────────┘
```

Each layer is its own concern, its own folder in this handbook, and its own file types in your workspace.

## What changed in modern agents

- **Identity files** — emerging `AGENTS.md` standard across tools
- **Skills** — workflows-as-files with progressive disclosure
- **MCP** — standardized integration layer
- **Risk-tiered tools** — every tool gets a label
- **Out-of-band approvals** — never inside the model loop
- **Observability is mandatory** — not "we'll add it later"
- **Evals as release gates** — regression + safety blocks ship

## What stayed the same

- The model is the model. Still hallucinates, still benefits from grounding.
- Smaller scope = better outputs.
- Tests beat opinions.
