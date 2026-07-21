import os
import shutil

from app.services.ingestion_service import IngestionService
from app.services.chunking_service import ChunkingService
from app.services.embedding_services import EmbeddingService
from app.services.vector_store_service import VectorStoreService
from app.vectorstores.vector_store_config import VectorStoreConfig
from app.vectorstores.chroma_vector_store import ChromaVectorStore


# ==============================================================================
# CONFIGURATION
# ==============================================================================

DOCUMENT_PATH = "data/raw/COFOG_Enterprise_Payroll_FAQ.txt"

DELETE_EXISTING_DB = True

CHUNK_SIZE = 1000

CHUNK_OVERLAP = 200


# ==============================================================================
# DELETE EXISTING DATABASE
# ==============================================================================

config = VectorStoreConfig()

if DELETE_EXISTING_DB:

    if os.path.exists(config.persist_directory):

        print("\nDeleting existing Chroma database...")

        shutil.rmtree(config.persist_directory)

        print("Database deleted.")

    else:

        print("\nNo existing database found.")


# ==============================================================================
# LOAD DOCUMENT
# ==============================================================================

print("\n" + "=" * 80)
print("STEP 1 - LOAD DOCUMENT")
print("=" * 80)

ingestion_service = IngestionService()

documents = ingestion_service.load_document(DOCUMENT_PATH)

print(f"Documents Loaded : {len(documents)}")

for index, document in enumerate(documents, start=1):

    print(f"\nDocument {index}")

    print(f"Characters : {len(document.content)}")

    print(f"Source     : {document.metadata.get('source')}")


# ==============================================================================
# CHUNK DOCUMENT
# ==============================================================================

print("\n" + "=" * 80)
print("STEP 2 - CHUNK DOCUMENT")
print("=" * 80)

chunking_service = ChunkingService()

#
# IMPORTANT
#
# This assumes your ChunkingService supports overriding chunk size.
#
# If it currently doesn't, I'll show you how to add that.
#

chunks = chunking_service.chunk_documents(
    documents,
    chunk_size=CHUNK_SIZE,
    chunk_overlap=CHUNK_OVERLAP,
)

print(f"\nChunks Created : {len(chunks)}")

for index, chunk in enumerate(chunks, start=1):

    print("\n" + "-" * 80)

    print(f"Chunk #{index}")

    print(f"Length : {len(chunk.content)}")

    print(chunk.content)

print("-" * 80)


# ==============================================================================
# GENERATE EMBEDDINGS
# ==============================================================================

print("\n" + "=" * 80)
print("STEP 3 - GENERATE EMBEDDINGS")
print("=" * 80)

embedding_service = EmbeddingService()

embeddings = embedding_service.generate_embeddings(chunks)

print(f"Embeddings Generated : {len(embeddings)}")


# ==============================================================================
# STORE EMBEDDINGS
# ==============================================================================

print("\n" + "=" * 80)
print("STEP 4 - STORE EMBEDDINGS")
print("=" * 80)

vector_store_service = VectorStoreService()

vector_store_service.add_embeddings(embeddings)

print("Embeddings stored successfully.")


# ==============================================================================
# VERIFY DATABASE
# ==============================================================================

print("\n" + "=" * 80)
print("STEP 5 - VERIFY DATABASE")
print("=" * 80)

vector_store = ChromaVectorStore(config)

count = vector_store.collection.count()

print(f"Collection Count : {count}")


# ==============================================================================
# TEST SEARCH
# ==============================================================================

print("\n" + "=" * 80)
print("STEP 6 - TEST RETRIEVAL")
print("=" * 80)

query = "What is the payroll cutoff date?"

query_embedding = embedding_service.generate_query_embedding(query)

results = vector_store.similarity_search(
    query_embedding=query_embedding,
    top_k=3,
)

print("\nRetrieved Results")

for index, document in enumerate(results["documents"][0], start=1):

    metadata = results["metadatas"][0][index - 1]

    distance = results["distances"][0][index - 1]

    print("\n" + "-" * 80)

    print(f"Result #{index}")

    print(f"Distance : {distance:.6f}")

    print(f"Chunk ID : {metadata['chunk_id']}")

    print(document)

print("\n" + "=" * 80)
print("INDEXING COMPLETED SUCCESSFULLY")
print("=" * 80)