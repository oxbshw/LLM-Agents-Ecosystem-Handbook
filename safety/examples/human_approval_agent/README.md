# Human approval agent (skeleton)

A docs-first example of an agent with an out-of-band approval queue.

## Flow

```
agent → wants High tool ──> approval queue (file/db) ──> human UI
                                                              │
agent ← decision  ────────  approval queue   <───────  approve/deny
```

## Why out-of-band?

If approval is *inside* the model loop, the model can talk itself into approving. The human's decision must be impossible to forge from the model's outputs.

## File-based MVP

```
.agent/approvals/
├── pending/                # JSON files written by the agent
│   └── 2026-04-12_001.json
├── decided/
│   ├── 2026-04-12_001.approved.json
│   └── 2026-04-12_002.denied.json
└── log.jsonl               # append-only audit
```

The agent writes a request, polls `decided/`, proceeds or stops based on the decision file. The human side is a CLI or a tiny web UI.

## Request format

See [/templates/HUMAN_APPROVAL_POLICY.md.template](../../../templates/HUMAN_APPROVAL_POLICY.md.template).

## What to test

- Agent stops cleanly on denial
- Agent does **not** re-request the same action without changed context
- Audit log is append-only and tamper-evident (hash chain or signing)
