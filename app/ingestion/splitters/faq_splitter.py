"""
FAQ Splitter implementation.

Splits a FAQ document into one chunk
per Question–Answer pair.
"""

from __future__ import annotations

import re
from typing import List

from langchain_core.documents import Document

from app.ingestion.splitters.base_splitter import BaseSplitter


class FAQSplitter(BaseSplitter):
    """
    Split FAQ documents into Question–Answer chunks.
    """

    QUESTION_PATTERN = re.compile(
        r"(\d+\.\s*)?Q:\s*(.*?)\nA:\s*(.*?)(?=\n\d+\.\s*Q:|\Z)",
        re.DOTALL,
    )

    def split_documents(
        self,
        documents: List[Document],
    ) -> List[Document]:
        """
        Split documents into FAQ chunks.

        Args:
            documents:
                Input LangChain documents.

        Returns:
            List of FAQ chunks.
        """

        chunks: List[Document] = []

        for document in documents:

            matches = self.QUESTION_PATTERN.findall(
                document.page_content
            )

            if not matches:
                chunks.append(document)
                continue

            for _, question, answer in matches:

                chunk_text = (
                    f"Question:\n"
                    f"{question.strip()}\n\n"
                    f"Answer:\n"
                    f"{answer.strip()}"
                )

                metadata = dict(document.metadata)

                metadata["chunk_type"] = "faq"

                chunks.append(
                    Document(
                        page_content=chunk_text,
                        metadata=metadata,
                    )
                )

        return chunks