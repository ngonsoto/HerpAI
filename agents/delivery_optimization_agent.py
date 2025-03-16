from agents.base_agent import BaseAgent

class DeliveryOptimizationAgent(BaseAgent):
    def __init__(self, context=None, variables=None):
        super().__init__(agent_name="delivery_optimization", context=context, variables=variables)