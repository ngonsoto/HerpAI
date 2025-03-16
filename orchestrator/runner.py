from agents.target_prioritization_agent import TargetPrioritizationAgent
from agents.virology_agent import VirologyAgent
from agents.transmission_prevention_agent import TransmissionPreventionAgent
from agents.crispr_design_agent import CRISPRDesignAgent
from agents.drug_design_agent import DrugDesignAgent
from agents.delivery_optimization_agent import DeliveryOptimizationAgent
from src.utils import extract_json_from_markdown
from src.config_loader import AppConfig

def main():
    try:
        config = AppConfig.load()
        context = {}

        print("\n[Step 1] Running Virology Agent...")
        virology_agent = VirologyAgent(variables={"virus_type": "HSV-2"})
        virology_agent.run()
        context["virology"] = virology_agent.get_json()

        print("\n[Step 2] Running Transmission Prevention Agent...")
        transmission_agent = TransmissionPreventionAgent(context=context["virology"], variables={})
        transmission_agent.run()
        context["transmission_prevention"] = transmission_agent.get_json()

        print("\n[Step 3] Running Target Prioritization Agent...")
        target_agent = TargetPrioritizationAgent(context=context["virology"], variables={"virus_type": "HSV-2"})
        target_agent.run()
        context["target_prioritization"] = target_agent.get_json()

        print("\n[Step 4] Running Drug Design Agent...")
        drug_agent = DrugDesignAgent(context=context["target_prioritization"], variables={"virus_type": "HSV-2"})
        drug_agent.run()
        context["drug_design"] = drug_agent.get_json()

        print("\n[Step 5] Running CRISPR Design Agent...")
        crispr_agent = CRISPRDesignAgent(context=context["virology"], variables={"virus_type": "HSV-2"})
        crispr_agent.run()
        context["crispr_design"] = crispr_agent.get_json()

        print("\n[Step 6] Running Delivery Optimization Agent...")
        delivery_agent = DeliveryOptimizationAgent(context=context["crispr_design"], variables={"virus_type": "HSV-2"})
        delivery_agent.run()
        context["delivery_optimization"] = delivery_agent.get_json()

        print("\n=== Final Output ===")
        for key, value in context.items():
            print(f"{key.replace('_', ' ').title()} Output:", value)

    except Exception as e:
        print(f"[ERROR] Execution failed: {e}")

if __name__ == "__main__": 
    main()
