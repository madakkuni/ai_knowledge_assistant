from app.models.chunk import Chunk
from app.services.embedding_services import EmbeddingService
from app.services.retrieval_service import RetrievalService

print("\n" + "=" * 80)
print("              FEATURE 010 - RETRIEVAL TEST")
print("=" * 80)

# ------------------------------------------------------------------
# STEP 1 - User Query
# ------------------------------------------------------------------

print("\n❓ STEP 1 : User Question")

question = "What is the payroll cutoff date?"

print(question)

# ------------------------------------------------------------------
# STEP 2 - Generate Query Embedding
# ------------------------------------------------------------------

print("\n🧠 STEP 2 : Generate Query Embedding")

embedding_service = EmbeddingService()

query_chunk = Chunk(
    content=question,
    metadata={
        "source": "user_query",
        "chunk_id": "query",
    },
)

query_embedding = embedding_service.generate_embeddings(
    [query_chunk]
)[0]

print("Query embedding generated successfully.")

# ------------------------------------------------------------------
# STEP 3 - Retrieve Relevant Chunks
# ------------------------------------------------------------------

print("\n🔍 STEP 3 : Retrieve Relevant Chunks")

retrieval_service = RetrievalService()

results = retrieval_service.retrieve(
    query_embedding=query_embedding,
    top_k=5,
)

documents = results["documents"][0]
metadatas = results["metadatas"][0]
distances = results["distances"][0]

print(f"Retrieved {len(documents)} matching chunks.")

print("\n" + "-" * 80)
print("TOP MATCHES")
print("-" * 80)

for index, (document, metadata, distance) in enumerate(
    zip(documents, metadatas, distances),
    start=1,
):

    print(f"\nResult #{index}")
    print(f"Chunk ID : {metadata.get('chunk_id')}")
    print(f"Distance : {distance:.6f}")
    print(f"Source   : {metadata.get('source')}")

    preview = document.replace("\n", " ")

    if len(preview) > 200:
        preview = preview[:200] + "..."

    print(f"Content  : {preview}")

print("\n" + "=" * 80)
print("FEATURE 010 RETRIEVAL TEST COMPLETED")
print("=" * 80)