import logging
from fastapi import APIRouter
from app.services.ingestion_service import IngestionService
from app.models.load_document_request import LoadDocumentRequest

logger = logging.getLogger("ai_knowledge_assistant")

router = APIRouter(
    prefix="/documents",
    tags=["Documents"]
)

ingestion_service = IngestionService()


@router.post("/load")
def load_document(request: LoadDocumentRequest):

    logger.info("Received document load request")

    documents = ingestion_service.load_document(request.file_path)

    logger.info("Returning response")

    return {
        "success": True,
        "documents_loaded": len(documents),
        "documents": [
            {
                "content": document.content,
                "metadata": document.metadata
            }
            for document in documents
        ]
    }