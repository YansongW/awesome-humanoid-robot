#!/usr/bin/env python3
"""Translate wiki/roadmap pages from Chinese to en/ko via DeepSeek.

Mirrors the zh source trees into per-language directories that the site
builder picks up:

    wiki/docs/**        -> wiki/docs-en/**, wiki/docs-ko/**
    roadmap/docs/**     -> roadmap/docs-en/**, roadmap/docs-ko/**

Long pages are translated in section-sized chunks and reassembled.
Idempotent/resumable: a page is re-translated only when its source sha1
changes or the mirror file is missing. Progress: .staging/wiki_translation_progress.jsonl

Usage:
    python scripts/translate_wiki_pages.py --limit 4        # pilot
    python scripts/translate_wiki_pages.py --lang ko        # one language
    python scripts/translate_wiki_pages.py --only roadmap   # one product
    python scripts/translate_wiki_pages.py                  # full run
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parent.parent
PROGRESS = ROOT / ".staging" / "wiki_translation_progress.jsonl"

API_URL = "https://api.deepseek.com/chat/completions"
API_KEY = os.environ.get("DEEPSEEK_API_KEY") or (
    Path.home() / "Desktop" / ".ai_credentials.txt"
).read_text(encoding="utf-8").split("DEEPSEEK_API_KEY=")[1].split("\n")[0].strip()

# source dir -> (mirror dir per lang)
PRODUCTS = {
    "wiki": {"src": ROOT / "wiki" / "docs", "en": ROOT / "wiki" / "docs-en", "ko": ROOT / "wiki" / "docs-ko"},
    "roadmap": {"src": ROOT / "roadmap" / "docs", "en": ROOT / "roadmap" / "docs-en", "ko": ROOT / "roadmap" / "docs-ko"},
}

CHUNK_TARGET = 4000  # chars per translation call
MAX_CJK_RATIO = {"en": 0.10, "ko": 0.35}  # ko keeps some hanja/terms

LANG_NAME = {"en": "English", "ko": "Korean"}

PROMPT = (
    "Translate the following Markdown document excerpt from Chinese to {lang}. "
    "Preserve ALL Markdown structure exactly: heading levels (translate the heading text), "
    "tables, lists, admonitions (!!! note blocks), code fences (do NOT translate code or commands), "
    "math ($...$, $$...$$, \\(...\\)), and links (keep URLs, file paths and .md targets unchanged; "
    "translate only the link text). Keep proper nouns, product/company names, entity ids (ent_...), "
    "and numbers with units. Do not add commentary. Output ONLY the translated Markdown."
)

_write_lock = threading.Lock()


def sha1(text: str) -> str:
    return hashlib.sha1(text.encode("utf-8")).hexdigest()


def cjk_ratio(text: str) -> float:
    cjk = sum(1 for c in text if "一" <= c <= "鿿")
    letters = sum(1 for c in text if c.isalpha())
    return cjk / letters if letters else 0.0


def split_chunks(text: str, target: int = CHUNK_TARGET) -> list[str]:
    """Split markdown into <=target-char chunks on heading/paragraph boundaries."""
    blocks = re.split(r"(?m)(?=^##\s)", text)  # keep delimiter with lookahead
    chunks: list[str] = []
    buf = ""
    for block in blocks:
        if not block:
            continue
        if len(buf) + len(block) <= target:
            buf += block
            continue
        if buf:
            chunks.append(buf)
            buf = ""
        if len(block) <= target:
            buf = block
            continue
        # oversize block: split on paragraph boundaries
        for para in re.split(r"(\n\n+)", block):
            if len(buf) + len(para) > target and buf:
                chunks.append(buf)
                buf = para
            else:
                buf += para
    if buf:
        chunks.append(buf)
    return [c for c in chunks if c.strip()]


def call_deepseek(system: str, content: str, retries: int = 3) -> str | None:
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    payload = {
        "model": "deepseek-chat",
        "messages": [{"role": "system", "content": system}, {"role": "user", "content": content}],
        "temperature": 0.2,
        "max_tokens": 8192,
    }
    for attempt in range(retries + 1):
        try:
            resp = requests.post(API_URL, headers=headers, json=payload, timeout=180)
            if resp.status_code != 200:
                raise RuntimeError(f"HTTP {resp.status_code}: {resp.text[:200]}")
            return resp.json()["choices"][0]["message"]["content"].strip()
        except Exception as exc:  # noqa: BLE001
            if attempt == retries:
                print(f"    API failed after {retries + 1} attempts: {exc}", file=sys.stderr)
                return None
            time.sleep(2 ** attempt * 3)
    return None


def translate_page(text: str, lang: str) -> str | None:
    """Translate a full page chunk by chunk; None on any chunk failure."""
    chunks = split_chunks(text)
    out: list[str] = []
    system = PROMPT.format(lang=LANG_NAME[lang])
    for i, chunk in enumerate(chunks):
        translated = call_deepseek(system, chunk)
        if translated is None:
            return None
        # strip accidental code fences wrapping the whole output
        translated = re.sub(r"\A```(?:markdown|md)?\n(.*)\n```\s*\Z", r"\1", translated, flags=re.S)
        if cjk_ratio(translated) > MAX_CJK_RATIO[lang]:
            retry = call_deepseek(system + " Your previous output contained untranslated Chinese; translate everything.", chunk)
            if retry is None:
                return None
            retry = re.sub(r"\A```(?:markdown|md)?\n(.*)\n```\s*\Z", r"\1", retry, flags=re.S)
            if cjk_ratio(retry) > MAX_CJK_RATIO[lang]:
                print(f"    chunk {i + 1}/{len(chunks)} still too CJK after retry", file=sys.stderr)
                return None
            translated = retry
        out.append(translated)
    return "\n\n".join(out).strip() + "\n"


def load_progress() -> dict[str, str]:
    """{(relpath|lang): source_sha1} of completed translations."""
    done: dict[str, str] = {}
    if PROGRESS.exists():
        for line in PROGRESS.read_text(encoding="utf-8").splitlines():
            try:
                rec = json.loads(line)
            except json.JSONDecodeError:
                continue
            done[f"{rec['path']}|{rec['lang']}"] = rec["sha1"]
    return done


def mark_done(relpath: str, lang: str, digest: str) -> None:
    with _write_lock:
        PROGRESS.parent.mkdir(parents=True, exist_ok=True)
        with PROGRESS.open("a", encoding="utf-8") as f:
            f.write(json.dumps({"path": relpath, "lang": lang, "sha1": digest,
                                "ts": datetime.now(timezone.utc).isoformat()}, ensure_ascii=False) + "\n")


def process_page(src_path: Path, src_root: Path, dst_root: Path, lang: str,
                 done: dict[str, str], stats: dict) -> None:
    rel = src_path.relative_to(src_root)
    key = f"{src_root.parent.name}/{rel}|{lang}"
    text = src_path.read_text(encoding="utf-8")
    digest = sha1(text)
    dst = dst_root / rel
    if done.get(key) == digest and dst.exists():
        stats["skipped"] += 1
        return
    translated = translate_page(text, lang)
    if translated is None:
        stats["failed"] += 1
        print(f"  FAILED {lang}: {rel}", file=sys.stderr)
        return
    with _write_lock:
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_text(translated, encoding="utf-8")
    mark_done(f"{src_root.parent.name}/{rel}", lang, digest)
    stats["translated"] += 1
    print(f"  {lang}: {rel} ({len(text)} -> {len(translated)} chars)")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--lang", choices=["en", "ko"], help="only one language")
    ap.add_argument("--only", choices=list(PRODUCTS), help="only one product tree")
    ap.add_argument("--limit", type=int, default=0, help="max pages per language (pilot)")
    ap.add_argument("--workers", type=int, default=6)
    args = ap.parse_args()

    langs = [args.lang] if args.lang else ["en", "ko"]
    done = load_progress()
    stats = {"translated": 0, "skipped": 0, "failed": 0}

    tasks = []
    for product, dirs in PRODUCTS.items():
        if args.only and product != args.only:
            continue
        src_root: Path = dirs["src"]
        pages = sorted(
            p for p in src_root.rglob("*.md")
            if "kg/relationships" not in p.as_posix() and "kg/entities" not in p.as_posix()
        )
        for lang in langs:
            dst_root: Path = dirs[lang]
            selected = pages[: args.limit] if args.limit else pages
            for p in selected:
                tasks.append((p, src_root, dst_root, lang))

    print(f"{len(tasks)} page-language tasks (workers={args.workers})")
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {
            pool.submit(process_page, p, src_root, dst_root, lang, done, stats): (p, lang)
            for p, src_root, dst_root, lang in tasks
        }
        for fut in as_completed(futures):
            fut.result()

    print(f"done: translated={stats['translated']} skipped={stats['skipped']} failed={stats['failed']}")
    if stats["failed"]:
        sys.exit(1)


if __name__ == "__main__":
    main()
