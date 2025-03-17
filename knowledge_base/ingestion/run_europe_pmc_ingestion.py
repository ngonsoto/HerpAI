from knowledge_base.ingestion.europe_pmc_fetcher import EuropePMCFetcher
from knowledge_base.catalog.document_catalog import DocumentCatalogManager

# Initialize fetcher and catalog
fetcher = EuropePMCFetcher(email="openbiocure@gmail.com")
queries = [
    "HSV-2 latency",
    "HSV-2 reactivation",
    "Herpes simplex virus epigenetics",
    "Herpesvirus immune evasion",
    "HSV latency transcriptome",
    "HSV latency treatment"
]

catalog = DocumentCatalogManager()

# Run all queries and store results
for query in queries:
    results = fetcher.search_and_fetch(query, max_results=100)
    for doc in results:
        print(doc["abstract"])
        catalog.add_document(
            file_name=doc["id"] + ".txt",
            file_type="txt",
            title=doc["title"],
            content=doc["abstract"],
            tags="HSV2,EuropePMC,Latency,Reactivation"
        )
        

print("[Ingestion] Europe PMC ingestion completed successfully.")