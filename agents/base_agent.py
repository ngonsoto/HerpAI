import os
from agents.model_router import ModelRouter
from src.config_loader import AppConfig
from langchain_community.vectorstores.faiss import FAISS

class BaseAgent:
    """
    Base class for HerpAI agents. Handles loading config, model routing, prompt handling, and context injection.
    """

    def __init__(self, agent_name, context=None, variables=None):
        self.agent_name = agent_name
        self.context = context or {}
        self.variables = variables or {}
        self.config = AppConfig.load().agents[agent_name]
        self._load_rag_retriever()
        self.router = ModelRouter(agent_name=agent_name)
        self.raw_output = None

    def _load_rag_retriever(self, base_path="data/rag_indexes"):
        """
        Load the appropriate RAG retriever for the agent based on agent_name convention.
        """
        retriever_path = os.path.join(base_path, f"{self.agent_name}_rag")
        if os.path.exists(retriever_path):
            try:
                from langchain_community.embeddings import HuggingFaceEmbeddings
                embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
                self.rag_retriever = FAISS.load_local(retriever_path, embeddings=embedding_model)
                print(f"[RAG] Loaded retriever from: {retriever_path}")
            except Exception as e:
                print(f"[RAG] Failed to load retriever for {self.agent_name}: {e}")
                self.rag_retriever = None
        else:
            print(f"[RAG] No RAG index found at: {retriever_path}")
            self.rag_retriever = None

    def load_prompt(self):
        """
        Loads the raw prompt file from disk.
        """
        version = self.config.prompt_version
        path = f"prompts/{self.agent_name}_prompt_{version}.md"
        with open(path, "r") as f:
            return f.read()

    def inject_context(self, prompt, context_fields=None, section_header="[Contextual Input]"):
        """
        Injects context values and replaces template variables in the prompt.

        Args:
            prompt (str): The prompt string to process.
            context_fields (list): Specific context fields to inject if desired.
            section_header (str): Header text for context injection.

        Returns:
            str: Final prompt string.
        """
        # Replace template variables
        for key, value in self.variables.items():
            placeholder = f"{{{{{key}}}}}"
            prompt = prompt.replace(placeholder, str(value))

        # Inject contextual fields if provided
        if self.context and isinstance(self.context, dict) and context_fields:
            extra_context = f"\n\n{section_header}\n"
            for field in context_fields:
                value = self.context.get(field, [])
                extra_context += f"{field}: {value}\n"
            prompt += extra_context

        return prompt

    def default_context_injection(self, prompt, context_fields=None, section_header="[Contextual Input]"):
        """
        Injects default structured context into the prompt based on selected fields from self.context.
        Args:
            prompt (str): Original prompt.
            context_fields (list): List of fields from self.context to inject.
            section_header (str): Optional header to insert before context data.
        Returns:
            str: Prompt with injected context.
        """
        extra_context = f"\n\n{section_header}\n"
        if not self.context or not isinstance(self.context, dict):
            return prompt
        for field in context_fields or []:
            value = self.context.get(field, [])
            extra_context += f"{field}: {value}\n"
        return prompt + extra_context

    def run(self):
        """
        Runs the agent workflow: loads prompt, injects RAG context, queries LLM.
        """
        prompt = self.load_prompt()

        # Always retrieve documents from RAG retriever and inject into context
        if hasattr(self, "rag_retriever"):
            documents = self.rag_retriever.retrieve(self.variables)
            rag_context = "\n".join([doc.page_content for doc in documents])
            self.variables["context"] = rag_context

        final_prompt = self.inject_context(prompt)
        self.raw_output = self.router.query(final_prompt)
        return self.raw_output

    def get_json(self):
        """
        Extracts structured JSON content from self.raw_output.
        Returns:
            dict: Parsed JSON content or empty dict on failure.
        """
        from src.utils import extract_json_from_markdown
        try:
            return extract_json_from_markdown(self.raw_output)
        except Exception as e:
            print(f"[Warning] Failed to extract structured output: {e}")
            return {}
