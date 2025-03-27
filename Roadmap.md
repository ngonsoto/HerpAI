# HerpAI: Intensive Roadmap for ML+LLM Multi-Agent Therapeutics Framework (HSV-2 Focus)

---

## 1. Objective

Establish a modular, scalable, AI-powered discovery pipeline for HSV-2 therapeutic targeting using both:

- LLM-based reasoning agents (prompt-driven)
- ML-based analytical models (data-driven)

---

## 2. Integration Strategy

| Component               | Description                                                       |
|------------------------|-------------------------------------------------------------------|
| LLM Agents              | Prompt-based domain experts (e.g., VirologyAgent, DrugDesignAgent)|
| ML Scoring Modules      | Scoring/classification/regression models for target ranking        |
| RAG Agents              | Knowledge-augmented LLM reasoning via document retrieval           |
| Task Framework          | Abstracted task execution class for chaining ML, RAG, LLM agents   |

---

## 3. ML Layer Integration

| Layer                    | ML Use Case                          | Algorithms                        |
|-------------------------|--------------------------------------|-----------------------------------|
| Target Prioritization   | Predict therapeutic relevance (low P)| Logistic Regression, XGBoost     |
| Drug Efficacy Scoring   | Predict compound EC50, binding score | Random Forest, SVM, Neural Nets  |
| CRISPR Off-Target Risk  | Predict gRNA off-target effects      | Gradient Boosting, CNN           |
| Delivery Success Modeling| Predict delivery route performance   | Regression, Meta Learning         |

---

## 4. ML Dataset Sources (To Be Collected)

| Source Type         | Examples                                                              |
|---------------------|-----------------------------------------------------------------------|
| Virology Datasets   | GEO, ENA, NCBI Viral DB, Virus Pathogen Resource (ViPR)               |
| Drug Activity       | ChEMBL, PubChem BioAssays, DrugBank                                   |
| CRISPR Datasets     | CRISPR-ERA, CRISPR-Benchmark, CRISPRitz off-target datasets           |
| Delivery Vectors    | AAV tropism datasets, LNP formulation studies (PubMed, Kaggle)        |
| Literature Knowledge| Ingested papers from PubMed, EuropePMC, PMC PDFs                      |

---

## 5. RAG Architecture

| Layer         | Tool/Lib             | Description                                |
|---------------|----------------------|--------------------------------------------|
| Chunking      | Langchain / Local    | Chunk PDF/CSV/TXT data                     |
| Embedding     | SentenceTransformers | Create vector representations              |
| Vector Store  | FAISS / Chroma       | Store documents for fast similarity search |
| Retriever     | Langchain Retriever  | Retrieve top-k documents per prompt        |
| Prompt Inject | Inject into agents   | Augment LLM answers with grounded context  |

---

## 6. Task Framework (Planned)

| Task Node Type         | Purpose                                    |
|------------------------|--------------------------------------------|
| LLMAgentTask           | Executes an LLM agent with variable injection |
| MLScoringTask          | Runs model predictions on structured data  |
| RAGTask                | Embeds & retrieves relevant literature     |
| AggregatorTask         | Combines multi-agent outputs               |

Visual chaining can be supported later via Langflow-compatible task graphing.

---

## 7. Confidence Index / Scoring Layer

Each agent’s output should be:

- Post-processed via a scoring model (mock or trained)
- Annotated with P-Value or Confidence Score
- Thresholded before final report generation

---

## 8. Team Roles Required

| Role                      | Background Needed                             |
|---------------------------|-----------------------------------------------|
| ML Engineer               | Biomedical datasets, model training/pipelines |
| Data Scientist            | Feature engineering, ML interpretability      |
| Virologist/Biologist      | Curate gene-level information, validate targets |
| Bioinformatics Specialist | Sequence & gene regulatory understanding      |
| Software Engineer         | Backend microservices, agents, pipelines      |
| MLOps/DevOps              | Deploy models, orchestrate retraining         |
| UX Designer               | Scientific visualization & report builder     |

---

## 9. Next Steps (Immediate)

- [ ] Refactor agents to support scoring layer  
- [ ] Extend pipeline with MLScoringTask  
- [ ] Add confidence annotations in report  
- [ ] Begin dataset gathering scripts  
- [ ] Scaffold `data/curation/` module for ML dataset cleaning  
- [ ] Extend RAG system to auto-index new papers  
