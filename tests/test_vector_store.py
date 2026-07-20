from app.services.ingestion_service import IngestionService
from app.services.chunking_service import ChunkingService
from app.services.embedding_services import EmbeddingService
from app.services.vector_store_service import VectorStoreService

print("\n" + "=" * 80)
print("              FEATURE 009 - VECTOR STORE TEST")
print("=" * 80)

# ------------------------------------------------------------------
# Load Document
# ------------------------------------------------------------------

print("\n📄 STEP 1 : Loading Document")

ingestion_service = IngestionService()

documents = ingestion_service.load_document(
    "data/raw/COFOG_Enterprise_Payroll_FAQ.txt"
)

print(f"✅ Documents Loaded : {len(documents)}")

# ------------------------------------------------------------------
# Chunk Document
# ------------------------------------------------------------------

print("\n🧩 STEP 2 : Chunking Document")

chunking_service = ChunkingService()

chunks = chunking_service.chunk_documents(documents)

print(f"✅ Chunks Created : {len(chunks)}")

# ------------------------------------------------------------------
# Generate Embeddings
# ------------------------------------------------------------------

print("\n🧠 STEP 3 : Generating Embeddings")

embedding_service = EmbeddingService()

embeddings = embedding_service.generate_embeddings(chunks)

print(f"✅ Embeddings Generated : {len(embeddings)}")

# ------------------------------------------------------------------
# Store Embeddings
# ------------------------------------------------------------------

print("\n💾 STEP 4 : Storing Embeddings")

vector_store_service = VectorStoreService()

vector_store_service.add_embeddings(embeddings)

print("✅ Embeddings stored successfully.")

# ------------------------------------------------------------------
# Similarity Search
# ------------------------------------------------------------------

print("\n🔍 STEP 5 : Similarity Search")

query_embedding = embeddings[0].vector

results = vector_store_service.similarity_search(
    query_embedding=query_embedding,
    top_k=3,
)

print(f"✅ Matches Found : {len(results['ids'][0])}")

print("\n" + "-" * 80)
print("TOP MATCHES")
print("-" * 80)

for index, document in enumerate(results["documents"][0], start=1):

    metadata = results["metadatas"][0][index - 1]
    distance = results["distances"][0][index - 1]

    print(f"\nResult #{index}")
    print(f"Chunk ID : {metadata['chunk_id']}")
    print(f"Distance : {distance:.6f}")
    print(f"Source   : {metadata['source']}")

    preview = document.replace("\n", " ")

    if len(preview) > 120:
        preview = preview[:120] + "..."

    print(f"Content  : {preview}")

print("\n" + "=" * 80)
print("🎉 FEATURE 009 TEST COMPLETED SUCCESSFULLY")
print("=" * 80)