import requests

class EuropePMCFetcher:
    BASE_URL = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"

    def search_and_fetch(self, query, max_results=100):
        params = {
            "query": query,
            "format": "json",
            "pageSize": max_results
        }
        response = requests.get(self.BASE_URL, params=params)
        data = response.json()
        results = []

        for record in data.get("resultList", {}).get("result", []):
            title = record.get("title", "")
            abstract = record.get("abstractText", "")
            pmid = record.get("id", record.get("pmid", "unknown"))

            results.append({
                "id": pmid,
                "title": title,
                "abstract": abstract
            })
        return results

    def save_results_as_text(self, results, output_dir, catalog=None, tag="europe_pmc"):
        import os
        from datetime import datetime

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
