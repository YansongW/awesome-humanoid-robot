#!/usr/bin/env python3
"""Translate entry bodies (概述/核心内容) from Chinese to en/ko via DeepSeek.

Appends `## Overview`/`## Content` (en) or `## 개요`/`## 핵심 내용` (ko) sections
to research/*.md bodies. Idempotent: skips entries whose target-language body
already has >=100 chars. Checkpoints by writing each file immediately.

Usage:
    python scripts/translate_entry_bodies.py --limit 20        # pilot
    python scripts/translate_entry_bodies.py                   # full run
    python scripts/translate_entry_bodies.py --lang ko --workers 4
"""
from __future__ import annotations

import argparse
import os
import re
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import requests
import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "website"))
from builder.loader import filter_body_by_language  # noqa: E402

API_URL = "https://api.deepseek.com/chat/completions"
API_KEY = os.environ.get("DEEPSEEK_API_KEY") or (
    Path.home() / "Desktop" / ".ai_credentials.txt"
).read_text(encoding="utf-8").split("DEEPSEEK_API_KEY=")[1].split("\n")[0].strip()

MAX_SOURCE_CHARS = 7000

PROMPTS = {
    "en": (
        "Translate the following Markdown from Chinese to English. "
        "Preserve Markdown structure: headings, bold, lists, links, math notation "
        "(\\(...\\), $$...$$), and code. Keep proper nouns, model names, and arXiv IDs. "
        "Translate the heading '## 概述' as '## Overview' and '## 核心内容' as '## Content'. "
        "Output ONLY the translated Markdown, no commentary."
    ),
    "ko": (
        "Translate the following Markdown from Chinese to Korean. "
        "Preserve Markdown structure: headings, bold, lists, links, math notation "
        "(\\(...\\), $$...$$), and code. Keep proper nouns, model names, and arXiv IDs. "
        "Translate the heading '## 概述' as '## 개요' and '## 核心内容' as '## 핵심 내용'. "
        "Output ONLY the translated Markdown, no commentary."
    ),
}

MIN_CJK_RATIO_RETRY = {"en": 0.05, "ko": 0.30}  # ko keeps some hanja/terms


def zh_source_body(body: str) -> str:
    """Extract the Chinese body (概述/核心内容 etc., minus 参考) for translation."""
    zh = filter_body_by_language(body, "zh")
    # Drop the 参考 section: URLs need no translation and the template shows sources.
    zh = re.split(r"(?m)^##\s*参考\s*$", zh)[0].rstrip()
    if len(zh) > MAX_SOURCE_CHARS:
        cut = zh[:MAX_SOURCE_CHARS]
        # truncate at a paragraph boundary
        para = cut.rfind("\n\n")
        zh = cut[:para] if para > MAX_SOURCE_CHARS // 2 else cut
    return zh.strip()


def call_deepseek(prompt: str, content: str, retries: int = 2) -> str | None:
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    payload = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "system", "content": prompt},
            {"role": "user", "content": content},
        ],
        "temperature": 0.2,
    }
    for attempt in range(retries + 1):
        try:
            resp = requests.post(API_URL, headers=headers, json=payload, timeout=120)
            if resp.status_code != 200:
                time.sleep(2 * (attempt + 1))
                continue
            data = resp.json()
            return data["choices"][0]["message"]["content"].strip()
        except Exception:
            time.sleep(2 * (attempt + 1))
    return None


def cjk_ratio(text: str) -> float:
    if not text:
        return 0.0
    return sum(1 for c in text if "一" <= c <= "鿿") / len(text)


def translate_for_lang(zh_body: str, lang: str) -> str | None:
    out = call_deepseek(PROMPTS[lang], zh_body)
    if not out:
        return None
    # Strip code fences the model may wrap around the answer.
    out = re.sub(r"^```(?:markdown|md)?\s*\n", "", out)
    out = re.sub(r"\n```\s*$", "", out)
    if "##" not in out:
        return None
    if cjk_ratio(out) > MIN_CJK_RATIO_RETRY[lang]:
        # one retry with a stricter instruction
        out2 = call_deepseek(PROMPTS[lang] + " Do NOT leave any Chinese characters.", zh_body)
        if out2 and cjk_ratio(out2) <= MIN_CJK_RATIO_RETRY[lang]:
            out = out2
        elif cjk_ratio(out) > MIN_CJK_RATIO_RETRY[lang] * 2:
            return None
    return out


def split_file(text: str):
    m = re.match(r"\A---\n(.*?)\n---\n(.*)\Z", text, re.S)
    if not m:
        return None, None
    try:
        fm = yaml.safe_load(m.group(1))
    except yaml.YAMLError:
        return None, None
    return fm, m.group(2)


def process(path: Path, langs: list[str], write_lock: threading.Lock, stats: dict) -> None:
    text = path.read_text(encoding="utf-8")
    fm, body = split_file(text)
    if fm is None or body is None:
        return
    src = zh_source_body(body)
    if len(src) < 50:
        return
    additions = []
    for lang in langs:
        existing = filter_body_by_language(body, lang).strip()
        if len(existing) >= 100:
            stats[f"skip_{lang}"] += 1
            continue
        translated = translate_for_lang(src, lang)
        if translated:
            additions.append(translated)
            stats[f"ok_{lang}"] += 1
        else:
            stats[f"fail_{lang}"] += 1
    if not additions:
        return
    new_body = body.rstrip() + "\n\n" + "\n\n".join(additions) + "\n"
    out = "---\n" + yaml.safe_dump(fm, allow_unicode=True, sort_keys=False, width=120) + "---\n" + new_body
    with write_lock:
        path.write_text(out, encoding="utf-8")
    stats["files"] += 1


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--lang", choices=["en", "ko"], action="append", dest="langs")
    parser.add_argument("--workers", type=int, default=4)
    args = parser.parse_args()
    langs = args.langs or ["en", "ko"]

    paths = sorted(ROOT.glob("research/**/*.md"))
    if args.limit:
        paths = paths[: args.limit]
    stats: dict = {"files": 0, "ok_en": 0, "ok_ko": 0, "skip_en": 0, "skip_ko": 0, "fail_en": 0, "fail_ko": 0}
    lock = threading.Lock()
    t0 = time.time()
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = [pool.submit(process, p, langs, lock, stats) for p in paths]
        done = 0
        for f in as_completed(futures):
            f.result()
            done += 1
            if done % 50 == 0:
                print(f"[{done}/{len(paths)}] {stats} elapsed={time.time()-t0:.0f}s", flush=True)
    print(f"DONE in {time.time()-t0:.0f}s: {stats}")


if __name__ == "__main__":
    main()
