from abc import ABC, abstractmethod

from app.models.document import Document


class BaseLoader(ABC):

    @abstractmethod
    def load(self, source: str) -> list[Document]:
        pass