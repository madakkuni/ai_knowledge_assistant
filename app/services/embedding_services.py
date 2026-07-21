import logging

from app.embeddings.embedding_config import EmbeddingConfig
from app.embeddings.embedding_factory import EmbeddingFactory
from app.models.chunk import Chunk
from app.models.embedding import Embedding

logger = logging.getLogger(__name__)


class EmbeddingService:

    def __init__(self):

        config = EmbeddingConfig()

        self.provider = EmbeddingFactory.get_provider(
            "azure_openai",
            config
        )

    def generate_embeddings(
        self,
        chunks: list[Chunk]
    ) -> list[Embedding]:

        logger.info(
            "Generating embeddings for %d chunks.",
            len(chunks)
        )

        return self.provider.generate_embeddings(chunks)
    
    def generate_query_embedding(
        self,
        question: str,
    ) -> Embedding:
        """
        Generate embedding for a user question.
        """

        logger.info(
            "Generating query embedding."
        )

        return self.provider.generate_query_embedding(
            question
        )