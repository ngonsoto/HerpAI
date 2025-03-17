# File: knowledge_base/ingestion/europe_pmc_fetcher.py

import requests

class EuropePMCFetcher:
    BASE_URL = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"

    def __init__(self, email=None):
        self.email = email

    def search_and_fetch(self, query, max_results=100):
        results = []
        params = {
            "query": query,
            "format": "json",
            "pageSize": max_results,
        }
        response = requests.get(self.BASE_URL, params=params)
        data = response.json()
        for i, result in enumerate(data.get("resultList", {}).get("result", []), 1):
            title = result.get("title", "")
            abstract = result.get("abstractText", "")
            results.append({
                "id": f"eupmc_{result.get('id') or i}",
                "title": title,
                "abstract": abstract
            })
        return results