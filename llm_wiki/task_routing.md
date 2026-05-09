# Task routing (LLM wiki view)

When you're an LLM and someone hands you a task in this repo, route it through this map.

## "I want to …"

| Goal | Read in order |
|---|---|
| Build a new agent from scratch | [`/checklists/agent_design_checklist.md`](../checklists/agent_design_checklist.md) → closest [blueprint](../blueprints/) → fill [templates/](../templates/) → walk [release checklist](../templates/AGENT_RELEASE_CHECKLIST.md) |
| Add provider X | [`/coding_agents/prompts/provider_expansion_prompt.md`](../coding_agents/prompts/provider_expansion_prompt.md) → [providers/provider_abstraction.md](../providers/provider_abstraction.md) → edit [utilities/provider_config.py](../utilities/provider_config.py) |
| Pick a provider for task Y | [providers/model_selection_guide.md](../providers/model_selection_guide.md) → [providers/router_patterns.md](../providers/router_patterns.md) |
| Wire memory | [memory/README.md](../memory/README.md) → [memory/memory_distillation.md](../memory/memory_distillation.md) → [skills/examples/agent-memory-curator/SKILL.md](../skills/examples/agent-memory-curator/SKILL.md) |
| Add MCP integration | [skills/examples/mcp-security-reviewer/SKILL.md](../skills/examples/mcp-security-reviewer/SKILL.md) → [templates/MCP_SERVER.md.template](../templates/MCP_SERVER.md.template) → [checklists/mcp_security_checklist.md](../checklists/mcp_security_checklist.md) |
| Improve a system prompt | [prompt_engineering/system_prompt_design.md](../prompt_engineering/system_prompt_design.md) → [evals/prompt_evals.md](../evals/prompt_evals.md) → [checklists/agent_prompt_checklist.md](../checklists/agent_prompt_checklist.md) |
| Resist prompt injection | [prompt_engineering/prompt_injection_defense.md](../prompt_engineering/prompt_injection_defense.md) → [safety/prompt_injection.md](../safety/prompt_injection.md) → [evals/safety_evals.md](../evals/safety_evals.md) |
| Write a design doc / ADR | [design_docs/agent_design_doc.md](../design_docs/agent_design_doc.md) → [templates/DESIGN_DOC.md.template](../templates/DESIGN_DOC.md.template) → [templates/ADR.md.template](../templates/ADR.md.template) |
| Audit a repo | [skills/examples/repo-auditor/SKILL.md](../skills/examples/repo-auditor/SKILL.md) → [coding_agents/prompts/repo_audit_prompt.md](../coding_agents/prompts/repo_audit_prompt.md) |
| Open a clean PR | [skills/catalog/pr-summarizer/SKILL.md](../skills/catalog/pr-summarizer/SKILL.md) → [coding_agents/review_checklist.md](../coding_agents/review_checklist.md) |
| Run regression evals | [evals/eval_design.md](../evals/eval_design.md) → [evals/regression_evals.md](../evals/regression_evals.md) → [evals/examples/regression_eval_plan.md](../evals/examples/regression_eval_plan.md) |
| Roll out a change | [design_docs/rollout_plan.md](../design_docs/rollout_plan.md) → [checklists/production_readiness_checklist.md](../checklists/production_readiness_checklist.md) |

## Quick "where is X?"

- "What's MCP?" → [mcp/mcp_basics.md](../mcp/mcp_basics.md)
- "What's a Skill?" → [skills/README.md](../skills/README.md)
- "What's an Agent OS?" → [agent_os/README.md](../agent_os/README.md)
- "What providers exist?" → [providers/provider_matrix.md](../providers/provider_matrix.md)
- "What frameworks should I pick?" → [docs/framework_comparison.md](../docs/framework_comparison.md)
- "What goes in MEMORY.md?" → [templates/MEMORY.md.template](../templates/MEMORY.md.template)
- "What's a tool risk level?" → [safety/tool_risk_levels.md](../safety/tool_risk_levels.md)
- "How do I run an example?" → [tutorials/quickstart.md](../tutorials/quickstart.md)
