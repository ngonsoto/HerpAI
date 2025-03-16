# HerpAI  
*Accelerating the discovery of a functional cure for HSV-1 and HSV-2 using AI.*

---

## ✨ What is HerpAI?

**HerpAI** is an open-source, AI-driven discovery platform designed to accelerate the search for a **real, functional cure for Herpes Simplex Virus (HSV-1 and HSV-2)**.

Built under the **OpenBioCure** initiative, HerpAI leverages a **modular multi-agent architecture** powered by **Large Language Models (LLMs)**, generative chemistry, gene editing design, and biological simulations — all structured to generate actionable scientific outputs such as:

- Small molecule drug candidates  
- CRISPR-based gene editing strategies  
- Delivery optimization protocols  
- Latency disruption hypotheses  
- Detailed scientific reports for wet-lab testing

---

## 🎯 Project Goals

- Build a transparent, open-source discovery engine for HSV cure research  
- Enable collaborative biomedical innovation powered by AI  
- Publish molecule and strategy candidates as open scientific artifacts  
- Support researchers and labs with AI-generated insights  
- Push HSV cure research beyond what any single lab or pharma company is doing

---

## 🧠 Key Features

- Modular multi-agent architecture:
  - Virology Agent
  - Target Prioritization Agent
  - Drug Design Agent
  - CRISPR Design Agent
  - Delivery Optimization Agent
  - Simulation Agent
- SMILES molecule generation and structure prediction
- gRNA (guide RNA) design for gene editing
- AutoDock and SwissADME-based simulation
- Markdown/PDF scientific report generation
- Future-ready for adaptation to other diseases

---

## 🚀 Getting Started

Follow these steps to set up and run HerpAI on your local machine.

### 1. Clone the repository
```bash
git clone https://github.com/openbiocure/HerpAI.git
cd HerpAI
```

### 2. Create a virtual environment (optional but recommended)
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install required Python packages
```bash
pip install -r requirements.txt
```

### 4. Configure environment variables
Create a `.env` file in the project root with your API keys:

```bash
touch .env
```
Then add the following:
```
SONNET_API_KEY=your-sonnet-api-key-here
OPENAI_API_KEY=your-openai-api-key-here
```

### 5. Run the pipeline
```bash
make run
```

This will:
- Execute all AI agents in sequence
- Export individual agent outputs to `/output`
- Generate a compiled Markdown report at `/output/final_report.md`


You should see output from the active agent execution printed to your terminal.

---

## 📁 Repository Structure
      .
      ├── agents/                # Modular AI agents
      ├── prompts/               # Prompt templates
      ├── molecule_generation/   # SMILES generation logic
      ├── simulation/            # Docking, ADMET, delivery models
      ├── knowledge_base/        # Paper ingestion and vector search
      ├── orchestrator/          # Agent pipeline orchestration
      ├── output/                # Generated scientific reports
      ├── api/                   # REST API interface
      ├── ui/                    # Optional user interface (Streamlit/Gradio)
      ├── tests/                 # Unit and integration tests
      ├── docs/                  # Whitepaper, diagrams, technical docs
      ├── LICENSE                # MIT License
      └── README.md              # Project documentation

---


## 🧠 AI Agent Modules Overview

| Agent Name                  | Description                                                                                      | Status           |
|----------------------------|--------------------------------------------------------------------------------------------------|------------------|
| VirologyAgent              | Extracts HSV latency, replication, reactivation genes, and regulatory data from LLMs             | ✅ Implemented    |
| TargetPrioritizationAgent   | Prioritizes genes/proteins for therapeutic targeting based on impact score                       | ✅ Implemented    |
| DrugDesignAgent            | Generates novel compound suggestions using AI-driven molecular synthesis                         | ✅ Implemented    |
| CRISPRDesignAgent          | Designs CRISPR guide RNAs targeting key latency/reactivation genes                              | ✅ Implemented    |
| DeliveryOptimizationAgent   | Suggests delivery mechanisms for CRISPR or drugs (e.g., AAV, LNP, microfluidics)                | ✅ Implemented    |
| TransmissionPreventionAgent | Identifies non-invasive strategies to reduce outbreaks and transmission risk                    | ✅ Implemented    |
| ReportGeneratorAgent       | Creates structured biomedical reports from agent outputs                                        | ✅ Implemented    |

## 🧠 Agent Execution Flow

HerpAI is designed to support modular and flexible chaining of AI agents. Below is the current planned **Branch + Merge flow** architecture:

```
VirologyAgent
   ↘                              ↘
TargetPrioritizationAgent      TransmissionPreventionAgent
   ↘                                   ↘
DrugDesignAgent                   ← Merge Insights →
   ↓
CRISPRDesignAgent
   ↓
DeliveryOptimizationAgent
   ↓
ReportGeneratorAgent
```

This structure enables parallel exploration of both **cure-focused** and **prevention-focused** strategies before converging into delivery simulations and final biomedical report generation.

## 📂 Export & Reporting

After executing all agents through the Pipeline Manager, HerpAI automatically exports agent outputs to structured JSON files under the `/output` directory.

Planned enhancements include:
- Markdown/PDF biomedical report compilation
- Scientific charts and agent summary visualization
- Scientific charts (e.g., gene impact bar charts, gRNA design matrix) will be integrated into reports

## 📊 Output Structure

HerpAI saves two layers of output:
1. **Structured Agent Results**: Saved as individual JSON files in the `/output` folder. Example: `virology_output.json`, `drug_design_output.json`, etc.
2. **Final Report**: A compiled scientific report is generated in Markdown format at `output/final_report.md` and includes findings from all agents.

This dual-output format supports both programmatic consumption and human-readable insight. Reports may include embedded diagrams and scientific charts saved in `/output` (e.g., PNG visualizations).

## 📄 License

HerpAI is released under the **MIT License** — feel free to use, extend, or remix it for scientific and research purposes.

---

## 📚 Additional Resources

- 📄 [Whitepaper Outline](docs/whitepaper-outline.md) – Full structure of the HerpAI scientific paper detailing system architecture, methodology, and discovery flows.
- 📜 [Code of Conduct](CODE_OF_CONDUCT.md) – Guidelines for respectful, inclusive, and collaborative contribution.
- 🤝 [Contributing Guide](CONTRIBUTING.md) – Instructions for getting started, contributing code, or collaborating with the project.

---

### 🤝 Collaboration Opportunities

- Prompt engineering and optimization
- New agent contributions (biology, chemistry, CRISPR, etc.)
- Validation feedback from researchers
- Technical documentation and scientific writing
- Frontend/API integration enhancements

## 📬 Contact

**Email:** openbiocure@gmail.com  
**GitHub:** [https://github.com/openbiocure/HerpAI](https://github.com/openbiocure/HerpAI)

> Let’s end HSV — together.
