from app.services.indexing_service import IndexingService

print("=" * 80)
print("FEATURE 011 - INDEXING TEST")
print("=" * 80)

indexing_service = IndexingService()

indexing_service.index_document(
    "data/raw/COFOG_Enterprise_Payroll_FAQ.txt"
)

print("\nIndexing completed successfully.")