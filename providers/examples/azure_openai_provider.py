"""Azure OpenAI provider example.

Setup:
    pip install openai
    export AZURE_OPENAI_API_KEY=...
    export AZURE_OPENAI_ENDPOINT=https://<resource>.openai.azure.com

In Azure OpenAI, ``model`` is your *deployment* name (not the model id).
The ``openai`` SDK supports Azure via the ``AzureOpenAI`` class, but our
wrapper goes through the standard OpenAI client with the Azure endpoint
as ``base_url``. For full Azure features (api-version routing, AAD auth)
use ``AzureOpenAI`` directly:

    from openai import AzureOpenAI
    client = AzureOpenAI(
        api_key=os.environ["AZURE_OPENAI_API_KEY"],
        azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
        api_version="2024-08-01-preview",
    )
"""

from utilities import get_provider


def main() -> None:
    p = get_provider("azure_openai")
    out = p.chat(
        [{"role": "user", "content": "Three governance reasons enterprises pick Azure OpenAI."}],
        model="gpt-4o-mini",  # your deployment name
        max_tokens=200,
    )
    print(out["text"])


if __name__ == "__main__":
    main()
