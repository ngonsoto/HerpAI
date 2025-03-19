from abc import ABC, abstractmethod

class BaseIngestor(ABC):
    @abstractmethod
    def fetch(self, query: str, **kwargs) -> list:
        pass

    @abstractmethod
    def save(self, results: list, output_dir: str, catalog=None, **kwargs):
        pass

    def ingest(self, query: str, output_dir: str, catalog=None, **kwargs):
        results = self.fetch(query, **kwargs)
        self.save(results, output_dir, catalog=catalog, **kwargs)