# Model selection guide

A short, practical guide to picking a model for a given task.

## Step 1 — name the task class

Before picking a model, name what the model is doing:

| Task class | Examples | Sensitive to |
|---|---|---|
| Classification / extraction | label sentiment, parse fields | speed, cost |
| Summarization | TL;DR, exec summary | quality at cheap cost |
| Drafting | first-pass code, prose | quality, voice |
| Planning / reasoning | multi-step plans, tool selection | quality, structured outputs |
| Tool-using agent | calls tools, decides next step | tool calling fidelity |
| Long doc analysis | 100K+ context | context window, recall |
| Vision | parse images, screenshots | vision quality |
| Search / research | live web grounded | freshness |

Different task classes deserve different models. Don't pay flagship prices for sentiment classification.

## Step 2 — pick a *family*, not a model

Model names change monthly. Map your task class to a family:

| Task class | Family |
|---|---|
| Classification / extraction | "cheap fast" — small open models, mini-tier hosted |
| Summarization | "cheap mid" — Haiku-class, Flash-class, mini-tier |
| Drafting | "mid" — Sonnet-class, GPT mid-tier |
| Planning / reasoning | "flagship reasoning" — Opus-class, GPT flagship, Gemini Pro |
| Tool-using agent | "flagship tool-using" — Anthropic, OpenAI, Google |
| Long doc analysis | "long context" — Gemini Pro, Anthropic |
| Vision | "vision-capable" — OpenAI, Google, Anthropic, xAI |
| Research | "research-grounded" — Perplexity, then frontier |

## Step 3 — pin a specific model

Once a family is chosen, pin a specific version. Use the provider's stable model id, not "latest." Track upgrades via a changelog.

```python
# Bad
provider.chat(msgs, model="latest")

# Good
provider.chat(msgs, model="claude-3-5-haiku-20241022")
```

## Step 4 — eval, then commit

A model is only "right" if it passes your evals at acceptable cost/latency. Use:

- [evals/regression_evals.md](../evals/regression_evals.md) — must still pass past tasks
- [evals/tool_call_evals.md](../evals/tool_call_evals.md) — for agentic flows
- [evals/eval_design.md](../evals/eval_design.md) — overall design

Don't ship "this seems better" — measure.

## Step 5 — version the choice

Treat model choice like a dependency:

- Note the model id + provider in `MEMORY.md` decisions
- Bump on a schedule, not on whim
- Re-run evals on every model bump
- Keep a one-version rollback

## Heuristics

- **Test on hard cases, not easy ones.** A model that aces your golden path may collapse on edge cases.
- **Watch tool call fidelity.** Many models claim tool-calling support; few are equally reliable.
- **Long context ≠ long understanding.** Recall degrades over context length on most models. Test it.
- **Reasoning modes cost.** "Thinking" tokens are billed.
- **Don't over-fit one provider.** Even if you prefer one, having a fallback means surviving a 4-hour incident.

## Pitfalls

- **"Latest" deprecation.** Pinned models avoid surprise behavioral shifts.
- **Tokenizer drift.** Different providers count tokens differently — your "max_tokens" cap is provider-relative.
- **JSON mode degradation under tool use.** Many providers' JSON mode and tool calling don't compose cleanly. Test the combo you'll ship.
- **Vision context inflation.** A high-res image can eat 5K+ tokens — budget accordingly.
