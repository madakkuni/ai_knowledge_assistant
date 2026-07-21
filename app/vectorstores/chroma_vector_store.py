import logging

import chromadb
from chromadb.config import Settings

from app.embeddings.embedding_config import EmbeddingConfig
from app.exceptions.vector_store_exception import VectorStoreException
from app.models.embedding import Embedding
from app.vectorstores.base_vector_store import BaseVectorStore
from app.vectorstores.vector_store_config import VectorStoreConfig

logger = logging.getLogger(__name__)


class ChromaVectorStore(BaseVectorStore):
    """
    ChromaDB implementation of the vector store.
    """

    def __init__(
        self,
        config: VectorStoreConfig,
    ):

        self.config = config

        try:

            self.client = chromadb.PersistentClient(
                path=self.config.persist_directory,
                settings=Settings(
                    anonymized_telemetry=False
                )
            )

            self.collection = self.client.get_or_create_collection(
                name=self.config.collection_name,
                metadata={
                    "hnsw:space": self.config.distance_function
                }
            )

            logger.info(
                "Connected to Chroma collection '%s'",
                self.config.collection_name
            )

        except Exception as ex:

            logger.exception(
                "Failed to initialize ChromaDB."
            )

            raise VectorStoreException(
                "Unable to initialize vector store."
            ) from ex

    def add_embeddings(
        self,
        embeddings: list[Embedding],
    ) -> None:

        if not embeddings:

            logger.warning(
                "No embeddings supplied."
            )

            return

        try:

            ids = []

            vectors = []

            documents = []

            metadatas = []

            for embedding in embeddings:

                metadata = embedding.metadata

                ids.append(
                    f"chunk_{metadata['chunk_id']}"
                )

                vectors.append(
                    embedding.vector
                )

                documents.append(embedding.content)

                metadatas.append(
                    metadata
                )

            self.collection.add(
                ids=ids,
                embeddings=vectors,
                documents=documents,
                metadatas=metadatas
            )

            logger.info(
                "Stored %d embeddings.",
                len(ids)
            )

        except Exception as ex:

            logger.exception(
                "Failed storing embeddings."
            )

            raise VectorStoreException(
                "Unable to store embeddings."
            ) from ex

    def similarity_search(
        self,
        query_embedding: list[float],
        top_k: int = 5,
    ):

        try:

            result = self.collection.query(
                query_embeddings=[query_embedding],
                n_results=top_k,
            )

            logger.info(
                "Similarity search returned %d results.",
                top_k
            )

            return result

        except Exception as ex:

            logger.exception(
                "Similarity search failed."
            )

            raise VectorStoreException(
                "Similarity search failed."
            ) from ex
        
    def get_chunks(
        self,
        limit: int = 100,
    ):
        """
        Retrieve indexed chunks from ChromaDB.

        Args:
            limit:
                Maximum number of chunks.

        Returns:
            List of indexed chunks.
        """

        logger.info(
            "Loading up to %d chunks from ChromaDB.",
            limit,
        )

        try:

            results = self.collection.get(
                limit=limit,
                include=[
                    "documents",
                    "metadatas",
                ],
            )

            chunks = []

            for document, metadata in zip(
                results.get("documents", []),
                results.get("metadatas", []),
            ):

                chunks.append(
                    {
                        "content": document,
                        "metadata": metadata,
                    }
                )

            chunks.sort(
                key=lambda chunk: chunk["metadata"].get(
                    "chunk_id",
                    0,
                )
            )

            logger.info(
                "Retrieved %d chunks.",
                len(chunks),
            )

            return chunks

        except Exception as ex:

            logger.exception(
                "Failed to retrieve chunks."
            )

            raise VectorStoreException(
                "Unable to retrieve chunks."
            ) from ex