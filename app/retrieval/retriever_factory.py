from app.retrieval.base_retriever import BaseRetriever
from app.retrieval.retrieval_config import RetrievalConfig
from app.retrieval.vector_retriever import VectorRetriever


class RetrieverFactory:
    """
    Factory class for creating retriever implementations.
    """

    @staticmethod
    def get_retriever(
        provider: str,
        config: RetrievalConfig,
    ) -> BaseRetriever:

        provider = provider.lower()

        if provider == "vector":
            return VectorRetriever(config)

        raise ValueError(
            f"Unsupported retriever provider: {provider}"
        )