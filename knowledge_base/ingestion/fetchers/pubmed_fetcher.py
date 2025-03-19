import requests
from xml.etree import ElementTree

class PubMedFetcher:
    def __init__(self, email="openbiocure@gmail.com"):
        self.base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
        self.email = email

    def search_and_fetch(self, query, max_results=100):
        search_url = f"{self.base_url}esearch.fcgi"
        params = {
            "db": "pubmed",
            "term": query,
            "retmax": max_results,
            "retmode": "xml",
            "email": self.email
        }
        search_response = requests.get(search_url, params=params)
        print(f"[✓] Fetched: {search_url}")
        search_tree = ElementTree.fromstring(search_response.content)
        id_list = [id_elem.text for id_elem in search_tree.findall(".//Id")]

        summaries = []
        for pubmed_id in id_list:
            summary = self.fetch_summary(pubmed_id)
            if summary:
                summaries.append(summary)
                
        print(f"[✓] Fetched: {summaries.count}")
        return summaries

    def fetch_summary(self, pubmed_id):
        summary_url = f"{self.base_url}esummary.fcgi"
        params = {
            "db": "pubmed",
            "id": pubmed_id,
            "retmode": "xml",
            "email": self.email
        }
        summary_response = requests.get(summary_url, params=params)
        summary_tree = ElementTree.fromstring(summary_response.content)

        title_elem = summary_tree.find(".//Item[@Name='Title']")
        abstract = self.fetch_abstract(pubmed_id)

        return {
            "id": pubmed_id,
            "title": title_elem.text if title_elem is not None else "",
            "abstract": abstract
        }

    def fetch_abstract(self, pubmed_id):
        fetch_url = f"{self.base_url}efetch.fcgi"
        params = {
            "db": "pubmed",
            "id": pubmed_id,
            "retmode": "xml",
            "rettype": "abstract",
            "email": self.email
        }
        fetch_response = requests.get(fetch_url, params=params)
        tree = ElementTree.fromstring(fetch_response.content)
        abstract_texts = tree.findall(".//AbstractText")
        abstract = " ".join([elem.text for elem in abstract_texts if elem.text])
        return abstract
