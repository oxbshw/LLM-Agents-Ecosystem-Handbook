# Skill-enabled research agent (example)

A research agent built around Skills + a small set of tools. See blueprint: [/blueprints/research_agent.md](../../blueprints/research_agent.md).

## What you'd copy

- `SOUL.md`, `AGENTS.md`, `MEMORY.md`, `TOOLS.md` from [agent_os/examples/research_agent_workspace/](../../agent_os/examples/research_agent_workspace/)
- Skills from [skills/examples/research-summarizer/](../../skills/examples/research-summarizer/) and [skills/examples/agent-memory-curator/](../../skills/examples/agent-memory-curator/)

## Wiring (sketch)

```python
from utilities.llm_provider import complete
# ... your framework of choice (LangGraph / OpenAI Agents SDK / Pydantic AI / …)

agent = build_agent(
    instructions=load("SOUL.md") + "\n" + load("AGENTS.md"),
    tools=[web_search, fetch_url, read_pdf, write_file],
    skills_dir="skills/",
)

briefing = agent.run({"task": "Brief me on the state of MCP adoption in 2026", "depth": "shallow"})
```

## What's actually doing the work

1. The Skill tells the model *how* to research (plan → search → fetch → cluster → draft → validate)
2. The references inside the Skill carry templates and rules (loaded only when needed)
3. Tools are dumb but well-scoped (fetch is allow-listed, write is to one file)
4. Memory keeps per-domain learnings across runs

## Smoke test

- Set provider env vars (`.env.example` at repo root)
- Run the agent with a simple topic
- Confirm: ≥ 5 sources, ≥ 3 distinct domains, every claim has a citation
