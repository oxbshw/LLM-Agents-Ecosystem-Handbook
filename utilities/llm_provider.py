"""Multi-provider LLM abstraction.

Goals
-----
- One interface (`LLMProvider`) over 20+ providers.
- OpenAI-compatible HTTP path covers most providers without extra SDKs.
- Anthropic (and stub paths for Bedrock/Replicate) handled separately.
- Backwards-compatible `complete()` for existing examples.

Quick start
-----------
    from utilities.llm_provider import complete, get_provider

    # Backwards-compatible one-shot:
    text = complete("Summarize MCP in one sentence.")

    # Modern: explicit provider object
    p = get_provider("groq")
    out = p.chat([
        {"role": "system", "content": "You are concise."},
        {"role": "user", "content": "Summarize MCP in one sentence."},
    ], model="llama-3.1-8b-instant")
    print(out["text"])

Switch providers at runtime via the ``LLM_PROVIDER`` environment variable
or by passing ``provider=`` to ``complete()`` / ``get_provider()``.

Design notes
------------
- We import provider SDKs lazily — installing ``openai`` is enough to reach
  OpenAI, Groq, Together, Fireworks, OpenRouter, Mistral, DeepSeek, xAI,
  Perplexity, Cohere, NVIDIA NIM, Hugging Face, and every local runtime
  via OpenAI-compatible base URLs.
- ``anthropic`` is needed for Anthropic. ``boto3`` is needed for Bedrock.
- Errors are typed (``provider_errors.py``).
"""

from __future__ import annotations

import os
from typing import Any, Iterable, Optional

from . import provider_config as cfg
from .provider_errors import (
    ProviderAuth,
    ProviderError,
    ProviderNotConfigured,
    ProviderRateLimited,
    ProviderSDKMissing,
    ProviderTransient,
    ProviderUnsupportedCapability,
)


# ---------------------------------------------------------------------------
# Public interface
# ---------------------------------------------------------------------------


