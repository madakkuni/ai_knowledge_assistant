import logging

from app.ingestion.splitters.base_splitter import BaseSplitter
from app.ingestion.splitters.text_splitter_config import TextSplitterConfig
from app.models.chunk import Chunk
from app.models.document import Document

logger = logging.getLogger("ai_knowledge_assistant")


class FixedSizeSplitter(BaseSplitter):

    def __init__(self, config: TextSplitterConfig):

        self.config = config

    def split(self, document: Document) -> list[Chunk]:

        logger.info(
            "Splitting document: %s",
            document.metadata["source"]
        )

        text = document.content

        chunks: list[Chunk] = []

        start = 0

        chunk_id = 1

        while start < len(text):

            end = start + self.config.chunk_size

            chunk_text = text[start:end]

            chunks.append(
                Chunk(
                    content=chunk_text,
                    metadata={
                        **document.metadata,
                        "chunk_id": chunk_id,
                        "start_index": start,
                        "end_index": min(end, len(text))
                    }
                )
            )

            chunk_id += 1

            start += (
                self.config.chunk_size
                - self.config.chunk_overlap
            )

        logger.info(
            "Created %d chunks",
            len(chunks)
        )

        return chunks