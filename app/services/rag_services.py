"""
Service responsible for orchestrating
the Retrieval-Augmented Generation (RAG) pipeline.
"""

import logging
import time

from app.models.chunk import Chunk
from app.services.chat_service import ChatCompletionService
from app.services.prompt_builder_service import PromptBuilderService
from app.services.retrieval_service import RetrievalService
from app.exceptions.rag_exceptions import RAGException
from app.services.embedding_services import EmbeddingService


logger = logging.getLogger(__name__)
    

class RAGService:
    """
    Service responsible for orchestrating the RAG workflow.
    """

    def __init__(self) -> None:

        self._retrieval_service = RetrievalService()
        self._prompt_builder_service = PromptBuilderService()
        self._chat_service = ChatCompletionService()
        self._embedding_service = EmbeddingService()

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
        """

        logger.info(
            "Building prompt for user question."
        )

        # Generate embedding for the user question
        query_embedding = (
            self._embedding_service.generate_query_embedding(
                question
            )
        )

        # Retrieve relevant chunks
        query_embedding = (
            self._embedding_service.generate_query_embedding(
                question
            )
        )

        chunks = self._retrieval_service.retrieve(
            query_embedding=query_embedding
        )

        logger.info(
            "Retrieved %d chunks.",
            len(chunks),
        )

        for i, chunk in enumerate(chunks, start=1):
            logger.info("=" * 80)
            logger.info(f"Chunk {i}")
            logger.info(chunk.content)
        prompt = self._prompt_builder_service.build_prompt(
            question=question,
            chunks=chunks,
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
        Execute the complete RAG pipeline.

        Args:
            question:
                User question.

        Returns:
            Generated answer.
        """

        self._validate_question(question)

        logger.info(
            "Starting RAG pipeline."
        )

        start_time = time.perf_counter()

        try:

            prompt = self.build_prompt(question)

            response = self._chat_service.generate_response(
                prompt
            )

            elapsed = time.perf_counter() - start_time

            logger.info(
                "RAG pipeline completed successfully in %.2f seconds.",
                elapsed,
            )

            return response

        except RAGException:
            raise

        except Exception as ex:

            logger.exception(
                "Unexpected error while executing RAG pipeline."
            )

            raise RAGException(
                "Failed to generate response."
            ) from ex
    

    @staticmethod
    def _validate_question(
        question: str,
    ) -> None:
        """
        Validate the user question.

        Args:
            question:
                User question.

        Raises:
            RAGException:
                If the question is invalid.
        """

        if question is None:
            raise RAGException(
                "Question cannot be None."
            )

        if not question.strip():
            raise RAGException(
                "Question cannot be empty."
            )

        if len(question) > 5000:
            raise RAGException(
                "Question exceeds maximum allowed length."
            )