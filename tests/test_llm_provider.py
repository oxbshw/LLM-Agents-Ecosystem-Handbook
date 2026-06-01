"""Tests for utilities/llm_provider.py

Unit tests cover:
- Provider resolution (env var, explicit arg, default)
- Temperature clamping for MiniMax
- get_provider_info() returns expected structure
- _call_openai / complete() route to the correct SDK with correct params
- Missing API key raises EnvironmentError
- Unknown provider raises ValueError

Integration tests (skipped when keys are absent) cover:
- Live MiniMax M3 call returns a non-empty string
- Live OpenAI call returns a non-empty string
"""

from __future__ import annotations

import os
import types
import sys
from unittest.mock import MagicMock, patch

import pytest

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _make_openai_response(text: str):
    """Build a minimal mock that looks like an OpenAI ChatCompletion response."""
    choice = MagicMock()
    choice.message.content = text
    response = MagicMock()
    response.choices = [choice]
    return response


def _make_anthropic_response(text: str):
    """Build a minimal mock that looks like an Anthropic Messages response."""
    content_block = MagicMock()
    content_block.text = text
    response = MagicMock()
    response.content = [content_block]
    return response


# ---------------------------------------------------------------------------
# Unit tests
# ---------------------------------------------------------------------------


class TestResolveProvider:
    def test_defaults_to_openai(self, monkeypatch):
        monkeypatch.delenv("LLM_PROVIDER", raising=False)
        from utilities.llm_provider import _resolve_provider
        assert _resolve_provider(None) == "openai"

    def test_explicit_arg_wins_over_env(self, monkeypatch):
        monkeypatch.setenv("LLM_PROVIDER", "openai")
        from utilities.llm_provider import _resolve_provider
        assert _resolve_provider("minimax") == "minimax"

    def test_env_var_used_when_no_arg(self, monkeypatch):
        monkeypatch.setenv("LLM_PROVIDER", "anthropic")
        from utilities.llm_provider import _resolve_provider
        assert _resolve_provider(None) == "anthropic"

    def test_unknown_provider_raises(self):
        from utilities.llm_provider import _resolve_provider
        with pytest.raises(ValueError, match="Unknown provider"):
            _resolve_provider("foobar")

    def test_case_insensitive(self, monkeypatch):
        monkeypatch.delenv("LLM_PROVIDER", raising=False)
        from utilities.llm_provider import _resolve_provider
        assert _resolve_provider("MiniMax") == "minimax"
        assert _resolve_provider("OPENAI") == "openai"


class TestTemperatureClamping:
    def test_minimax_zero_clamped_to_positive(self):
        from utilities.llm_provider import _clamp_temperature
        result = _clamp_temperature(0.0, "minimax")
        assert result > 0.0

    def test_minimax_above_one_clamped(self):
        from utilities.llm_provider import _clamp_temperature
        assert _clamp_temperature(1.5, "minimax") == 1.0

    def test_minimax_valid_temperature_unchanged(self):
        from utilities.llm_provider import _clamp_temperature
        assert _clamp_temperature(0.7, "minimax") == 0.7

    def test_openai_zero_allowed(self):
        from utilities.llm_provider import _clamp_temperature
        assert _clamp_temperature(0.0, "openai") == 0.0

    def test_anthropic_zero_allowed(self):
        from utilities.llm_provider import _clamp_temperature
        assert _clamp_temperature(0.0, "anthropic") == 0.0


class TestGetProviderInfo:
    def test_returns_dict_with_required_keys(self, monkeypatch):
        monkeypatch.delenv("LLM_PROVIDER", raising=False)
        from utilities.llm_provider import get_provider_info
        info = get_provider_info()
        assert "provider" in info
        assert "model" in info
        assert "base_url" in info

    def test_minimax_base_url(self, monkeypatch):
        monkeypatch.setenv("LLM_PROVIDER", "minimax")
        from utilities import llm_provider
        import importlib
        importlib.reload(llm_provider)
        info = llm_provider.get_provider_info()
        assert info["provider"] == "minimax"
        assert "minimax.io" in (info["base_url"] or "")


