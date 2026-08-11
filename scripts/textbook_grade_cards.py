#!/usr/bin/env python3
"""textbook_grade_cards.py — textbook-grade upgrade pipeline for non-paper cards.

Consolidated from .staging/textbook_grade (pilot + B1 batch, 26 cards applied).
Scope: non-paper cards (method/component/technology/concept/oem/software/...)
whose bodies are template filler. Unlike deep_read_cards.py, the zh body text
itself is written by the agent (judgment work); this script automates
everything around it:

  select   rank candidate cards of one type by graph degree, skip upgraded
  fetch    rate-limited (UA, 3s) download of per-card first-hand sources
           (URLs come from the targets file; HTML is stripped to text)
  corpus   build a default corpus map (wiki chapters by keyword + one-hop
           neighbor cards) for the number whitelist audit
  audit    number whitelist: every number in a body fragment must appear in
           the corpus (delegates to scripts/audit_card_numbers.py)
  apply    swap in the new zh body (frontmatter untouched except an appended
           verification.notes line, asserted; yaml round-trip; backup first;
           idempotent via notes marker); old en/ko sections are dropped
  translate  rebuild en/ko via scripts/translate_entry_bodies.py on these
           cards only (never a repo-wide run)
  check    schema-validate all target cards

Body fragments are expected at <workdir>/bodies/<id>.zh.md with exactly one
each of '## 概述', '## 核心内容', '## 参考'.

State lives in .staging/textbook_grade_run/ (gitignored) unless --workdir is
given. All stages are checkpointed and safe to re-run.

Usage:
  python scripts/textbook_grade_cards.py select --type method --top 50
  python scripts/textbook_grade_cards.py fetch   # after adding urls to targets.json
  python scripts/textbook_grade_cards.py corpus --chapters chapter-18 chapter-19
  python scripts/textbook_grade_cards.py audit
  python scripts/textbook_grade_cards.py apply
  python scripts/textbook_grade_cards.py translate
  python scripts/textbook_grade_cards.py check
"""
from __future__ import annotations

import argparse
import html as H
import json
import re
import shutil
import subprocess
import sys
import threading
import time
from collections import Counter, defaultdict
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
STATE = ROOT / ".staging" / "textbook_grade_run"
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 awesome-humanoid-robot-textbook/1.0")
NOTE_MARKER = "textbook-grade"

_lock = threading.Lock()


# ---------------------------------------------------------------------- helpers
def split_file(text: str):
    assert text.startswith("---\n"), "no frontmatter"
    _, rest = text.split("---\n", 1)
    yaml_text, body = rest.split("\n---\n", 1)
    return yaml.safe_load(yaml_text), body


def load_degrees() -> Counter:
    deg = Counter()
    for f in ROOT.glob("data/relationships/*.md"):
        txt = f.read_text(encoding="utf-8", errors="ignore")
        s = re.search(r"source:\s*\n\s+id:\s*(\S+)", txt)
        t = re.search(r"target:\s*\n\s+id:\s*(\S+)", txt)
        if s:
            deg[s.group(1)] += 1
        if t:
            deg[t.group(1)] += 1
    return deg


def one_hop_neighbors(card_id: str) -> list:
    out = set()
    for f in ROOT.glob("data/relationships/*.md"):
        txt = f.read_text(encoding="utf-8", errors="ignore")
        s = re.search(r"source:\s*\n\s+id:\s*(\S+)", txt)
        t = re.search(r"target:\s*\n\s+id:\s*(\S+)", txt)
        if not (s and t):
            continue
        if s.group(1) == card_id:
            out.add(t.group(1))
        elif t.group(1) == card_id:
            out.add(s.group(1))
    return sorted(out)


def find_card_file(card_id: str) -> Path | None:
    hits = list(ROOT.glob(f"research/**/{card_id}.md"))
    return hits[0] if hits else None


def extract_html(raw: str) -> str:
    raw = re.sub(r"<(script|style|nav|header|footer)[^>]*>.*?</\1>", " ", raw, flags=re.S | re.I)
    raw = re.sub(r"</(tr|p|div|section|h[1-6]|li|table|caption|figure)>", "\n", raw, flags=re.I)
    raw = re.sub(r"</t[dh]>", " | ", raw, flags=re.I)
    text = re.sub(r"<[^>]+>", " ", raw)
    text = H.unescape(text)
    text = re.sub(r"[ \t]+", " ", text)
    return re.sub(r"\n\s*\n+", "\n\n", text).strip()


def workdir(args) -> Path:
    d = Path(args.workdir) if args.workdir else STATE
    d.mkdir(parents=True, exist_ok=True)
    return d


def load_targets(args):
    return json.loads((workdir(args) / "targets.json").read_text(encoding="utf-8"))


