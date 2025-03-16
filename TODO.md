## 🛣 Roadmap

The HerpAI roadmap outlines major development milestones, agent expansion plans, and areas open for collaboration.

### 🔖 Milestones Overview

- ✅ Claude Sonnet 3.7 integration
- ✅ VirologyAgent scaffold
- ✅ Centralized configuration via config.yaml
- ✅ ModelRouter abstraction for multi-model support
- ✅ Secure secret handling via .env
- ✅ Makefile for streamlined execution

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
