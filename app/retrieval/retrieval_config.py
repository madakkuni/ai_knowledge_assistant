from dataclasses import dataclass


@dataclass
class RetrievalConfig:
    """
    Configuration for retrieval operations.
    """

    top_k: int = 5