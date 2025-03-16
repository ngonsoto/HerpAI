from agents.model_router import ModelRouter

class VirologyAgent:
    def __init__(self):
        self.name = "Virology Agent"
        self.llm = ModelRouter(agent_name="virology")

    def analyze_latency_and_reactivation(self, virus_type="HSV-2"):
        prompt = f"""
        As a molecular virology expert, identify the key genes involved in latency and reactivation of {virus_type}.
        Also list typical reactivation triggers based on known studies.
        Format response as:
        - Latency Genes: [...]
        - Replication Genes: [...]
        - Reactivation Triggers: [...]
        """
        return self.llm.query(prompt)