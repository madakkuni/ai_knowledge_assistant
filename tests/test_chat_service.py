"""
Unit tests for ChatCompletionService.
"""

from unittest.mock import MagicMock, patch

import pytest

from app.exceptions.chat_completion_exceptions import ChatCompletionException
from app.services.chat_service import ChatCompletionService


class TestChatCompletionService:
    """
    Test suite for ChatCompletionService.
    """

    @patch("app.services.chat_service.ChatFactory.create")
    def test_generate_response_success(
        self,
        mock_create,
    ):
        """
        Should return the response from the provider.
        """

        mock_provider = MagicMock()

        mock_provider.generate_response.return_value = (
            "VPN password reset successful."
        )

        mock_create.return_value = mock_provider

        service = ChatCompletionService()

        response = service.generate_response(
            "Reset my VPN password"
        )

        assert response == "VPN password reset successful."

        mock_provider.generate_response.assert_called_once_with(
            "Reset my VPN password"
        )

    @patch("app.services.chat_service.ChatFactory.create")
    def test_generate_response_empty_prompt(
        self,
        mock_create,
    ):
        """
        Should raise ChatException for an empty prompt.
        """

        mock_provider = MagicMock()

        mock_create.return_value = mock_provider

        service = ChatCompletionService()

        with pytest.raises(ChatCompletionException):

            service.generate_response("")

    @patch("app.services.chat_service.ChatFactory.create")
    def test_generate_response_none_prompt(
        self,
        mock_create,
    ):
        """
        Should raise ChatException for a None prompt.
        """

        mock_provider = MagicMock()

        mock_create.return_value = mock_provider

        service = ChatCompletionService()

        with pytest.raises(ChatCompletionException):

            service.generate_response(None)

    @patch("app.services.chat_service.ChatFactory.create")
    def test_provider_exception(
        self,
        mock_create,
    ):
        """
        Provider exceptions should propagate.
        """

        mock_provider = MagicMock()

        mock_provider.generate_response.side_effect = ChatCompletionException(
            "Azure failure."
        )

        mock_create.return_value = mock_provider

        service = ChatCompletionService()

        with pytest.raises(ChatCompletionException):

            service.generate_response(
                "Hello"
            )