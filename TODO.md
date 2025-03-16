## 🛣 Roadmap

The HerpAI roadmap outlines major development milestones, agent expansion plans, and areas open for collaboration.

### 🔖 Visionary Milestones

- 🌐 Establish HerpAI as an open, modular platform for AI-driven drug discovery
- 🧠 Demonstrate multi-agent collaboration for molecular target identification and treatment design
- 📊 Enable transparent, reproducible scientific discovery via open-source LLM pipelines
- 🧬 Bridge AI-generated insights with wet-lab testing through standardized report outputs
- 🔎 Foster global collaboration between AI engineers, researchers, and molecular biologists
- 📄 Publish and maintain an open whitepaper and research framework on HSV cure discovery
- 🚀 Set the foundation for expanding HerpAI into broader bio-cure discovery beyond HSV

### 📌 Upcoming Features, Stories, and Tasks

#### 🚀 Feature: Agent Expansion
- [ ] Story: Build TargetPrioritizationAgent to prioritize molecular targets based on virology output
- [ ] Story: Develop DrugDesignAgent to generate SMILES-based drug candidates using LLM
- [ ] Story: Implement CRISPRDesignAgent to propose CRISPR guide sequences targeting HSV genes

#### 📊 Feature: Scientific Report Engine
- [ ] Story: Add logic for generating structured scientific reports from agent outputs
- [ ] Task: Create sample report templates in Markdown and PDF format

#### 🧠 Feature: Multi-Model Abstraction Layer
- [ ] Story: Extend ModelRouter to support local LLM providers (e.g., Mistral, LLaMA)
- [ ] Task: Add fallback mechanism between providers in ModelRouter

#### 🧪 Feature: Testing & Validation
- [ ] Story: Add unit tests for all agents and core utilities
- [ ] Task: Add integration tests for multi-agent execution pipeline

#### 💻 Feature: Optional Frontend Interface
- [ ] Story: Build lightweight UI interface using Streamlit or Gradio to run agents interactively

#### 📄 Feature: Whitepaper Publication
- [ ] Story: Draft and finalize the HerpAI whitepaper for public scientific release

#### 🔧 Feature: Developer Productivity Tooling
- [ ] Task: Setup CI/CD automation with GitHub Actions for testing and linting
