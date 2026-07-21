"""
Service responsible for prompt generation.
"""

import time
from typing import List

from app.core.logging import logger
from app.models.chunk import Chunk
from app.prompting.prompt_builder_factory import PromptBuilderFactory
from app.exceptions.bad_request_exception import BadRequestException


class PromptBuilderService:
    """
    Service responsible for validating inputs and
    generating prompts for the LLM.
    """

    def __init__(self) -> None:
        self._builder = PromptBuilderFactory.create()

    def build_prompt(
        self,
        question: str,
        chunks: List[Chunk],
    ) -> str:
        """
        Build a prompt for the LLM.

        Args:
            question:
                User question.

            chunks:
                Retrieved document chunks.

        Returns:
            Fully formatted prompt.
        """

        logger.info("Starting prompt generation.")

        self._validate_question(question)

        logger.info(
            "Question Length=%d | Retrieved Chunks=%d",
            len(question),
            len(chunks),
        )

        start_time = time.perf_counter()

        prompt = self._builder.build_prompt(
            question=question,
            chunks=chunks,
        )

        execution_time = time.perf_counter() - start_time

        logger.info(
            "Prompt generated successfully."
        )

        logger.info(
            "Prompt Length=%d characters",
            len(prompt),
        )

        logger.info(
            "Prompt Builder Execution Time=%.3f seconds",
            execution_time,
        )

        return prompt

    @staticmethod
    def _validate_question(question: str) -> None:
        """
        Validate the user question.

        Raises:
            BadRequestException:
                If the question is invalid.
        """

        if question is None:
            logger.error("Question is None.")
            raise BadRequestException(
                "Question cannot be None."
            )

        if not question.strip():
            logger.error("Question is empty.")
            raise BadRequestException(
                "Question cannot be empty."
            )