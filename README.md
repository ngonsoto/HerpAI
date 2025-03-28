# HerpAI

[![Lint and Test](https://github.com/ngonsoto/HerpAI/actions/workflows/lintformattest.yml/badge.svg)](https://github.com/ngonsoto/HerpAI/actions/workflows/lintformattest.yml)
[![Nightly](https://github.com/ngonsoto/HerpAI/actions/workflows/nightly.yml/badge.svg)](https://github.com/ngonsoto/HerpAI/actions/workflows/nightly.yml)

*Accelerating the discovery of a functional cure for HSV-1 and HSV-2 using AI.*

➡️ **[View Final Sample Report (Markdown)](./simulation/v1/final_report.md)**  
See what HerpAI is capable of generating — a comprehensive scientific report built by chaining AI agents.

📍 **[Project Roadmap](./Roadmap.md)** – See the strategic vision, goals, and ML/LLM multi-agent architecture.

👉 **[Meet Our Contributors](./CONTRIBUTORS.md)** - See who is working and supporting the project.

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
pip install -e .
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

---

## 🧪 Sample Simulation Outputs

To help researchers and contributors understand how HerpAI outputs are structured, we’ve included **sample simulation result files** generated from pipeline execution.

You can find them in the following folder:

```
./simulation/v1/
```

Each file corresponds to the structured output of one AI agent. These simulations help illustrate the JSON format, scientific data points, and types of insights HerpAI can generate.

### Example: TargetPrioritizationAgent Output

```json
{
  "Top Targets": [
    "UL30 (DNA polymerase)",
    "UL5/UL8/UL52 (Helicase-primase complex)",
    "UL39 (Ribonucleotide reductase)"
  ],
  "Rationale": "These targets were prioritized based on essential functions in viral replication, proven druggability with precedent antivirals, and high sequence conservation across HSV strains. UL30 is the primary target of current nucleoside analogs like acyclovir, while the helicase-primase complex offers an orthogonal mechanism of action demonstrated by clinical candidates. UL39 (ribonucleotide reductase) is essential for viral DNA synthesis in non-dividing cells and has well-characterized active sites amenable to inhibitor design."
}
```

> 💡 Note: As the project evolves, we may migrate these simulations under a more structured location like `./data/simulations/` to align with a standardized data management structure.

## 📚 Knowledge Base Data Sources

| Source             | Description                                             | Format(s)        | Status       | Notes                                      |
|--------------------|---------------------------------------------------------|------------------|--------------|--------------------------------------------|
| **PubMed**         | Biomedical abstracts and metadata via NCBI Entrez API   | Text/Abstract    | ✅ Implemented | Limited to abstracts unless PDF manually retrieved |
| **Europe PMC**     | Full-text and abstracts from biomedical literature      | Text/Abstract    | ✅ Implemented | Some open-access full-text available        |
| **ClinicalTrials.gov** | Clinical trial descriptions and metadata            | XML / JSON       | 🔜 Planned    | Can be used to augment clinical context     |
| **bioRxiv / medRxiv** | Preprint articles in biomedical sciences             | PDF / Text       | 🔜 Planned    | Can scrape PDFs and metadata via RSS/API    |
| **arXiv (q-bio)**  | Preprints in quantitative biology                       | PDF / Text       | 🔜 Planned    | Use arXiv API and download PDFs             |
| **CORD-19 Dataset** | COVID-19 research dataset from Allen Institute         | JSON / PDF       | 🔜 Planned    | Large biomedical literature collection      |
| **Patent Databases** | Biomedical patent literature (e.g., Espacenet, USPTO) | PDF / Text       | 🔜 Planned    | Relevant for drug discovery IP landscape    |
| **Open Access Repositories** | Institutional OA content                       | PDF / Text       | 🔜 Planned    | Target bioinformatics and virology OA repos |
| **WHO Database**   | Reports and publications related to virology            | PDF              | 🔜 Planned    | Public reports useful for public health context |

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

**Email:** <openbiocure@gmail.com>  
**GitHub:** [https://github.com/openbiocure/HerpAI](https://github.com/openbiocure/HerpAI)

 ---

## 🙋‍♀️ Help Needed — Join the Mission

 We welcome passionate collaborators to help scale HerpAI and push scientific innovation forward. Below are roles where we need your support:

 | Role                          | Background/Expertise Needed                                               |
 |-------------------------------|---------------------------------------------------------------------------|
 | Biomedical Research Advisor   | Virology, molecular biology, HSV-specific research                        |
 | Computational Biologist       | Omics data processing, protein structure modeling, pathway analysis       |
 | AI/ML Engineer                | LLM prompt tuning, LangChain integration, RAG pipelines                   |
 | Software Engineer (Backend)   | Python, API development, data pipelines                                   |
 | UI/UX Designer                | Streamlit/Gradio UI design, scientific visualization                      |
 | Scientific Writer             | Assist in report writing, whitepaper contributions, and academic output   |
 | DevOps Contributor            | CI/CD pipelines, deployment scaffolding, automation scripting             |
 | Community Manager             | Facilitate open collaboration, respond to contributors, handle outreach   |

 > 💡 If you want to contribute or collaborate, please open an issue or send an email to [openbiocure@gmail.com](mailto:openbiocure@gmail.com).

