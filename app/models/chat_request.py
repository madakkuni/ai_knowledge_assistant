"""
Request model for Chat API.
"""

from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    """
    Chat request payload.
    """

    question: str = Field(
        ...,
        min_length=1,
        description="User question.",
        examples=[
            "How do I reset my VPN password?"
        ],
    )