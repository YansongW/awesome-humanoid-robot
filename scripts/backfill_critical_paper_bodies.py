#!/usr/bin/env python3
"""
Backfill structured Chinese bodies for paper entries still flagged as critical.

Uses DeepSeek API to expand title/summary/tags into a structured Markdown body
with 概述 / 核心内容 / 参考 sections. The generated content is marked as
AI-generated and unverified for human review.

Uses concurrent workers to speed up generation.

Usage:
    python scripts/backfill_critical_paper_bodies.py [--limit N] [--dry-run] [--workers N]
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Any

import requests
import yaml

sys.path.insert(0, str(Path(__file__).parent))

ROOT = Path(__file__).parent.parent
STAGING_DIR = ROOT / ".staging"
CACHE_PATH = STAGING_DIR / "critical_paper_body_cache.json"
REPORT_PATH = STAGING_DIR / "critical_paper_body_report.json"
LATEST_REPORT = STAGING_DIR / "quality_reports"

API_URL = "https://api.deepseek.com/chat/completions"
API_KEY = os.environ.get("DEEPSEEK_API_KEY") or (
    Path.home() / "Desktop" / ".ai_credentials.txt"
).read_text(encoding="utf-8").split("DEEPSEEK_API_KEY=")[1].split("\n")[0]

MIN_ZH_CHARS_CORE = 350
API_DELAY = 0.3
MAX_WORKERS = 6

cache_lock = threading.Lock()


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


def load_critical_paper_ids(limit: int | None = None) -> list[str]:
    reports = sorted(LATEST_REPORT.glob("quality_report_*.json"))
    if not reports:
        raise RuntimeError("No quality report found")
    data = json.loads(reports[-1].read_text(encoding="utf-8"))
    ids = [
        e["id"]
        for e in data.get("critical_entries", [])
        if e.get("type") == "paper"
    ]
    return ids[:limit] if limit is not None else ids


def build_prompt(fm: dict[str, Any]) -> str:
    names = fm.get("names", {}) or {}
    summary = fm.get("summary", {}) or {}
    sources = fm.get("sources", []) or []
    tags = fm.get("tags", []) or []
    domains = fm.get("domains", []) or []
    layers = fm.get("layers", []) or []

    source_lines = "\n".join(
        f"- {s.get('title', '')} ({s.get('url', 'no url')})" for s in sources
    ) or "- 无可用来源"

    prompt = f"""你是一位机器人学领域的学术写作助手。请根据下面这篇人形机器人相关论文的元数据，撰写一段结构化的中文正文，用于知识图谱条目页面。

要求：
1. 必须使用 Markdown 格式，且只包含三个一级标题：## 概述、## 核心内容、## 参考。
2. ## 概述：用 2-4 句话概括研究动机与主要贡献，不要与提供的 summary 逐字重复，但可以基于它改写和扩展。
3. ## 核心内容：写 4-6 段，深入阐述（a）研究背景与问题，（b）方法或模型框架，（c）关键技术创新，（d）实验/验证或应用价值。内容要具体、有信息量，避免空泛套话。总中文字符数不少于 350 字。
4. ## 参考：直接列出下面提供的来源信息，每条一行，格式为 "- 标题（URL）"。如果没有 URL，只写标题。
5. 全文使用学术中文，术语准确。不要编造不存在的实验数据，但可以基于标题、标签和摘要合理推断研究范式和意义。

论文元数据：
- 英文标题：{names.get('en', 'N/A')}
- 中文标题：{names.get('zh', 'N/A')}
- 英文摘要：{summary.get('en', 'N/A')}
- 中文摘要：{summary.get('zh', 'N/A')}
- 领域标签：{', '.join(domains)}
- 层级标签：{', '.join(layers)}
- 关键词：{', '.join(tags)}

来源信息：
{source_lines}

