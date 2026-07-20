import logging

from app.models.embedding import Embedding
from app.retrieval.retrieval_config import RetrievalConfig
from app.retrieval.retriever_factory import RetrieverFactory

logger = logging.getLogger(__name__)


class RetrievalService:
    """
    Service responsible for retrieving relevant document chunks.
    """

    def __init__(self):

        config = RetrievalConfig()

        self.retriever = RetrieverFactory.get_retriever(
            provider="vector",
            config=config,
        )

    def retrieve(
        self,
        query_embedding: Embedding,
        top_k: int = 5,
    ):
        """
        Retrieve the top-k most relevant chunks.
        """

        logger.info(
            "Retrieving top %d relevant chunks.",
            top_k,
        )

        return self.retriever.retrieve(
            query_embedding=query_embedding,
            top_k=top_k,
        )