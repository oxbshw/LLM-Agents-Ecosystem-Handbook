"""Fireworks AI provider example.

Setup:
    pip install openai
    export FIREWORKS_API_KEY=...
"""

from utilities import get_provider


def main() -> None:
    p = get_provider("fireworks")
    out = p.chat(
        [{"role": "user", "content": "Why batch inference matters for cost."}],
        model="accounts/fireworks/models/llama-v3p1-8b-instruct",
        max_tokens=200,
    )
    print(out["text"])


if __name__ == "__main__":
    main()
