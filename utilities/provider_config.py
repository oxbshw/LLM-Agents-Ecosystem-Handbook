"""Provider capability registry.

Single source of truth for which providers exist, what they can do, and
which env var holds their key. Adapters import this — never hardcode.

Design:
- All metadata is data, not code. New providers = a new dict entry.
- `openai_compatible=True` means the provider speaks the OpenAI Chat
  Completions wire format and can be reached with the `openai` SDK by
  setting a custom `base_url`. This covers the majority of providers
  on the market and lets us avoid a dozen heavy SDK dependencies.
- Capabilities are best-effort booleans for routing. Verify against
  current upstream docs for production decisions; the ecosystem moves.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional


@dataclass(frozen=True)
class ProviderInfo:
    """Static facts about a provider."""

    name: str
    display_name: str
    api_key_env: Optional[str]
    base_url_env: Optional[str] = None
    default_base_url: Optional[str] = None
    default_model: Optional[str] = None
    openai_compatible: bool = True
    family: str = "frontier"  # frontier | fast | marketplace | enterprise | specialty | local
    capabilities: frozenset = field(default_factory=frozenset)
    notes: str = ""


_C = lambda *xs: frozenset(xs)  # noqa: E731 — capability shorthand


# Capability tokens
CHAT = "chat"
STREAMING = "streaming"
TOOLS = "tool_calling"
STRUCTURED = "structured_outputs"
JSON = "json_mode"
VISION = "vision"
EMBEDDINGS = "embeddings"
RERANK = "rerank"
LONG_CONTEXT = "long_context"
LOCAL = "local"


PROVIDERS: dict[str, ProviderInfo] = {
    # --- Frontier APIs ---
    "openai": ProviderInfo(
        name="openai",
        display_name="OpenAI",
        api_key_env="OPENAI_API_KEY",
        default_model="gpt-4o-mini",
        family="frontier",
        capabilities=_C(CHAT, STREAMING, TOOLS, STRUCTURED, JSON, VISION, EMBEDDINGS, LONG_CONTEXT),
    ),
    "anthropic": ProviderInfo(
        name="anthropic",
        display_name="Anthropic",
        api_key_env="ANTHROPIC_API_KEY",
        default_model="claude-3-5-haiku-20241022",
        openai_compatible=False,
        family="frontier",
        capabilities=_C(CHAT, STREAMING, TOOLS, JSON, VISION, LONG_CONTEXT),
        notes="Uses the Anthropic Messages API; a separate SDK path.",
    ),
    "google": ProviderInfo(
        name="google",
        display_name="Google Gemini",
        api_key_env="GOOGLE_API_KEY",
        default_model="gemini-1.5-flash",
        openai_compatible=True,
        default_base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
        family="frontier",
        capabilities=_C(CHAT, STREAMING, TOOLS, JSON, VISION, EMBEDDINGS, LONG_CONTEXT),
        notes="Gemini exposes an OpenAI-compatible endpoint at the URL above.",
    ),
    # --- Enterprise ---
    "azure_openai": ProviderInfo(
        name="azure_openai",
        display_name="Azure OpenAI",
        api_key_env="AZURE_OPENAI_API_KEY",
        base_url_env="AZURE_OPENAI_ENDPOINT",
        family="enterprise",
        capabilities=_C(CHAT, STREAMING, TOOLS, STRUCTURED, JSON, VISION, EMBEDDINGS, LONG_CONTEXT),
        notes="Use deployment name as `model`. Requires API version header.",
    ),
    "bedrock": ProviderInfo(
        name="bedrock",
        display_name="AWS Bedrock",
        api_key_env="AWS_ACCESS_KEY_ID",
        openai_compatible=False,
        family="enterprise",
        capabilities=_C(CHAT, STREAMING, TOOLS, VISION, EMBEDDINGS, LONG_CONTEXT),
        notes="Use boto3; sigv4-signed. Adapter is a stub doc.",
    ),
    # --- Fast inference ---
    "groq": ProviderInfo(
        name="groq",
        display_name="Groq",
        api_key_env="GROQ_API_KEY",
        default_base_url="https://api.groq.com/openai/v1",
        default_model="llama-3.1-8b-instant",
        family="fast",
        capabilities=_C(CHAT, STREAMING, TOOLS, JSON),
    ),
    "cerebras": ProviderInfo(
        name="cerebras",
        display_name="Cerebras",
        api_key_env="CEREBRAS_API_KEY",
        default_base_url="https://api.cerebras.ai/v1",
        default_model="llama3.1-8b",
        family="fast",
        capabilities=_C(CHAT, STREAMING, TOOLS, JSON),
    ),
    "sambanova": ProviderInfo(
        name="sambanova",
        display_name="SambaNova",
        api_key_env="SAMBANOVA_API_KEY",
        default_base_url="https://api.sambanova.ai/v1",
        family="fast",
        capabilities=_C(CHAT, STREAMING),
    ),
    # --- Marketplaces ---
    "openrouter": ProviderInfo(
        name="openrouter",
        display_name="OpenRouter",
        api_key_env="OPENROUTER_API_KEY",
        default_base_url="https://openrouter.ai/api/v1",
        default_model="openai/gpt-4o-mini",
        family="marketplace",
        capabilities=_C(CHAT, STREAMING, TOOLS, JSON, VISION, LONG_CONTEXT),
    ),
    "together": ProviderInfo(
        name="together",
        display_name="Together AI",
        api_key_env="TOGETHER_API_KEY",
        default_base_url="https://api.together.xyz/v1",
        default_model="meta-llama/Llama-3.1-8B-Instruct-Turbo",
        family="marketplace",
        capabilities=_C(CHAT, STREAMING, TOOLS, JSON, EMBEDDINGS, LONG_CONTEXT),
    ),
    "fireworks": ProviderInfo(
        name="fireworks",
        display_name="Fireworks AI",
        api_key_env="FIREWORKS_API_KEY",
        default_base_url="https://api.fireworks.ai/inference/v1",
        family="marketplace",
        capabilities=_C(CHAT, STREAMING, TOOLS, JSON, EMBEDDINGS, LONG_CONTEXT),
    ),
    "deepinfra": ProviderInfo(
        name="deepinfra",
        display_name="DeepInfra",
        api_key_env="DEEPINFRA_API_KEY",
        default_base_url="https://api.deepinfra.com/v1/openai",
        family="marketplace",
        capabilities=_C(CHAT, STREAMING, EMBEDDINGS),
    ),
    # --- Specialty ---
    "mistral": ProviderInfo(
        name="mistral",
        display_name="Mistral",
        api_key_env="MISTRAL_API_KEY",
        default_base_url="https://api.mistral.ai/v1",
        default_model="mistral-small-latest",
        family="specialty",
        capabilities=_C(CHAT, STREAMING, TOOLS, JSON, EMBEDDINGS, LONG_CONTEXT),
    ),
    "cohere": ProviderInfo(
        name="cohere",
        display_name="Cohere",
        api_key_env="COHERE_API_KEY",
        default_base_url="https://api.cohere.ai/compatibility/v1",
        default_model="command-r",
        family="specialty",
        capabilities=_C(CHAT, STREAMING, TOOLS, EMBEDDINGS, RERANK, LONG_CONTEXT),
        notes="Cohere ships the best-known reranker.",
    ),
    "deepseek": ProviderInfo(
        name="deepseek",
        display_name="DeepSeek",
        api_key_env="DEEPSEEK_API_KEY",
        default_base_url="https://api.deepseek.com/v1",
        default_model="deepseek-chat",
        family="specialty",
        capabilities=_C(CHAT, STREAMING, TOOLS, JSON, LONG_CONTEXT),
    ),
    "xai": ProviderInfo(
        name="xai",
        display_name="xAI",
        api_key_env="XAI_API_KEY",
        default_base_url="https://api.x.ai/v1",
        default_model="grok-2",
        family="specialty",
        capabilities=_C(CHAT, STREAMING, TOOLS, JSON, VISION, LONG_CONTEXT),
    ),
    "perplexity": ProviderInfo(
        name="perplexity",
        display_name="Perplexity",
        api_key_env="PERPLEXITY_API_KEY",
        default_base_url="https://api.perplexity.ai",
        default_model="sonar",
        family="specialty",
        capabilities=_C(CHAT, STREAMING),
        notes="Built-in web search — useful for research-class agents.",
    ),
    "huggingface": ProviderInfo(
        name="huggingface",
        display_name="Hugging Face Inference",
        api_key_env="HF_TOKEN",
        default_base_url="https://api-inference.huggingface.co/v1",
        family="specialty",
        capabilities=_C(CHAT, STREAMING, EMBEDDINGS),
    ),
    "replicate": ProviderInfo(
        name="replicate",
        display_name="Replicate",
        api_key_env="REPLICATE_API_TOKEN",
        openai_compatible=False,
        family="specialty",
        capabilities=_C(CHAT, VISION),
        notes="Hosted models with predict-style API; adapter is a stub.",
    ),
    "nvidia": ProviderInfo(
        name="nvidia",
        display_name="NVIDIA NIM",
        api_key_env="NVIDIA_API_KEY",
        default_base_url="https://integrate.api.nvidia.com/v1",
        family="specialty",
        capabilities=_C(CHAT, STREAMING, TOOLS, EMBEDDINGS),
    ),
    "minimax": ProviderInfo(
        name="minimax",
        display_name="MiniMax",
        api_key_env="MINIMAX_API_KEY",
        default_base_url="https://api.minimax.io/v1",
        default_model="MiniMax-M3",
        family="specialty",
        capabilities=_C(CHAT, STREAMING, LONG_CONTEXT),
        notes="MiniMax-M3 default (512K context); MiniMax-M2.7 / MiniMax-M2.7-highspeed available. Temperature must be > 0.",
    ),
    # --- Local ---
    "ollama": ProviderInfo(
        name="ollama",
        display_name="Ollama",
        api_key_env=None,
        base_url_env="OLLAMA_BASE_URL",
        default_base_url="http://localhost:11434/v1",
        default_model="llama3.1",
        family="local",
        capabilities=_C(CHAT, STREAMING, TOOLS, JSON, VISION, EMBEDDINGS, LOCAL),
    ),
    "lmstudio": ProviderInfo(
        name="lmstudio",
        display_name="LM Studio",
        api_key_env=None,
        base_url_env="LMSTUDIO_BASE_URL",
        default_base_url="http://localhost:1234/v1",
        family="local",
        capabilities=_C(CHAT, STREAMING, TOOLS, JSON, EMBEDDINGS, LOCAL),
    ),
    "vllm": ProviderInfo(
        name="vllm",
        display_name="vLLM",
        api_key_env=None,
        base_url_env="VLLM_BASE_URL",
        default_base_url="http://localhost:8000/v1",
        family="local",
        capabilities=_C(CHAT, STREAMING, TOOLS, JSON, LOCAL, LONG_CONTEXT),
    ),
    "llamacpp": ProviderInfo(
        name="llamacpp",
        display_name="llama.cpp",
        api_key_env=None,
        base_url_env="LLAMACPP_BASE_URL",
        default_base_url="http://localhost:8080/v1",
        family="local",
        capabilities=_C(CHAT, STREAMING, JSON, LOCAL),
    ),
    "openai_compatible": ProviderInfo(
        name="openai_compatible",
        display_name="Generic OpenAI-compatible endpoint",
        api_key_env="LOCAL_OPENAI_COMPATIBLE_API_KEY",
        base_url_env="LOCAL_OPENAI_COMPATIBLE_BASE_URL",
        family="local",
        capabilities=_C(CHAT, STREAMING),
        notes="Catch-all for self-hosted endpoints (TGI, RayServe, etc.).",
    ),
}


def get(name: str) -> ProviderInfo:
    name = name.lower().strip()
    if name not in PROVIDERS:
        raise KeyError(
            f"Unknown provider '{name}'. Known: {sorted(PROVIDERS.keys())}"
        )
    return PROVIDERS[name]


def by_family(family: str) -> list[ProviderInfo]:
    return [p for p in PROVIDERS.values() if p.family == family]


def supporting(capability: str) -> list[ProviderInfo]:
    return [p for p in PROVIDERS.values() if capability in p.capabilities]
