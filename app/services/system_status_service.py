"""
Service responsible for retrieving
system health and application status.
"""

import logging

from app.core.config import settings
from app.services.vector_store_service import VectorStoreService

logger = logging.getLogger(__name__)


class SystemStatusService:
    """
    Service responsible for retrieving
    application and AI system status.
    """

    def __init__(self) -> None:
        """
        Initialize the System Status Service.
        """

        self._vector_store_service = VectorStoreService()

        logger.info(
            "System Status Service initialized successfully."
        )

    def get_status(self) -> dict:
        """
        Retrieve current system status.
        """

        logger.info(
            "Collecting system status."
        )

        try:

            chunks = self._vector_store_service.get_chunks()

            document_names = {
                chunk["metadata"].get(
                    "source",
                    "Unknown",
                )
                for chunk in chunks
            }

            return {
                "application_name": settings.app_name,
                "application_version": settings.app_version,
                "environment": settings.environment,
                "status": "Healthy",
                "vector_store": "ChromaDB",
                "embedding_model": settings.azure_openai_embedding_deployment,
                "chat_model": settings.azure_openai_chat_deployment,
                "chunk_strategy": "FAQ Splitter",
                "documents_indexed": len(document_names),
                "chunks_indexed": len(chunks),
            }

        except Exception as ex:

            logger.exception(
                "Failed to collect system status."
            )

            return {
                "application_name": settings.app_name,
                "application_version": settings.app_version,
                "environment": settings.environment,
                "status": "Unavailable",
                "vector_store": "ChromaDB",
                "embedding_model": settings.azure_openai_embedding_deployment,
                "chat_model": settings.azure_openai_chat_deployment,
                "chunk_strategy": "FAQ Splitter",
                "documents_indexed": 0,
                "chunks_indexed": 0,
                "error": str(ex),
            }