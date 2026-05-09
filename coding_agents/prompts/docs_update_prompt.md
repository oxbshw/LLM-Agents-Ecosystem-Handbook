# Docs update prompt

```text
You are updating the documentation.

TASK
{{Describe the doc change — e.g., "MCP server X just shipped, update mcp/mcp_server_catalog.md and llm_wiki/mcp_matrix.md"}}

WORKFLOW
1. Identify every file that references the topic (grep + Read).
2. Plan the smallest set of edits that keeps the docs consistent.
3. Edit. Cross-reference any other doc that should link here.
4. Update navigation:
   - README.md (if the topic is user-visible)
   - llms.txt and llms-full.txt (if a major doc was added/moved)
   - llm_wiki/index.md (if it changes "where to read what")
5. Verify all internal links resolve.

CONSTRAINTS
- Don't fabricate facts about external projects. Link to upstream docs.
- Hedge claims where the ecosystem moves fast.
- Keep the tone professional, no marketing language.
- No emojis added unless the user asked for them.
- Markdown must render cleanly on GitHub.

VERIFICATION
- All new/modified internal links resolve
- No `TODO` / `FIXME` shipped
- No external folder paths in committed files
- Navigation files (README, llms.txt) reflect the change
```
