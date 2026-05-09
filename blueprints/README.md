# Blueprints

End-to-end architectures for common agent shapes. Each blueprint includes use case, components, tools, memory, skills, safety, evals, deployment, and extensions.

## Index

| Blueprint | Use case |
|---|---|
| [research_agent.md](research_agent.md) | Sourced briefings on a topic |
| [coding_agent.md](coding_agent.md) | Reads issues, edits code, opens PRs |
| [customer_support_agent.md](customer_support_agent.md) | Tier-1 support with escalation |
| [data_analysis_agent.md](data_analysis_agent.md) | CSV / SQL → insights |
| [personal_assistant_agent.md](personal_assistant_agent.md) | Calendar, email, tasks |
| [multi_agent_team.md](multi_agent_team.md) | Planner + workers + reviewer |
| [rag_agent.md](rag_agent.md) | Retrieval-grounded Q&A |
| [mcp_agent.md](mcp_agent.md) | Agent built around MCP integrations |
| [secure_action_agent.md](secure_action_agent.md) | Agent that takes high-risk actions safely |

## How to use

1. Pick the closest blueprint
2. Copy the folder structure
3. Fill in templates from [/templates](../templates)
4. Wire skills from [/skills/examples](../skills/examples)
5. Walk the [release checklist](../templates/AGENT_RELEASE_CHECKLIST.md)

## What every blueprint has

- Use case + non-goals
- Architecture diagram
- Components
- Tools (with risk levels)
- Memory plan
- Skills used
- Safety controls
- Eval plan
- Deployment notes
- Extension ideas
