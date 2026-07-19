#!/usr/bin/env python3
"""Repair notes lines corrupted by an ad-hoc downgrade append on 2026-07-17.

An earlier session appended ` [downgraded to low on 2026-07-17: hedged LLM evidence]`
AFTER the closing quote of single-quoted YAML notes values, producing invalid
frontmatter like:

    notes: 'Evidence: ...' [downgraded to low on 2026-07-17: hedged LLM evidence]

These files were silently skipped by the audit (unparseable frontmatter).
This script moves the bracket note INSIDE the quotes and validates every
repair with a yaml.safe_load round-trip (AGENTS.md rule 4).

Usage:
    python scripts/fix_notes_downgrade_quote.py            # dry-run
    python scripts/fix_notes_downgrade_quote.py --write
"""
from __future__ import annotations

import argparse
import json
import re
from datetime import date
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
MARKER = "[downgraded to low on 2026-07-17: hedged LLM evidence]"
PATTERN = re.compile(
    r"^(?P<prefix>\s*notes:\s*)'(?P<body>.*)'\s*" + re.escape(MARKER) + r"\s*$",
    re.M,
)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()

    fixed: list[str] = []
    failed: list[dict[str, str]] = []

    for path in sorted((ROOT / "data" / "relationships").rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        if MARKER not in text:
            continue
        m = PATTERN.search(text)
        if not m:
            failed.append({"path": str(path), "error": "marker present but pattern not matched"})
            continue

        def _repl(match: re.Match[str]) -> str:
            return f"{match.group('prefix')}'{match.group('body')} {MARKER}'"

        new_text = PATTERN.sub(_repl, text, count=1)

        # round-trip validation: frontmatter must parse and keep the marker
        fm_match = re.match(r"\A---\n(.*?)\n---\n", new_text, re.S)
        try:
            fm = yaml.safe_load(fm_match.group(1)) if fm_match else None
        except yaml.YAMLError as exc:  # noqa: BLE001
            failed.append({"path": str(path), "error": f"yaml parse failed after repair: {exc}"})
            continue
        notes = ((fm or {}).get("verification") or {}).get("notes", "")
        if MARKER not in notes:
            failed.append({"path": str(path), "error": "marker missing from parsed notes after repair"})
            continue

        if args.write:
            path.write_text(new_text, encoding="utf-8")
        fixed.append(str(path.relative_to(ROOT)))

    manifest = {
        "date": date.today().isoformat(),
        "script": "scripts/fix_notes_downgrade_quote.py",
        "mode": "write" if args.write else "dry-run",
        "fixed_count": len(fixed),
        "failed_count": len(failed),
        "fixed": fixed,
        "failed": failed,
    }
    out = ROOT / ".staging" / f"fix_notes_quote_manifest_{date.today().isoformat()}.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"{'repaired' if args.write else 'would repair'}: {len(fixed)} files; failed: {len(failed)}")
    for f in failed[:10]:
        print(" FAILED:", f["path"], "->", f["error"])
    print(f"manifest: {out}")


if __name__ == "__main__":
    main()
