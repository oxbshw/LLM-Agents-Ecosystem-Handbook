# Skill catalog index

Curated skills in this repo. Status follows [skill_maturity_model.md](../skill_maturity_model.md).

| Skill | Category | Use case | Inputs | Outputs | Risk | Status |
|---|---|---|---|---|---|---|
| [research-summarizer](../examples/research-summarizer/SKILL.md) | Research | Sourced multi-source briefings | topic, depth | briefing.md | Low | beta |
| [repo-auditor](../examples/repo-auditor/SKILL.md) | Engineering | Pre-PR audit of changed code | base ref | audit report | Low | beta |
| [mcp-security-reviewer](../examples/mcp-security-reviewer/SKILL.md) | Agent ops | Review an MCP server before connecting | repo URL, version | filled MCP_SERVER.md | Medium | beta |
| [agent-memory-curator](../examples/agent-memory-curator/SKILL.md) | Memory | Promote episodic notes → semantic memory | since, categories | MEMORY.md diff | Low | beta |
| [api-design-reviewer](api-design-reviewer/SKILL.md) | Engineering | Review proposed REST/GraphQL designs | OpenAPI / schema | review notes | Low | experimental |
| [pr-summarizer](pr-summarizer/SKILL.md) | Engineering | Produce a clean PR description | branch, base | PR body | Low | experimental |
| [adr-writer](adr-writer/SKILL.md) | Design | Capture an architecture decision | context, options | ADR-NNNN.md | Low | experimental |
| [incident-postmortem](incident-postmortem/SKILL.md) | Ops / SRE | Draft a blameless postmortem | incident notes | postmortem.md | Low | experimental |
| [sprint-planner](sprint-planner/SKILL.md) | Product / PM | Turn intake into a planned sprint | tickets, capacity | sprint plan | Low | experimental |
| [dataset-profiler](dataset-profiler/SKILL.md) | Data | Profile a dataset end-to-end | file path | report.md | Low | experimental |

**Categories**: see [categories.md](categories.md). **Submit a skill**: see [README.md](README.md).

## Notes

- Skills are intentionally generic. Project-specific variants belong in your `.agent/skills/`.
- Each skill is self-contained; reference files are loaded progressively per [skill_packaging.md](../skill_packaging.md).
