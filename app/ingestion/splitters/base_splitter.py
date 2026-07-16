from abc import ABC, abstractmethod

from app.models.chunk import Chunk
from app.models.document import Document


class BaseSplitter(ABC):

    @abstractmethod
    def split(self, document: Document) -> list[Chunk]:
        """Split a document into chunks."""
        pass