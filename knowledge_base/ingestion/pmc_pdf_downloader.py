import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

class PMCPDFDownloader:
    def __init__(self, output_dir="knowledge_base/data/raw/"):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def fetch_pdf_links_from_search(self, query, max_articles=10):
        headers = {"User-Agent": "Mozilla/5.0"}
        search_url = f"https://www.ncbi.nlm.nih.gov/pmc/?term={query.replace(' ', '+')}"
        response = requests.get(search_url, headers=headers)
        soup = BeautifulSoup(response.content, "html.parser")
        article_links = soup.select("a.view[href*='/articles/PMC']")
        pdf_links = []

        for i, link in enumerate(article_links[:max_articles]):
            article_href = link.get("href")
            article_url = urljoin("https://pmc.ncbi.nlm.nih.gov", article_href)

            if article_url.endswith(".pdf"):
                article_pdf_link = article_url
            else:
                article_pdf_link = self.extract_pdf_link(article_url)

            if article_pdf_link:
                pdf_links.append((article_pdf_link, f"article_{i+1}.pdf"))

        return pdf_links

    def extract_pdf_link(self, article_url):
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(article_url, headers=headers)
        soup = BeautifulSoup(response.content, "html.parser")
        meta_pdf = soup.find("meta", attrs={"name": "citation_pdf_url"})
        if meta_pdf and meta_pdf.get("content"):
            return meta_pdf.get("content")
        pdf_link_tag = soup.find("a", href=True, string="PDF")
        if pdf_link_tag:
            return urljoin("https://pmc.ncbi.nlm.nih.gov", pdf_link_tag.get("href"))
        return None

    def save(self, results, output_dir, catalog=None, tag="pmc_pdf", **kwargs):
        headers = {"User-Agent": "Mozilla/5.0"}
        for pdf_url, filename in results:
            response = requests.get(pdf_url, headers=headers)
            output_path = os.path.join(output_dir, filename)
            with open(output_path, "wb") as f:
                f.write(response.content)
                print(f"[✓] Downloaded: {output_path}")