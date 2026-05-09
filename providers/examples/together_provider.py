"""Together AI provider example.

Setup:
    pip install openai
    export TOGETHER_API_KEY=...
"""

from utilities import get_provider


def main() -> None:
    p = get_provider("together")
    out = p.chat(
        [{"role": "user", "content": "Pros and cons of model marketplaces, 3 of each."}],
        model="meta-llama/Llama-3.1-8B-Instruct-Turbo",
        max_tokens=300,
    )
    print(out["text"])


if __name__ == "__main__":
    main()
