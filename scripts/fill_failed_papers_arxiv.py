#!/usr/bin/env python3
"""Try to fill the remaining empty paper entries by searching arXiv title variants."""

from __future__ import annotations

import json
import re
import sys
import time
import urllib.parse
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any

import requests
import yaml

ROOT = Path(__file__).parent.parent
PAPERS_DIR = ROOT / "research" / "papers"
REPORT_PATH = ROOT / ".staging" / "abstract_backfill_report.json"
RESULTS_PATH = ROOT / ".staging" / "arxiv_title_search_results.json"


def arxiv_search(title: str) -> dict[str, str] | None:
    q = urllib.parse.quote(f'ti:"{title}"')
    url = f"http://export.arxiv.org/api/query?search_query={q}&start=0&max_results=3"
    try:
        r = requests.get(url, timeout=20)
        r.raise_for_status()
    except Exception:
        return None
    root = ET.fromstring(r.text)
    ns = {"atom": "http://www.w3.org/2005/Atom"}
    for entry in root.findall("atom:entry", ns):
        t = entry.findtext("atom:title", "", ns).replace("\n", " ").strip()
        s = entry.findtext("atom:summary", "", ns).replace("\n", " ").strip()
        id_url = entry.findtext("atom:id", "", ns).strip()
        if t and s:
            return {"title": t, "abstract": s, "source": id_url}
    return None


def variants(title: str) -> list[str]:
    vs = [title]
    if ":" in title:
        vs.append(title.split(":", 1)[1].strip())
        vs.append(title.split(":", 1)[0].strip())
    vs.append(re.sub(r"\s*\([^)]*\)\s*$", "", title).strip())
    return list(dict.fromkeys(v for v in vs if v))


def main() -> int:
    report = json.loads(REPORT_PATH.read_text(encoding="utf-8"))
    failed_ids = [x["id"] for x in report.get("failed_ids", [])]

    out: list[dict[str, Any]] = []
    for eid in failed_ids:
        p = PAPERS_DIR / f"{eid}.md"
        if not p.exists():
            continue
        fm = yaml.safe_load(p.read_text(encoding="utf-8").split("---", 2)[1])
        title = fm.get("names", {}).get("en", "")
        res = None
        used_variant = ""
        for v in variants(title):
            res = arxiv_search(v)
            if res:
                used_variant = v
                break
            time.sleep(3)
        out.append(
            {
                "id": eid,
                "title": title,
                "found": bool(res),
                "variant": used_variant,
                "result": res,
            }
        )
        if res:
            print(f"FOUND {eid}: {res['title'][:80]}")
        else:
            print(f"MISS {eid}")

    RESULTS_PATH.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Done. Found {sum(1 for x in out if x['found'])}/{len(out)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
