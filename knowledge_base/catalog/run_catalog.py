from knowledge_base.catalog.document_catalog import DocumentCatalogManager

# Initialize catalog manager
catalog = DocumentCatalogManager()

# Example: Add a document
catalog.add_document(
    file_name="example_paper.pdf",
    file_type="pdf",
    title="A Novel Approach to HSV-2 Latency",
    content="This is a test content about latency and reactivation genes.",
    tags="HSV,Latency,Genomics"
)

# Example: Query and export documents
catalog.query_documents(keyword="latency", tag_filter="HSV", export_dir="downloads")