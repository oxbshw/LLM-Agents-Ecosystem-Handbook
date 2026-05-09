# Blueprint: Personal assistant agent

## Use case
Calendar, email, tasks, light research. Lives across sessions; learns the user's preferences.

## Non-goals
- Sending email without explicit per-message approval
- Spending money
- Sharing memory across users

## Architecture

```
user (chat)
    │
    ▼
[router]  ── intent (calendar / email draft / task / research / chitchat)
    │
    ▼
specialists ── per intent
    │
    ▼
[summary + next-step suggestion]
```

## Tools (MCP-heavy)

| Tool | Risk |
|---|---|
| `gcal.read` | Low |
| `gcal.write` | Medium (approval first time) |
| `gmail.read` | Low |
| `gmail.draft` | Medium |
| `gmail.send` | High (always approval) |
| `tasks.write` | Medium |
| `web_search` / `fetch_url` | Low |

## Memory
- `USER.md`: profile, preferences, tone
- `MEMORY.md`: recurring people, routines, recurring tasks
- Per-topic semantic files for ongoing projects

## Skills
- `meeting-prep` — gather context before a meeting
- `inbox-triage` — classify and draft replies
- `agent-memory-curator` — daily

## Safety
- Strict per-user isolation
- Email send is always gated — no exceptions
- Approval must include the *full* draft and recipient list
- Privacy-first defaults: no sharing across providers without consent

## Evals
- Calendar correctness on golden cases
- Draft quality (LLM-judge against examples user accepted)
- Refusal: never auto-sends, even when prompted
- Memory recall + isolation

## Deployment
- Per-user instance (no shared state)
- Encrypted memory store
- One-click "forget me" wipes user memory + traces

## Extensions
- Voice
- Proactive ("you have 5 unanswered emails older than 3 days")
- Cross-app workflows (e.g., "convert this email to a task with deadline")
