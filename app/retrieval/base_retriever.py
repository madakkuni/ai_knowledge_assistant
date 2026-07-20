from abc import ABC, abstractmethod

from app.models.embedding import Embedding


class BaseRetriever(ABC):
    """
    Abstract base class for retrieval providers.
    """

    @abstractmethod
    def retrieve(
        self,
        query_embedding: Embedding,
        top_k: int = 5,
    ):
        """
        Retrieve the most relevant documents using the query embedding.
        """
        pass