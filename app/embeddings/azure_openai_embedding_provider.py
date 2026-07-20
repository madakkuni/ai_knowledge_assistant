import logging

from app.core.azure_openai_client_factory import AzureOpenAIClientFactory
from app.embeddings.base_embedding_provider import BaseEmbeddingProvider
from app.embeddings.embedding_config import EmbeddingConfig
from app.exceptions.embedding_exceptions import EmbeddingException
from app.models.chunk import Chunk
from app.models.embedding import Embedding
from app.core.config import settings

logger = logging.getLogger(__name__)


class AzureOpenAIEmbeddingProvider(BaseEmbeddingProvider):

    def __init__(
        self,
        config: EmbeddingConfig
    ):

        self.config = config

        self.client = AzureOpenAIClientFactory.create_client()

        logger.info(
            "Azure OpenAI Embedding Provider initialized."
        )

    def generate_embedding(
        self,
        chunk: Chunk
    ) -> Embedding:

        try:

            logger.info(
                "Generating embedding for chunk %s",
                chunk.metadata.get("chunk_id", "N/A")
            )

            response = self.client.embeddings.create(
                model=settings.azure_openai_embedding_deployment,
                input=chunk.content,
            )

            return Embedding(
                vector=response.data[0].embedding,
                metadata=chunk.metadata
            )

        except Exception as ex:

            logger.exception(
                "Failed to generate embedding."
            )

            raise EmbeddingException(
                "Embedding generation failed."
            ) from ex

    def generate_embeddings(
        self,
        chunks: list[Chunk]
    ) -> list[Embedding]:

        try:

            logger.info(
                "Generating embeddings for %d chunks.",
                len(chunks)
            )

            texts = [
                chunk.content
                for chunk in chunks
            ]

            response = self.client.embeddings.create(
                model=settings.azure_openai_embedding_deployment,
                input=texts,
            )

            embeddings = []

            for chunk, item in zip(
                chunks,
                response.data
            ):

                embeddings.append(
                    Embedding(
                        vector=item.embedding,
                        metadata=chunk.metadata
                    )
                )

            logger.info(
                "Successfully generated %d embeddings.",
                len(embeddings)
            )

            return embeddings

        except Exception as ex:

            logger.exception(
                "Batch embedding generation failed."
            )

            raise EmbeddingException(
                "Embedding generation failed."
            ) from ex