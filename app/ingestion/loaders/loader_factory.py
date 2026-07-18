from pathlib import Path

from app.exceptions.document_exceptions import DocumentLoadException
from app.ingestion.loaders.base_loader import BaseLoader
from app.ingestion.loaders.text_loader import TextLoader


class LoaderFactory:

    @staticmethod
    def get_loader(file_path: str) -> BaseLoader:

        extension = Path(file_path).suffix.lower()

        if extension == ".txt":
            return TextLoader()

        raise DocumentLoadException(
            f"Unsupported document type: {extension}"
        )