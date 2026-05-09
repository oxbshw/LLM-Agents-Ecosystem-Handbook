"""Groq provider example — sub-second latency.

Setup:
    pip install openai
    export GROQ_API_KEY=...

Groq is optimized for time-to-first-token; great for interactive UX and
high-throughput classification/extraction.
"""

import time

from utilities import get_provider


def main() -> None:
    p = get_provider("groq")
    t0 = time.time()
    out = p.chat(
        [{"role": "user", "content": "List 5 latency-sensitive agent use cases."}],
        model="llama-3.1-8b-instant",
        max_tokens=200,
    )
    print(out["text"])
    print(f"\n[wall_time] {time.time() - t0:.2f}s")


if __name__ == "__main__":
    main()
