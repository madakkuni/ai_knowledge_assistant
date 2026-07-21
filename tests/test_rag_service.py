from unittest.mock import MagicMock, patch

import pytest

from app.exceptions.rag_exceptions import RAGException
from app.services.rag_services import RAGService


@patch("app.services.rag_services.ChatCompletionService")
@patch("app.services.rag_services.PromptBuilderService")
@patch("app.services.rag_services.RetrievalService")
def test_generate_answer_success(
    mock_retrieval,
    mock_prompt_builder,
    mock_chat,
):
    """
    Should generate the final answer successfully.
    """

    retrieval = MagicMock()
    retrieval.retrieve.return_value = ["chunk1"]

    prompt_builder = MagicMock()
    prompt_builder.build_prompt.return_value = "Generated Prompt"

    chat = MagicMock()
    chat.generate_response.return_value = "Final Answer"

    mock_retrieval.return_value = retrieval
    mock_prompt_builder.return_value = prompt_builder
    mock_chat.return_value = chat

    service = RAGService()

    response = service.generate_answer(
        "How do I reset my password?"
    )

    assert response == "Final Answer"

    retrieval.retrieve.assert_called_once_with(
        "How do I reset my password?"
    )

    prompt_builder.build_prompt.assert_called_once()

    chat.generate_response.assert_called_once_with(
        "Generated Prompt"
    )


@patch("app.services.rag_services.ChatCompletionService")
def test_generate_answer_none_question(
    mock_chat,
):
    """
    Should raise RAGException for None question.
    """

    mock_chat.return_value = MagicMock()

    service = RAGService()

    with pytest.raises(RAGException):
        service.generate_answer(None)


@patch("app.services.rag_services.ChatCompletionService")
def test_generate_answer_empty_question(
    mock_chat,
):
    """
    Should raise RAGException for empty question.
    """

    mock_chat.return_value = MagicMock()

    service = RAGService()

    with pytest.raises(RAGException):
        service.generate_answer("")


@patch("app.services.rag_services.ChatCompletionService")
def test_generate_answer_blank_question(
    mock_chat,
):
    """
    Should raise RAGException for blank question.
    """

    mock_chat.return_value = MagicMock()

    service = RAGService()

    with pytest.raises(RAGException):
        service.generate_answer("     ")


@patch("app.services.rag_services.ChatCompletionService")
def test_generate_answer_long_question(
    mock_chat,
):
    """
    Should raise RAGException for question exceeding max length.
    """

    mock_chat.return_value = MagicMock()

    service = RAGService()

    with pytest.raises(RAGException):
        service.generate_answer("A" * 5001)


@patch("app.services.rag_services.ChatCompletionService")
@patch("app.services.rag_services.PromptBuilderService")
@patch("app.services.rag_services.RetrievalService")
def test_generate_answer_chat_failure(
    mock_retrieval,
    mock_prompt_builder,
    mock_chat,
):
    """
    Should wrap unexpected exceptions.
    """

    retrieval = MagicMock()
    retrieval.retrieve.return_value = ["chunk"]

    prompt_builder = MagicMock()
    prompt_builder.build_prompt.return_value = "Prompt"

    chat = MagicMock()
    chat.generate_response.side_effect = Exception(
        "Azure OpenAI Error"
    )

    mock_retrieval.return_value = retrieval
    mock_prompt_builder.return_value = prompt_builder
    mock_chat.return_value = chat

    service = RAGService()

    with pytest.raises(RAGException):
        service.generate_answer("Hello")