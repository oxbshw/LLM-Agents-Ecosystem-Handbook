# Open-source quality checklist

For PRs to *this* handbook (and a useful template for any open-source repo).

## PR basics
- [ ] One concept per PR
- [ ] Title describes the change in < 70 chars
- [ ] Description: what + why + how to verify
- [ ] Linked to an issue if applicable

## Content quality
- [ ] Existing content preserved unless broken or obsolete (with reason)
- [ ] No fabricated facts about external projects (link to their docs)
- [ ] Claims hedged where the ecosystem moves fast
- [ ] No emojis added unless requested
- [ ] Markdown renders cleanly on GitHub

## Links + paths
- [ ] All internal links resolve
- [ ] No `your-username/...` placeholders
- [ ] External URLs are HTTPS and current

## Style
- [ ] Tables / checklists / diagrams used where useful
- [ ] Sections are short and scannable
- [ ] Tone: practical, professional, not hyped

## Files
- [ ] No secrets / API keys
- [ ] No huge binaries
- [ ] New files placed in the right directory

## Tests / examples
- [ ] If adding code: minimal, env-var-based, no hardcoded keys
- [ ] If adding a Skill: walks [skill_quality_checklist](skill_quality_checklist.md)
- [ ] If adding an MCP integration: walks [mcp_security_checklist](mcp_security_checklist.md)

## Updates
- [ ] CHANGELOG.md updated
- [ ] README navigation updated if structure changed
- [ ] [llm_wiki/index.md](../llm_wiki/index.md) updated if major sections added
