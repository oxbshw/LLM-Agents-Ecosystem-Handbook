# Agent Release Checklist

Use this gate before shipping any version of an agent to production.

## Identity & instructions
- [ ] `SOUL.md` reviewed and current
- [ ] `AGENTS.md` matches current repo conventions
- [ ] `USER.md` reflects target user, not previous one

## Memory
- [ ] `MEMORY.md` distilled (no transcripts)
- [ ] No PII / secrets in any memory file
- [ ] Memory expiry policy in place
- [ ] Memory eval suite passes

## Skills
- [ ] Each Skill has clear `when to use` + `when NOT to use`
- [ ] No project-specific paths hard-coded in Skills
- [ ] Each Skill has at least one example and one failure mode documented

## Tools / MCP
- [ ] Every tool labelled with risk level in `TOOLS.md`
- [ ] All MCP servers reviewed against `checklists/mcp_security_checklist.md`
- [ ] MCP server versions pinned
- [ ] Approval gates wired for High / Critical tools

## Safety
- [ ] `GUARDRAILS.md` current
- [ ] `HUMAN_APPROVAL_POLICY.md` current
- [ ] Refusal eval passes
- [ ] Prompt-injection eval passes for known vectors
- [ ] Audit logging verified end-to-end

## Observability
- [ ] Traces emit for every run
- [ ] Cost / latency dashboards reachable
- [ ] Alerting in place for: cost spike, repeated guardrail trips, error rate

## Evals
- [ ] Regression eval ≥ baseline
- [ ] Tool-call eval ≥ baseline
- [ ] Memory eval ≥ baseline
- [ ] Safety eval = 100% on criticals
- [ ] Eval report archived under `evals/runs/{{release-tag}}/`

## Deploy
- [ ] Rollback plan written (one paragraph)
- [ ] Kill switch tested
- [ ] On-call knows about the release
- [ ] CHANGELOG.md updated
