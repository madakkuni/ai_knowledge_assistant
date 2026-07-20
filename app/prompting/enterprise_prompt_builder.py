"""
Enterprise prompt builder implementation.
"""

from typing import List

from app.models.chunk import Chunk
from app.prompting.base_prompt_builder import BasePromptBuilder
from app.prompting.prompt_config import PromptConfig


class EnterprisePromptBuilder(BasePromptBuilder):
    """
    Builds prompts for enterprise Retrieval-Augmented Generation (RAG).

    This implementation combines:
    - System instructions
    - Retrieved document context
    - User question

    into a single prompt that can be sent to an LLM.
    """

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
            Fully formatted prompt string.
        """

        context = self._build_context(chunks)

        prompt = (
            f"{PromptConfig.SYSTEM_MESSAGE}\n\n"
            f"{PromptConfig.SEPARATOR}\n"
            f"{PromptConfig.CONTEXT_HEADER}\n"
            f"{PromptConfig.SEPARATOR}\n"
            f"{context}\n\n"
            f"{PromptConfig.SEPARATOR}\n"
            f"{PromptConfig.QUESTION_HEADER}\n"
            f"{PromptConfig.SEPARATOR}\n"
            f"{question}\n\n"
            f"{PromptConfig.ANSWER_HEADER}"
        )

        return prompt

    def _build_context(
        self,
        chunks: List[Chunk],
    ) -> str:
        """
        Convert retrieved chunks into a formatted context block.

        Args:
            chunks:
                Retrieved chunks.

        Returns:
            Context string.
        """

        if not chunks:
            return "No relevant context found."

        return "\n\n".join(chunk.content.strip() for chunk in chunks)