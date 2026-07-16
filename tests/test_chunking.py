from app.ingestion.loaders.text_loader import TextLoader
from app.ingestion.splitters.text_splitter_config import TextSplitterConfig
from app.services.chunking_service import ChunkingService

loader = TextLoader()

documents = loader.load(
    "data/raw/COFOG_Enterprise_Payroll_FAQ.txt"
)

service = ChunkingService()

chunks = service.chunk_documents(documents)

print(len(chunks))

for chunk in chunks[:3]:
    print(chunk.metadata)
    print(chunk.content)