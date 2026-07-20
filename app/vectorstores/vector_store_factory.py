from app.vectorstores.base_vector_store import BaseVectorStore
from app.vectorstores.chroma_vector_store import ChromaVectorStore
from app.vectorstores.vector_store_config import VectorStoreConfig


class VectorStoreFactory:
    """
    Factory class for creating vector store implementations.
    """

    @staticmethod
    def get_store(
        provider: str,
        config: VectorStoreConfig,
    ) -> BaseVectorStore:

        provider = provider.lower()

        if provider == "chroma":
            return ChromaVectorStore(config)

        raise ValueError(
            f"Unsupported vector store provider: {provider}"
        )