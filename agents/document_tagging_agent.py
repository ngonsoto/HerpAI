from agents.base_agent import BaseAgent
from knowledge_base.catalog.document_catalog import DocumentCatalogManager
from knowledge_base.catalog.document_scanner import read_document_content
from src.config_loader import AppConfig
import logging

class DocumentTaggingAgent(BaseAgent):
    """
    Agent responsible for analyzing documents and assigning high-level tags
    like 'virology', 'drug_design', 'crispr', etc., based on content.
    """

    def __init__(self, context=None, variables=None, catalog_path="data/catalog/document_catalog.db"):
        super().__init__(agent_name="document_tagging", context=context, variables=variables)
        self.catalog = DocumentCatalogManager(db_path=catalog_path)
        self.app_config = AppConfig.load()
        self.logger = logging.getLogger("DocumentTaggingAgent")

    def run(self):
        """
        Overrides the base run method to perform tagging for all documents.
        """
        documents = self.catalog.get_all_documents()
        for doc in documents:
            content = read_document_content(doc["path"])
            self.variables["document_content"] = content
            self.variables["tag_categories"] = self._get_research_category_agents()
            self.logger.debug(f"[Tagging] Injected tag categories: {self.variables['tag_categories']}")
            tags = self._assign_tags(content)
            self.catalog.update_tags(doc["id"], tags)
            self.logger.info(f"[Tagging] Tagged document {doc['file_name']} -> {tags}")
        return "[Tagging] Completed tagging documents."

    def _assign_tags(self, content):
        agent_tag_map = {}
        if hasattr(self.app_config, "agents"):
            for agent_name, agent_config in self.app_config.agents.items():
                agent_keywords = getattr(agent_config, "tags", [])
                matched_keywords = [kw for kw in agent_keywords if kw.lower() in content.lower()]
                if matched_keywords:
                    # Add the agent name as an additional tag category
                    tag_entry = list(set(matched_keywords + [agent_name]))
                    agent_tag_map[agent_name] = tag_entry
        return agent_tag_map

    def _get_all_tag_categories(self):
        all_tags = set()
        if hasattr(self.app_config, "agents"):
            for agent_name, agent_config in self.app_config.agents.items():
                agent_tags = getattr(agent_config, "tags", [])
                all_tags.update(agent_tags)
                all_tags.add(agent_name)
        return list(all_tags)

    def _get_research_category_agents(self):
        return [
            agent_name
            for agent_name, agent_config in self.app_config.agents.items()
            if getattr(agent_config, "research_category", False)
        ]

if __name__ == "__main__":
    agent = DocumentTaggingAgent()
    agent.run()
