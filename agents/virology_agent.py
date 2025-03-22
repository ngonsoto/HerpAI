from agents.model_router import ModelRouter
from agents.base_agent import BaseAgent
import os
from src.config_loader import AgentConfig, AppConfig

class VirologyAgent(BaseAgent):
    """
    VirologyAgent is responsible for analyzing HSV latency and reactivation patterns
    using either standard prompt-based AI or a RAG pipeline with vectorstore retrieval.
    """

    def __init__(self, context=None, variables=None):
        super().__init__(agent_name="virology", context=context, variables=variables)