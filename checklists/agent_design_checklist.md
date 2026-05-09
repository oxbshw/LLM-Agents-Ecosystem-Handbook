# Agent design checklist

Before you write the first prompt:

## Scope
- [ ] Use case in one sentence
- [ ] Non-goals listed
- [ ] Closest existing blueprint identified
- [ ] Success criteria written down (what does "good" look like?)

## Identity
- [ ] `SOUL.md` drafted (identity, voice, values, refusal style)
- [ ] `AGENTS.md` drafted (project conventions)
- [ ] `USER.md` drafted (who's actually using this)

## Tools / capabilities
- [ ] Smallest set of tools to solve the task
- [ ] Each tool risk-tiered
- [ ] Approval gates picked (which tools need them)
- [ ] Forbidden actions enumerated

## Memory
- [ ] What persists across runs vs what stays ephemeral
- [ ] Per-user vs per-project scope
- [ ] What does NOT go in memory (PII, secrets) explicit

## Skills
- [ ] Repeatable workflows identified
- [ ] Each Skill has a specific "use when" trigger
- [ ] References that load progressively

## MCP
- [ ] Existing MCP server can do the integration? Use it.
- [ ] Otherwise: plain function calling
- [ ] If new server: sized appropriately, version pinned

## Safety
- [ ] `GUARDRAILS.md` outlined
- [ ] Approval policy outlined
- [ ] Adversarial cases listed (what could go wrong, what could be tried)

## Observability
- [ ] Tracing backend chosen
- [ ] Cost / latency budget per run
- [ ] Failure modes named

## Evals
- [ ] Eval suites planned (regression, tool-call, memory, safety)
- [ ] Pass thresholds chosen
- [ ] CI hook planned

If you can't tick most of these, you're not ready to write the prompt yet.
