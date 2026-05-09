# Blueprint: Multi-agent team

## Use case
Tasks too large for a single agent context, with distinct sub-skills (plan / execute / review).

## Non-goals
- "More agents = better" — start with one; split when you have a real reason
- Real-time collaboration — these agents typically work sequentially or branch + join

## When to split

✅ Different skills genuinely benefit from different prompts/identities
✅ Context window pressure (one agent can't hold everything)
✅ Different tool / risk profiles per role

❌ "It feels more capable" — usually it's just slower and noisier

## Roles (typical)

| Role | Owns |
|---|---|
| **Planner** | Decomposes the task; emits a plan |
| **Worker(s)** | Execute steps; can be parallel for independent work |
| **Reviewer** | Audits worker output; can reject + send back |
| **Coordinator** (optional) | Owns approvals and handoffs; keeps the trace tidy |

## Architecture

```
   user task
       │
       ▼
  [Planner]  ── plan.md
       │
       ▼
   [Worker A] ─────────► artifacts/
   [Worker B] ─────────► artifacts/
       │
       ▼
  [Reviewer]  ── pass | rework
       │
       ▼
  final output
```

## Communication

- **Files, not chat.** Workers write to a shared `artifacts/` dir; the reviewer reads files. This keeps traces clean and makes work resumable.
- **Structured handoffs.** Each role writes a tiny "handoff" JSON: what it did, what's next.
- **No infinite loops.** The reviewer can request rework once or twice; after that, escalate to human.

## Identity per role

Each role gets its own `SOUL.md`:
- Planner: terse, structured, conservative
- Worker: focused on the assigned step, no scope creep
- Reviewer: skeptical, criteria-driven

## Memory
- Shared `MEMORY.md` at project level
- Each role keeps a private session-only scratch (not promoted)

## Safety
- Risk policy lives at the coordinator
- Workers cannot self-approve — only the coordinator interfaces with the human
- Audit log includes all handoffs

## Evals
- End-to-end on real tasks
- Per-role evals (planner alone, reviewer alone)
- Loop guardrail eval (rework count cap, escalation correctness)

## Frameworks
- LangGraph for explicit graph orchestration
- CrewAI for role-based teams
- AutoGen for event-driven HITL teams
- OpenAI Agents SDK for handoffs and structured workflows

Pick by your team's existing stack, not by hype.

## Extensions
- Specialist workers added on demand (security reviewer, performance reviewer)
- Long-running planner with checkpointing
