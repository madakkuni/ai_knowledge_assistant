import logging
from fastapi import APIRouter
from app.services.ingestion_service import IngestionService
from app.models.load_document_request import LoadDocumentRequest
from app.models.load_document_response import LoadDocumentResponse

logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/documents",
    tags=["Documents"]
)

ingestion_service = IngestionService()


@router.post(
    "/load",
    response_model=LoadDocumentResponse
)
def load_document(request: LoadDocumentRequest):

    documents = ingestion_service.load_document(request.file_path)

    response_documents = [
        {
            "source": document.metadata["source"],
            "type": document.metadata["type"],
            "characters": len(document.content)
        }
        for document in documents
    ]

    return LoadDocumentResponse(
        success=True,
        documents_loaded=len(documents),
        documents=response_documents
    )