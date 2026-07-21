"""
Configuration values for chat completion.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class ChatConfig:
    """
    Configuration used for chat completion requests.
    """

    TEMPERATURE: float = 0.2

    MAX_TOKENS: int = 1000

    TOP_P: float = 0.95

    FREQUENCY_PENALTY: float = 0.0

    PRESENCE_PENALTY: float = 0.0