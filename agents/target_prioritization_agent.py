from agents.base_agent import BaseAgent

class TargetPrioritizationAgent(BaseAgent):
    def __init__(self, context=None, variables=None):
        super().__init__(agent_name="target_prioritization", context=context, variables=variables)