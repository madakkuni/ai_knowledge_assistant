"""
Service responsible for orchestrating
the Retrieval-Augmented Generation (RAG) pipeline.
"""

import logging

from app.models.chunk import Chunk
from app.services.chat_service import ChatCompletionService
from app.services.prompt_builder_service import PromptBuilderService
from app.services.retrieval_service import RetrievalService

logger = logging.getLogger(__name__)


class RAGService:
    """
    Service responsible for orchestrating the RAG workflow.
    """

    def __init__(self) -> None:

        self._retrieval_service = RetrievalService()
        self._prompt_builder_service = PromptBuilderService()
        self._chat_service = ChatCompletionService()

        logger.info(
            "RAG Service initialized successfully."
        )

    def retrieve_context(
        self,
        question: str,
    ) -> list[Chunk]:
        """
        Retrieve relevant document chunks.

        Args:
            question:
                User question.

        Returns:
            List of retrieved chunks.
        """

        logger.info(
            "Retrieving context for user question."
        )

        chunks = self._retrieval_service.retrieve(
            question
        )

        logger.info(
            "Retrieved %d chunks.",
            len(chunks),
        )

        return chunks