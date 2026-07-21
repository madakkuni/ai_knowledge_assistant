"""
Chat API endpoints.
"""

import logging

from fastapi import APIRouter

from app.models.chat_request import ChatRequest
from app.models.chat_response import ChatResponse
from app.services.rag_services import RAGService

logger = logging.getLogger(__name__)
rag_service = RAGService()

router = APIRouter(
    prefix="/chat",
    tags=["Chat"],
)


@router.post(
    "",
    response_model=ChatResponse,
)
async def chat(
    request: ChatRequest,
) -> ChatResponse:
    """
    Chat endpoint.

    Args:
        request:
            Chat request.

    Returns:
        Chat response.
    """

    logger.info(
        "Received chat request."
    )

    logger.info(
        "Question: %s",
        request.question,
    )

    answer = rag_service.generate_answer(
        request.question
    )

    return ChatResponse(
        answer = answer
    )