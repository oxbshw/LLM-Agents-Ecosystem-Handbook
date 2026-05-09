"""Provider router example — chains, fallbacks, capability filters.

Run:
    python providers/examples/router_example.py

This script shows the most useful router patterns. Wrap or adapt for your
own agent runtime.
"""

from __future__ import annotations

from utilities.provider_router import ProviderRouter


def demo_cheap() -> None:
    """Try cheap providers in order; first to respond wins."""
    print("\n=== cheap-first ===")
    router = ProviderRouter()
    out = router.chat(
        [{"role": "user", "content": "TL;DR: model context protocol."}],
        task_class="cheap",
        max_tokens=150,
    )
    print("provider:", out["_router"]["provider_used"])
    print(out["text"])


def demo_local_first() -> None:
    """Stay local for privacy; fall back to hosted only on outright failure."""
    print("\n=== local-first ===")
    router = ProviderRouter(
        chains={"default": ["ollama", "lmstudio", "openai"]}
    )
    out = router.chat(
        [{"role": "user", "content": "What does 'local-first agent' mean?"}],
        max_tokens=150,
    )
    print("provider:", out["_router"]["provider_used"])
    print(out["text"][:300])


def demo_capability_filter() -> None:
    """Only use providers that support BOTH tool calling and vision."""
    print("\n=== capability filter ===")
    router = ProviderRouter()
    chain = router.select(
        "reasoning",
        constraints=["tool_calling", "vision"],
    )
    print("filtered chain:", chain)


def demo_inspect_attempts() -> None:
    """See which providers were tried and why others were skipped."""
    print("\n=== attempts ===")
    router = ProviderRouter()
    try:
        router.chat([{"role": "user", "content": "Hello"}], task_class="cheap", max_tokens=20)
    except Exception as exc:
        print(f"router exhausted: {exc}")
    for a in router.last_attempts:
        flag = "✅" if a.success else "❌"
        print(f"  {flag} {a.provider}  {a.error or ''}")


if __name__ == "__main__":
    demo_capability_filter()
    # The next demos make real calls — comment out unless you have keys set.
    # demo_cheap()
    # demo_local_first()
    # demo_inspect_attempts()
