from pydantic import BaseModel


class DocumentSummary(BaseModel):
    source: str
    type: str
    characters: int