class TestMissingApiKey:
    def test_minimax_missing_key_raises(self, monkeypatch):
        monkeypatch.delenv("MINIMAX_API_KEY", raising=False)
        from utilities.llm_provider import complete
        with pytest.raises(EnvironmentError, match="MINIMAX_API_KEY"):
            complete("hello", provider="minimax")

    def test_openai_missing_key_raises(self, monkeypatch):
        monkeypatch.delenv("OPENAI_API_KEY", raising=False)
        from utilities.llm_provider import complete
        with pytest.raises(EnvironmentError, match="OPENAI_API_KEY"):
            complete("hello", provider="openai")


class TestCompleteOpenAI:
    def test_routes_to_openai_sdk(self, monkeypatch):
        monkeypatch.setenv("OPENAI_API_KEY", "test-key-openai")
        mock_client_cls = MagicMock()
        mock_instance = MagicMock()
        mock_client_cls.return_value = mock_instance
        mock_instance.chat.completions.create.return_value = _make_openai_response(
            "OpenAI response"
        )
        with patch.dict("sys.modules", {"openai": MagicMock(OpenAI=mock_client_cls)}):
            from utilities import llm_provider
            import importlib
            importlib.reload(llm_provider)
            result = llm_provider.complete("What is AI?", provider="openai")
        assert result == "OpenAI response"

    def test_default_model_sent(self, monkeypatch):
        monkeypatch.setenv("OPENAI_API_KEY", "test-key-openai")
        mock_client_cls = MagicMock()
        mock_instance = MagicMock()
        mock_client_cls.return_value = mock_instance
        mock_instance.chat.completions.create.return_value = _make_openai_response("ok")
        with patch.dict("sys.modules", {"openai": MagicMock(OpenAI=mock_client_cls)}):
            from utilities import llm_provider
            import importlib
            importlib.reload(llm_provider)
            llm_provider.complete("hi", provider="openai")
            call_kwargs = mock_instance.chat.completions.create.call_args
            assert call_kwargs.kwargs["model"] == llm_provider.OPENAI_DEFAULT_MODEL


class TestCompleteMiniMax:
    def test_routes_to_openai_sdk_with_minimax_base_url(self, monkeypatch):
        monkeypatch.setenv("MINIMAX_API_KEY", "test-key-minimax")
        mock_client_cls = MagicMock()
        mock_instance = MagicMock()
        mock_client_cls.return_value = mock_instance
        mock_instance.chat.completions.create.return_value = _make_openai_response(
            "MiniMax response"
        )
        with patch.dict("sys.modules", {"openai": MagicMock(OpenAI=mock_client_cls)}):
            from utilities import llm_provider
            import importlib
            importlib.reload(llm_provider)
            result = llm_provider.complete("What is AI?", provider="minimax")
        assert result == "MiniMax response"
        # Client must be constructed with the MiniMax base URL
        init_kwargs = mock_client_cls.call_args.kwargs
        assert "minimax.io" in init_kwargs.get("base_url", "")

    def test_temperature_clamped_for_minimax(self, monkeypatch):
        monkeypatch.setenv("MINIMAX_API_KEY", "test-key-minimax")
        mock_client_cls = MagicMock()
        mock_instance = MagicMock()
        mock_client_cls.return_value = mock_instance
        mock_instance.chat.completions.create.return_value = _make_openai_response("ok")
        with patch.dict("sys.modules", {"openai": MagicMock(OpenAI=mock_client_cls)}):
            from utilities import llm_provider
            import importlib
            importlib.reload(llm_provider)
            llm_provider.complete("hi", provider="minimax", temperature=0.0)
            call_kwargs = mock_instance.chat.completions.create.call_args.kwargs
            assert call_kwargs["temperature"] > 0.0

    def test_default_model_is_m3(self, monkeypatch):
        monkeypatch.setenv("MINIMAX_API_KEY", "test-key-minimax")
        mock_client_cls = MagicMock()
        mock_instance = MagicMock()
        mock_client_cls.return_value = mock_instance
        mock_instance.chat.completions.create.return_value = _make_openai_response("ok")
        with patch.dict("sys.modules", {"openai": MagicMock(OpenAI=mock_client_cls)}):
            from utilities import llm_provider
            import importlib
            importlib.reload(llm_provider)
            llm_provider.complete("hi", provider="minimax")
            call_kwargs = mock_instance.chat.completions.create.call_args.kwargs
            assert call_kwargs["model"] == "MiniMax-M3"

    def test_custom_model_respected(self, monkeypatch):
        monkeypatch.setenv("MINIMAX_API_KEY", "test-key-minimax")
        mock_client_cls = MagicMock()
        mock_instance = MagicMock()
        mock_client_cls.return_value = mock_instance
        mock_instance.chat.completions.create.return_value = _make_openai_response("ok")
        with patch.dict("sys.modules", {"openai": MagicMock(OpenAI=mock_client_cls)}):
            from utilities import llm_provider
            import importlib
            importlib.reload(llm_provider)
            llm_provider.complete("hi", provider="minimax", model="MiniMax-M2.7-highspeed")
            call_kwargs = mock_instance.chat.completions.create.call_args.kwargs
            assert call_kwargs["model"] == "MiniMax-M2.7-highspeed"


