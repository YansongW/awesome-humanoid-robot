#!/usr/bin/env bash
# Proactive ingestion pipeline for external sources.
# Run from project root: bash scripts/ingest_all_sources.sh
set -uo pipefail

cd "$(dirname "$0")/.."
source .venv/bin/activate
export PYTHONPATH=scripts

LOG_DIR=".staging/ingest_logs"
mkdir -p "$LOG_DIR"
LOG_FILE="$LOG_DIR/ingest_$(date +%Y%m%d_%H%M%S).log"
JSON_FILE="$LOG_DIR/ingest_$(date +%Y%m%d_%H%M%S).json"

exec > >(tee -a "$LOG_FILE")
exec 2>&1

echo "=== Starting proactive source ingestion at $(date -Iseconds) ==="

# Unified ingestion pipeline with per-source timeout and JSON summary.
python -m ingestion.pipeline --all --json --summary --timeout 120 | tee "$JSON_FILE"
PIPELINE_EXIT=${PIPESTATUS[0]}

echo ""
echo "--- Ingestion summary ---"
python3 - "$JSON_FILE" <<'PY'
import json, os, sys
path = sys.argv[1]
if not os.path.exists(path):
    print("No JSON summary found.")
    sys.exit(0)
data = json.load(open(path))
total_added = 0
total_dup = 0
total_err = 0
total_skip = 0
errors = []
for sid, payload in data.items():
    summary = payload.get("summary", {})
    total_added += summary.get("added", 0)
    total_dup += summary.get("duplicate", 0)
    total_err += summary.get("error", 0)
    total_skip += summary.get("skipped", 0)
    for item in payload.get("items", []):
        if item["status"] == "error":
            errors.append((sid, item.get("title", ""), item.get("message", "")[:120]))
print(f"Total added: {total_added}")
print(f"Total duplicates: {total_dup}")
print(f"Total errors: {total_err}")
print(f"Total skipped: {total_skip}")
if errors:
    print("\nError samples:")
    for sid, title, msg in errors[:20]:
        print(f"  {sid}: {title} -> {msg}")
PY

if [ "$PIPELINE_EXIT" -eq 0 ]; then
    echo "--- Validation and dashboard refresh ---"
    python scripts/validate_entries.py || true
    PYTHONPATH=scripts python scripts/coverage_dashboard.py || true
else
    echo "--- Pipeline exited with code $PIPELINE_EXIT; skipping validation/dashboard ---"
fi

echo "=== Finished proactive source ingestion at $(date -Iseconds) ==="
echo "Log saved to $LOG_FILE"
echo "JSON summary saved to $JSON_FILE"
