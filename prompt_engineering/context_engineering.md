# Context engineering

What you put in the model's context window — and in what order — often matters more than how cleverly the prompt is phrased.

## The budget

Context is finite (and billed). Allocate it like a small team's time:

| Section | Typical share | Notes |
|---|---|---|
| System prompt | 10–20% | Identity, contracts |
| User task | 5–15% | The actual ask |
| Memory (distilled) | 5–10% | Facts the model needs |
| Skills loaded | 5–15% | Workflow currently selected |
| Tool schemas | 5–10% | Tools available this turn |
| Retrieved content | 30–50% | RAG / docs / fetched pages |
| Reflection / scratchpad | 5–10% | Plan + notes |
| Response budget | 10–20% | Output room |

If retrieval eats 80%, the rest collapses. Be deliberate.

## Order matters

Context isn't a bag — most models attend differently to early vs late content.

- **Early:** identity, output contract, durable rules
- **Late:** the most-relevant retrieved chunk, the final user instruction
- **Middle:** schemas, examples, less-relevant retrievals

For long context: put the *answerable signal* near the end. Models tend to "lost in the middle."

## Compression strategies

When context is tight:

1. **Distill memory** ([memory/memory_distillation.md](../memory/memory_distillation.md)) — facts, not transcripts
2. **Summarize prior turns** — replace long history with a recap
3. **Filter retrieval** — prefer 5 high-quality chunks to 50 mediocre ones
4. **Rerank** — cross-encoder rerank cuts noise dramatically
5. **Drop unused tools** — don't ship 50 tool schemas every turn
6. **Trim verbose output** — set `max_tokens`, encourage tight outputs in the contract

## Long-context pitfalls

- **Recall degrades** with length. Test how your model performs at 100K vs 10K.
- **Latency grows** roughly with context squared (attention) — even on long-context-friendly models, expect a slowdown.
- **Cost grows linearly** with input tokens.
- **Tokenization differences** mean "200K context" is provider-specific.

A long-context model is not a substitute for retrieval. Retrieval still helps.

## Multimodal

Images count for a *lot* of tokens. A high-res screenshot might consume 3–5K tokens. Budget accordingly.

## Streaming and incremental context

For agent loops:

- After a tool call, **append** the tool result to the context, don't re-render the world
- After many turns, a **rolling summary** keeps the early system prompt + a digest of mid-history + recent turns
- Be careful: bad summarization is worse than honest truncation

## Eval the budget

Add a smoke check: log token usage per run. If it drifts up, find the section that grew. Cost dashboards ([observability/cost_tracking.md](../observability/cost_tracking.md)) pay for themselves.
