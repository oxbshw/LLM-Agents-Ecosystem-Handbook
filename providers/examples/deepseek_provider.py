"""DeepSeek provider example.

Setup:
    pip install openai
    export DEEPSEEK_API_KEY=...
"""

from utilities import get_provider


def main() -> None:
    p = get_provider("deepseek")
    out = p.chat(
        [{"role": "user", "content": "List 3 strengths of DeepSeek-R1 / V3 series."}],
        model="deepseek-chat",
        max_tokens=200,
    )
    print(out["text"])


if __name__ == "__main__":
    main()
