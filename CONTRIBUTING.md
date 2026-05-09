# Contributing

Thank you for considering a contribution. This handbook aims to be the *practical* operating manual for modern LLM agents — your contributions help that.

## What we want

- New blueprints, templates, checklists, examples, Skills, MCP integration docs
- Updates to the framework matrix as the ecosystem evolves
- Better diagrams, tables, and decision flowcharts
- Translations
- Fixes to broken links, stale facts, formatting

## What we don't want

- Pure link-list additions without context
- Hyped claims without evidence
- Vendor marketing content
- Large untested code drops
- Files added without updating the navigation ([README.md](README.md), [llms.txt](llms.txt), [llm_wiki/index.md](llm_wiki/index.md))

## Workflow

1. **Open an issue first** for anything non-trivial. Reference an [issue template](.github/ISSUE_TEMPLATE/).
2. **Fork → branch → PR.** Use the [PR template](.github/PULL_REQUEST_TEMPLATE.md).
3. **One concept per PR.** Easier to review, faster to merge.
4. **Walk the quality checklist**: [checklists/open_source_quality_checklist.md](checklists/open_source_quality_checklist.md).

## Quality bar

- Markdown renders cleanly on GitHub (preview your PR)
- Internal links resolve
- No fabricated facts about external projects (link to upstream docs)
- Hedge claims where the ecosystem moves fast
- No emojis added unless the user requested them (we keep the tone professional)
- No CI badges that don't have a real pipeline behind them

## Adding examples

When adding code:

- Keep it simple, no surprise dependencies
- Use environment variables — never hardcode keys
- Add an [.env.example](.env.example) entry if a new key is required
- Document any paid services as optional

## Adding Skills, MCP integrations, blueprints

Each has a checklist:

- Skills: [checklists/skill_quality_checklist.md](checklists/skill_quality_checklist.md)
- MCP: [checklists/mcp_security_checklist.md](checklists/mcp_security_checklist.md)
- Blueprints: follow the structure of an existing one in [blueprints/](blueprints/)

## Generating new agent skeletons

Use [`scripts/create_agent.py`](scripts/create_agent.py) for a consistent starter. Then fill in `AGENTS.md`, `SOUL.md`, and `TOOLS.md` from [/templates](templates/).

## Code of Conduct

Be respectful. See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

## License

By contributing you agree your contributions are MIT-licensed.
