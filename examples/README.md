# Examples

End-to-end agent workspaces you can read and adapt. Documentation-first — most examples are READMEs + filled templates, not full runtimes.

## Index

| Example | What it shows |
|---|---|
| [agent_workspace_minimal/](agent_workspace_minimal/) | Smallest viable Agent OS workspace |
| [agent_workspace_production/](agent_workspace_production/) | Full layout with safety + evals |
| [skill_enabled_research_agent/](skill_enabled_research_agent/) | Research agent that uses Skills |
| [memory_enabled_assistant/](memory_enabled_assistant/) | Persistent assistant with memory layer |
| [mcp_enabled_coding_agent/](mcp_enabled_coding_agent/) | Coding agent built around MCP |
| [guarded_action_agent/](guarded_action_agent/) | Agent with risk-tiered tool gating |
| [traced_agent_run/](traced_agent_run/) | What a real trace looks like |

Also see the existing [`agents/`](../agents/) folder for 100+ task-specific scaffolds.

## How to adapt one

1. Copy the folder
2. Fill the templates (see [/templates](../templates))
3. Wire your runtime — most examples are framework-agnostic
4. Walk the [release checklist](../templates/AGENT_RELEASE_CHECKLIST.md) before turning it loose
