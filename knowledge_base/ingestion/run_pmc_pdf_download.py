from knowledge_base.ingestion.pmc_pdf_downloader import PMCPDFDownloader

downloader = PMCPDFDownloader()
search_url = "https://www.ncbi.nlm.nih.gov/pmc/?term=HSV-2+latency+genes"
pdf_links = downloader.fetch_pdf_links_from_search(search_url, max_articles=10)
downloader.download_pdfs(pdf_links)