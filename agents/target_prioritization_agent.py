from agents.base_agent import BaseAgent
import matplotlib.pyplot as plt
import os

class TargetPrioritizationAgent(BaseAgent):
    def __init__(self, context=None, variables=None):
        super().__init__(agent_name="target_prioritization", context=context, variables=variables)

    def run(self):
        self.raw_output = super().run()
        self._generate_visualization(self.raw_output)
        return self.raw_output

    def _generate_visualization(self, output_data):
        try:
            
            jsonResult = self.get_json()
            genes = jsonResult.get("Top Targets", [])
            if not genes:
                print("[TargetPrioritizationAgent] No gene targets found to visualize.")
                return

            impact_scores = [len(g) % 10 + 1 for g in genes]  # Simulated impact scores
            plt.figure(figsize=(10, 6))
            plt.bar(genes, impact_scores)
            plt.xlabel("Target Genes")
            plt.ylabel("Impact Score (Simulated)")
            plt.title("Target Prioritization: Gene Impact Chart")
            plt.xticks(rotation=45, ha="right")
            plt.tight_layout()
            os.makedirs("output", exist_ok=True)
            plt.savefig("output/fig_target_prioritization.png")
            plt.close()
            print("[TargetPrioritizationAgent] Visualization saved to output/fig_target_prioritization.png")
        except Exception as e:
            print(f"[TargetPrioritizationAgent] Visualization error: {e}")