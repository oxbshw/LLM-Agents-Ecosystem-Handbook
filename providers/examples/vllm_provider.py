"""vLLM provider example — production-grade local serving.

Setup:
    pip install vllm
    vllm serve meta-llama/Llama-3.1-8B-Instruct \\
        --host 0.0.0.0 --port 8000 \\
        --max-model-len 16000

    # VLLM_BASE_URL defaults to http://localhost:8000/v1

vLLM batches concurrent requests automatically — way better throughput
than Ollama for production load.
"""

from utilities import get_provider


def main() -> None:
    p = get_provider("vllm")
    out = p.chat(
        [{"role": "user", "content": "When is vLLM the right choice over Ollama?"}],
        model="meta-llama/Llama-3.1-8B-Instruct",
        max_tokens=300,
    )
    print(out["text"])


if __name__ == "__main__":
    main()
