.PHONY: init run test ingest precommit

init:
	python3 -m venv venv
	. venv/bin/activate && pip install -r requirements.txt

precommit:
	pip install pre-commit
	pre-commit install --hook-type commit-msg

run:
	set -a && . .env && set -a && PYTHONPATH=. python3 orchestrator/runner.py

test:
	export SONNET_API_KEY=dummy_key; \
	export PYTHONPATH=.; \
	python3 -m unittest discover tests

ingest:
	. venv/bin/activate && PYTHONPATH=. python3 knowledge_base/ingestion/orchestrators/orchestrator.py