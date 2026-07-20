"""
Configuration values for prompt construction.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class PromptConfig:
    """
    Configuration used while building prompts.
    """

    SYSTEM_MESSAGE: str = (
        "You are an enterprise knowledge assistant.\n"
        "Answer ONLY using the provided context.\n"
        "If the answer cannot be found in the context, "
        'respond with: "I don\'t have enough information."'
    )

    CONTEXT_HEADER: str = "Context"

    QUESTION_HEADER: str = "Question"

    ANSWER_HEADER: str = "Answer"

    SEPARATOR: str = "-" * 60