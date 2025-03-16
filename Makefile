.PHONY: init run test

init:
	python3 -m venv venv
	. venv/bin/activate && pip install -r requirements.txt

run:
	set -a && . .env && set -a && PYTHONPATH=. python3 orchestrator/runner.py

test:
	PYTHONPATH=. python3 -m unittest discover tests