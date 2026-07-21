import logging

from app.models.embedding import Embedding
from app.vectorstores.vector_store_config import VectorStoreConfig
from app.vectorstores.vector_store_factory import VectorStoreFactory

logger = logging.getLogger(__name__)


class VectorStoreService:
    """
    Business service responsible for vector storage operations.
    """

    def __init__(self):

        config = VectorStoreConfig()

        self.vector_store = VectorStoreFactory.get_store(
            "chroma",
            config
        )

    def add_embeddings(
        self,
        embeddings: list[Embedding],
    ) -> None:

        logger.info(
            "Adding %d embeddings to vector store.",
            len(embeddings)
        )

        self.vector_store.add_embeddings(
            embeddings
        )

    def similarity_search(
        self,
        query_embedding: list[float],
        top_k: int = 5,
    ):

        logger.info(
            "Performing similarity search."
        )

        return self.vector_store.similarity_search(
            query_embedding=query_embedding,
            top_k=top_k,
        )

    def get_chunks(
        self,
        limit: int = 100,
    ):
        """
        Retrieve all indexed chunks.
        """

        logger.info(
            "Loading indexed chunks from vector store."
        )

        return self.vector_store.get_chunks(
            limit=limit
        )