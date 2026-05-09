# User memory

What the agent knows about the user, across sessions.

## Where it lives

- `USER.md` — profile, stable preferences (changes rarely)
- `MEMORY.md#user` — accumulating user facts (more dynamic)

## What to store

✅ Preferences (response length, format, language)
✅ Profile (role, technical level, primary stack)
✅ Recurring goals
✅ Don't-assume notes
✅ Feedback ("always do X" / "never do Y") with reasons

## What NOT to store

🚫 Mood ("user seemed annoyed") — judgments age badly
🚫 Sensitive personal info beyond what the user explicitly shared
🚫 Inferred private data without consent
🚫 Anything you wouldn't show the user if they asked

## Privacy + retention

- The user **owns** this memory. Provide a way to view, export, and delete.
- Document retention period in `USER.md` or a privacy note.
- Never sync user memory across users / projects without explicit opt-in.
- For multi-tenant agents, keep user memory **isolated per user** — never cross-contaminate.

## Updates

User memory updates are usually triggered by:

- Direct statement: "always do X" → store as feedback
- Repeated pattern: same correction twice → promote
- Confirmation of a suggestion: validated approach worth keeping

## Show your work

Periodically summarize what the agent remembers about the user, so they can correct it. A good cadence: at session end, or on demand.

> "Quick check — I'm remembering: terse responses, diffs over prose, you use pnpm. Anything I should drop or update?"
