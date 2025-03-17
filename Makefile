.PHONY: init run test

init:
	python3 -m venv venv
	. venv/bin/activate && pip install -r requirements.txt

run:
	set -a && . .env && set -a && PYTHONPATH=. python3 orchestrator/runner.py

test:
	export SONNET_API_KEY=dummy_key; \
	export PYTHONPATH=.; \
	python3 -m unittest discover tests

ingest_pubmed:
	. venv/bin/activate && PYTHONPATH=. python3 knowledge_base/ingestion/run_pubmed_ingestion.py

ingest_europe_pmc:
	. venv/bin/activate && PYTHONPATH=. python3 knowledge_base/ingestion/run_europe_pmc_ingestion.py

ingest: ingest_pubmed ingest_europe_pmc