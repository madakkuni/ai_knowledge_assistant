"""
Abstract base class for chat providers.
"""

from abc import ABC, abstractmethod


class BaseChatProvider(ABC):
    """
    Defines the contract for all chat providers.

    A chat provider is responsible for sending a prompt
    to a Large Language Model (LLM) and returning
    the generated response.
    """

    @abstractmethod
    def generate_response(
        self,
        prompt: str,
    ) -> str:
        """
        Generate a response from the LLM.

        Args:
            prompt:
                Fully constructed prompt.

        Returns:
            Generated response from the LLM.
        """
        raise NotImplementedError