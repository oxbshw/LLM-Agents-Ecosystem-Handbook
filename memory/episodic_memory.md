# Episodic memory

Episodic memory is the record of *what happened*: each notable event, with timestamp and context. It's the raw material distillation turns into semantic memory.

## What lives here

- Tool calls and their outcomes
- Decisions made (and their alternatives)
- Errors encountered and how they were resolved
- User feedback and corrections
- Observations from runs that *might* matter later

## Where it lives

- `logs/episodic/{{YYYY-MM-DD}}.md` (one file per day) **or**
- `logs/episodic/{{run_id}}.md` (one file per run, indexed by date)

Append-only. Don't rewrite history — that's what distillation is for.

## Format

```markdown
## 2026-04-12

### 14:32  decision  #migration
Picked alembic over raw SQL for migrations. Alternative: handcrafted scripts. Reason: rollback story matters for prod. (Run: r-2026-04-12-001)

### 14:55  error  #db
Migration 0042 failed on staging — `NOT NULL` on existing rows. Fixed by adding default in same migration.

### 15:08  feedback  #user
User: "always show the diff before applying migrations." Promote to MEMORY.md#user.
```

## Why bother?

Without episodic logs, you can't:

- Reconstruct *why* a decision was made
- Detect repeating errors that warrant a guardrail
- Promote real signals to semantic memory (vs guessing)

## When to read episodic memory

- During a related task (search by tag)
- During incident postmortems
- During curator runs
- Almost never as raw context for the model — it's too low-signal

## Retention

- Default: keep 90 days
- Exception: anything tagged `decision` or `incident` — keep indefinitely
- Auto-rotate older logs to `logs/episodic/archive/`
