from abc import ABC, abstractmethod

from app.models.chunk import Chunk
from app.models.embedding import Embedding

class BaseEmbeddingProvider(ABC):

    @abstractmethod
    def generate_query_embedding(
        self,
        question: str,
    ) -> Embedding:
        """
        Generate an embedding for a user query.
        """
        pass