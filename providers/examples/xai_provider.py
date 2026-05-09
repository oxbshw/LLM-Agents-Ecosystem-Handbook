"""xAI Grok provider example.

Setup:
    pip install openai
    export XAI_API_KEY=...
"""

from utilities import get_provider


def main() -> None:
    p = get_provider("xai")
    out = p.chat(
        [{"role": "user", "content": "When would you reach for a Grok-class model?"}],
        model="grok-2",
        max_tokens=200,
    )
    print(out["text"])


if __name__ == "__main__":
    main()
