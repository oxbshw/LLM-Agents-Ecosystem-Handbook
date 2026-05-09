# Provider matrix (LLM wiki view)

A condensed view for LLM navigation. Full matrix lives at [`/providers/provider_matrix.md`](../providers/provider_matrix.md).

## Families

| Family | Members |
|---|---|
| Frontier | OpenAI, Anthropic, Google Gemini |
| Enterprise | Azure OpenAI, AWS Bedrock |
| Fast inference | Groq, Cerebras, SambaNova |
| Marketplaces | OpenRouter, Together, Fireworks, DeepInfra |
| Specialty | Mistral, Cohere, DeepSeek, xAI, Perplexity, Hugging Face, Replicate, NVIDIA NIM, MiniMax |
| Local | Ollama, LM Studio, vLLM, llama.cpp, generic OpenAI-compatible |

## When to pick what (one-liner each)

- Cheap classification → Groq, DeepSeek, OpenRouter cheap variants
- Top reasoning → Anthropic, OpenAI flagship, Google Pro
- Lowest latency → Groq, Cerebras
- Long context → Google Gemini, Anthropic, MiniMax (204K)
- Vision → OpenAI, Google, Anthropic, xAI
- Real-time web grounded → Perplexity
- Embeddings → OpenAI, Cohere, Mistral
- Reranker → Cohere
- Local / offline → Ollama (dev), vLLM (prod)
- Enterprise compliance → Azure OpenAI, Bedrock

## Routing table

| Task class | Default chain |
|---|---|
| `cheap` | Groq → DeepSeek → Together → OpenRouter |
| `fast` | Groq → Cerebras → Fireworks |
| `reasoning` | Anthropic → OpenAI → Google → DeepSeek |
| `long_context` | Google → Anthropic → MiniMax → OpenAI |
| `vision` | OpenAI → Google → Anthropic → xAI |
| `local` | Ollama → LM Studio → vLLM → llama.cpp |
| `research` | Perplexity → OpenAI → Anthropic |

📖 [providers/router_patterns.md](../providers/router_patterns.md)

## Adapter implementation

Most providers reach the model through a single OpenAI-compatible HTTP path. Anthropic uses its own SDK. Bedrock and Replicate are documented as stubs. See [providers/provider_abstraction.md](../providers/provider_abstraction.md).

## Adding a provider

Walk the [provider expansion prompt](../coding_agents/prompts/provider_expansion_prompt.md). Most provider additions are: 1 entry in [`utilities/provider_config.py`](../utilities/provider_config.py) + 1 example file + a `.env.example` line + a row in [`provider_matrix.md`](../providers/provider_matrix.md).
