"""
Service responsible for browsing the knowledge base.
"""

import logging

from app.services.vector_store_service import VectorStoreService

logger = logging.getLogger(__name__)


class KnowledgeBaseService:
    """
    Provides read-only access to indexed knowledge.
    """

    def __init__(self):

        self._vector_store_service = VectorStoreService()

    def get_chunks(
        self,
        limit: int = 100,
    ):
        """
        Return indexed chunks.
        """

        logger.info(
            "Loading knowledge base chunks."
        )

        return self._vector_store_service.get_chunks(
            limit=limit
        )