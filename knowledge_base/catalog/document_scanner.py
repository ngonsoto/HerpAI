import os
import sqlite3
import pdfplumber
import pandas as pd
from datetime import datetime

from knowledge_base.catalog.document_catalog import DocumentCatalogManager

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
logger = logging.getLogger(__name__)

# Configuration constants
RAW_DOCUMENTS_PATH = "data/raw"

# Extract text from PDF
def parse_pdf(file_path):
    with pdfplumber.open(file_path) as pdf:
        text = "\n".join(page.extract_text() or "" for page in pdf.pages)
    return text

# Read CSV content as plain text
def parse_csv(file_path):
    df = pd.read_csv(file_path)
    return df.to_csv(index=False)

# Read TXT file content
def parse_txt(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

# Main ingestion loop
def ingest_all_documents():
    catalog = DocumentCatalogManager()
    for root, _, files in os.walk(RAW_DOCUMENTS_PATH):
        for file in files:
            file_path = os.path.join(root, file)
            ext = file.lower().split(".")[-1]
            content = ""

            try:
                if ext == "pdf":
                    content = parse_pdf(file_path)
                elif ext == "csv":
                    content = parse_csv(file_path)
                elif ext == "txt":
                    content = parse_txt(file_path)
                else:
                    logger.warning(f"Unsupported file type: {file}")
                    continue

                catalog.add_document(file_name=file, file_type=ext, title=file, path=file_path, ingested_at=datetime.utcnow())
                logger.info(f"[✓] Ingested: {file}")
            except Exception as e:
                logger.error(f"[✗] Failed to ingest {file}: {e}")

if __name__ == "__main__":
    ingest_all_documents()
