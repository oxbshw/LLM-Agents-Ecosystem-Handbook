# Coding-agent guide (LLM wiki view)

For the LLM coding agent dropping into this repo. Compact orientation.

## In 30 seconds

- This repo is a **handbook** — most files are documentation, not code
- Code lives mainly in [`utilities/`](../utilities/) (provider abstraction) and [`providers/examples/`](../providers/examples/)
- Skill specs live in [`skills/examples/<name>/SKILL.md`](../skills/examples/) and [`skills/catalog/<name>/SKILL.md`](../skills/catalog/)
- Templates live in [`templates/`](../templates/)
- See [`llms.txt`](../llms.txt) for the curated index

## How to do common tasks

| Task | First read | Then |
|---|---|---|
| Add a provider | [`coding_agents/prompts/provider_expansion_prompt.md`](../coding_agents/prompts/provider_expansion_prompt.md) | edit [`utilities/provider_config.py`](../utilities/provider_config.py); add example |
| Add a skill | [`templates/SKILL.md.template`](../templates/SKILL.md.template) | place under `skills/catalog/<name>/`; update catalog index |
| Add an MCP doc | [`templates/MCP_SERVER.md.template`](../templates/MCP_SERVER.md.template) | place under `mcp/examples/<server>/`; update catalog |
| Audit the repo | [`coding_agents/prompts/repo_audit_prompt.md`](../coding_agents/prompts/repo_audit_prompt.md) | run skill `repo-auditor` if installed |
| Modernize a stale section | [`coding_agents/prompts/modernization_prompt.md`](../coding_agents/prompts/modernization_prompt.md) | walk MIGRATION_PLAN-style |
| Update docs | [`coding_agents/prompts/docs_update_prompt.md`](../coding_agents/prompts/docs_update_prompt.md) | update README + llms.txt navigation |
| Pre-release review | [`coding_agents/prompts/release_review_prompt.md`](../coding_agents/prompts/release_review_prompt.md) | walk production_readiness_checklist |

## Hard rules when contributing

- Preserve existing valuable content
- One concept per PR
- No fabricated facts about external projects (link upstream)
- No fake CI badges
- No `TODO` / `FIXME` / `lorem` / `placeholder` shipped
- No external folder paths in committed docs
- No real API keys
- All new internal links resolve before merge

## Files coding agents read first

- `README.md` (humans + agents)
- `AGENTS.md` (the project's own — this repo's `AGENTS.md` template lives at [`/templates/AGENTS.md.template`](../templates/AGENTS.md.template); the repo doesn't ship its own AGENTS.md because it's a handbook, not a buildable app)
- `llms.txt` (curated index)
- `llm_wiki/index.md` (this folder)

## Tool neutrality

This guide is tool-neutral. Specific harness notes: [`coding_agents/claude_code.md`](../coding_agents/claude_code.md), [`coding_agents/cursor.md`](../coding_agents/cursor.md), [`coding_agents/codex.md`](../coding_agents/codex.md).
