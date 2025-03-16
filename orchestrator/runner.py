from agents.virology_agent import VirologyAgent
from src.utils import extract_json_from_markdown

def main():

    agent = VirologyAgent()
    print(f"Running {agent.name}...\n")

    # Get the analysis results for HSV-2
    raw_response = agent.analyze_latency_and_reactivation(virus_type="HSV-2")
    results = extract_json_from_markdown(raw_response)

    # Assuming results is a dictionary with structured data
    print("Key Targets Identified:")
    print("- Latency Genes:", results.get('Latency Genes', 'No data available'))
    print("- Replication Genes:", results.get('Replication Genes', 'No data available'))
    print("- Reactivation Triggers:", results.get('Reactivation Triggers', 'No data available'))
    print("- Gene Regulation:", results.get('Gene Regulation', 'No data available'))

if __name__ == "__main__":
    main()
