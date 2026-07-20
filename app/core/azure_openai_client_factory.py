from openai import AzureOpenAI

from app.core.config import settings


class AzureOpenAIClientFactory:

    @staticmethod
    def create_client() -> AzureOpenAI:

        return AzureOpenAI(
            api_key=settings.azure_openai_api_key,
            azure_endpoint=settings.azure_openai_endpoint,
            api_version=settings.azure_openai_api_version,
        )