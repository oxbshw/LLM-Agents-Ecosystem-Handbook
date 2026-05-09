# Contributor notes (for LLMs)

Read this if you're a coding agent making a PR to this handbook.

## What good contributions look like

- One concept per PR
- Add concrete content (table, checklist, example) — not vague exposition
- Preserve existing valuable content
- Keep claims hedged where the ecosystem moves fast — link upstream

## Where to put new content

| New thing | Goes in |
|---|---|
| Concept doc on an Agent OS layer | `agent_os/` |
| New template | `templates/` |
| New Skill spec | `skills/examples/<name>/SKILL.md` (+ `references/`) |
| New blueprint | `blueprints/<name>.md` |
| New checklist | `checklists/` |
| New worked example | `examples/<name>/` |
| MCP server doc | `mcp/examples/<server>/` |
| Eval doc / dataset | `evals/` |

## Quality bar

- Markdown renders cleanly on GitHub (preview before opening PR)
- Internal links resolve (no broken paths)
- No fabricated facts about external projects
- No emojis unless the user requested them
- No CI badges that don't exist

## When you change major structure

- Update [README.md](../README.md) navigation
- Update [llms.txt](../llms.txt) and [llms-full.txt](../llms-full.txt)
- Update [llm_wiki/index.md](index.md)

## Style

- Tables > prose for comparisons
- Numbered steps > prose for workflows
- Bullets > paragraphs
- Short sentences

## What to avoid

- Don't add "Comprehensive guide" without committing to depth
- Don't restate text from other files; link instead
- Don't add a section just for SEO; add it because someone will use it
