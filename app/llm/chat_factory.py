"""
Factory responsible for creating chat providers.
"""

from app.llm.azure_openai_chat_provider import AzureOpenAIChatProvider
from app.llm.base_chat_provider import BaseChatProvider
from app.llm.chat_config import ChatConfig


class ChatFactory:
    """
    Factory responsible for creating chat provider implementations.
    """

    @staticmethod
    def create() -> BaseChatProvider:
        """
        Create the configured chat provider.

        Returns:
            BaseChatProvider implementation.
        """

        config = ChatConfig()

        return AzureOpenAIChatProvider(config)