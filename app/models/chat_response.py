"""
Response model for Chat API.
"""

from pydantic import BaseModel


class ChatResponse(BaseModel):
    """
    Chat response payload.
    """

    answer: str