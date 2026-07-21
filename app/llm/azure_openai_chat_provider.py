"""
Azure OpenAI chat provider implementation.
"""

from openai import AzureOpenAI

from app.core.config import settings
from app.llm.base_chat_provider import BaseChatProvider
from app.llm.chat_config import ChatConfig

import logging
logger = logging.getLogger(__name__)


class AzureOpenAIChatProvider(BaseChatProvider):
    """
    Azure OpenAI implementation of the chat provider.
    """

    def __init__(self) -> None:
        """
        Initialize the Azure OpenAI client.
        """

        self._client = AzureOpenAI(
            api_key=settings.azure_openai_api_key,
            azure_endpoint=settings.azure_openai_endpoint,
            api_version=settings.azure_openai_api_version,
        )

    def generate_response(
        self,
        prompt: str,
    ) -> str:
        """
        Generate a response using Azure OpenAI.

        Args:
            prompt:
                Fully constructed prompt.

        Returns:
            Generated response.
        """

        logger.info("Sending prompt to Azure OpenAI.")

        response = self._client.chat.completions.create(
            model=settings.azure_openai_chat_deployment,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            temperature=ChatConfig.TEMPERATURE,
            max_tokens=ChatConfig.MAX_TOKENS,
            top_p=ChatConfig.TOP_P,
            frequency_penalty=ChatConfig.FREQUENCY_PENALTY,
            presence_penalty=ChatConfig.PRESENCE_PENALTY,
        )

        answer = response.choices[0].message.content

        logger.info("Response received from Azure OpenAI.")

        return answer.strip() if answer else ""