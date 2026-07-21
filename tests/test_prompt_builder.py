"""
Unit tests for PromptBuilderService.
"""

import pytest

from app.models.chunk import Chunk
from app.services.prompt_builder_service import PromptBuilderService
from app.exceptions.bad_request_exception import BadRequestException


@pytest.fixture
def prompt_service() -> PromptBuilderService:
    """
    Create a PromptBuilderService instance.
    """
    return PromptBuilderService()


@pytest.fixture
def sample_chunks() -> list[Chunk]:
    """
    Create sample retrieved chunks.
    """
    return [
        Chunk(
            content="VPN passwords can be reset through the Service Portal.",
            metadata={"source": "kb001.txt"},
        ),
        Chunk(
            content="Employees must complete MFA verification before resetting passwords.",
            metadata={"source": "kb002.txt"},
        ),
    ]


def test_build_prompt_success(
    prompt_service: PromptBuilderService,
    sample_chunks: list[Chunk],
) -> None:
    """
    Verify that a prompt is successfully generated.
    """

    question = "How do I reset my VPN password?"

    prompt = prompt_service.build_prompt(
        question=question,
        chunks=sample_chunks,
    )

    assert prompt is not None

    assert "You are an enterprise knowledge assistant" in prompt

    assert "Context" in prompt

    assert "Question" in prompt

    assert "Answer" in prompt

    assert question in prompt

    assert "VPN passwords can be reset through the Service Portal." in prompt

    assert (
        "Employees must complete MFA verification"
        in prompt
    )


def test_build_prompt_with_empty_chunks(
    prompt_service: PromptBuilderService,
) -> None:
    """
    Verify prompt generation when retrieval returns no chunks.
    """

    question = "How do I reset my VPN password?"

    prompt = prompt_service.build_prompt(
        question=question,
        chunks=[],
    )

    assert prompt is not None

    assert "No relevant context found." in prompt

    assert question in prompt


def test_build_prompt_with_empty_question(
    prompt_service: PromptBuilderService,
    sample_chunks: list[Chunk],
) -> None:
    """
    Verify that an empty question raises BadRequestException.
    """

    with pytest.raises(BadRequestException):

        prompt_service.build_prompt(
            question="",
            chunks=sample_chunks,
        )


def test_build_prompt_with_none_question(
    prompt_service: PromptBuilderService,
    sample_chunks: list[Chunk],
) -> None:
    """
    Verify that a None question raises BadRequestException.
    """

    with pytest.raises(BadRequestException):

        prompt_service.build_prompt(
            question=None,
            chunks=sample_chunks,
        )


def test_prompt_contains_all_chunks(
    prompt_service: PromptBuilderService,
    sample_chunks: list[Chunk],
) -> None:
    """
    Verify every retrieved chunk is included in the prompt.
    """

    prompt = prompt_service.build_prompt(
        question="Sample question",
        chunks=sample_chunks,
    )

    for chunk in sample_chunks:
        assert chunk.content in prompt


def test_prompt_contains_question(
    prompt_service: PromptBuilderService,
    sample_chunks: list[Chunk],
) -> None:
    """
    Verify that the user's question is present in the prompt.
    """

    question = "What is MFA?"

    prompt = prompt_service.build_prompt(
        question=question,
        chunks=sample_chunks,
    )

    assert question in prompt


def test_prompt_is_string(
    prompt_service: PromptBuilderService,
    sample_chunks: list[Chunk],
) -> None:
    """
    Verify the generated prompt is a string.
    """

    prompt = prompt_service.build_prompt(
        question="Test",
        chunks=sample_chunks,
    )

    assert isinstance(prompt, str)