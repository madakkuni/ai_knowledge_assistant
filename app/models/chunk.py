from dataclasses import dataclass


@dataclass
class Chunk:

    content: str

    chunk_id: int

    source: str

    start_index: int

    end_index: int