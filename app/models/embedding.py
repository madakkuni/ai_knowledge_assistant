from dataclasses import dataclass
from typing import Any


@dataclass
class Embedding:
    vector: list[float]
    content: str
    metadata: dict[str, Any]