from agents.base_agent import BaseAgent

class CRISPRDesignAgent(BaseAgent):
    def __init__(self, context=None, variables=None):
        super().__init__(agent_name="crispr_design", context=context, variables=variables)