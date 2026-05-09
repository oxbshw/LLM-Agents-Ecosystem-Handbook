# Environment variables

Single source of truth for the env vars the provider abstraction reads. Mirror in [.env.example](../.env.example).

## Selection

| Var | Default | Purpose |
|---|---|---|
| `LLM_PROVIDER` | `openai` | Default provider name for `complete()` and `get_provider(None)` |

## API keys

| Provider | Key var |
|---|---|
| OpenAI | `OPENAI_API_KEY` |
| Anthropic | `ANTHROPIC_API_KEY` |
| Google Gemini | `GOOGLE_API_KEY` |
| Azure OpenAI | `AZURE_OPENAI_API_KEY` (+ `AZURE_OPENAI_ENDPOINT`) |
| AWS Bedrock | `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_REGION` |
| Mistral | `MISTRAL_API_KEY` |
| Cohere | `COHERE_API_KEY` |
| Groq | `GROQ_API_KEY` |
| Cerebras | `CEREBRAS_API_KEY` |
| SambaNova | `SAMBANOVA_API_KEY` |
| OpenRouter | `OPENROUTER_API_KEY` |
| Together | `TOGETHER_API_KEY` |
| Fireworks | `FIREWORKS_API_KEY` |
| DeepInfra | `DEEPINFRA_API_KEY` |
| DeepSeek | `DEEPSEEK_API_KEY` |
| xAI | `XAI_API_KEY` |
| Perplexity | `PERPLEXITY_API_KEY` |
| Hugging Face | `HF_TOKEN` |
| Replicate | `REPLICATE_API_TOKEN` |
| NVIDIA NIM | `NVIDIA_API_KEY` |
| MiniMax | `MINIMAX_API_KEY` |

## Local runtime base URLs

| Provider | Var | Default |
|---|---|---|
| Ollama | `OLLAMA_BASE_URL` | `http://localhost:11434/v1` |
| LM Studio | `LMSTUDIO_BASE_URL` | `http://localhost:1234/v1` |
| vLLM | `VLLM_BASE_URL` | `http://localhost:8000/v1` |
| llama.cpp | `LLAMACPP_BASE_URL` | `http://localhost:8080/v1` |
| Generic OpenAI-compat | `LOCAL_OPENAI_COMPATIBLE_BASE_URL` (+ `LOCAL_OPENAI_COMPATIBLE_API_KEY` if any) | — |

## Router overrides

Set comma-separated provider names to override default chains:

| Var | Used for `task_class` |
|---|---|
| `ROUTER_DEFAULT` | `"default"` |
| `ROUTER_CHEAP` | `"cheap"` |
| `ROUTER_FAST` | `"fast"` |
| `ROUTER_REASONING` | `"reasoning"` |
| `ROUTER_LONG_CONTEXT` | `"long_context"` |
| `ROUTER_VISION` | `"vision"` |
| `ROUTER_LOCAL` | `"local"` |
| `ROUTER_RESEARCH` | `"research"` |

Example:
```bash
export ROUTER_CHEAP="groq,deepseek,together"
```

## Conventions

- **Never commit `.env`.** Use `.env.example` as the documented surface.
- **Per-tenant scoping** is the runtime's job; the abstraction reads process env.
- **Missing key ≠ crash.** The router skips providers with `ProviderNotConfigured` and tries the next.