请只输出正文 Markdown，不要输出任何解释、注释或代码块包裹。"""
    return prompt


def call_deepseek(prompt: str) -> str:
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": "deepseek-chat",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.4,
        "max_tokens": 1800,
    }
    r = requests.post(API_URL, headers=headers, json=payload, timeout=120)
    r.raise_for_status()
    return r.json()["choices"][0]["message"]["content"]


def clean_body(text: str) -> str:
    text = text.strip()
    if text.startswith("```"):
        text = re.sub(r"^```[\w]*\n?", "", text)
        text = re.sub(r"\n?```\s*$", "", text)
    return text.strip()


def zh_chars_in_body(body: str, exclude: list[str]) -> int:
    text = re.sub(r"^#{1,6}\s+", "", body, flags=re.MULTILINE)
    text = re.split(r"\n## 参考|\n## References|\n## 참고", text, flags=re.IGNORECASE)[0]
    for s in exclude:
        if s:
            text = text.replace(s, "")
    return len(re.findall(r"[\u4e00-\u9fff]", text))


def save_cache(cache: dict[str, Any]) -> None:
    with cache_lock:
        CACHE_PATH.write_text(json.dumps(cache, ensure_ascii=False, indent=2), encoding="utf-8")


def process_one(args: tuple[str, dict[str, Any], bool]) -> dict[str, Any]:
    eid, cache, dry_run = args
    p = ROOT / "research" / "papers" / f"{eid}.md"
    result = {"id": eid, "status": "failed", "reason": "", "zh_chars": 0}

    if not p.exists():
        result["reason"] = "file not found"
        return result

    try:
        text = p.read_text(encoding="utf-8")
        fm, body = split_fm(text)
        if fm is None:
            result["reason"] = "no frontmatter"
            return result

        summary = fm.get("summary", {}) or {}
        names = fm.get("names", {}) or {}
        exclude = [s for s in (names.get("zh", ""), names.get("en", ""), summary.get("zh", ""), summary.get("en", "")) if s]
        current_zh = zh_chars_in_body(body, exclude)
        if current_zh >= MIN_ZH_CHARS_CORE:
            result["status"] = "skipped"
            result["reason"] = f"already rich ({current_zh} zh chars)"
            return result

        cache_key = f"{eid}:v1"
        if cache_key in cache:
            generated = cache[cache_key]
        else:
            prompt = build_prompt(fm)
            generated = clean_body(call_deepseek(prompt))
            cache[cache_key] = generated
            if not dry_run:
                save_cache(cache)
            time.sleep(API_DELAY)

        if "## 概述" not in generated or "## 核心内容" not in generated or "## 参考" not in generated:
            result["reason"] = "missing required sections"
            return result

        core_zh = zh_chars_in_body(generated.split("## 参考")[0], exclude)
        if core_zh < MIN_ZH_CHARS_CORE:
            result["reason"] = f"core content too short ({core_zh} zh chars)"
            return result

        ver = fm.get("verification", {}) or {}
        ver["status"] = "unverified"
        ver["reviewed_by"] = "ai"
        ver["reviewed_at"] = "2026-07-15"
        ver["confidence"] = "low"
        ver["notes"] = "Structured body generated by scripts/backfill_critical_paper_bodies.py via DeepSeek API from entry metadata."
        fm["verification"] = ver

        if not dry_run:
            new_yaml = yaml.safe_dump(fm, allow_unicode=True, sort_keys=False, width=120, default_flow_style=False)
            p.write_text(f"---\n{new_yaml}---\n{generated}\n", encoding="utf-8")

        result["status"] = "updated"
        result["zh_chars"] = core_zh
        return result
    except Exception as exc:
        result["reason"] = f"error: {exc}"
        return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--workers", type=int, default=MAX_WORKERS)
    args = parser.parse_args()

    STAGING_DIR.mkdir(parents=True, exist_ok=True)
    cache: dict[str, Any] = json.loads(CACHE_PATH.read_text(encoding="utf-8")) if CACHE_PATH.exists() else {}

    ids = load_critical_paper_ids(args.limit)
    print(f"Processing {len(ids)} critical paper entries with {args.workers} workers")

    updated: list[dict[str, Any]] = []
    failed: list[dict[str, Any]] = []
    skipped: list[dict[str, Any]] = []

    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = {executor.submit(process_one, (eid, cache, args.dry_run)): eid for eid in ids}
        for future in as_completed(futures):
            res = future.result()
            if res["status"] == "updated":
                updated.append({"id": res["id"], "zh_chars": res["zh_chars"]})
            elif res["status"] == "skipped":
                skipped.append({"id": res["id"], "reason": res["reason"]})
            else:
                failed.append({"id": res["id"], "reason": res["reason"]})
            print(f"  {res['status'].upper()}: {res['id']} ({res.get('zh_chars', 0)} zh chars) {res.get('reason', '')}", flush=True)

    if not args.dry_run:
        save_cache(cache)
        report = {
            "processed": len(ids),
            "updated": len(updated),
            "skipped": len(skipped),
            "failed": len(failed),
            "updated_ids": updated,
            "failed_ids": failed,
            "skipped_reasons": skipped,
        }
        REPORT_PATH.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Done: updated {len(updated)}, skipped {len(skipped)}, failed {len(failed)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
