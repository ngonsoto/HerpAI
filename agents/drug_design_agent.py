from agents.base_agent import BaseAgent

class DrugDesignAgent(BaseAgent):
    def __init__(self, context=None, variables=None):
        super().__init__(agent_name="drug_design", context=context, variables=variables)