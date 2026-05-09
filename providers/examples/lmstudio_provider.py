"""LM Studio provider example.

Setup:
    1. Install LM Studio (https://lmstudio.ai)
    2. Download a model
    3. Open Local Server tab, click "Start Server"
    4. LMSTUDIO_BASE_URL defaults to http://localhost:1234/v1

The "model" arg can be left as the loaded model's name (LM Studio
ignores it and uses the loaded model).
"""

from utilities import get_provider


def main() -> None:
    p = get_provider("lmstudio")
    out = p.chat(
        [{"role": "user", "content": "What's a quick test for whether LM Studio is up?"}],
        model="local-model",
        max_tokens=200,
    )
    print(out["text"])


if __name__ == "__main__":
    main()
