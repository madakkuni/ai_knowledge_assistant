from abc import ABC, abstractmethod

from app.models.embedding import Embedding


class BaseVectorStore(ABC):
    """
    Abstract base class for vector store implementations.
    """

    @abstractmethod
    def add_embeddings(
        self,
        embeddings: list[Embedding],
    ) -> None:
        """
        Store embeddings in the vector database.
        """
        pass

    @abstractmethod
    def similarity_search(
        self,
        query_embedding: list[float],
        top_k: int = 5,
    ):
        """
        Retrieve the most similar vectors.
        """
        pass