"""
Service responsible for orchestrating
the Retrieval-Augmented Generation (RAG) pipeline.
"""

import logging

from app.services.chat_service import ChatCompletionService
from app.services.prompt_builder_service import PromptBuilderService
from app.services.retrieval_service import RetrievalService

logger = logging.getLogger(__name__)


class RAGService:
    """
    Service responsible for orchestrating the RAG workflow.

    Responsibilities:
        - Retrieve relevant document chunks
        - Build the LLM prompt
        - Generate the final response
    """

    def __init__(self) -> None:
        """
        Initialize all required services.
        """

        self._retrieval_service = RetrievalService()
        self._prompt_builder_service = PromptBuilderService()
        self._chat_service = ChatCompletionService()

        logger.info(
            "RAG Service initialized successfully."
        )