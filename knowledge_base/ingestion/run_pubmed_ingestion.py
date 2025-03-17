from knowledge_base.ingestion.pubmed_fetcher import PubMedFetcher
from knowledge_base.catalog.document_catalog import DocumentCatalogManager

fetcher = PubMedFetcher(email="openbiocure@gmail.com")

search_query = (
    "HSV-2 latency reactivation"
    " OR herpes simplex virus latency"
    " OR HSV-2 gene expression"
    " OR herpes virus epigenetics"
    " OR HSV-2 immune evasion"
    " OR HSV-2 transmission prevention"
    " OR HSV-2 chromatin regulation"
    " OR HSV-2 viral replication"
)

results = fetcher.search_and_fetch(search_query, max_results=500)

catalog = DocumentCatalogManager()
for doc in results:
    catalog.add_document(
        file_name=doc["id"] + ".txt",
        file_type="txt",
        title=doc["title"],
        content=doc["abstract"],
        tags="HSV2,Latency"
    )
print("[Ingestion] PubMed ingestion completed successfully.")