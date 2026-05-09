"""Anthropic provider example.

Setup:
    pip install anthropic
    export ANTHROPIC_API_KEY=...

Run:
    python providers/examples/anthropic_provider.py

Note: Anthropic uses its own Messages API (not OpenAI-compatible). System
messages are extracted from the message list and passed separately by the
abstraction.
"""

from __future__ import annotations

from utilities import get_provider
from utilities.provider_errors import ProviderNotConfigured


def main() -> None:
    p = get_provider("anthropic")
    try:
        out = p.chat(
            [
                {"role": "system", "content": "You are a concise senior engineer."},
                {"role": "user", "content": "What's MCP and why does it matter? One paragraph."},
            ],
            model="claude-3-5-haiku-20241022",
            max_tokens=300,
        )
    except ProviderNotConfigured as exc:
        print(f"❌ {exc}")
        return
    print(out["text"])


if __name__ == "__main__":
    main()
