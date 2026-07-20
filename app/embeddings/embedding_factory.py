from app.embeddings.azure_openai_embedding_provider import (
    AzureOpenAIEmbeddingProvider,
)
from app.embeddings.base_embedding_provider import BaseEmbeddingProvider
from app.embeddings.embedding_config import EmbeddingConfig
from app.exceptions.embedding_exceptions import EmbeddingException


class EmbeddingFactory:

    @staticmethod
    def get_provider(
        provider_name: str,
        config: EmbeddingConfig,
    ) -> BaseEmbeddingProvider:

        provider_name = provider_name.lower()

        if provider_name == "azure_openai":
            return AzureOpenAIEmbeddingProvider(config)

        raise EmbeddingException(
            f"Unsupported embedding provider: {provider_name}"
        )