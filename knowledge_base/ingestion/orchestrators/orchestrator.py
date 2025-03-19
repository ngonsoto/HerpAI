
from knowledge_base.catalog.document_catalog import DocumentCatalogManager
from knowledge_base.ingestion.ingestors.europe_pmc_ingestor import EuropePMCIngestor
from knowledge_base.ingestion.ingestors.pmc_pdf_ingestor import PMCPDFIngestor
from knowledge_base.ingestion.ingestors.pubmed_ingestor import PubMedIngestor

def run_all_ingestions():
    catalog = DocumentCatalogManager()
    queries = ["HSV-2 latency"]
    ingestors = [
        PubMedIngestor(),
        EuropePMCIngestor(),
        PMCPDFIngestor()
    ]
    for ingestor in ingestors:
        for query in queries:
            output_dir = f"data/raw/{ingestor.__class__.__name__.lower()}/{query.replace(' ', '_')}"
            ingestor.ingest(query, output_dir=output_dir, catalog=catalog)

if __name__ == "__main__":
    run_all_ingestions()