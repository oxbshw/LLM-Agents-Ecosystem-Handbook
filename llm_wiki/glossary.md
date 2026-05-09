# Glossary

Definitions used consistently across the handbook.

| Term | Definition |
|---|---|
| **Agent** | An LLM-driven system that takes goals, plans, calls tools, and produces outcomes — beyond a single prompt-response. |
| **Agent OS** | The set of files, conventions, and runtime layers that make an agent reliable across runs. |
| **AGENTS.md** | Repo-specific instructions any coding agent reads when working in the project. |
| **SOUL.md** | Agent identity, voice, mission, refusal style. |
| **USER.md** | User profile and preferences. |
| **MEMORY.md** | Index of durable, distilled facts — not transcripts. |
| **TOOLS.md** | Inventory of tools with risk levels and approval gates. |
| **Tool** | One function the agent can invoke. |
| **Skill** | A reusable, model-loaded *workflow* described by `SKILL.md` + references + scripts. |
| **MCP (Model Context Protocol)** | Open standard for exposing tools, resources, and prompts to any compliant agent client. |
| **Guardrail** | Programmatic check around the agent loop (input / output / tool-call / loop). |
| **Approval gate** | Out-of-band human (or 2nd-reviewer) confirmation required for High/Critical actions. |
| **Risk level** | Low / Medium / High / Critical — drives approval and logging policy. |
| **Trace** | Tree of spans capturing one agent run for debugging. |
| **Span** | A single timed unit of work in a trace (model call, tool call, guardrail, etc.). |
| **Eval** | Automated test against an agent's behavior — regression, tool-call, memory, MCP, safety, quality. |
| **Episodic memory** | Per-event records (`logs/episodic/`). |
| **Semantic memory** | Distilled, generalized facts (`MEMORY.md`, `memory/semantic/`). |
| **Distillation** | Turning episodic notes into durable semantic memory entries. |
| **Memory poisoning** | Attacker plants malicious "memories" via untrusted content. |
| **Indirect prompt injection** | Untrusted content the agent consumes contains instructions the model follows. |
| **Progressive disclosure** | Loading detailed references only at the step that needs them; keeps Skill specs short. |
| **Blueprint** | An end-to-end agent architecture for a common shape (research, coding, etc.). |
