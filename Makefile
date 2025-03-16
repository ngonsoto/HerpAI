export $(shell grep -v '^#' .env | xargs)
run:
	PYTHONPATH=. python3 orchestrator/runner.py