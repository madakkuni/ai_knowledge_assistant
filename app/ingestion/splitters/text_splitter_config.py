from dataclasses import dataclass


@dataclass
class TextSplitterConfig:
    chunk_size: int = 1024
    chunk_overlap: int = 100
    def __post_init__(self):

        if self.chunk_size <= 0:
            raise ValueError("chunk_size must be greater than zero.")

        if self.chunk_overlap < 0:
            raise ValueError("chunk_overlap cannot be negative.")

        if self.chunk_overlap >= self.chunk_size:
            raise ValueError(
                "chunk_overlap must be smaller than chunk_size."
            )