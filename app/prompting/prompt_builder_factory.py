"""
Factory for creating prompt builders.
"""

from app.prompting.base_prompt_builder import BasePromptBuilder
from app.prompting.enterprise_prompt_builder import EnterprisePromptBuilder


class PromptBuilderFactory:
    """
    Factory responsible for creating prompt builder implementations.
    """

    @staticmethod
    def create() -> BasePromptBuilder:
        """
        Create the configured prompt builder.

        Returns:
            BasePromptBuilder implementation.
        """
        return EnterprisePromptBuilder()