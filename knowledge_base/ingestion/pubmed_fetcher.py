import os
from Bio import Entrez
from typing import List, Dict


class PubMedFetcher:
    def __init__(self, email: str, api_key: str = None):
        """
        Initialize the PubMed fetcher with the required Entrez credentials.
        """
        Entrez.email = email
        if api_key:
            Entrez.api_key = api_key
        self.email = email
        self.api_key = api_key

    def search(self, query: str, max_results: int = 10) -> List[str]:
        """
        Perform a search on PubMed and return a list of article IDs.
        """
        handle = Entrez.esearch(db="pubmed", term=query, retmax=max_results)
        record = Entrez.read(handle)
        handle.close()
        return record["IdList"]

    def fetch_details(self, ids: List[str]) -> List[Dict]:
        """
        Fetch article summaries (abstracts and metadata) for the given PubMed IDs.
        """
        handle = Entrez.efetch(db="pubmed", id=",".join(ids), rettype="abstract", retmode="xml")
        records = Entrez.read(handle)
        handle.close()

        articles = []
        for article in records["PubmedArticle"]:
            article_id = article["MedlineCitation"]["PMID"]
            title = article["MedlineCitation"]["Article"]["ArticleTitle"]
            abstract = ""
            try:
                abstract_sections = article["MedlineCitation"]["Article"]["Abstract"]["AbstractText"]
                abstract = " ".join(str(section) for section in abstract_sections)
            except KeyError:
                abstract = "No abstract available."

            articles.append({
                "id": str(article_id),
                "title": title,
                "abstract": abstract
            })

        return articles

    def search_and_fetch(self, query: str, max_results: int = 10) -> List[Dict]:
        """
        Search PubMed and fetch article details in one step.
        """
        ids = self.search(query=query, max_results=max_results)
        return self.fetch_details(ids)