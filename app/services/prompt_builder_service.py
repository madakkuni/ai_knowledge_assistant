"""
Service responsible for prompt generation.
"""

from typing import List

from app.models.chunk import Chunk
from app.prompting.prompt_builder_factory import PromptBuilderFactory


class PromptBuilderService:
    """
    Service responsible for generating prompts.

    This class hides the prompt builder implementation
    from callers.
    """

    def __init__(self) -> None:
        self._builder = PromptBuilderFactory.create()

    def build_prompt(
        self,
        question: str,
        chunks: List[Chunk],
    ) -> str:
        """
        Build the final prompt.

        Args:
            question:
                User question.

            chunks:
                Retrieved chunks.

        Returns:
            Formatted prompt.
        """

        return self._builder.build_prompt(
            question=question,
            chunks=chunks,
        )