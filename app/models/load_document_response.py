from pydantic import BaseModel

from app.models.document_summary import DocumentSummary


class LoadDocumentResponse(BaseModel):
    success: bool
    documents_loaded: int
    documents: list[DocumentSummary]