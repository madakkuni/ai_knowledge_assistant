import logging

from fastapi import APIRouter

from app.services.ingestion_service import IngestionService

logger = logging.getLogger("ai_knowledge_assistant")

router = APIRouter(
    prefix="/documents",
    tags=["Documents"]
)

ingestion_service = IngestionService()


@router.post("/load")
def load_document(file_path: str):

    logger.info("Received document load request")

    documents = ingestion_service.load_document(file_path)

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