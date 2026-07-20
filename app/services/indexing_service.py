import logging

from app.services.ingestion_service import IngestionService
from app.services.chunking_service import ChunkingService
from app.services.embedding_services import EmbeddingService
from app.services.vector_store_service import VectorStoreService

logger = logging.getLogger(__name__)


class IndexingService:
    """
    Service responsible for indexing documents into the vector store.
    """

    def __init__(self):

        self.ingestion_service = IngestionService()

        self.chunking_service = ChunkingService()

        self.embedding_service = EmbeddingService()

        self.vector_store_service = VectorStoreService()

    def index_document(
        self,
        file_path: str,
    ) -> None:

        logger.info(
            "Starting indexing for %s",
            file_path,
        )

        # Step 1 - Load document
        documents = self.ingestion_service.load_document(
            file_path
        )

        # Step 2 - Chunk document
        chunks = self.chunking_service.chunk_documents(
            documents
        )

        # Step 3 - Generate embeddings
        embeddings = self.embedding_service.generate_embeddings(
            chunks
        )

        # Step 4 - Store embeddings
        self.vector_store_service.add_embeddings(
            embeddings
        )

        logger.info(
            "Successfully indexed %d chunks.",
            len(embeddings),
        )