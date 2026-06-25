# Awesome Humanoid Robot — Standardized development commands
#
# This Makefile wraps the AI4Sci pipeline scripts so contributors and automation
# can interact with the project through a small, stable set of commands.

PYTHON := python3
VENV := .venv
PIP := $(VENV)/bin/pip
PY := $(VENV)/bin/python

# Default target
.PHONY: help
help:
	@echo "Awesome Humanoid Robot — available commands"
	@echo ""
	@echo "  make setup              Create venv and install dependencies"
	@echo "  make validate           Validate production entries and relationships"
	@echo "  make validate-all       Validate production + all staged workstream outputs"
	@echo "  make status             Show pending reviews and workstream progress"
	@echo "  make review             Interactive review of staged drafts"
	@echo "  make run-next           Run the next unexecuted workstream (conservative)"
	@echo "  make run-workstream W=definition/algorithm_survey/vla  Run a specific workstream config"
	@echo "  make orchestrate        Run all workstreams via the orchestrator"
	@echo "  make clean-staging      Remove all .staging/ outputs (use with caution)"
	@echo ""
	@echo "Set AI4SCI_API_KEY / AI4SCI_USE_KIMI_CLI before running workstreams."

.PHONY: setup
setup:
	$(PYTHON) -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -r scripts/requirements.txt
	@echo "Setup complete. Activate with: source $(VENV)/bin/activate"

.PHONY: validate
validate:
	$(PY) scripts/validate_entries.py

.PHONY: validate-all
validate-all:
	$(PY) scripts/validate_entries.py --include-workstreams

.PHONY: status
status:
	$(PY) scripts/ai4sci_status.py

.PHONY: review
review:
	$(PY) scripts/ai4sci_review.py

.PHONY: run-next
run-next:
	$(PY) scripts/ai4sci_run_next_workstream.py --max-papers 3 --max-workers 1

.PHONY: run-workstream
run-workstream:
	@if [ -z "$(W)" ]; then echo "Usage: make run-workstream W=<path_without_extension>"; exit 1; fi
	$(PY) scripts/ai4sci_batch_pipeline.py scripts/ai4sci_workstreams/$(W).yaml --max-papers 5 --max-workers 2

.PHONY: orchestrate
orchestrate:
	$(PY) scripts/ai4sci_orchestrator.py --max-workers 2 --max-batch-workers 1 --max-papers 5

.PHONY: clean-staging
clean-staging:
	@read -p "This will delete all staged outputs in .staging/. Are you sure? [y/N] " ans && [ "$$ans" = "y" ] && rm -rf .staging/*
