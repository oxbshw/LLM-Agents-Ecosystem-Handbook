# Local models

Privacy, cost control, offline development, and reproducibility. The same `LLMProvider` interface that talks to OpenAI talks to a local server.

## Runtimes

| Runtime | Best for | Default URL | OpenAI-compat |
|---|---|---|---|
| **Ollama** | Easiest dev loop on Mac/Linux/Windows | `http://localhost:11434/v1` | yes |
| **LM Studio** | GUI + model browsing | `http://localhost:1234/v1` | yes |
| **vLLM** | Production-grade throughput | `http://localhost:8000/v1` | yes |
| **llama.cpp (server)** | Smallest deps, edge devices | `http://localhost:8080/v1` | yes |
| **TGI / RayServe / etc.** | When you already run them | varies | varies |

## Ollama in 60 seconds

```bash
# install (macOS / Linux / Windows): https://ollama.com/download
ollama pull llama3.1
ollama serve   # starts API at :11434
```

```python
from utilities import get_provider
p = get_provider("ollama")
print(p.chat([{"role": "user", "content": "hi"}], model="llama3.1")["text"])
```

## LM Studio

1. Open LM Studio → download a model
2. Go to "Local Server" → start at `:1234`
3. `LMSTUDIO_BASE_URL=http://localhost:1234/v1` (default)

```python
from utilities import get_provider
get_provider("lmstudio").chat([{"role": "user", "content": "hi"}], model="local-model")
```

## vLLM (production)

```bash
pip install vllm
vllm serve meta-llama/Llama-3.1-8B-Instruct \
  --host 0.0.0.0 --port 8000 \
  --max-model-len 16000
```

Hit it via the abstraction:

```python
from utilities import get_provider
p = get_provider("vllm")
out = p.chat(
    [{"role": "user", "content": "Summarize MCP."}],
    model="meta-llama/Llama-3.1-8B-Instruct",
)
```

## llama.cpp HTTP server

```bash
llama-server -m model.gguf --host 0.0.0.0 --port 8080
```

Then `LLAMACPP_BASE_URL=http://localhost:8080/v1`.

## Generic OpenAI-compatible

For self-hosted endpoints (TGI, custom runtimes, internal proxies):

```bash
export LOCAL_OPENAI_COMPATIBLE_BASE_URL=https://internal-llm.company.com/v1
export LOCAL_OPENAI_COMPATIBLE_API_KEY=...
```

```python
get_provider("openai_compatible").chat([...], model="our-internal-model")
```

## When to choose local

| Choose local | Choose hosted |
|---|---|
| Sensitive data must not leave your network | You need top-shelf model quality |
| Predictable cost > peak quality | You need vision / huge context / latest models |
| Offline / edge deployment | You don't have GPU budget |
| Compliance forbids 3rd-party APIs | Speed-of-shipping > infra control |

## Pitfalls

- **Tool calling varies wildly.** Some local models support OpenAI-style tools; many don't. Test before assuming.
- **JSON mode drift.** Local "JSON mode" is often best-effort; validate output.
- **Context length lies.** A model trained at 4K with rope-scaled context to 32K is not the same as a native 200K model. Eval before relying.
- **Concurrency.** Ollama serializes; vLLM batches. For load, vLLM.
- **Memory bloat.** GGUF Q4_K_M ≈ ~5 GB for 8B; 70B Q4 ≈ 40 GB. Pick by your hardware.

## Hybrid pattern

Cheap path (local) for high-volume + simple; hosted for the hard cases:

```python
from utilities.provider_router import ProviderRouter

router = ProviderRouter(chains={
    "extract": ["ollama"],                      # local for bulk
    "reason":  ["anthropic", "openai"],         # hosted for hard
})
out = router.chat(messages, task_class="extract")
```

📖 [router_patterns.md](router_patterns.md)
