from abc import ABC, abstractmethod

from app.models.chunk import Chunk
from app.models.embedding import Embedding


class BaseEmbeddingProvider(ABC):

    @abstractmethod
    def generate_embedding(
        self,
        chunk: Chunk
    ) -> Embedding:
        """
        Generate an embedding for a single chunk.
        """
        pass

    @abstractmethod
    def generate_embeddings(
        self,
        chunks: list[Chunk]
    ) -> list[Embedding]:
        """
        Generate embeddings for multiple chunks.
        """
        pass