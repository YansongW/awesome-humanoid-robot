#!/usr/bin/env python3
"""Backfill missing verification.confidence on legacy workflow relationships.

Adds ONLY `confidence: medium` and a traceable `notes` line to relationship
files whose verification block lacks confidence. Nothing else is touched.

Usage:
    python scripts/backfill_rel_confidence.py            # dry-run
    python scripts/backfill_rel_confidence.py --write
"""
from __future__ import annotations

import argparse
import re
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TODAY = date.today().isoformat()
NOTE = f"bulk-added confidence on {TODAY} by backfill_rel_confidence.py; pending human review"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()

    changed = 0
    for path in sorted((ROOT / "data" / "relationships").rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        m = re.match(r"\A---\n(.*?)\n---\n(.*)\Z", text, re.S)
        if not m:
            continue
        fm = m.group(1)
        if "verification:" not in fm:
            continue
        ver = fm.split("verification:", 1)[1]
        if re.search(r"^\s{2}confidence:", ver, re.M):
            continue
        # insert confidence + notes right after the verification: line
        insertion = f"verification:\n  confidence: medium\n  notes: {NOTE}"
        new_text = text.replace("verification:\n", insertion + "\n", 1)
        if args.write:
            path.write_text(new_text, encoding="utf-8")
        changed += 1

    print(f"{'backfilled' if args.write else 'would backfill'}: {changed} relationship files")


if __name__ == "__main__":
    main()
