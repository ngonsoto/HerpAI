import os
import logging
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.documents import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from knowledge_base.catalog.document_catalog import DocumentCatalogManager
from knowledge_base.catalog.document_scanner import DocumentScanner

logging.basicConfig(level=logging.INFO)

def build_vector_index(
    agent_name,
    index_path="rag_indexes",
    chunk_size=500,
    chunk_overlap=50,
    filter_by_agent=True,):
    docs = []
    catalog = DocumentCatalogManager()
    entries = catalog.get_all_documents()

    for entry in entries:
        # Filter documents by agent name if enabled
        if filter_by_agent and agent_name not in entry.get("tags", ""):
            continue

        file_path = entry.get("file_path") or os.path.join("data", "raw", entry["file_name"])
        try:
            content = DocumentScanner.read_document_content(file_path)
        except Exception as e:
            logging.warning(f"[!] Failed to read file {file_path}: {e}")
            continue

        raw_doc = Document(
            page_content=content,
            metadata={
                "source": entry["file_name"],
                "title": entry["title"],
                "tags": entry["tags"],
            }
        )

        # Split document into smaller chunks
        splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
        split_docs = splitter.split_documents([raw_doc])
        docs.extend(split_docs)

    if not docs:
        logging.warning(f"[!] No documents found for agent: {agent_name}")
        return

    embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vector_store = FAISS.from_documents(docs, embedding_model)

    os.makedirs(index_path, exist_ok=True)
    vector_store.save_local(os.path.join(index_path, f"{agent_name}_rag"))

    logging.info(f"[✔] Vector index built for agent: {agent_name} with {len(docs)} chunks.")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Build vector index for HerpAI documents")
    parser.add_argument("--agent", type=str, help="Agent name to build index for", required=False)
    parser.add_argument("--index_path", type=str, default="rag_indexes", help="Output path for vector index")
    parser.add_argument("--filter_by_agent", action="store_true", help="Enable filtering documents by agent tag")

    args = parser.parse_args()

    if args.agent:
        build_vector_index(
            agent_name=args.agent,
            index_path=args.index_path,
            filter_by_agent=args.filter_by_agent,
        )
    else:
        from src.config_loader import AppConfig
        config = AppConfig.load()
        for agent_name in config.agents.keys():
            build_vector_index(
                agent_name=agent_name,
                index_path=args.index_path,
                filter_by_agent=args.filter_by_agent,
            )