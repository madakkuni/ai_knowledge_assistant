from dataclasses import dataclass


@dataclass
class EmbeddingConfig:
    model_name: str = "text-embedding-3-small"
    batch_size: int = 16