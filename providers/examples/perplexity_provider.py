"""Perplexity provider example — built-in web search grounding.

Setup:
    pip install openai
    export PERPLEXITY_API_KEY=...

Perplexity returns web-grounded answers; great for research-class agents
where freshness matters and you don't want to wire your own retrieval.
"""

from utilities import get_provider


def main() -> None:
    p = get_provider("perplexity")
    out = p.chat(
        [
            {"role": "user", "content": "What is MCP, and which clients support it as of this year?"},
        ],
        model="sonar",
        max_tokens=400,
    )
    print(out["text"])


if __name__ == "__main__":
    main()
