# Provider matrix

Capability comparison. **Verify against upstream docs** — capabilities ship and change weekly.

## Legend

- ✅ supported, well-documented
- 🟡 partial / model-dependent
- ❌ not supported
- 🔧 via OpenAI-compatible base URL (no separate SDK needed)

## Hosted providers

| Provider | Family | Chat | Tools | JSON / Structured | Vision | Embeddings | Long ctx | OpenAI-compat | Adapter |
|---|---|---|---|---|---|---|---|---|---|
| OpenAI | frontier | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | native | `openai` |
| Anthropic | frontier | ✅ | ✅ | 🟡 (JSON via tool) | ✅ | ❌ | ✅ | ❌ | `anthropic` |
| Google Gemini | frontier | ✅ | ✅ | 🟡 | ✅ | ✅ | ✅ | 🔧 | `openai` |
| Azure OpenAI | enterprise | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 🔧 | `openai` |
| AWS Bedrock | enterprise | ✅ | ✅ | 🟡 | ✅ | ✅ | ✅ | ❌ | `boto3` (stub) |
| Groq | fast | ✅ | ✅ | ✅ | 🟡 | ❌ | 🟡 | 🔧 | `openai` |
| Cerebras | fast | ✅ | 🟡 | ✅ | ❌ | ❌ | 🟡 | 🔧 | `openai` |
| SambaNova | fast | ✅ | 🟡 | 🟡 | ❌ | ❌ | 🟡 | 🔧 | `openai` |
| OpenRouter | marketplace | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | 🔧 | `openai` |
| Together | marketplace | ✅ | ✅ | ✅ | 🟡 | ✅ | ✅ | 🔧 | `openai` |
| Fireworks | marketplace | ✅ | ✅ | ✅ | 🟡 | ✅ | ✅ | 🔧 | `openai` |
| DeepInfra | marketplace | ✅ | 🟡 | 🟡 | 🟡 | ✅ | 🟡 | 🔧 | `openai` |
| Mistral | specialty | ✅ | ✅ | ✅ | 🟡 | ✅ | ✅ | 🔧 | `openai` |
| Cohere | specialty | ✅ | ✅ | 🟡 | ❌ | ✅ | ✅ | 🔧 | `openai` |
| DeepSeek | specialty | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ | 🔧 | `openai` |
| xAI | specialty | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | 🔧 | `openai` |
| Perplexity | specialty | ✅ | ❌ | ❌ | ❌ | ❌ | 🟡 | 🔧 | `openai` |
| Hugging Face | specialty | ✅ | 🟡 | 🟡 | 🟡 | ✅ | 🟡 | 🔧 | `openai` |
| Replicate | specialty | ✅ | ❌ | ❌ | ✅ | ❌ | 🟡 | ❌ | predict-style (stub) |
| NVIDIA NIM | specialty | ✅ | ✅ | 🟡 | 🟡 | ✅ | 🟡 | 🔧 | `openai` |
| MiniMax | specialty | ✅ | 🟡 | 🟡 | ❌ | ❌ | ✅ (512K with M3) | 🔧 | `openai` |

## Local runtimes

| Provider | Chat | Tools | JSON | Vision | Embeddings | Long ctx | Notes |
|---|---|---|---|---|---|---|---|
| Ollama | ✅ | ✅ | ✅ | 🟡 | ✅ | model-dep | OpenAI-compat at `:11434/v1` |
| LM Studio | ✅ | ✅ | ✅ | ❌ | ✅ | model-dep | OpenAI-compat at `:1234/v1` |
| vLLM | ✅ | ✅ | ✅ | 🟡 | ❌ | ✅ | OpenAI-compat at `:8000/v1` |
| llama.cpp (server) | ✅ | 🟡 | ✅ | ❌ | ❌ | model-dep | OpenAI-compat at `:8080/v1` |
| Generic OpenAI-compat | ✅ | model-dep | model-dep | model-dep | model-dep | model-dep | Set `LOCAL_OPENAI_COMPATIBLE_BASE_URL` |

## Choosing by need

| Need | Try first | Then |
|---|---|---|
| Cheap classification / extraction | Groq, DeepSeek | Together, OpenRouter |
| Top-shelf reasoning + tool use | Anthropic, OpenAI | Google Gemini |
| Lowest latency | Groq, Cerebras | Fireworks |
| Long-context analysis | Google Gemini, Anthropic | MiniMax (M3, 512K) |
| Vision tasks | OpenAI, Google, Anthropic | xAI |
| Real-time web search built in | Perplexity | (build it yourself) |
| Embeddings | OpenAI, Cohere, Mistral | Together |
| Reranker | Cohere | (most others lack it) |
| Local / offline | Ollama, LM Studio | vLLM (production) |
| Enterprise compliance | Azure OpenAI, Bedrock | Vertex AI |
