import logging

from fastapi import APIRouter

from app.models.load_document_request import LoadDocumentRequest
from app.models.load_document_response import LoadDocumentResponse
from app.services.ingestion_service import IngestionService
from app.models.chunk_document_response import ChunkDocumentResponse
from app.services.chunking_service import ChunkingService

logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/documents",
    tags=["Documents"]
)

ingestion_service = IngestionService()
chunking_service = ChunkingService()


@router.post(
    "/load",
    response_model=LoadDocumentResponse
)
def load_document(request: LoadDocumentRequest):

    logger.info(
        "Received document load request: %s",
        request.file_path
    )

    documents = ingestion_service.load_document(
        request.file_path
    )

    response_documents = [
        {
            "source": document.metadata["source"],
            "type": document.metadata["type"],
            "characters": len(document.content)
        }
        for document in documents
    ]

    logger.info(
        "Loaded %d document(s)",
        len(documents)
    )

    return LoadDocumentResponse(
        success=True,
        documents_loaded=len(documents),
        documents=response_documents
    )

@router.post(
    "/chunk",
    response_model=ChunkDocumentResponse
)
def chunk_document(request: LoadDocumentRequest):

    logger.info(
        "Received chunk request: %s",
        request.file_path
    )

    documents = ingestion_service.load_document(
        request.file_path
    )

    chunks = chunking_service.chunk_documents(
        documents
    )

    logger.info(
        "Generated %d chunks",
        len(chunks)
    )

    return ChunkDocumentResponse(
        success=True,
        chunks_created=len(chunks),
        chunks=[
            {
                "content": chunk.content,
                "metadata": chunk.metadata
            }
            for chunk in chunks
        ]
    )