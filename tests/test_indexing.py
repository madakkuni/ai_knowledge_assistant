from app.services.ingestion_service import IngestionService
from app.services.chunking_service import ChunkingService
from app.services.indexing_service import IndexingService
from app.services.vector_store_service import VectorStoreService

print("=" * 100)
print("FEATURE 011 - INDEXING TEST")
print("=" * 100)

FILE_PATH = "data/raw/COFOG_Enterprise_Payroll_FAQ.txt"

# -----------------------------------------------------------------------------
# STEP 1 - Load Document
# -----------------------------------------------------------------------------

print("\nSTEP 1 : Loading Document")

ingestion_service = IngestionService()

documents = ingestion_service.load_document(FILE_PATH)

print(f"Documents Loaded : {len(documents)}")

# -----------------------------------------------------------------------------
# STEP 2 - Chunk Document
# -----------------------------------------------------------------------------

print("\nSTEP 2 : Chunking Document")

chunking_service = ChunkingService()

chunks = chunking_service.chunk_documents(documents)

print(f"Chunks Created : {len(chunks)}")

print("\n" + "=" * 100)
print("GENERATED CHUNKS")
print("=" * 100)

for index, chunk in enumerate(chunks, start=1):

    print(f"\nChunk #{index}")
    print(f"Length : {len(chunk.content)} characters")
    print("-" * 100)
    print(chunk.content)
    print("-" * 100)

# -----------------------------------------------------------------------------
# STEP 3 - Index Document
# -----------------------------------------------------------------------------

print("\nSTEP 3 : Creating Embeddings and Index")

indexing_service = IndexingService()

indexing_service.index_document(FILE_PATH)

print("Indexing completed successfully.")

# -----------------------------------------------------------------------------
# STEP 4 - Read ChromaDB
# -----------------------------------------------------------------------------

print("\nSTEP 4 : Reading ChromaDB")

vector_store_service = VectorStoreService()

# Access the underlying Chroma collection
collection = vector_store_service._vector_store._collection

results = collection.get(
    include=["documents", "metadatas", "embeddings"]
)

print(f"\nTotal Chunks Stored : {len(results['ids'])}")

print("\n" + "=" * 100)
print("STORED CHUNKS")
print("=" * 100)

for i in range(len(results["ids"])):

    chunk = results["documents"][i]
    metadata = results["metadatas"][i]

    print(f"\nChunk #{i+1}")
    print(f"ID       : {results['ids'][i]}")
    print(f"Length   : {len(chunk)} characters")
    print(f"Chunk Id : {metadata.get('chunk_id')}")
    print(f"Source   : {metadata.get('source')}")
    print("-" * 100)
    print(chunk)
    print("-" * 100)

print("\n" + "=" * 100)
print("INDEX VALIDATION COMPLETED")
print("=" * 100)