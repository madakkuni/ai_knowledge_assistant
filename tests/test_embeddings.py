from app.services.ingestion_service import IngestionService
from app.services.chunking_service import ChunkingService
from app.services.embedding_services import EmbeddingService

print("=" * 60)
print("Loading document...")
print("=" * 60)

ingestion_service = IngestionService()

documents = ingestion_service.load_document(
    "data/raw/COFOG_Enterprise_Payroll_FAQ.txt"
)

print(f"Documents Loaded : {len(documents)}")

print()

print("=" * 60)
print("Chunking document...")
print("=" * 60)

chunking_service = ChunkingService()

chunks = chunking_service.chunk_documents(documents)

print(f"Chunks Created : {len(chunks)}")

print()

print("=" * 60)
print("Generating embeddings...")
print("=" * 60)

embedding_service = EmbeddingService()

embeddings = embedding_service.generate_embeddings(chunks)

print(f"Embeddings Generated : {len(embeddings)}")

print()

print("=" * 60)
print("Sample Embedding")
print("=" * 60)

print("Metadata:")
print(embeddings[0].metadata)

print()

print("Vector Length:")
print(len(embeddings[0].vector))

print()

print("First 10 Dimensions:")
print(embeddings[0].vector[:10])