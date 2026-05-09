"""Google Gemini provider example (via OpenAI-compatible endpoint).

Setup:
    pip install openai
    export GOOGLE_API_KEY=...

Gemini ships an OpenAI-compatible base URL — no separate google-genai SDK
required for the basic chat path.

Run:
    python providers/examples/google_provider.py
"""

from __future__ import annotations

from utilities import get_provider


def main() -> None:
    p = get_provider("google")
    out = p.chat(
        [{"role": "user", "content": "Three ways Gemini differs from GPT-4o-class models."}],
        model="gemini-1.5-flash",
        max_tokens=300,
    )
    print(out["text"])


if __name__ == "__main__":
    main()
