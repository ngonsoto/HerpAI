from .base_ingestor import BaseIngestor
from .europe_pmc_fetcher import EuropePMCFetcher

class EuropePMCIngestor(BaseIngestor):
    def __init__(self):
        self.fetcher = EuropePMCFetcher()

    def fetch(self, query, **kwargs):
        return self.fetcher.search_and_fetch(query, **kwargs)

    def save(self, results, output_dir, catalog=None, tag="europe_pmc", **kwargs):
        self.fetcher.save_results_as_text(results, output_dir, catalog=catalog, tag=tag)