# src/utils.py
import json
import re
from langchain_community.vectorstores import FAISS 

def extract_json_from_markdown(response: str) -> dict:
    match = re.search(r"```json\s*(\{.*?\})\s*```", response, re.DOTALL)
    if match:
        try:
            return json.loads(match.group(1))
        except json.JSONDecodeError:
            print("⚠️ Could not decode JSON block.")
            return {}
    else:
        print("⚠️ No JSON block found in response.")
        return {}


def get_rag_retriever(retriever_name):
    # Example: based on name, load appropriate retriever index
    if retriever_name == "virology_rag":
        return FAISS.load_local("rag_indexes/virology_rag")
    elif retriever_name == "transmission_prevention_rag":
        return FAISS.load_local("rag_indexes/transmission_prevention_rag")
    else:
        raise ValueError(f"No retriever found for: {retriever_name}")