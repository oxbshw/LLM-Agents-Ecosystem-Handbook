# Identity Layer — `SOUL.md`, `AGENTS.md`, `USER.md`

Identity is the most undervalued layer. A well-defined identity reduces hallucination, prevents persona drift, and makes refusals consistent.

## The three files, and the one-line difference

| File | Answers | Audience |
|---|---|---|
| **`SOUL.md`** | "*Who* is the agent — voice, mission, refusal style?" | The agent itself |
| **`AGENTS.md`** | "How do I work in *this repo*?" | Any coding agent reading the project |
| **`USER.md`** | "Who is the *user*, and how do they like to collaborate?" | Personalization layer |

Keep them small. If `SOUL.md` exceeds ~150 lines, you're writing a constitution — split out a `policies/` folder.

## SOUL.md — what to put in it

- **Identity** — name, role, scope (e.g., "I'm a senior backend code reviewer")
- **Mission** — the *why* in one sentence
- **Voice** — terse vs verbose, formal vs casual, examples of preferred phrasing
- **Values** — what the agent prioritizes when goals conflict (correctness > speed)
- **Boundaries** — domains and actions out of scope
- **Refusal style** — how to decline gracefully without lecturing
- **Quality bar** — what "done" looks like

Keep it declarative, not anecdotal. See [templates/SOUL.md.template](../templates/SOUL.md.template).

## AGENTS.md — what to put in it

- **Project context** — what this repo is, in 3 lines
- **Coding conventions** — language, style guides, lint commands
- **Testing** — how to run, what must pass before commit
- **Documentation rules** — what to update when
- **Tool usage** — preferred CLIs, package managers
- **PR expectations** — title format, review process
- **Safety rules** — destructive commands that are forbidden, secrets handling

`AGENTS.md` is becoming an emerging cross-tool standard (Cursor, Claude Code, Codex, Aider all read variants). Keep it tool-neutral.

See [templates/AGENTS.md.template](../templates/AGENTS.md.template).

## USER.md — what to put in it

- **Profile** — role, seniority, technical level
- **Preferences** — formats, languages, response length
- **Recurring goals** — what the user typically asks for
- **Don't-assume** — common pitfalls when guessing intent

See [templates/USER.md.template](../templates/USER.md.template).

## Anti-patterns

- ❌ Putting a chat history into `SOUL.md` — that's memory, not identity
- ❌ Hard-coding API keys or specific endpoints in `AGENTS.md` — that's config
- ❌ Listing every project preference in `USER.md` — keep it under ~30 lines, focused on *non-obvious* preferences
