from knowledge_base.ingestion.fetchers.pmc_pdf_downloader import PMCPDFDownloader


import os
from datetime import datetime

from knowledge_base.ingestion.ingestors.base_ingestor import BaseIngestor

class PMCPDFIngestor(BaseIngestor):
    def __init__(self):
        self.downloader = PMCPDFDownloader()

    def fetch(self, query, **kwargs):
        return self.downloader.fetch_pdf_links_from_search(query, **kwargs)

    def save(self, results, output_dir, catalog=None, tag="pmc_pdf", **kwargs):
        os.makedirs(output_dir, exist_ok=True)
        self.downloader.save(results, output_dir, catalog=catalog, tag=tag)