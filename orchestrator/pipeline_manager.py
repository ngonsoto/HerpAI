from agents.virology_agent import VirologyAgent
from agents.transmission_prevention_agent import TransmissionPreventionAgent
from agents.target_prioritization_agent import TargetPrioritizationAgent
from agents.drug_design_agent import DrugDesignAgent
from agents.crispr_design_agent import CRISPRDesignAgent
from agents.delivery_optimization_agent import DeliveryOptimizationAgent


class PipelineManager:
    def __init__(self, virus_type="HSV-2"):
        self.virus_type = virus_type
        self.context = {}

    def run_pipeline(self):
        print("[Pipeline] Running Virology Agent...")
        virology_agent = VirologyAgent(variables={"virus_type": self.virus_type})
        virology_agent.run()
        self.context["virology"] = virology_agent.get_json()

        print("[Pipeline] Running Transmission Prevention Agent...")
        transmission_agent = TransmissionPreventionAgent(context=self.context["virology"], variables={})
        transmission_agent.run()
        self.context["transmission_prevention"] = transmission_agent.get_json()

        print("[Pipeline] Running Target Prioritization Agent...")
        target_agent = TargetPrioritizationAgent(context=self.context["virology"], variables={"virus_type": self.virus_type})
        target_agent.run()
        self.context["target_prioritization"] = target_agent.get_json()

        print("[Pipeline] Running Drug Design Agent...")
        drug_agent = DrugDesignAgent(context=self.context["target_prioritization"], variables={"virus_type": self.virus_type})
        drug_agent.run()
        self.context["drug_design"] = drug_agent.get_json()

        print("[Pipeline] Running CRISPR Design Agent...")
        crispr_agent = CRISPRDesignAgent(context=self.context["virology"], variables={"virus_type": self.virus_type})
        crispr_agent.run()
        self.context["crispr_design"] = crispr_agent.get_json()

        print("[Pipeline] Running Delivery Optimization Agent...")
        delivery_agent = DeliveryOptimizationAgent(context=self.context["crispr_design"], variables={"virus_type": self.virus_type})
        delivery_agent.run()
        self.context["delivery_optimization"] = delivery_agent.get_json()

        return self.context

    def export_results(self, output_dir="output"):
        import os
        import json

        os.makedirs(output_dir, exist_ok=True)
        for agent, result in self.context.items():
            path = os.path.join(output_dir, f"{agent}_output.json")
            with open(path, "w") as f:
                json.dump(result, f, indent=2)
        print(f"[Pipeline] Results saved to '{output_dir}/'")
