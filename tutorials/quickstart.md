# Quickstart

Get value from this repo in about 10 minutes.

## 1. Clone

```bash
git clone https://github.com/oxbshw/LLM-Agents-Ecosystem-Handbook.git
cd LLM-Agents-Ecosystem-Handbook
```

## 2. Browse by intent

| You want to… | Open |
|---|---|
| Browse concepts | [agent_os/README.md](../agent_os/README.md) |
| Pick / wire a provider | [providers/README.md](../providers/README.md) → [providers/provider_matrix.md](../providers/provider_matrix.md) |
| Find a starting blueprint | [blueprints/](../blueprints/) |
| Copy templates | [templates/](../templates/) |
| Read curated skills | [skills/catalog/](../skills/catalog/) and [skills/examples/](../skills/examples/) |
| Read coding-agent prompts | [coding_agents/prompts/](../coding_agents/prompts/) |
| Improve a prompt | [prompt_engineering/](../prompt_engineering/) |
| Read a worked design doc | [design_docs/examples/](../design_docs/examples/) |
| See the LLM-readable index | [llms.txt](../llms.txt) |

## 3. Set up Python (only needed for runnable adapters)

```bash
python -m venv .venv
source .venv/bin/activate     # Windows: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
cp .env.example .env          # then fill in keys you need
```

## 4. Choose a provider

The handbook ships an `LLMProvider` abstraction across 24+ providers. Pick by need:

| Need | Try |
|---|---|
| Cheap classification | Groq, DeepSeek, OpenRouter cheap variants |
| Strong reasoning | Anthropic, OpenAI, Google Gemini |
| Fastest latency | Groq, Cerebras |
| Long context | Google Gemini Pro, Anthropic, MiniMax (M3, 512K) |
| Local / privacy | Ollama, LM Studio, vLLM |
| Vision | OpenAI, Google, Anthropic, xAI |
| Web-grounded research | Perplexity |

📖 [providers/model_selection_guide.md](../providers/model_selection_guide.md) • [providers/provider_matrix.md](../providers/provider_matrix.md)

## 5. Set env vars

```bash
# Pick one or more (full list in providers/env_vars.md):
export OPENAI_API_KEY=...
export ANTHROPIC_API_KEY=...
export GROQ_API_KEY=...
# Local? Set OLLAMA_BASE_URL or LMSTUDIO_BASE_URL — defaults to localhost.

# Default provider for the abstraction:
export LLM_PROVIDER=openai     # or anthropic, groq, ollama, etc.
```

## 6. Try the abstraction

```python
from utilities import get_provider, list_providers

# What's available?
for p in list_providers(family="fast"):
    print(p["name"], p["default_model"])

# Use one explicitly:
out = get_provider("groq").chat(
    [{"role": "user", "content": "Summarize MCP in one sentence."}],
    model="llama-3.1-8b-instant",
)
print(out["text"])
```

Or use the router (with fallback chains):

```python
from utilities.provider_router import ProviderRouter
router = ProviderRouter()
out = router.chat(
    [{"role": "user", "content": "Summarize this PR in 3 bullets."}],
    task_class="cheap",   # Groq → DeepSeek → Together → OpenRouter
)
print(out["_router"]["provider_used"])
```

📖 [providers/router_patterns.md](../providers/router_patterns.md)

## 7. Run an existing agent skeleton

Each agent in [`agents/`](../agents/) has a `README.md` and `main.py`. Pick one and follow its README.

```bash
cd agents/summarization_agent
# read README.md
python main.py
```

## How to add a new provider

1. Read [providers/provider_abstraction.md](../providers/provider_abstraction.md)
2. Add a `ProviderInfo(...)` entry to [`utilities/provider_config.py`](../utilities/provider_config.py)
3. Drop a minimal example in [`providers/examples/`](../providers/examples/)
4. Update [`.env.example`](../.env.example) and [`providers/env_vars.md`](../providers/env_vars.md)
5. Update [`providers/provider_matrix.md`](../providers/provider_matrix.md)

📖 [coding_agents/prompts/provider_expansion_prompt.md](../coding_agents/prompts/provider_expansion_prompt.md) — paste-able prompt

## How to add a new agent example

1. `python scripts/create_agent.py my_new_agent`
2. Fill `agents/my_new_agent/README.md` (use case, tools, risk levels, link to closest [blueprint](../blueprints/))
3. Drop the relevant template files from [/templates](../templates) (`AGENTS.md`, `SOUL.md`, …)
4. Walk [checklists/agent_design_checklist.md](../checklists/agent_design_checklist.md)

## How to add a new Skill

1. Copy [templates/SKILL.md.template](../templates/SKILL.md.template) into `skills/catalog/<your-skill>/SKILL.md`
2. Add references under `references/`
3. Walk [checklists/skill_quality_checklist.md](../checklists/skill_quality_checklist.md)
4. Update `skills/catalog/index.md`

## How to add a new MCP integration

1. Run [`mcp-security-reviewer`](../skills/examples/mcp-security-reviewer/SKILL.md)
2. Fill [templates/MCP_SERVER.md.template](../templates/MCP_SERVER.md.template) under `mcp/examples/<server>/`
3. Walk [checklists/mcp_security_checklist.md](../checklists/mcp_security_checklist.md)

## How to use this repo with a coding agent

1. Open the repo in Claude Code, Cursor, Codex, Aider, Cline, or your custom runtime
2. Point it at [`llms.txt`](../llms.txt) — that's the curated map
3. Use a prompt from [`coding_agents/prompts/`](../coding_agents/prompts/) for whatever task you have
4. Walk the relevant checklist before merging

## How to contribute

See [CONTRIBUTING.md](../CONTRIBUTING.md) and [checklists/open_source_quality_checklist.md](../checklists/open_source_quality_checklist.md).
