# Memory distillation rules

## Format

Every entry follows: `- {{fact}} ({{YYYY-MM-DD}})`

## Promotion threshold

Promote an episodic note to semantic memory only if it is:

- **General** — applies beyond one session
- **Confident** — observed at least twice OR explicitly stated by the user
- **Stable** — unlikely to change next week
- **Useful** — would change a future decision

If any of those is false, leave it in episodic logs.

## What to distill

| Source signal | Memory category |
|---|---|
| User says "always do X" / "never do Y" | feedback |
| User confirms a non-obvious approach worked | feedback |
| Decision made with rationale | decision |
| Discovered fact about the project that isn't in code/git | project |
| User profile detail | user |

## What NOT to distill

- Single-session task state
- Information derivable from `git log` or current code
- Vague impressions ("user seemed annoyed")
- Anything containing secrets, tokens, or PII

## Conflict resolution

When new evidence contradicts existing memory:
1. Update the existing entry (don't dual-state)
2. Move the old fact to "Outdated" with a `superseded by ...` note
3. If conflict is unresolved, demote both to "Open questions"

## Expiry

Entries with a date older than {{policy: 6 months}} should be reviewed:
- Still true → re-date
- No longer true → move to Outdated
- Unclear → demote to Open question
