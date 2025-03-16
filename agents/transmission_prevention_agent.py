from agents.base_agent import BaseAgent
from src.config_loader import AppConfig
from agents.model_router import ModelRouter

class TransmissionPreventionAgent(BaseAgent):
    """
    TransmissionPreventionAgent is responsible for suggesting preventive strategies
    to reduce HSV transmission and outbreak risk using LLMs.
    """

    def __init__(self, context=None, variables=None):
        super().__init__(agent_name="transmission_prevention", context=context, variables=variables)

    def inject_context(self, prompt):
        return self.default_context_injection(prompt, context_fields=["Latency Genes", "Reactivation Triggers"])