# ------------------------------------------------------------------ select
def stage_select(args) -> int:
    deg = load_degrees()
    cands = []
    for p in sorted(ROOT.glob("research/**/*.md")):
        text = p.read_text(encoding="utf-8", errors="ignore")
        try:
            fm = yaml.safe_load(text.split("---", 2)[1])
        except Exception:
            continue
        if not fm or fm.get("type") != args.type:
            continue
        notes = (fm.get("verification") or {}).get("notes") or ""
        if NOTE_MARKER in notes:
            continue  # already upgraded
        if "## 它改变了什么" in text:
            continue  # deep-read style already
        cands.append((deg.get(fm["$id"], 0), fm["$id"]))
    cands.sort(reverse=True)
    top = cands[: args.top] if args.top else cands
    targets = [{"id": cid, "degree": d, "urls": {}} for d, cid in top]
    (workdir(args) / "targets.json").write_text(json.dumps(targets, ensure_ascii=False, indent=1),
                                                encoding="utf-8")
    print(f"select: type={args.type} -> {len(targets)} targets "
          f"(degree {top[-1][0]}..{top[0][0] if top else 0}) -> {workdir(args)/'targets.json'}")
    print("next: add per-card source URLs to targets.json, then run `fetch`.")
    return 0


# ------------------------------------------------------------------ fetch
def fetch_url(url: str, out: Path, min_size: int = 1500) -> bool:
    r = subprocess.run(["curl", "-sL", "--max-time", "60", "-A", UA,
                        "-w", "%{http_code}", "-o", str(out), url],
                       capture_output=True, text=True)
    code = (r.stdout or "").strip()[-3:]
    return code == "200" and out.exists() and out.stat().st_size > min_size


def stage_fetch(args) -> int:
    targets = load_targets(args)
    stats = Counter()
    for t in targets:
        urls = t.get("urls") or {}
        if not urls:  # default: fetch the card's own declared sources
            card = find_card_file(t["id"])
            if card:
                fm, _ = split_file(card.read_text(encoding="utf-8", errors="ignore"))
                for i, s in enumerate(fm.get("sources") or []):
                    if (s.get("url") or "").startswith("http"):
                        urls[f"card_source_{i+1}"] = s["url"]
        d = workdir(args) / "sources" / t["id"]
        d.mkdir(parents=True, exist_ok=True)
        for slug, url in urls.items():
            txt = d / f"{slug}.txt"
            if txt.exists() and txt.stat().st_size > 500:
                stats["cached"] += 1
                continue
            raw = d / f"{slug}.html"
            if fetch_url(url, raw):
                if url.endswith(".md"):
                    raw.rename(txt)
                else:
                    txt.write_text(extract_html(raw.read_text(encoding="utf-8", errors="ignore")),
                                   encoding="utf-8")
                    raw.unlink(missing_ok=True)
                stats["ok"] += 1
            else:
                raw.unlink(missing_ok=True)
                stats["fail"] += 1
                print(f"  fetch FAIL {t['id']}/{slug} {url}", flush=True)
            time.sleep(3)
    print(f"fetch DONE: {dict(stats)}")
    return 0


