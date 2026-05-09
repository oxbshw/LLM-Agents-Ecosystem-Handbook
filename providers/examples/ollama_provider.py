"""Ollama provider example — local first.

Setup:
    # install Ollama: https://ollama.com/download
    ollama pull llama3.1
    ollama serve
    # OLLAMA_BASE_URL defaults to http://localhost:11434/v1
"""

from utilities import get_provider


def main() -> None:
    p = get_provider("ollama")
    out = p.chat(
        [{"role": "user", "content": "Three reasons to run inference locally."}],
        model="llama3.1",
        max_tokens=200,
    )
    print(out["text"])


if __name__ == "__main__":
    main()
