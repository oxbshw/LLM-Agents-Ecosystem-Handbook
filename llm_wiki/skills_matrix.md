# Skills matrix

Skills shipped with the handbook + how to think about adding more.

## Shipped examples

| Skill | When | Risk | Status |
|---|---|---|---|
| [research-summarizer](../skills/examples/research-summarizer/SKILL.md) | Multi-source briefings with citations | Low | example |
| [repo-auditor](../skills/examples/repo-auditor/SKILL.md) | Pre-PR audit | Low | example |
| [mcp-security-reviewer](../skills/examples/mcp-security-reviewer/SKILL.md) | Before connecting an MCP server | Medium (review only) | example |
| [agent-memory-curator](../skills/examples/agent-memory-curator/SKILL.md) | End-of-session memory distillation | Low | example |

## Skill design lookup

| Property | See |
|---|---|
| How to write a description that triggers correctly | [skills/skill_design_guide.md](../skills/skill_design_guide.md) |
| When NOT to make something a Skill | [skills/skill_vs_tool_vs_mcp.md](../skills/skill_vs_tool_vs_mcp.md) |
| Quality gate before merge | [checklists/skill_quality_checklist.md](../checklists/skill_quality_checklist.md) |
| Security review | [skills/security_checklist.md](../skills/security_checklist.md) |

## Anti-patterns to avoid

- Vague description ("helps with research")
- Long monolithic `SKILL.md` instead of references
- No success criteria
- Hard-coded project paths
- Skills with executable scripts but no security review
