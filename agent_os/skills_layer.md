# Skills Layer

A **Skill** is a reusable, model-loaded workflow described by a `SKILL.md` plus optional `scripts/` and `references/`. Skills are the unit of "how this agent does X repeatably."

## When something is a Skill

Use a Skill when the task:

1. Repeats across runs
2. Has more than one or two steps
3. Benefits from references (templates, examples, checklists)
4. Should produce consistent outputs

If it's a one-shot prompt, don't make it a Skill. If it's a single function call, make it a tool.

## Anatomy

```
skills/research-summarizer/
├── SKILL.md                ← name, when-to-use, workflow, IO
├── references/
│   ├── report-template.md
│   └── citation-style.md
└── scripts/                ← optional helpers (e.g. cite formatter)
```

The model reads `SKILL.md` first. References load only when relevant — this is **progressive disclosure**, the central design idea. A 50-page reference file does not bloat your context; it gets loaded only at the step that needs it.

## Skill design rules

1. **Triggering is everything.** The `description:` line in `SKILL.md` decides if the model picks it up. Be specific about *when* it applies.
2. **One Skill, one purpose.** Don't bundle "research + summarize + post-to-slack" into one Skill. Compose smaller Skills.
3. **Make it portable.** No project-specific paths in the Skill itself; pass them as inputs.
4. **Validate.** Define what "successful output" looks like in the Skill itself.
5. **Fail loudly.** If preconditions aren't met, the Skill should say so clearly, not silently degrade.

## Skill vs Tool vs MCP

See [skills/skill_vs_tool_vs_mcp.md](../skills/skill_vs_tool_vs_mcp.md). Short version:

- **Tool** = one function call
- **Skill** = a workflow the agent runs internally
- **MCP** = a standard for exposing tools/context across agents
