# Cost / latency matrix

Rough comparison. **Verify against current pricing pages before betting production budgets.**

> Numbers move weekly. We list orders of magnitude and qualitative tiers, not current rates. Always check the providers' own pricing.

## Cost tiers (per 1M tokens, input/output, mixed)

| Tier | Indicative range | Examples |
|---|---|---|
| **Ultra-cheap** | < $1 | DeepSeek, Groq small models, OpenRouter cheap variants, local |
| **Cheap** | $1 – $5 | OpenAI mini-class, Anthropic Haiku-class, Mistral small, Together Llama-class |
| **Mid** | $5 – $30 | OpenAI standard, Anthropic Sonnet-class, Gemini Flash-Pro |
| **High** | $30 – $100 | OpenAI flagship, Anthropic Opus-class, Gemini Ultra-class |
| **Local** | $0 marginal | Hardware + electricity (Ollama, vLLM, llama.cpp) |

## Latency tiers (TTFT — time to first token, hot caches)

| Tier | Range | Examples |
|---|---|---|
| **Ultra-fast** | < 200ms | Groq, Cerebras, SambaNova |
| **Fast** | 200ms – 1s | OpenAI mini, Anthropic Haiku, Gemini Flash, Fireworks |
| **Standard** | 1 – 3s | Most frontier flagship models |
| **Slow** | > 3s | Reasoning-mode models, very long context |

## Context-length tiers

| Tier | Range | Examples |
|---|---|---|
| Standard | 16K – 32K | Older / smaller models |
| Long | 100K – 200K | Anthropic, OpenAI flagship, MiniMax (204K) |
| Very long | 1M+ | Gemini 1.5 Pro, Gemini 2.x |

## Mixing cost and latency

| You want | Pick |
|---|---|
| Cheap + fast (high volume, simple tasks) | Groq small / DeepSeek |
| Cheap + capable (background batch) | DeepSeek, OpenRouter cheap |
| Fast + capable (interactive UX) | OpenAI mini / Anthropic Haiku / Gemini Flash |
| Capable, cost-no-object | OpenAI flagship / Anthropic Opus / Gemini Ultra |
| Long context + cheap | Gemini Flash, DeepSeek |
| Long context + capable | Gemini 1.5+ Pro, Anthropic Sonnet/Opus |

## What this matrix can't tell you

- Per-prompt actual cost (depends on tokens, caching, structured output overhead)
- Real p95 latency under your load (depends on region, time of day, rate-limit posture)
- Quality on YOUR task (only an [eval](../evals/) can answer that)

## Don't pick by cost alone

A 10× cheaper model that needs 3 retries is not 10× cheaper. Run a regression eval ([evals/regression_evals.md](../evals/regression_evals.md)) before swapping out a working provider for a cheaper one.
