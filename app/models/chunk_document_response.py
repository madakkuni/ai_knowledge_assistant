from pydantic import BaseModel
from typing import Any


class ChunkResponse(BaseModel):
    content: str
    metadata: dict[str, Any]


class ChunkDocumentResponse(BaseModel):
    success: bool
    chunks_created: int
    chunks: list[ChunkResponse]