# Load environment variables from .env file
include .env
export $(shell sed 's/=.*//' .env)

run:
	PYTHONPATH=. python3 orchestrator/runner.py