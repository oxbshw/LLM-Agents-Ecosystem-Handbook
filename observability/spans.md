# Spans

The unit of trace. Naming and structure matter more than tooling.

## Naming convention

`<category>.<name>` keeps spans groupable.

| Category | Example | Notes |
|---|---|---|
| `model.*` | `model.complete`, `model.embed` | LLM calls |
| `tool.*` | `tool.web_search`, `tool.write_file` | Function calls |
| `mcp.*` | `mcp.github.pr_create` | MCP tool calls (separate from tool.*) |
| `skill.*` | `skill.research-summarizer` | Workflow steps |
| `guardrail.*` | `guardrail.input`, `guardrail.output` | Policy checks |
| `approval.*` | `approval.requested`, `approval.granted` | Human gate events |
| `memory.*` | `memory.read`, `memory.write` | Memory operations |

## Attributes (recommended)

Always attach:

- `run_id`, `parent_run_id`
- `agent.name`, `agent.version`
- `cost_usd` (where applicable)
- `tokens_in`, `tokens_out` (model spans)
- `risk_level` (tool / mcp spans)
- `outcome` (`ok` / `error` / `denied` / `refused`)

## Errors

When a span fails, capture:

- Error class / type
- One-line message (no PII)
- Whether it's retryable
- Retry count

## Don't put in spans

- 🚫 Full prompts containing PII / secrets (hash / redact)
- 🚫 Full tool output if it could be poisoned (truncate + hash)
- 🚫 Tokens that would let someone replay the call

## Cardinality

Keep span names low-cardinality (no IDs in names). Put high-cardinality info in attributes.

✅ `tool.fetch_url` with attribute `url=https://example.com/...`
❌ `tool.fetch_url.example.com.path.subpath` (cardinality explosion)
