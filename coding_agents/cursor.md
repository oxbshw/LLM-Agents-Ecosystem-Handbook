# Cursor

Cursor is an IDE-integrated coding agent. The handbook's files (`AGENTS.md`, `SOUL.md`, etc.) work; you map them to Cursor's loading conventions.

## What Cursor reads

| File | Purpose |
|---|---|
| `.cursor/rules/*.mdc` | Modern rules format (replaces `.cursorrules`) |
| `.cursorrules` | Legacy single-file rules — still works |
| `AGENTS.md` | Increasingly read by default in agent mode |

## Mapping

| Handbook file | Cursor location |
|---|---|
| `AGENTS.md` | Reuse directly, or copy contents into `.cursor/rules/repo.mdc` |
| `SOUL.md` | Inline into `.cursor/rules/identity.mdc` |
| Skills | Cursor reads them when referenced from rules / chats |
| `TOOLS.md` | Documented surface; manually mirror critical tools into Cursor's allowlist |

## Patterns

### Rules organized by concern

```
.cursor/rules/
├── repo.mdc          ← from AGENTS.md
├── identity.mdc      ← from SOUL.md
├── testing.mdc       ← test commands and rules
└── safety.mdc        ← never-do list
```

Cursor loads matching rules per file/glob, which means:
- Rules can target specific languages or directories
- Smaller, more focused rules beat one mega-file

### Chat vs. agent

- **Chat mode**: short tasks, single file
- **Agent mode**: multi-step, multi-file. Walk the [coding agent workflows](coding_agent_workflows.md) before turning loose.

## Caveats

- Rule loading semantics evolve; verify current Cursor docs
- Some Cursor features expect specific frontmatter — check before relying on it
- Cursor's MCP support landed in 2024–2025; capabilities differ from Claude Code

## Migrating to / from Cursor

The handbook's `AGENTS.md` is intentionally tool-neutral. To move from Claude Code → Cursor (or back), you mainly:

1. Move tool/permission settings to the new tool's format
2. Re-load skills (Cursor loads via reference; Claude Code via folder structure)
3. Re-test on a representative regression eval