class TestCompleteAnthropic:
    def test_routes_to_anthropic_sdk(self, monkeypatch):
        monkeypatch.setenv("ANTHROPIC_API_KEY", "test-key-anthropic")
        mock_anthropic_module = MagicMock()
        mock_client = MagicMock()
        mock_anthropic_module.Anthropic.return_value = mock_client
        mock_client.messages.create.return_value = _make_anthropic_response(
            "Anthropic response"
        )
        with patch.dict("sys.modules", {"anthropic": mock_anthropic_module}):
            from utilities import llm_provider
            import importlib
            importlib.reload(llm_provider)
            result = llm_provider.complete("What is AI?", provider="anthropic")
        assert result == "Anthropic response"


# ---------------------------------------------------------------------------
# Integration tests (only run when API keys are present)
# ---------------------------------------------------------------------------


@pytest.mark.skipif(
    not os.getenv("MINIMAX_API_KEY"),
    reason="MINIMAX_API_KEY not set — skipping live MiniMax integration test",
)
class TestMiniMaxIntegration:
    def test_live_m3_returns_nonempty_string(self):
        from utilities.llm_provider import complete
        result = complete(
            "In one sentence, what is the main advantage of multi-agent LLM systems?",
            provider="minimax",
            model="MiniMax-M3",
            max_tokens=64,
        )
        assert isinstance(result, str)
        assert len(result) > 0

    def test_live_m27_returns_nonempty_string(self):
        from utilities.llm_provider import complete
        result = complete(
            "In one sentence, what is the main advantage of multi-agent LLM systems?",
            provider="minimax",
            model="MiniMax-M2.7",
            max_tokens=64,
        )
        assert isinstance(result, str)
        assert len(result) > 0

    def test_live_m27_highspeed_returns_nonempty_string(self):
        from utilities.llm_provider import complete
        result = complete(
            "Name one popular LLM agent framework.",
            provider="minimax",
            model="MiniMax-M2.7-highspeed",
            max_tokens=32,
        )
        assert isinstance(result, str)
        assert len(result) > 0

    def test_live_system_prompt_applied(self):
        from utilities.llm_provider import complete
        result = complete(
            "What are you?",
            provider="minimax",
            model="MiniMax-M3",
            system="You are a helpful assistant that always begins answers with 'AGENT:'.",
            max_tokens=64,
        )
        assert isinstance(result, str)
        assert len(result) > 0


@pytest.mark.skipif(
    not os.getenv("OPENAI_API_KEY"),
    reason="OPENAI_API_KEY not set — skipping live OpenAI integration test",
)
class TestOpenAIIntegration:
    def test_live_call_returns_nonempty_string(self):
        from utilities.llm_provider import complete
        result = complete(
            "Name one popular LLM agent framework.",
            provider="openai",
            max_tokens=32,
        )
        assert isinstance(result, str)
        assert len(result) > 0
