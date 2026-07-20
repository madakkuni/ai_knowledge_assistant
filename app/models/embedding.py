from dataclasses import dataclass
from typing import Any


@dataclass
class Embedding:
    vector: list[float]
    metadata: dict[str, Any]