"""
Configuration values for chat completion.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class ChatConfig:
    """
    Configuration used for chat completion requests.
    """

    temperature: float = 0.2

    max_tokens: int = 1000

    top_p: float = 0.95

    frequency_penalty: float = 0.0

    presence_penalty: float = 0.0