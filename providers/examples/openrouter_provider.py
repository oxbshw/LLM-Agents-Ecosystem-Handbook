"""OpenRouter provider example — single key, many models.

Setup:
    pip install openai
    export OPENROUTER_API_KEY=...

OpenRouter routes one HTTP request to many backends. Use it as a
fallback or when you need to A/B compare models without paying per-vendor.
"""

from utilities import get_provider


def main() -> None:
    p = get_provider("openrouter")
    out = p.chat(
        [{"role": "user", "content": "When does a model marketplace make sense?"}],
        model="openai/gpt-4o-mini",
        max_tokens=200,
    )
    print(out["text"])


if __name__ == "__main__":
    main()
