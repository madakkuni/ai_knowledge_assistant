import logging

from app.ingestion.loaders.loader_factory import LoaderFactory
from app.models.document import Document

logger = logging.getLogger(__name__)


class IngestionService:

    def load_document(self, file_path: str) -> list[Document]:

        logger.info("Starting ingestion for %s", file_path)

        loader = LoaderFactory.get_loader(file_path)

        documents = loader.load(file_path)

        logger.info("Successfully loaded %d document(s)", len(documents))

        return documents