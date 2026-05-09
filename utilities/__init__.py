"""Utilities package — provider abstraction and shared helpers."""

from .llm_provider import (
    LLMProvider,
    complete,
    get_provider,
    get_provider_info,
    list_providers,
)
from .provider_errors import (
    ProviderAuth,
    ProviderError,
    ProviderNotConfigured,
    ProviderRateLimited,
    ProviderSDKMissing,
    ProviderTransient,
    ProviderUnsupportedCapability,
    ProviderRouterExhausted,
)

__all__ = [
    "LLMProvider",
    "complete",
    "get_provider",
    "get_provider_info",
    "list_providers",
    "ProviderError",
    "ProviderNotConfigured",
    "ProviderSDKMissing",
    "ProviderUnsupportedCapability",
    "ProviderRateLimited",
    "ProviderTransient",
    "ProviderAuth",
    "ProviderRouterExhausted",
]
