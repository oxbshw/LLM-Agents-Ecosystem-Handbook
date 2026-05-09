# Guardrails

Programmatic checks that run *around* the agent loop. Not the model — the **runtime**.

## The four classes

### 1. Input guardrails
Run on incoming user / RAG / MCP / tool-output content before it reaches the model.

- **Sanitize** untrusted content (strip imperative text directed at the agent)
- **Length-cap** inputs; reject above N tokens
- **PII detection** + redaction (where required)
- **URL allow-list** for any fetch

### 2. Output guardrails
Run on model output before it's shown to the user or passed to a tool.

- **Secret detection** (regex + entropy)
- **PII filter** unless explicitly allowed
- **Policy refusal** for forbidden categories
- **Schema validation** when output should be structured

### 3. Tool-call guardrails
Run between the model deciding to call a tool and the tool actually firing.

- **Argument schema validation**
- **Argument allow-lists** (e.g., only push to non-`main` branches without approval)
- **Dry-run** for destructive operations — return the diff, get approval, then execute
- **Dangerous-pattern detection** (`rm -rf`, `DROP TABLE`, `--force`)

### 4. Loop guardrails
Bound the run.

- **Max iterations** (e.g., 20)
- **Wallclock timeout** (e.g., 10 min)
- **Cost ceiling** (e.g., $1 per run)
- **Repeat detection** — same tool/args ≥ 3 → break

## Where guardrails live

Outside the model. Implement in your agent runtime (or framework hooks). Don't trust the model to police itself.

```
user input
   ↓
[input guardrail]
   ↓
model
   ↓
[output guardrail] — for user-facing
   ↓
[tool-call guardrail] — for tool calls
   ↓
tool
   ↓
[input guardrail again on tool output]
   ↓
model
```

## Failure mode: the silent guardrail

Guardrails that drop bad content silently are dangerous — the agent thinks it succeeded. Always **surface** trips:

- Log the trip (category, content hash, run id)
- Return a structured error to the model so it can adjust
- Alert if trip rate spikes

## Calibration

Too tight → agent is useless.
Too loose → no protection.

Calibrate with a labeled eval set:

- True positives (caught harmful)
- False positives (caught harmless — agent UX hits)
- False negatives (missed harmful)
- True negatives

Tune to your acceptable false-negative rate, then live with the false positives.
