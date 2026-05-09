"""Mistral provider example (OpenAI-compatible).

Setup:
    pip install openai
    export MISTRAL_API_KEY=...
"""

from utilities import get_provider


def main() -> None:
    p = get_provider("mistral")
    out = p.chat(
        [{"role": "user", "content": "Three things Mistral does well."}],
        model="mistral-small-latest",
        max_tokens=200,
    )
    print(out["text"])


if __name__ == "__main__":
    main()
