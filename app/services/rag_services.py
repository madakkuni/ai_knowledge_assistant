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

    def build_prompt(
        self,
        question: str,
    ) -> str:
        """
        Retrieve relevant context and build
        the final prompt for the LLM.

        Args:
            question:
                User question.

        Returns:
            Final prompt string.
        """

        logger.info(
            "Building prompt for user question."
        )

        chunks: list[Chunk] = (
            self._retrieval_service.retrieve(question)
        )

        logger.info(
            "Retrieved %d chunks.",
            len(chunks),
        )

        prompt = (
            self._prompt_builder_service.build_prompt(
                question=question,
                chunks=chunks,
            )
        )

        logger.info(
            "Prompt built successfully."
        )

        return prompt
    def generate_answer(
        self,
        question: str,
    ) -> str:
        """
        Generate an answer for the user's question
        using the complete RAG pipeline.

        Args:
            question:
                User question.

        Returns:
            Generated answer from the LLM.
        """

        logger.info(
            "Generating answer using RAG pipeline."
        )

        prompt = self.build_prompt(question)

        logger.info(
            "Sending prompt to Chat Completion Service."
        )

        response = self._chat_service.generate_response(
            prompt
        )

        logger.info(
            "Successfully generated answer."
        )

        return response