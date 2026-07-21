

from app.ingestion.splitters.splitter_factory import SplitterFactory
from app.ingestion.splitters.text_splitter_config import TextSplitterConfig
from app.models.chunk import Chunk
from app.models.document import Document

import logging
logger = logging.getLogger(__name__)


class ChunkingService:

    def chunk_documents(
        self,
        documents: list[Document]
    ) -> list[Chunk]:

        logger.info("Starting chunking process")

        config = TextSplitterConfig(
            chunk_size=1025,
            chunk_overlap=200
        )

        splitter = SplitterFactory.get_splitter(
            "fixed",
            config
        )

        chunks: list[Chunk] = []

        for document in documents:

            chunks.extend(
                splitter.split(document)
            )

        logger.info(
            "Generated %d chunks",
            len(chunks)
        )

        return chunks