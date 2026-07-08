#!/usr/bin/env bash
# Proactive ingestion pipeline for external sources.
# Run from project root: bash scripts/ingest_all_sources.sh
set -euo pipefail

cd "$(dirname "$0")/.."
source .venv/bin/activate
export PYTHONPATH=scripts

LOG_DIR=".staging/ingest_logs"
mkdir -p "$LOG_DIR"
LOG_FILE="$LOG_DIR/ingest_$(date +%Y%m%d_%H%M%S).log"

exec > >(tee -a "$LOG_FILE")
exec 2>&1

echo "=== Starting proactive source ingestion at $(date -Iseconds) ==="

# Unified ingestion pipeline (replaces ad-hoc import_* scripts).
python -m ingestion.pipeline --all

echo "--- Validation and dashboard refresh ---"
python scripts/validate_entries.py
PYTHONPATH=scripts python scripts/coverage_dashboard.py

echo "=== Finished proactive source ingestion at $(date -Iseconds) ==="
echo "Log saved to $LOG_FILE"
