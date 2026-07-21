"""
Rebuild the vector database.

Workflow:
1. Load documents
2. Split documents
3. Generate embeddings
4. Store embeddings in ChromaDB
"""

import logging

from app.services.indexing_service import IndexingService

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)


def main():

    logger.info("Starting indexing...")

    indexing_service = IndexingService()

    file_path = "data/raw/COFOG_Enterprise_Payroll_FAQ.txt"

    result = indexing_service.index_document(file_path)

    logger.info("Indexing completed.")

    logger.info(result)


if __name__ == "__main__":
    main()