# ------------------------------------------------------------------ corpus
def stage_corpus(args) -> int:
    targets = load_targets(args)
    chapters = [f"wiki/docs/chapters/{c}.md" if not c.endswith(".md") else c for c in args.chapters]
    mapping = {}
    for t in targets:
        files = list(chapters)
        card = find_card_file(t["id"])
        if card:
            files.append(str(card.relative_to(ROOT)))
        for nb in one_hop_neighbors(t["id"])[: args.neighbors]:
            p = find_card_file(nb)
            if p:
                files.append(str(p.relative_to(ROOT)))
        mapping[t["id"]] = files
    out = workdir(args) / "corpus_map.json"
    out.write_text(json.dumps(mapping, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"corpus map -> {out} ({len(mapping)} cards, {len(chapters)} chapters + neighbors)")
    return 0


# ------------------------------------------------------------------ audit
def stage_audit(args) -> int:
    cmd = [sys.executable, str(ROOT / "scripts" / "audit_card_numbers.py"), "whitelist",
           "--bodies-dir", str(workdir(args) / "bodies"),
           "--corpus-map", str(workdir(args) / "corpus_map.json"),
           "--sources-dir", str(workdir(args) / "sources")]
    r = subprocess.run(cmd)
    return r.returncode


# ------------------------------------------------------------------ apply
def stage_apply(args) -> int:
    targets = load_targets(args)
    bodies = workdir(args) / "bodies"
    backup = workdir(args) / "backup"
    backup.mkdir(exist_ok=True)
    done = skipped = 0
    note = (f" [{args.date}] body upgraded to textbook-grade ({workdir(args).relative_to(ROOT)}): "
            f"zh 概述/核心内容/参考 rewritten from card + graph neighbors + wiki chapters + "
            f"first-hand sources (number whitelist audit passed); "
            f"en/ko sections to be regenerated by translate pipeline.")
    for t in targets:
        cid = t["id"]
        frag_path = bodies / f"{cid}.zh.md"
        if not frag_path.exists():
            print(f"  no fragment for {cid}, skipped")
            continue
        frag = frag_path.read_text(encoding="utf-8").strip()
        path = find_card_file(cid)
        if not path:
            print(f"  card file missing for {cid}, skipped")
            continue
        text = path.read_text(encoding="utf-8")
        fm, body = split_file(text)
        notes = (fm.get("verification") or {}).get("notes") or ""
        if NOTE_MARKER in notes:
            skipped += 1
            continue
        orig = yaml.safe_load(yaml.safe_dump(fm))
        for h in ("## 概述", "## 核心内容", "## 参考"):
            assert frag.count(h) == 1, f"{cid}: fragment heading {h} count != 1"
        fm.setdefault("verification", {})["notes"] = (notes + " " + note).strip()
        a, b = dict(orig), yaml.safe_load(yaml.safe_dump(fm))
        a.pop("verification")
        b.pop("verification")
        assert a == b, f"{cid}: frontmatter fields other than verification.notes changed"
        new_body = frag + "\n"
        out = ("---\n" + yaml.safe_dump(fm, allow_unicode=True, sort_keys=False, width=120)
               + "---\n" + new_body)
        fm2, body2 = split_file(out)
        assert fm2 == fm and body2.startswith("## 概述"), cid
        shutil.copy2(path, backup / path.name)
        path.write_text(out, encoding="utf-8")
        done += 1
        print(f"  applied {cid} ({len(new_body)} chars)")
    print(f"apply DONE: applied={done} skipped={skipped}")
    return 0


# ------------------------------------------------------------------ translate
def stage_translate(args) -> int:
    sys.path.insert(0, str(ROOT / "scripts"))
    import translate_entry_bodies as teb
    stats = {"files": 0, "ok_en": 0, "ok_ko": 0, "skip_en": 0, "skip_ko": 0, "fail_en": 0, "fail_ko": 0}
    lock = threading.Lock()
    for t in load_targets(args):
        p = find_card_file(t["id"])
        if p:
            teb.process(p, ["en", "ko"], lock, stats)
            print(t["id"], dict(stats), flush=True)
    print(f"translate FINAL {stats}")
    return 0 if stats["fail_en"] == 0 and stats["fail_ko"] == 0 else 1


# ------------------------------------------------------------------ check
def stage_check(args) -> int:
    from jsonschema import Draft7Validator
    schema = json.loads((ROOT / "data/schema/v1/entry_schema.json").read_text(encoding="utf-8"))
    validator = Draft7Validator(schema)
    bad = []
    for t in load_targets(args):
        p = find_card_file(t["id"])
        if not p:
            bad.append((t["id"], "file missing"))
            continue
        fm, body = split_file(p.read_text(encoding="utf-8"))
        errs = list(validator.iter_errors(fm))
        if errs:
            bad.append((t["id"], errs[0].message[:80]))
            continue
        heads = re.findall(r"^## .+", body, re.M)
        if not any(h.startswith("## Overview") for h in heads):
            bad.append((t["id"], "no en section"))
        if not any(h.startswith("## 개요") for h in heads):
            bad.append((t["id"], "no ko section"))
        ko = body.split("## 개요")[-1]
        for line in ko.splitlines():
            if "](" in line and not re.search(r"\[[^\]]*\]\([^)]*\)", line):
                bad.append((t["id"], "ko `](` adjacency"))
                break
    n = len(load_targets(args))
    print(f"check: {n - len(bad)}/{n} ok; issues={bad[:10]}")
    return 0 if not bad else 1


# ------------------------------------------------------------------ main
def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("stage", choices=["select", "fetch", "corpus", "audit", "apply", "translate", "check"])
    ap.add_argument("--workdir", help=f"state dir (default {STATE})")
    ap.add_argument("--type", default="method", help="card type for select")
    ap.add_argument("--top", type=int, default=50)
    ap.add_argument("--chapters", nargs="*", default=[], help="wiki chapters for corpus map, e.g. chapter-18")
    ap.add_argument("--neighbors", type=int, default=6, help="one-hop neighbor cards per card in corpus map")
    ap.add_argument("--date", default=time.strftime("%Y-%m-%d"))
    args = ap.parse_args()
    return {"select": stage_select, "fetch": stage_fetch, "corpus": stage_corpus,
            "audit": stage_audit, "apply": stage_apply, "translate": stage_translate,
            "check": stage_check}[args.stage](args)


if __name__ == "__main__":
    sys.exit(main())
