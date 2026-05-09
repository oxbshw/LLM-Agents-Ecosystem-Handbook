"""Provider routing + fallback chains.

Use cases
---------
- "I want fast & cheap for summarization" → ``router.select("fast_cheap")``
- "I want the strongest reasoning, fall back if rate-limited" → fallback chain
- "I want privacy / local" → local-only chain
- "I want a vision-capable provider" → capability-filtered selection

The router does *not* know prices or live latencies. It picks based on
provider *capability tags* and your declared *task class*; you supply the
chain. Treat this as routing scaffolding — production setups should wire
real-time signals (cost dashboards, rate-limit headers, health checks).

Configure routes via env or code:
- ``ROUTER_DEFAULT``: comma-separated provider names tried in order
- ``ROUTER_FAST``: chain for ``"fast"`` task class
- ``ROUTER_CHEAP``: chain for ``"cheap"``
- ``ROUTER_REASONING``: chain for ``"reasoning"``
- ``ROUTER_LONG_CONTEXT``: chain for ``"long_context"``
- ``ROUTER_VISION``: chain for ``"vision"``
- ``ROUTER_LOCAL``: chain for ``"local"``

You can also pass a chain explicitly to ``ProviderRouter(chains=…)``.

Example
-------
    from utilities.provider_router import ProviderRouter

    router = ProviderRouter()
    out = router.chat(
        [{"role": "user", "content": "Summarize this PR in 3 bullets."}],
        task_class="cheap",
    )
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Any, Callable, Iterable, Optional

from . import provider_config as cfg
from .llm_provider import LLMProvider, get_provider
from .provider_errors import (
    ProviderAuth,
    ProviderError,
    ProviderNotConfigured,
    ProviderRateLimited,
    ProviderRouterExhausted,
    ProviderTransient,
    ProviderUnsupportedCapability,
)


DEFAULT_CHAINS: dict[str, list[str]] = {
    # Sensible defaults; override via env or kwargs.
    "default": ["openai", "anthropic", "openrouter"],
    "cheap": ["groq", "deepseek", "together", "openrouter"],
    "fast": ["groq", "cerebras", "fireworks"],
    "reasoning": ["anthropic", "openai", "google", "deepseek"],
    "long_context": ["google", "anthropic", "minimax", "openai"],
    "vision": ["openai", "google", "anthropic", "xai"],
    "local": ["ollama", "lmstudio", "vllm", "llamacpp"],
    "research": ["perplexity", "openai", "anthropic"],
}


def _env_chain(env_var: str) -> Optional[list[str]]:
    raw = os.getenv(env_var)
    if not raw:
        return None
    return [s.strip() for s in raw.split(",") if s.strip()]


@dataclass
class RouteAttempt:
    provider: str
    success: bool
    error: Optional[str] = None


class ProviderRouter:
    """Selects providers by task class with fallback."""

    def __init__(
        self,
        chains: Optional[dict[str, list[str]]] = None,
        provider_factory: Callable[[str], LLMProvider] = get_provider,
    ):
        self.chains: dict[str, list[str]] = dict(DEFAULT_CHAINS)
        if chains:
            self.chains.update(chains)
        # Env overrides
        for task in list(self.chains):
            override = _env_chain(f"ROUTER_{task.upper()}")
            if override:
                self.chains[task] = override
        self._factory = provider_factory
        self.last_attempts: list[RouteAttempt] = []

    def select(
        self,
        task_class: str = "default",
        constraints: Optional[Iterable[str]] = None,
    ) -> list[str]:
        """Return the ordered list of provider names to try.

        ``constraints`` filters out providers that don't have all of the
        listed capabilities (e.g. ``["tool_calling", "vision"]``).
        """
        chain = list(self.chains.get(task_class, self.chains["default"]))
        if constraints:
            wanted = set(constraints)
            chain = [
                name
                for name in chain
                if wanted.issubset(cfg.PROVIDERS.get(name, cfg.ProviderInfo(
                    name=name, display_name=name, api_key_env=None
                )).capabilities)
            ]
        if not chain:
            raise ProviderError(
                f"No providers in chain '{task_class}' satisfy {sorted(constraints or [])}."
            )
        return chain

    def chat(
        self,
        messages: list[dict[str, Any]],
        *,
        task_class: str = "default",
        constraints: Optional[Iterable[str]] = None,
        retry_transient: bool = True,
        **chat_kwargs: Any,
    ) -> dict[str, Any]:
        """Try providers in order; return the first success.

        Falls back on these errors:
        - ``ProviderRateLimited``
        - ``ProviderTransient``
        - ``ProviderNotConfigured``  (skip; key not set)
        - ``ProviderUnsupportedCapability``
        - ``ProviderAuth``  (skip; bad key)

        Re-raises everything else so genuine bugs aren't masked.
        """
        chain = self.select(task_class, constraints)
        self.last_attempts = []
        last_exc: Optional[Exception] = None

        for name in chain:
            try:
                provider = self._factory(name)
            except ProviderError as exc:
                self.last_attempts.append(RouteAttempt(name, False, str(exc)))
                last_exc = exc
                continue

            try:
                result = provider.chat(messages, **chat_kwargs)
                self.last_attempts.append(RouteAttempt(name, True))
                result["_router"] = {
                    "provider_used": name,
                    "task_class": task_class,
                    "attempts": len(self.last_attempts),
                }
                return result
            except (
                ProviderNotConfigured,
                ProviderAuth,
                ProviderUnsupportedCapability,
                ProviderRateLimited,
                ProviderTransient,
            ) as exc:
                self.last_attempts.append(RouteAttempt(name, False, type(exc).__name__))
                last_exc = exc
                if not retry_transient and isinstance(exc, ProviderTransient):
                    raise
                continue
            # Non-routable errors propagate.

        raise ProviderRouterExhausted(
            f"All providers in chain '{task_class}' failed: "
            f"{[a.error for a in self.last_attempts]}"
        ) from last_exc


__all__ = ["ProviderRouter", "RouteAttempt", "DEFAULT_CHAINS"]
