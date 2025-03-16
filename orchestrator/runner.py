from agents.virology_agent import VirologyAgent
from agents.transmission_prevention_agent import TransmissionPreventionAgent
from src.utils import extract_json_from_markdown
from src.config_loader import AppConfig

def main():
    try:
        config = AppConfig.load()

        print("\n[Step 1] Running Virology Agent...")
        virology_agent = VirologyAgent(variables={"virus_type": "HSV-2"})
        virology_agent.run()
        virology_output = virology_agent.get_json()

        print("\n[Step 2] Running Transmission Prevention Agent with Virology context...")
        transmission_agent = TransmissionPreventionAgent(context=virology_output, variables={})
        transmission_agent.run()
        transmission_output = transmission_agent.get_json()

        print("\n=== Final Output ===")
        print("Virology Output:", virology_output)
        print("Transmission Prevention Output:", transmission_output)

    except Exception as e:
        print(f"[ERROR] Execution failed: {e}")

if __name__ == "__main__": 
    main()
