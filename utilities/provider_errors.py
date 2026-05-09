"""Typed errors for the provider layer.

Catch the narrowest one you can; let the rest bubble.
"""

from __future__ import annotations


class ProviderError(Exception):
    """Base class for all provider-layer errors."""


class ProviderNotConfigured(ProviderError):
    """A required env var is missing."""


class ProviderSDKMissing(ProviderError):
    """The provider's Python SDK is not installed."""


class ProviderUnsupportedCapability(ProviderError):
    """The provider doesn't support the requested capability."""


class ProviderRateLimited(ProviderError):
    """The provider returned a rate-limit error."""


class ProviderTransient(ProviderError):
    """A retry-eligible error (timeout, 5xx)."""


class ProviderAuth(ProviderError):
    """Auth failed (bad / expired key)."""


class ProviderRouterExhausted(ProviderError):
    """All providers in the fallback chain failed."""
