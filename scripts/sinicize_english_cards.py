#!/usr/bin/env python3
"""Backfill Chinese content for English-only entity cards via DeepSeek.

Target cards: research/**/*.md whose body (after frontmatter) has
CJK/letters < 0.05 — for those, summary.zh currently copies summary.en and the
body is the raw English abstract (duplicated across 概述/核心内容).

For each card the model produces, from the English abstract:
  - frontmatter summary.zh        (2-3 sentence Chinese brief; en/ko untouched)
  - body 概述                      (3-5 sentence Chinese summary)
  - body 核心内容                  (full Chinese compilation; proper nouns kept)
The original English abstract is preserved as a `## Overview` section (which
loader.filter_body_by_language detects as 'en' for the English site), and
`## 参考` is kept verbatim at the end. All other frontmatter fields are
untouched; verification.notes only gets an appended correction record.

Idempotent/resumable: cards with CJK/letters >= 0.05 are skipped, and every
processed file is checkpointed to .staging/sinicize_progress.jsonl.

Usage:
    python scripts/sinicize_english_cards.py --pilot            # 5 fixed cards
    python scripts/sinicize_english_cards.py --limit 20
    python scripts/sinicize_english_cards.py --workers 7        # full run
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
import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "website"))
from builder.loader import filter_body_by_language  # noqa: E402

API_URL = "https://api.deepseek.com/chat/completions"
API_KEY = os.environ.get("DEEPSEEK_API_KEY") or (
    Path.home() / "Desktop" / ".ai_credentials.txt"
).read_text(encoding="utf-8").split("DEEPSEEK_API_KEY=")[1].split("\n")[0].strip()

PROGRESS = ROOT / ".staging" / "sinicize_progress.jsonl"
MAX_SOURCE_CHARS = 6000
NOTE_RECORD = (" [2026-07-29] zh content backfilled from English abstract via"
               " scripts/sinicize_english_cards.py")

PILOT_IDS = [
    "ent_paper_hou_diffusion_transformer_policy_2024",
    "ent_paper_heft_heavy_payload_full_size_h_2026",
    "ent_paper_guidewalk_learning_unified_aut_2026",
    "ent_paper_gait_legged_robot_propriocepti_2026",
    "ent_paper_eschenbach_metric_based_imitation_learnin_2020",
]

SYSTEM_PROMPT = (
    "你是机器人学领域的中文技术编辑。基于用户提供的英文实体卡资料（名称、摘要、正文），"
    "产出三段中文内容，用指定的分隔标记输出。\n"
    "要求：\n"
    "1. 专有名词（模型名、基准名、数据集名、公司/机构名、产品名、人名）保持英文原文不译；公式符号保留。\n"
    "2. 除专有名词外全部使用自然流畅的中文，禁止整句照搬英文。\n"
    "3. 严格按以下格式输出，不要输出任何其他内容：\n"
    "<<<SUMMARY_ZH>>>\n（2-3 句中文精要：是什么、谁做的、核心贡献或关键参数）\n"
    "<<<OVERVIEW_ZH>>>\n（3-5 句中文精要段落，比 SUMMARY 略详，不要分点）\n"
    "<<<CONTENT_ZH>>>\n（完整中文编译：方法、架构、实验设置、关键数字、结论；"
    "可用 Markdown 列表与小标题（###），不要重复 OVERVIEW 的原文，不要遗漏关键数字）"
)

MARK_SUMMARY = "<<<SUMMARY_ZH>>>"
MARK_OVERVIEW = "<<<OVERVIEW_ZH>>>"
MARK_CONTENT = "<<<CONTENT_ZH>>>"


def split_file(text: str):
    m = re.match(r"\A---\n(.*?)\n---\n(.*)\Z", text, re.S)
    if not m:
        return None, None
    try:
        fm = yaml.safe_load(m.group(1))
    except yaml.YAMLError:
        return None, None
    return fm, m.group(2)


def cjk_count(text: str) -> int:
    return sum(1 for c in text if "一" <= c <= "鿿")


def cjk_letter_ratio(text: str) -> float:
    letters = sum(1 for c in text if c.isalpha())
    return cjk_count(text) / max(letters, 1)


def zh_quality_ok(text: str) -> bool:
    """Lenient Chinese-content check: CJK must dominate over Latin letters
    (proper nouns are expected to stay in English)."""
    latin = sum(1 for c in text if "a" <= c.lower() <= "z")
    cjk = cjk_count(text)
    return cjk > 0 and cjk / max(cjk + latin, 1) > 0.55


def call_deepseek(content: str, extra_instruction: str = "", retries: int = 2) -> str | None:
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    payload = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT + extra_instruction},
            {"role": "user", "content": content},
        ],
        "temperature": 0.2,
    }
    for attempt in range(retries + 1):
        try:
            resp = requests.post(API_URL, headers=headers, json=payload, timeout=180)
            if resp.status_code != 200:
                time.sleep(2 * (attempt + 1))
                continue
            return resp.json()["choices"][0]["message"]["content"].strip()
        except Exception:
            time.sleep(2 * (attempt + 1))
    return None


def parse_output(out: str) -> dict | None:
    """Split the marked model output into its three parts."""
    out = re.sub(r"^```(?:markdown|md)?\s*\n", "", out)
    out = re.sub(r"\n```\s*$", "", out)
    m = re.search(
        re.escape(MARK_SUMMARY) + r"\s*(.*?)\s*"
        + re.escape(MARK_OVERVIEW) + r"\s*(.*?)\s*"
        + re.escape(MARK_CONTENT) + r"\s*(.*)\Z",
        out, re.S,
    )
    if not m:
        return None
    parts = {"summary_zh": m.group(1).strip(), "overview_zh": m.group(2).strip(), "content_zh": m.group(3).strip()}
    if not all(parts.values()):
        return None
    return parts


def analyze_body(body: str) -> tuple[str, list[str], str]:
    """Split the current body into (english_text, preserved_sections, references).

    - english_text: the deduplicated content of the 概述/核心内容 sections (the
      raw English abstract these cards carry).
    - preserved_sections: non-Chinese heading sections already present from the
      en/ko translation pipeline (e.g. ## 개요 / ## 핵심 내용) that must not be
      lost. English sections duplicating english_text are dropped — the new
      ## Overview already carries that text.
    - references: the 参考 section including its heading, or "".
    """
    from builder.loader import _detect_heading_language  # local import to keep top clean

    parts = re.split(r"(?m)^(#{1,6}\s+.*)$", body.strip())
    # parts: [lead, heading, content, heading, content, ...]
    english_texts: list[str] = []
    seen: set[str] = set()
    preserved: list[str] = []
    references = ""
    for i in range(1, len(parts), 2):
        heading = parts[i].strip()
        content = parts[i + 1].strip() if i + 1 < len(parts) else ""
        title = re.sub(r"^#+\s*", "", heading).strip()
        if title == "参考":
            references = heading + ("\n" + content if content else "")
            continue
        if title in ("概述", "核心内容"):
            if content and content not in seen:
                seen.add(content)
                english_texts.append(content)
            continue
        # Sections from the translation pipeline (en/ko headings): keep unless
        # they duplicate the abstract we re-emit as ## Overview.
        lang = _detect_heading_language(heading)
        if lang in ("en", "ko") and content and content not in seen:
            preserved.append(heading + ("\n" + content if content else ""))
    english_text = "\n\n".join(english_texts).strip()
    return english_text, preserved, references.strip()


def process(path: Path, lock: threading.Lock, stats: dict) -> None:
    rel = path.relative_to(ROOT).as_posix()
    text = path.read_text(encoding="utf-8")
    fm, body = split_file(text)
    if fm is None or body is None:
        record(lock, rel, "", "failed_parse")
        stats["failed"] += 1
        stats["failed_list"].append(rel)
        return
    if cjk_letter_ratio(body) >= 0.05:
        stats["skipped"] += 1
        return

    english_text, preserved, references = analyze_body(body)
    name_en = (fm.get("names") or {}).get("en") or fm.get("$id", "")
    summary_en = (fm.get("summary") or {}).get("en") or ""
    source = (
        f"实体名称: {name_en}\n"
        f"类型: {fm.get('type', '')}\n"
        f"英文摘要: {summary_en}\n\n"
        f"英文正文:\n{english_text[:MAX_SOURCE_CHARS]}"
    )

    parts = parse_output(call_deepseek(source) or "")
    if parts and not (zh_quality_ok(parts["overview_zh"]) and zh_quality_ok(parts["content_zh"])):
        # One retry with a stricter Chinese-only instruction.
        parts2 = parse_output(call_deepseek(source, "\n4. 上次输出含过多英文，请确保除专有名词外全部为中文。") or "")
        if parts2 and zh_quality_ok(parts2["overview_zh"]) and zh_quality_ok(parts2["content_zh"]):
            parts = parts2
    if not parts or not (zh_quality_ok(parts["overview_zh"]) and zh_quality_ok(parts["content_zh"])):
        record(lock, rel, "", "failed_quality")
        stats["failed"] += 1
        stats["failed_list"].append(rel)
        return

    fm.setdefault("summary", {})["zh"] = parts["summary_zh"]
    ver = fm.setdefault("verification", {})
    notes = ver.get("notes") or ""
    if NOTE_RECORD.strip() not in notes:
        ver["notes"] = notes + NOTE_RECORD

    new_body = (
        f"## 概述\n{parts['overview_zh']}\n\n"
        f"## 核心内容\n{parts['content_zh']}\n\n"
        f"## Overview\n{english_text}\n"
    )
    if preserved:
        new_body += "\n" + "\n\n".join(preserved) + "\n"
    if references:
        new_body += f"\n{references}\n"

    out = "---\n" + yaml.safe_dump(fm, allow_unicode=True, sort_keys=False, width=120) + "---\n" + new_body
    # Round-trip check: the rewritten file must parse with all key fields intact.
    fm2, body2 = split_file(out)
    if fm2 is None or body2 is None or fm2.get("summary", {}).get("zh") != parts["summary_zh"] \
            or fm2.get("sources") != fm.get("sources") or fm2.get("tags") != fm.get("tags"):
        record(lock, rel, "", "failed_roundtrip")
        stats["failed"] += 1
        stats["failed_list"].append(rel)
        return
    path.write_text(out, encoding="utf-8")
    record(lock, rel, hashlib.sha1(out.encode("utf-8")).hexdigest(), "ok")
    stats["ok"] += 1


def record(lock: threading.Lock, rel: str, sha1: str, status: str) -> None:
    with lock:
        with PROGRESS.open("a", encoding="utf-8") as fh:
            fh.write(json.dumps({"path": rel, "sha1": sha1, "status": status}, ensure_ascii=False) + "\n")


def load_done() -> set[str]:
    done = set()
    if PROGRESS.exists():
        for line in PROGRESS.read_text(encoding="utf-8").splitlines():
            try:
                rec = json.loads(line)
            except json.JSONDecodeError:
                continue
            if rec.get("status") == "ok":
                done.add(rec.get("path"))
    return done


def is_target(path: Path) -> bool:
    fm, body = split_file(path.read_text(encoding="utf-8"))
    return body is not None and cjk_letter_ratio(body) < 0.05


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--workers", type=int, default=6)
    parser.add_argument("--pilot", action="store_true", help="run the 5-card pilot set")
    args = parser.parse_args()

    done = load_done()
    if args.pilot:
        paths = []
        for pid in PILOT_IDS:
            hits = list(ROOT.glob(f"research/**/{pid}.md"))
            if not hits:
                print(f"pilot id not found: {pid}")
                return
            paths.append(hits[0])
    else:
        paths = sorted(p for p in ROOT.glob("research/**/*.md")
                       if p.relative_to(ROOT).as_posix() not in done and is_target(p))
    if args.limit:
        paths = paths[: args.limit]
    print(f"cards to process: {len(paths)} (already done: {len(done)})")

    stats: dict = {"ok": 0, "skipped": 0, "failed": 0, "failed_list": []}
    lock = threading.Lock()
    t0 = time.time()
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = [pool.submit(process, p, lock, stats) for p in paths]
        done_n = 0
        for f in as_completed(futures):
            f.result()
            done_n += 1
            if done_n % 50 == 0:
                print(f"[{done_n}/{len(paths)}] ok={stats['ok']} failed={stats['failed']} "
                      f"elapsed={time.time()-t0:.0f}s", flush=True)

    manifest = {
        "ts": datetime.now(timezone.utc).isoformat(),
        "processed": len(paths),
        "ok": stats["ok"],
        "skipped_cjk_ok": stats["skipped"],
        "failed": stats["failed"],
        "failed_list": stats["failed_list"],
    }
    mpath = ROOT / ".staging" / f"sinicize_manifest_{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')}.json"
    mpath.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"DONE in {time.time()-t0:.0f}s: {manifest['ok']} ok, {manifest['failed']} failed, "
          f"manifest: {mpath}")


if __name__ == "__main__":
    main()
