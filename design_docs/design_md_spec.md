# `DESIGN.md` — machine-readable design specs

A simple format for design specs that **humans, agents, and tools can all parse**: YAML frontmatter for tokens / structured properties + Markdown prose for design rationale.

This pattern grew from open-source efforts (notably the `design.md` spec) to give product/UX teams a way to ship design tokens that LLMs can read directly. We adapt the idea into the handbook's voice; the handbook ships the *format*, not a CLI.

## Why

- Design tools export proprietary formats; LLMs can't navigate them
- Hand-written prose-only design docs are fine for humans, opaque to agents
- A single-file format with structured tokens + prose threads the needle

## Shape

```markdown
---
name: Atmospheric Glass
version: 0.3.0
description: A frosted-glass design system for productivity apps.
tokens:
  color:
    bg.surface:  "#0E1116"
    bg.elevated: "#161A21"
    fg.primary:  "#F4F5F7"
    fg.muted:    "#9CA3AF"
    accent:      "#7DD3FC"
  spacing:
    xs: 4
    sm: 8
    md: 16
    lg: 24
    xl: 40
  radius:
    sm: 6
    md: 12
    lg: 20
  type:
    body:    { size: 16, line: 24, weight: 400 }
    heading: { size: 28, line: 36, weight: 600 }
  motion:
    fast:   "120ms cubic-bezier(.2,.8,.2,1)"
    medium: "240ms cubic-bezier(.2,.8,.2,1)"
---

# Atmospheric Glass

## Voice
Calm, focused, technical. Avoid maximalism.

## Surface model
Two surface tiers (`bg.surface`, `bg.elevated`). All elevated layers use a 1px
inner glow at `fg.muted` 8% opacity.

## Typography
{{...}}

## Components
{{...}}
```

## Why this works for agents

- **Tokens are queryable.** An agent can read `tokens.color.accent` without parsing prose.
- **Prose is preserved.** Designers and reviewers don't lose the nuance.
- **Diffable.** Token changes show up cleanly in PRs.
- **Composable.** Multiple `DESIGN.md` files for different domains (mobile / web / email).

## Schema (suggested)

| Field | Type | Notes |
|---|---|---|
| `name` | string | Display name |
| `version` | semver | Bump on token changes |
| `description` | string | One sentence |
| `tokens` | object | Free-form, but recommended subkeys: `color`, `spacing`, `radius`, `type`, `motion` |
| `tags` | list | Optional |

The full token tree is project-specific. Pin a JSON Schema if you want strict validation.

## Tooling (optional)

- A small Python or TS validator that loads the YAML and checks the schema
- A CLI to extract tokens for code generation (CSS variables, Swift theme, etc.)
- Editor integration (most editors render YAML frontmatter in Markdown)

We ship the spec, not the tool — pick whatever fits your stack.

## Anti-patterns

- ❌ Putting design *prose* into the YAML
- ❌ Putting design *tokens* into the prose
- ❌ Mixing multiple unrelated systems in one file (split per domain)
- ❌ Versioning by date instead of semver (token changes are real breaks)

## Cross-references

- [`/templates/DESIGN_DOC.md.template`](../templates/DESIGN_DOC.md.template)
- [`design/`](../design/) for the existing design assets
