# Failure analysis

A practical loop for diagnosing bad agent runs.

## Triage by class

| Symptom | Likely class |
|---|---|
| Agent gives up early | Loop guardrail trip / refusal |
| Wrong tool / wrong args | Tool selection / schema |
| Right tool, wrong outcome | Tool itself / model misread of output |
| Loops forever | Repeat detection broken / no progress signal |
| Fabricates citations / facts | Memory / RAG quality |
| High cost, low value | Loop length / oversized model on easy tasks |
| Inconsistent across runs | Sampling temperature / underspecified prompt |

## Investigation flow

1. **Pull the trace.** Start with span tree; look for unusual durations or missing children.
2. **Check guardrails.** Did one trip silently? Was a tool call refused?
3. **Read the model's reasoning.** Where did it diverge?
4. **Compare with a successful run** of the same task — diff inputs, span structure, decisions.
5. **Reproduce locally** with the captured inputs.
6. **Add a regression eval case** so it can't recur silently.

## Common root causes

- **Tool description vague** → model misuses tool. Fix description and reprompt.
- **No success criteria in skill** → model declares any output a win. Add criteria.
- **Memory poisoning** → model "remembers" something injected. Curate, eval.
- **Bad output schema** → downstream parsing fails. Strict schema + retries.
- **Context bloat** → relevant info pushed out of window. Distil + retrieve.

## Postmortems

For incident-class failures (data loss, customer impact, cost incident):

- Timeline (from traces)
- Direct cause
- Contributing factors
- What we change (guardrail / eval / prompt / tool)
- Action items with owners + dates

Save in `memory/decisions/` so future-you and future-agents inherit the lesson.
