# HerpAI MVP1 – Scope and Checklist

This document defines the scope and success criteria for MVP1 of HerpAI – a research assistant system designed to accelerate herpes (HSV-1/2) cure discovery using AI.

---

## 🎯 MVP1 Goal
Deliver a working proof-of-concept that demonstrates HerpAI’s ability to:
- Ingest biomedical content from multiple sources
- Detect relevant viral targets like ICP0, LAT, and UL39
- Simulate treatment strategies using docking/ADMET tools
- Output a structured, researcher-ready scientific report

---

## 📌 MVP1 Scope

### ✅ In Scope:
- Ingestion pipelines for 3 sources:
  - PubMed (abstracts)
  - Europe PMC (full-text when available)
  - PDFs from local/test source
- Extraction of biological targets using tagging agents
- One working simulation (e.g., docking + ADMET)
- Structured output in the form of a discovery report (Markdown or JSON)
- Local data lake folder structure with raw and processed content
- MVP1 checklist and architecture decisions documented

### ❌ Out of Scope:
- Continuous polling / orchestration
- Full UI/dashboard
- Multi-agent coordination or scoring logic
- Multi-tenant or RBAC features
- OpenMetadata, GROBID, or Airbyte integration

---

## ✅ MVP1 Success Checklist

| Area               | Requirement                                                  | Status |
|--------------------|--------------------------------------------------------------|--------|
| **Ingestion**       | At least 3 source pipelines implemented                     | ☐      |
| **Cataloging**      | Metadata stored in local DB or structured files             | ☐      |
| **Target Extraction** | Detect key viral targets (ICP0, LAT, UL39) from documents   | ☐      |
| **Simulation**       | One docking + ADMET simulation pipeline                     | ☐      |
| **Report Output**    | Structured scientific report generated (Markdown or JSON)  | ☐      |
| **MVP Checklist**    | MVP scope & status documented in repo                       | ✅     |

---

## 👥 MVP1 Review Process
- You (Project Lead) confirm all checklist items are met
- At least 1 external reviewer (scientific or technical) confirms report readability and value
- Milestone tagged in GitHub: `v0.1 – MVP1 Ready`

---

*This document will be archived and versioned once MVP1 is complete.*