class LLMProvider:
    """Generic LLM provider.

    Adapters share this interface. Use ``chat()`` for messages-style calls
    and ``complete_text()`` for plain prompt-in / text-out.
    """

    def __init__(self, info: cfg.ProviderInfo):
        self.info = info
        self._key = self._resolve_key()
        self._base_url = self._resolve_base_url()

    # -- helpers --

    def _resolve_key(self) -> Optional[str]:
        if not self.info.api_key_env:
            return None  # local providers
        return os.getenv(self.info.api_key_env)

    def _resolve_base_url(self) -> Optional[str]:
        if self.info.base_url_env and (val := os.getenv(self.info.base_url_env)):
            return val
        return self.info.default_base_url

    def _require_key(self) -> str:
        if not self.info.api_key_env:
            return ""
        if not self._key:
            raise ProviderNotConfigured(
                f"{self.info.display_name}: set {self.info.api_key_env} in your environment."
            )
        return self._key

    def _require(self, capability: str) -> None:
        if capability not in self.info.capabilities:
            raise ProviderUnsupportedCapability(
                f"{self.info.display_name} does not support '{capability}'."
            )

    # -- core methods --

    def chat(
        self,
        messages: list[dict[str, Any]],
        *,
        model: Optional[str] = None,
        temperature: float = 0.2,
        max_tokens: int = 1024,
        tools: Optional[list[dict]] = None,
        response_format: Optional[dict] = None,
        stream: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Send chat messages and return a normalized response.

        Returns
        -------
        dict with keys:
            - ``text``: assistant content (str)
            - ``tool_calls``: list of tool calls (or [])
            - ``usage``: provider-reported token usage (or {})
            - ``raw``: the raw provider response (provider-specific)
        """
        if self.info.name == "anthropic":
            return _chat_anthropic(self, messages, model, temperature, max_tokens, tools, **kwargs)

        if self.info.name == "bedrock":
            raise ProviderError(
                "Bedrock adapter is documented but not implemented in code. "
                "See providers/local_models.md and providers/examples/ — use boto3 + bedrock-runtime."
            )
        if self.info.name == "replicate":
            raise ProviderError(
                "Replicate adapter is documented but not implemented in code. "
                "See providers/examples/ for the predict-style API pattern."
            )

        if not self.info.openai_compatible:
            raise ProviderError(
                f"{self.info.display_name}: no OpenAI-compatible adapter; see providers/examples/."
            )

        return _chat_openai_compatible(
            self,
            messages,
            model=model or self.info.default_model,
            temperature=_clamp_temperature(temperature, self.info.name),
            max_tokens=max_tokens,
            tools=tools,
            response_format=response_format,
            stream=stream,
            **kwargs,
        )

    def complete_text(
        self,
        prompt: str,
        *,
        system: str = "You are a helpful AI assistant.",
        model: Optional[str] = None,
        temperature: float = 0.2,
        max_tokens: int = 1024,
    ) -> str:
        """Convenience: turn a single prompt into a single string response."""
        out = self.chat(
            [{"role": "system", "content": system}, {"role": "user", "content": prompt}],
            model=model,
            temperature=temperature,
            max_tokens=max_tokens,
        )
        return (out.get("text") or "").strip()


# ---------------------------------------------------------------------------
# Adapter implementations
# ---------------------------------------------------------------------------


def _import_openai():
    try:
        from openai import OpenAI  # type: ignore

        return OpenAI
    except ImportError as exc:  # pragma: no cover
        raise ProviderSDKMissing(
            "Install the OpenAI SDK: `pip install openai` "
            "(used for all OpenAI-compatible providers)."
        ) from exc


def _chat_openai_compatible(
    p: "LLMProvider",
    messages: list[dict],
    *,
    model: Optional[str],
    temperature: float,
    max_tokens: int,
    tools: Optional[list[dict]],
    response_format: Optional[dict],
    stream: bool,
    **kwargs: Any,
) -> dict[str, Any]:
    OpenAI = _import_openai()
    client_kwargs: dict[str, Any] = {}
    if p._base_url:
        client_kwargs["base_url"] = p._base_url
    if p.info.api_key_env:
        client_kwargs["api_key"] = p._require_key()
    else:
        # local providers often want any non-empty key
        client_kwargs["api_key"] = "local-no-key"

    client = OpenAI(**client_kwargs)

    call_kwargs: dict[str, Any] = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
        "max_tokens": max_tokens,
    }
    if tools:
        call_kwargs["tools"] = tools
    if response_format:
        call_kwargs["response_format"] = response_format
    if stream:
        call_kwargs["stream"] = True
    call_kwargs.update(kwargs)

    try:
        resp = client.chat.completions.create(**call_kwargs)
    except Exception as exc:
        raise _map_openai_exc(exc) from exc

    if stream:
        return {"text": None, "tool_calls": [], "usage": {}, "raw": resp, "stream": True}

    msg = resp.choices[0].message
    text = msg.content or ""
    tool_calls = getattr(msg, "tool_calls", None) or []
    usage = getattr(resp, "usage", None)
    return {
        "text": text,
        "tool_calls": [tc.model_dump() if hasattr(tc, "model_dump") else tc for tc in tool_calls],
        "usage": usage.model_dump() if usage and hasattr(usage, "model_dump") else {},
        "raw": resp,
    }


def _chat_anthropic(
    p: "LLMProvider",
    messages: list[dict],
    model: Optional[str],
    temperature: float,
    max_tokens: int,
    tools: Optional[list[dict]],
    **kwargs: Any,
) -> dict[str, Any]:
    try:
        import anthropic as _anthropic  # type: ignore
    except ImportError as exc:  # pragma: no cover
        raise ProviderSDKMissing(
            "Install Anthropic SDK: `pip install anthropic`."
        ) from exc

    p._require_key()

    # Anthropic separates system from messages.
    system = ""
    converted: list[dict] = []
    for m in messages:
        if m["role"] == "system":
            system += (("\n\n" if system else "") + str(m["content"]))
        else:
            converted.append(m)

    client = _anthropic.Anthropic()
    try:
        resp = client.messages.create(
            model=model or p.info.default_model,
            max_tokens=max_tokens,
            temperature=temperature,
            system=system or None,
            messages=converted,
            tools=tools or [],
        )
    except Exception as exc:
        raise _map_anthropic_exc(exc) from exc

    text_parts: list[str] = []
    tool_calls: list[dict] = []
    for block in resp.content:
        if getattr(block, "type", None) == "text":
            text_parts.append(getattr(block, "text", ""))
        elif getattr(block, "type", None) == "tool_use":
            tool_calls.append(
                {
                    "id": getattr(block, "id", None),
                    "name": getattr(block, "name", None),
                    "input": getattr(block, "input", None),
                }
            )

    usage = getattr(resp, "usage", None)
    return {
        "text": "".join(text_parts).strip(),
        "tool_calls": tool_calls,
        "usage": usage.model_dump() if usage and hasattr(usage, "model_dump") else {},
        "raw": resp,
    }


# ---------------------------------------------------------------------------
# Error mapping
# ---------------------------------------------------------------------------


def _map_openai_exc(exc: Exception) -> ProviderError:
    name = type(exc).__name__.lower()
    msg = str(exc)
    if "ratelimit" in name or "429" in msg:
        return ProviderRateLimited(msg)
    if "auth" in name or "401" in msg or "403" in msg:
        return ProviderAuth(msg)
    if "timeout" in name or "apiconnection" in name:
        return ProviderTransient(msg)
    return ProviderError(msg)


def _map_anthropic_exc(exc: Exception) -> ProviderError:
    name = type(exc).__name__.lower()
    msg = str(exc)
    if "ratelimit" in name:
        return ProviderRateLimited(msg)
    if "authentication" in name or "permission" in name:
        return ProviderAuth(msg)
    if "apitimeout" in name or "apiconnection" in name:
        return ProviderTransient(msg)
    return ProviderError(msg)


# ---------------------------------------------------------------------------
# Module-level helpers
# ---------------------------------------------------------------------------


def _clamp_temperature(temperature: float, provider: str) -> float:
    """Clamp temperature into provider-specific valid range."""
    if provider == "minimax":
        return max(0.01, min(temperature, 1.0))
    return max(0.0, min(temperature, 2.0))


def _resolve_provider_name(provider: Optional[str]) -> str:
    name = (provider or os.getenv("LLM_PROVIDER", "openai")).lower().strip()
    if name not in cfg.PROVIDERS:
        raise ProviderError(
            f"Unknown provider '{name}'. Known: {sorted(cfg.PROVIDERS)}"
        )
    return name


def get_provider(name: Optional[str] = None) -> LLMProvider:
    """Return an `LLMProvider` for the given name (or the env-default)."""
    return LLMProvider(cfg.get(_resolve_provider_name(name)))


# ---------------------------------------------------------------------------
# Backwards-compatible API
# ---------------------------------------------------------------------------


def complete(
    prompt: str,
    *,
    provider: Optional[str] = None,
    model: Optional[str] = None,
    system: str = "You are a helpful AI assistant.",
    temperature: float = 0.7,
    max_tokens: int = 1024,
) -> str:
    """One-shot prompt → text response. Backwards-compatible with the
    pre-1.0.1 utility."""
    p = get_provider(provider)
    return p.complete_text(
        prompt,
        system=system,
        model=model,
        temperature=temperature,
        max_tokens=max_tokens,
    )


def get_provider_info() -> dict:
    """Inspect the default-resolved provider."""
    p = get_provider(None)
    return {
        "provider": p.info.name,
        "display_name": p.info.display_name,
        "model": p.info.default_model,
        "base_url": p._base_url,
        "family": p.info.family,
        "capabilities": sorted(p.info.capabilities),
        "openai_compatible": p.info.openai_compatible,
    }


def list_providers(family: Optional[str] = None) -> list[dict]:
    """Enumerate known providers (optionally filtered by family)."""
    sources: Iterable[cfg.ProviderInfo] = (
        cfg.by_family(family) if family else cfg.PROVIDERS.values()
    )
    return [
        {
            "name": p.name,
            "display_name": p.display_name,
            "family": p.family,
            "capabilities": sorted(p.capabilities),
            "api_key_env": p.api_key_env,
            "default_base_url": p.default_base_url,
            "default_model": p.default_model,
            "openai_compatible": p.openai_compatible,
        }
        for p in sources
    ]


__all__ = [
    "LLMProvider",
    "ProviderError",
    "complete",
    "get_provider",
    "get_provider_info",
    "list_providers",
]
