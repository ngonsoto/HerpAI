from .base_ingestor import BaseIngestor
from .pubmed_fetcher import PubMedFetcher
import os
from datetime import datetime

class PubMedIngestor(BaseIngestor):
    def __init__(self, email="openbiocure@gmail.com"):
        self.fetcher = PubMedFetcher(email=email)

    def fetch(self, query, **kwargs):
        return self.fetcher.search_and_fetch(query, **kwargs)

    def save(self, results, output_dir, catalog=None, tag="pubmed", **kwargs):
        os.makedirs(output_dir, exist_ok=True)
        for result in results:
            file_id = result["id"]
            title = result["title"].strip().replace("\n", " ")
            abstract = result["abstract"].strip().replace("\n", " ")
            file_name = f"{file_id}.txt"
            file_path = os.path.join(output_dir, file_name)
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(f"Title: {title}\n\nAbstract:\n{abstract}")
            print(f"[✓] Saved: {file_path}")
            if catalog:
                catalog.add_document(
                    file_name=file_name,
                    file_type="txt",
                    title=title,
                    path=file_path,
                    ingested_at=datetime.utcnow(),
                    tags=tag
                )