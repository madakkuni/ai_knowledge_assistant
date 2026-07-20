"""
Abstract base class for all prompt builders.
"""

from abc import ABC, abstractmethod
from typing import List

from app.models.chunk import Chunk


class BasePromptBuilder(ABC):
    """
    Defines the contract for prompt builders.

    Prompt builders are responsible for transforming a user question
    and retrieved document chunks into a formatted prompt that can be
    sent to an LLM.
    """

    @abstractmethod
    def build_prompt(
        self,
        question: str,
        chunks: List[Chunk],
    ) -> str:
        """
        Build the final prompt.

        Args:
            question:
                User's question.

            chunks:
                Retrieved document chunks.

        Returns:
            Formatted prompt string.
        """
        raise NotImplementedError