# Provider expansion prompt

Add a new LLM provider to the abstraction.

```text
You are extending this repo's provider abstraction (utilities/, providers/)
to support {{NEW_PROVIDER_NAME}}.

WORKFLOW
1. Read providers/README.md, providers/provider_abstraction.md, and
   utilities/provider_config.py to understand the registry pattern.
2. Determine: is the provider OpenAI-compatible? (Most modern hosted
   providers are. Local OpenAI-compat servers definitely are.)
3. If OpenAI-compatible:
   a. Add a ProviderInfo(...) entry to utilities/provider_config.py
   b. Wire env vars; document in providers/env_vars.md and .env.example
   c. Add a minimal example to providers/examples/<name>_provider.py
   d. Update providers/provider_matrix.md with capability flags
   e. Re-run any existing smoke check
4. If NOT OpenAI-compatible:
   a. Add ProviderInfo(..., openai_compatible=False)
   b. Add a _chat_<name>(...) adapter in utilities/llm_provider.py
   c. Add error mapping in _map_<name>_exc(...)
   d. Document the adapter in providers/<name>.md (if non-trivial)
   e. Add the example as above

CONSTRAINTS
- No new heavy dependencies unless required (most providers can use the
  openai SDK with a custom base_url).
- Lazy imports — never break the package on missing optional SDKs.
- Errors raised must be typed (utilities/provider_errors.py).
- Update DEFAULT_CHAINS in utilities/provider_router.py if this provider
  fits a routing tier (cheap / fast / reasoning / vision / etc.).

VERIFICATION
- python -c "from utilities import list_providers; print({p['name']: p['family'] for p in list_providers()})" includes the new provider
- providers/examples/<name>_provider.py runs (or fails with a clear
  ProviderNotConfigured if the key isn't set)
- .env.example has the new key
- providers/env_vars.md and providers/provider_matrix.md updated

OUTPUT
- Diff summary
- Updated CHANGELOG entry
```

## Pair with

- [providers/provider_abstraction.md](../../providers/provider_abstraction.md)
- [providers/provider_matrix.md](../../providers/provider_matrix.md)
