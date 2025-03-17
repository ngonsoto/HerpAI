import os
import sqlite3
from datetime import datetime

DB_PATH = "knowledge_base/catalog.db"

class DocumentCatalogManager:
    def __init__(self, db_path=DB_PATH):
        self.db_path = db_path
        self._init_db()

    def _init_db(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS documents_catalog (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                file_name TEXT,
                file_type TEXT,
                title TEXT,
                content TEXT,
                tags TEXT,
                ingestion_date TEXT
            )
        """)
        conn.commit()
        conn.close()

    def add_document(self, file_name, file_type, title, content, tags=""):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        # Check if the document already exists by file_name
        cursor.execute("""
            SELECT COUNT(*) FROM documents_catalog WHERE file_name = ?
        """, (file_name,))
        exists = cursor.fetchone()[0]

        if exists:
            print(f"[Catalog] Skipping duplicate entry: {file_name}")
        else:
            cursor.execute("""
                INSERT INTO documents_catalog (file_name, file_type, title, content, tags, ingestion_date)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (file_name, file_type, title, content, tags, datetime.now().isoformat()))
            conn.commit()
            print(f"[Catalog] Document added: {file_name}")

        conn.close()

    def query_documents(self, keyword=None, tag_filter=None, export_dir="downloads"):
        os.makedirs(export_dir, exist_ok=True)
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        query = "SELECT id, file_name, file_type, title, content FROM documents_catalog WHERE 1=1"
        params = []
        if keyword:
            query += " AND content LIKE ?"
            params.append(f"%{keyword}%")
        if tag_filter:
            query += " AND tags LIKE ?"
            params.append(f"%{tag_filter}%")
        rows = cursor.execute(query, params).fetchall()
        conn.close()

        for row in rows:
            doc_id, fname, ftype, title, content = row
            output_path = os.path.join(export_dir, f"{doc_id}_{fname}.txt")
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"[↓] Exported: {output_path}")