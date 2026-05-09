# Human approval

When to ask, how to ask, and how to *not* ask too much.

## Goal
Catch the actions that, if wrong, cost real money / time / trust. Skip everything else — friction kills agents.

## When to require approval

| Trigger | Approval |
|---|---|
| Tool labelled High in `TOOLS.md` | required |
| Tool labelled Critical | always + 2nd reviewer |
| First-time use of a Medium tool in a session | one-time |
| Action breaches a budget cap (cost / rate / count) | required |
| Pattern flagged dangerous (`force`, `delete`, `transfer`) | required |

## How to ask

Show:

- **What**: tool name + arguments
- **Why**: agent's rationale (one paragraph)
- **Impact**: reversibility + blast radius
- **Preview**: dry-run output if possible

Example:

```yaml
approval_request:
  tool: gh.pull_request.merge
  args: { repo: "org/app", pr: 312 }
  rationale: "Tests green; reviewer approved; matches release plan."
  reversibility: "reversible (revert PR)"
  blast_radius: "team — production deploys on merge"
  preview: |
    Merging will close PR #312, deploy v2026.04.12.0 to staging, and queue a prod deploy.
```

## How NOT to ask

- ❌ "Continue?" without showing what
- ❌ Bundling 5 actions into one approval
- ❌ Auto-approving on timeout
- ❌ Asking again after recent denial without changed context

## Approval fatigue

If users approve everything reflexively, you've lost the value. Counter-measures:

- Tier carefully — most actions should need 0 prompts
- Allow batch approval with explicit count ("approve next 5 ticket creations")
- Show *why* the action was risky, so denial is meaningful

## Audit

Every approval and denial → durable log:

- request_id, run_id, user_id
- timestamp
- decision
- decider
- payload (or hash if sensitive)

Logs are append-only and reviewed weekly.

📖 Template: [templates/HUMAN_APPROVAL_POLICY.md.template](../templates/HUMAN_APPROVAL_POLICY.md.template)
