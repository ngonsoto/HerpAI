from agents.virology_agent import VirologyAgent
from agents.transmission_prevention_agent import TransmissionPreventionAgent
from agents.target_prioritization_agent import TargetPrioritizationAgent
from agents.drug_design_agent import DrugDesignAgent
from agents.crispr_design_agent import CRISPRDesignAgent
from agents.delivery_optimization_agent import DeliveryOptimizationAgent
from agents.report_generator_agent import ReportGeneratorAgent


class PipelineManager:
    def __init__(self, virus_type="HSV-2"):
        self.virus_type = virus_type
        self.context = {}

    def run_pipeline(self):
        agent_steps = [
            ("virology", VirologyAgent, {"variables": {"virus_type": self.virus_type}}),
            ("transmission_prevention", TransmissionPreventionAgent, {"context_key": "virology"}),
            ("target_prioritization", TargetPrioritizationAgent, {"context_key": "virology", "variables": {"virus_type": self.virus_type}}),
            ("drug_design", DrugDesignAgent, {"context_key": "target_prioritization", "variables": {"virus_type": self.virus_type}}),
            ("crispr_design", CRISPRDesignAgent, {"context_key": "virology", "variables": {"virus_type": self.virus_type}}),
            ("delivery_optimization", DeliveryOptimizationAgent, {"context_key": "crispr_design", "variables": {"virus_type": self.virus_type}}),
            ("report", ReportGeneratorAgent, {"context_key": None, "variables": {"virus_type": self.virus_type}})
        ]

        for name, agent_cls, params in agent_steps:
            print(f"[Pipeline] Running {name.replace('_', ' ').title()} Agent...")
            context = self.context.get(params.get("context_key")) if params.get("context_key") else self.context
            variables = params.get("variables", {})
            agent = agent_cls(context=context, variables=variables)
            agent.run()
            self.context[name] = agent.get_json()

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
