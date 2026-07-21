"""
FAQ Splitter implementation.

Creates one Chunk per Question-Answer pair.
"""

import logging
import re

from app.ingestion.splitters.base_splitter import BaseSplitter
from app.models.chunk import Chunk
from app.models.document import Document

logger = logging.getLogger("ai_knowledge_assistant")


class FAQSplitter(BaseSplitter):

    QUESTION_PATTERN = re.compile(
        r"(\d+\.\s*)?Q:\s*(.*?)\nA:\s*(.*?)(?=\n\d+\.\s*Q:|\Z)",
        re.DOTALL,
    )

    def split(
        self,
        document: Document,
    ) -> list[Chunk]:

        logger.info(
            "Splitting FAQ document: %s",
            document.metadata["source"],
        )

        matches = self.QUESTION_PATTERN.findall(
            document.content
        )

        chunks: list[Chunk] = []

        chunk_id = 1

        for _, question, answer in matches:

            chunk_text = (
                f"Question:\n"
                f"{question.strip()}\n\n"
                f"Answer:\n"
                f"{answer.strip()}"
            )

            chunks.append(
                Chunk(
                    content=chunk_text,
                    metadata={
                        **document.metadata,
                        "chunk_id": chunk_id,
                        "chunk_type": "faq",
                        "question": question.strip(),
                    },
                )
            )

            chunk_id += 1

        logger.info(
            "Created %d FAQ chunks.",
            len(chunks),
        )

        return chunks