"""Cohere provider example (OpenAI-compatible endpoint).

Setup:
    pip install openai
    export COHERE_API_KEY=...

Cohere is best known for its reranker. The chat path here uses Cohere's
OpenAI-compatibility endpoint. For reranking, use the dedicated cohere SDK
(`pip install cohere`) and call `client.rerank(...)`.
"""

from utilities import get_provider


def main() -> None:
    p = get_provider("cohere")
    out = p.chat(
        [{"role": "user", "content": "Two strengths of Cohere Command-R."}],
        model="command-r",
        max_tokens=200,
    )
    print(out["text"])


if __name__ == "__main__":
    main()
