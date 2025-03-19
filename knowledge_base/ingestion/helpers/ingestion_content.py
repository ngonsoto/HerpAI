import os
import sqlite3
import pdfplumber
import pandas as pd
from datetime import datetime

# Base paths
RAW_DIR = "knowledge_base/raw"

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

# Insert document record into DB
def store_metadata(file_name, file_type, content, tags=""):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO documents_catalog (file_name, file_type, title, content, tags, ingestion_date)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (file_name, file_type, file_name, content, tags, datetime.now().isoformat()))
    conn.commit()
    conn.close()

# Main ingestion loop
def ingest_all_documents():
    for root, _, files in os.walk(RAW_DIR):
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
                    print(f"Unsupported file type: {file}")
                    continue

                store_metadata(file, ext, content)
                print(f"[✓] Ingested: {file}")
            except Exception as e:
                print(f"[✗] Failed to ingest {file}: {e}")

if __name__ == "__main__":
    ingest_all_documents()
