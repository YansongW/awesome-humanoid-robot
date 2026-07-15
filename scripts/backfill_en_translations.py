#!/usr/bin/env python3
"""
Machine-translate missing English names and summaries from Chinese fields.

Uses the `translators` library with the Alibaba engine (which is reachable in
this environment) and caches results to avoid repeated translation of identical
text.  All generated fields are marked with a verification note so reviewers
know they are AI-translated and may need refinement.

Usage:
    python scripts/backfill_en_translations.py [--dry-run]
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path
from typing import Any

import yaml

try:
    import translators as ts
except ImportError as exc:  # pragma: no cover
    print(f"ERROR: translators package not installed: {exc}", file=sys.stderr)
    sys.exit(1)

ROOT = Path(__file__).resolve().parent.parent
RESEARCH_DIR = ROOT / "research"
CACHE_PATH = ROOT / ".staging" / "en_translation_cache.json"
TRANSLATORS = ["caiyun", "lingvanex"]
SRC_LANG = "zh"
TARGET_LANG = "en"
DELAY_SECONDS = 0.2


def split_fm(text: str) -> tuple[dict[str, Any] | None, str]:
    if not text.startswith("---"):
        return None, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None, text
    try:
        fm = yaml.safe_load(parts[1]) or {}
    except Exception:
        return None, text
    return fm, parts[2]


def load_cache() -> dict[str, str]:
    if not CACHE_PATH.exists():
        return {}
    try:
        return json.loads(CACHE_PATH.read_text(encoding="utf-8"))
    except Exception:
        return {}


def save_cache(cache: dict[str, str]) -> None:
    CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
    CACHE_PATH.write_text(json.dumps(cache, ensure_ascii=False, indent=2), encoding="utf-8")


def translate(text: str, cache: dict[str, str], flush_every: int = 50) -> str:
    text = text.strip()
    if not text:
        return ""
    if text in cache:
        return cache[text]
    last_exc = None
    for engine in TRANSLATORS:
        try:
            result = ts.translate_text(
                text,
                translator=engine,
                from_language=SRC_LANG,
                to_language=TARGET_LANG,
            )
            result = result.strip()
            if result:
                cache[text] = result
                if len(cache) % flush_every == 0:
                    save_cache(cache)
                time.sleep(DELAY_SECONDS)
                return result
        except Exception as exc:
            last_exc = exc
            continue
    print(f"  Translation failed for '{text[:40]}...': {last_exc}", file=sys.stderr)
    return ""


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    cache = load_cache()
    updated = 0
    skipped = 0
    failed = 0

    for p in sorted(RESEARCH_DIR.rglob("*.md")):
        text = p.read_text(encoding="utf-8")
        fm, body = split_fm(text)
        if fm is None:
            continue

        names = fm.get("names", {}) or {}
        summary = fm.get("summary", {}) or {}
        if not isinstance(names, dict):
            names = {}
        if not isinstance(summary, dict):
            summary = {}

        zh_name = names.get("zh", "").strip()
        zh_summary = summary.get("zh", "").strip()
        changed = False

        if not names.get("en") and zh_name:
            en_name = translate(zh_name, cache)
            if en_name:
                fm.setdefault("names", {})
                fm["names"]["en"] = en_name
                changed = True
            else:
                failed += 1

        if not summary.get("en") and zh_summary:
            en_summary = translate(zh_summary, cache)
            if en_summary:
                fm.setdefault("summary", {})
                fm["summary"]["en"] = en_summary
                changed = True
            else:
                failed += 1

        if not changed:
            skipped += 1
            continue

        # Update verification note
        fm["verification"] = fm.get("verification", {}) or {}
        note = fm["verification"].get("notes", "")
        marker = "English name/summary machine-translated from Chinese by scripts/backfill_en_translations.py."
        if marker not in note:
            fm["verification"]["notes"] = (note + " " + marker).strip()
        fm["verification"]["reviewed_at"] = fm["verification"].get("reviewed_at") or "2026-07-15"

        if args.dry_run:
            print(f"DRY-RUN {fm.get('$id', p.stem)}: en_name={'yes' if 'en' in (fm.get('names') or {}) else 'no'}, en_summary={'yes' if 'en' in (fm.get('summary') or {}) else 'no'}")
            updated += 1
            continue

        new_yaml = yaml.safe_dump(fm, allow_unicode=True, sort_keys=False, width=120, default_flow_style=False)
        p.write_text(f"---\n{new_yaml}---\n{body}\n", encoding="utf-8")
        updated += 1
        print(f"UPDATED {fm.get('$id', p.stem)}")

    save_cache(cache)
    print(f"\nUpdated {updated} entries; skipped {skipped}; translation failures {failed}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
