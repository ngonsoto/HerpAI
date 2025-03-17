import os
import unittest
import sqlite3
from unittest.mock import patch
from datetime import datetime
from tempfile import TemporaryDirectory

from knowledge_base.catalog.document_catalog import DocumentCatalogManager

class TestDocumentCatalog(unittest.TestCase):
    def setUp(self):
        self.temp_dir = TemporaryDirectory()
        self.db_path = os.path.join(self.temp_dir.name, "test.db")

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_init_db(self):
        catalog = DocumentCatalogManager(db_path=self.db_path)
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='documents_catalog'")
        table_exists = cursor.fetchone() is not None
        conn.close()
        self.assertTrue(table_exists)

    def test_add_document(self):
        catalog = DocumentCatalogManager(db_path=self.db_path)
        catalog.add_document(
            file_name="sample.pdf",
            file_type="pdf",
            title="Sample PDF",
            content="This is a sample PDF file.",
            tags="sample,pdf"
        )
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM documents_catalog")
        row = cursor.fetchone()
        conn.close()
        self.assertIsNotNone(row)
        self.assertEqual(row[1], "sample.pdf")
        self.assertEqual(row[2], "pdf")
        self.assertEqual(row[3], "Sample PDF")
        self.assertEqual(row[4], "This is a sample PDF file.")
        self.assertEqual(row[5], "sample,pdf")
        self.assertIsNotNone(row[6])

    def test_query_documents(self):
        with TemporaryDirectory() as temp_dir:
            catalog = DocumentCatalogManager(db_path=self.db_path)

            catalog.add_document(
                file_name="sample1.pdf",
                file_type="pdf",
                title="Sample 1",
                content="This is the first sample.",
                tags="sample,pdf"
            )
            catalog.add_document(
                file_name="sample2.txt",
                file_type="txt",
                title="Sample 2",
                content="This is the second sample.",
                tags="sample,text"
            )

            # Test keyword search
            catalog.query_documents(keyword="first", export_dir=temp_dir)
            export_path_1 = os.path.join(temp_dir, "1_sample1.pdf.txt")
            self.assertTrue(os.path.exists(export_path_1))
            with open(export_path_1, "r", encoding="utf-8") as f:
                content = f.read()
            self.assertEqual(content, "This is the first sample.")
            os.remove(export_path_1)

            # Test tag search
            catalog.query_documents(tag_filter="text", export_dir=temp_dir)
            export_path_2 = os.path.join(temp_dir, "2_sample2.txt.txt")
            self.assertTrue(os.path.exists(export_path_2))
            with open(export_path_2, "r", encoding="utf-8") as f:
                content = f.read()
            self.assertEqual(content, "This is the second sample.")
            os.remove(export_path_2)

if __name__ == "__main__":
    unittest.main()
