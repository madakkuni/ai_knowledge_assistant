import logging

from app.exceptions.retrieval_exception import RetrievalException
from app.models.embedding import Embedding
from app.retrieval.base_retriever import BaseRetriever
from app.retrieval.retrieval_config import RetrievalConfig
from app.services.vector_store_service import VectorStoreService
from app.models.chunk import Chunk

logger = logging.getLogger(__name__)


class VectorRetriever(BaseRetriever):
    """
    Vector-based retriever using the configured vector store.
    """

    def __init__(
        self,
        config: RetrievalConfig,
    ):

        self.config = config
        self.vector_store = VectorStoreService()

        logger.info(
            "Vector Retriever initialized."
        )

    def retrieve(
        self,
        query_embedding: Embedding,
        top_k: int = 5,
    ):

        try:

            logger.info(
                "Retrieving top %d relevant chunks.",
                top_k
            )

            results = self.vector_store.similarity_search(
                query_embedding=query_embedding.vector,
                top_k=top_k,
            )

            documents = results.get("documents", [[]])[0]
            metadatas = results.get("metadatas", [[]])[0]

            chunks = [
                Chunk(
                    content=document,
                    metadata=metadata,
                )
                for document, metadata in zip(
                    documents,
                    metadatas,
                )
            ]

            logger.info(
                "Retrieved %d matching chunks.",
                len(chunks)
            )

            return chunks

        except Exception as ex:

            logger.exception(
                "Vector retrieval failed."
            )

            raise RetrievalException(
                "Failed to retrieve relevant chunks."
            ) from ex