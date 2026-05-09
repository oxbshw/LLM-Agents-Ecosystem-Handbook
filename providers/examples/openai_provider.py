"""OpenAI provider example.

Setup:
    pip install openai
    export OPENAI_API_KEY=sk-...

Run:
    python providers/examples/openai_provider.py
"""

from __future__ import annotations

from utilities import get_provider
from utilities.provider_errors import ProviderNotConfigured


def main() -> None:
    p = get_provider("openai")
    try:
        out = p.chat(
            [
                {"role": "system", "content": "You are concise."},
                {"role": "user", "content": "Summarize MCP in one sentence."},
            ],
            model="gpt-4o-mini",
        )
    except ProviderNotConfigured as exc:
        print(f"❌ {exc}")
        return
    print(out["text"])
    print(f"\n[usage] {out['usage']}")


if __name__ == "__main__":
    main()
