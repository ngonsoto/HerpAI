# runner.py

from agents.virology_agent import VirologyAgent

def main():
    agent = VirologyAgent()
    print(f"Running {agent.name}...\n")

    results = agent.analyze_latency_and_reactivation(virus_type="HSV-2")
    
    print("Key Targets Identified:")
    print("- Latency Genes:", results['latency_genes'])
    print("- Replication Genes:", results['replication_genes'])
    print("- Reactivation Triggers:", results['reactivation_triggers'])

if __name__ == "__main__":
    main()