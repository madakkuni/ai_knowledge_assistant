from dataclasses import dataclass


@dataclass
class VectorStoreConfig:
    """
    Configuration settings for the vector store.
    """

    collection_name: str = "knowledge_base"

    persist_directory: str = "data/vector_db"

    distance_function: str = "cosine"