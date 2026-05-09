# Index — for LLMs reading this repo

You are a coding agent reading this handbook. Start here.

## What this repo is

A practical, production-oriented manual for modern LLM agent systems. It bundles concepts, templates, blueprints, runnable provider adapters, curated skills, prompt engineering patterns, coding-agent workflows, and design docs.

## What to read first (depending on the task)

| Task | Read |
|---|---|
| Understand the repo | [README.md](../README.md), then [agent_os/README.md](../agent_os/README.md) |
| Pick / wire a provider | [providers/README.md](../providers/README.md), [providers/provider_matrix.md](../providers/provider_matrix.md), [providers/router_patterns.md](../providers/router_patterns.md) |
| Add a new provider | [coding_agents/prompts/provider_expansion_prompt.md](../coding_agents/prompts/provider_expansion_prompt.md) + [providers/provider_abstraction.md](../providers/provider_abstraction.md) |
| Design a new agent | [checklists/agent_design_checklist.md](../checklists/agent_design_checklist.md), then closest [blueprint](../blueprints/) |
| Add a Skill | [skills/skill_design_guide.md](../skills/skill_design_guide.md), [templates/SKILL.md.template](../templates/SKILL.md.template), [checklists/skill_quality_checklist.md](../checklists/skill_quality_checklist.md) |
| Add an MCP integration | [mcp/mcp_security.md](../mcp/mcp_security.md), [skills/examples/mcp-security-reviewer/SKILL.md](../skills/examples/mcp-security-reviewer/SKILL.md), [checklists/mcp_security_checklist.md](../checklists/mcp_security_checklist.md) |
| Set up memory | [memory/README.md](../memory/README.md), [memory/memory_distillation.md](../memory/memory_distillation.md), [checklists/memory_safety_checklist.md](../checklists/memory_safety_checklist.md) |
| Wire safety | [safety/README.md](../safety/README.md), [safety/secure_agent_checklist.md](../safety/secure_agent_checklist.md) |
| Improve a prompt | [prompt_engineering/agent_prompt_patterns.md](../prompt_engineering/agent_prompt_patterns.md), [checklists/agent_prompt_checklist.md](../checklists/agent_prompt_checklist.md) |
| Defend against injection | [prompt_engineering/prompt_injection_defense.md](../prompt_engineering/prompt_injection_defense.md), [safety/prompt_injection.md](../safety/prompt_injection.md) |
| Use a coding agent on this repo | [llms.txt](../llms.txt), [coding_agents/README.md](../coding_agents/README.md), [coding_agents/prompts/](../coding_agents/prompts/) |
| Write a design doc / ADR | [design_docs/agent_design_doc.md](../design_docs/agent_design_doc.md), [templates/DESIGN_DOC.md.template](../templates/DESIGN_DOC.md.template), [templates/ADR.md.template](../templates/ADR.md.template) |
| Write evals | [evals/eval_design.md](../evals/eval_design.md), [evals/examples/](../evals/examples/), [evals/prompt_evals.md](../evals/prompt_evals.md) |
| Ship | [checklists/production_readiness_checklist.md](../checklists/production_readiness_checklist.md), [templates/AGENT_RELEASE_CHECKLIST.md](../templates/AGENT_RELEASE_CHECKLIST.md), [design_docs/rollout_plan.md](../design_docs/rollout_plan.md) |

## Where concepts live

- **`SOUL.md` / `AGENTS.md` / `USER.md`** — [agent_os/agent_identity.md](../agent_os/agent_identity.md) + [/templates](../templates)
- **`MEMORY.md`** — [memory/](../memory/) + [/templates/MEMORY.md.template](../templates/MEMORY.md.template)
- **`TOOLS.md`** — [/templates/TOOLS.md.template](../templates/TOOLS.md.template) + [safety/tool_risk_levels.md](../safety/tool_risk_levels.md)
- **Skills** — [skills/](../skills/) + [/templates/SKILL.md.template](../templates/SKILL.md.template)
- **MCP** — [mcp/](../mcp/) + [/templates/MCP_SERVER.md.template](../templates/MCP_SERVER.md.template)
- **Providers** — [providers/](../providers/) + [utilities/llm_provider.py](../utilities/llm_provider.py)
- **System prompts** — [prompt_engineering/system_prompt_design.md](../prompt_engineering/system_prompt_design.md) + [/templates/SYSTEM_PROMPT.md.template](../templates/SYSTEM_PROMPT.md.template)
- **Design docs / ADRs** — [design_docs/](../design_docs/) + [/templates/DESIGN_DOC.md.template](../templates/DESIGN_DOC.md.template) + [/templates/ADR.md.template](../templates/ADR.md.template)
- **Coding agents** — [coding_agents/](../coding_agents/) + [/templates/CODING_AGENT_TASK.md.template](../templates/CODING_AGENT_TASK.md.template)
- **Guardrails / approvals** — [/templates/GUARDRAILS.md.template](../templates/GUARDRAILS.md.template) + [/templates/HUMAN_APPROVAL_POLICY.md.template](../templates/HUMAN_APPROVAL_POLICY.md.template)
- **Tracing / spans** — [observability/tracing.md](../observability/tracing.md) + [observability/spans.md](../observability/spans.md)
- **LLM-readable docs pattern** — [docs/llm_readable_docs.md](../docs/llm_readable_docs.md), [llm_wiki/wiki_pattern.md](wiki_pattern.md)

## How to contribute (as a coding agent)

1. Walk [checklists/open_source_quality_checklist.md](../checklists/open_source_quality_checklist.md)
2. Place new content in the right directory (use the file map above)
3. Update [llms.txt](../llms.txt) and [llms-full.txt](../llms-full.txt) when major sections are added
4. Update [README.md](../README.md) navigation if user-visible structure changed
5. Open one PR per concept

## How to add an example

- Copy the closest existing example folder
- Replace `{{placeholders}}` with realistic content
- Document risk levels in `TOOLS.md`
- Add at least one paragraph in the README about non-goals

## How to update framework comparisons

- Modify [docs/framework_comparison.md](../docs/framework_comparison.md) and the matrix in [llm_wiki/framework_matrix.md](framework_matrix.md)
- Hedge when facts change month-to-month — link the upstream docs
- Don't remove an entry just because something newer launched; update with a "best for" note

## What NOT to do

- Don't duplicate content — link instead
- Don't add CI badges that don't exist
- Don't change the conventions in [/templates](../templates) without bumping versions
- Don't write LLM-judge prompts that include the answer
- Don't reference `F:\…` external folder paths in any committed doc
