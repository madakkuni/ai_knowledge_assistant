from pathlib import Path
import logging

from app.exceptions.document_exceptions import DocumentLoadException
from app.ingestion.loaders.base_loader import BaseLoader
from app.models.document import Document

logger = logging.getLogger("ai_knowledge_assistant")


class TextLoader(BaseLoader):

    def load(self, source: str) -> list[Document]:

        logger.info("Loading text document: %s", source)

        try:
            path = Path(source)

            text = path.read_text(encoding="utf-8")

            logger.info("Successfully loaded text document: %s", source)

            return [
                Document(
                    content=text,
                    metadata={
                        "source": str(path),
                        "type": "text"
                    }
                )
            ]

        except FileNotFoundError as ex:

            logger.exception("Document not found: %s", source)

            raise DocumentLoadException(
                f"Document not found: {source}"
            ) from ex

        except PermissionError as ex:

            logger.exception("Permission denied while reading: %s", source)

            raise DocumentLoadException(
                f"Permission denied: {source}"
            ) from ex

        except UnicodeDecodeError as ex:

            logger.exception("Invalid text encoding: %s", source)

            raise DocumentLoadException(
                f"Unable to decode text file: {source}"
            ) from ex

        except Exception as ex:

            logger.exception("Unexpected error while loading document: %s", source)

            raise DocumentLoadException(
                f"Failed to load document: {source}"
            ) from ex