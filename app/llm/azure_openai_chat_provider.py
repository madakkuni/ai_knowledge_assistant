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

    def __init__(
        self,
        config: ChatConfig,
    ) -> None:
        """
        Initialize the Azure OpenAI client.

        Args:
            config:
                Chat configuration.
        """

        self._config = config

        self._client = AzureOpenAI(
            api_key=settings.azure_openai_api_key,
            azure_endpoint=settings.azure_openai_endpoint,
            api_version=settings.azure_openai_api_version,
        )

        logger.info(
            "Azure OpenAI Chat Provider initialized."
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
            temperature=self._config.temperature,
            max_tokens=self._config.max_tokens,
            top_p=self._config.top_p,
            frequency_penalty=self._config.frequency_penalty,
            presence_penalty=self._config.presence_penalty,
        )

        answer = response.choices[0].message.content

        logger.info("Response received from Azure OpenAI.")

        return answer.strip() if answer else ""