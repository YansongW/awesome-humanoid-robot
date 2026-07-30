#!/usr/bin/env python3
"""Weekly discovery of new humanoid-robotics papers from arXiv.

Layer 1 of the weekly evolution pipeline:
  1. Query the arXiv API for papers published since `--since` (default: 7 days
     ago) across a fixed set of humanoid/legged-robotics search terms
     (cat:cs.RO based), with polite rate limiting and a descriptive UA.
  2. Deduplicate against existing research/papers/ cards by arXiv ID and
     normalized title.
  3. Draft Chinese entity cards with DeepSeek (capped at 30 new cards/week).
  4. Validate every drafted card against data/schema/v1/entry_schema.json
     (reusing scripts/validate_entries.py); failures are dropped and recorded.
  5. Write new cards to research/papers/ plus a report to
     .staging/weekly_discovery/report_<date>.md and a machine-readable
     last_run.json for the GitHub Actions workflow.

Data discipline (AGENTS.md): additive only — never touches existing cards;
every card carries its arXiv source URL; verification.status stays
`unverified` with reviewed_by `ai` until a human merges the weekly PR.

Usage:
    python scripts/weekly_discovery.py                  # full run (writes cards)
    python scripts/weekly_discovery.py --dry-run        # report only, no cards
    python scripts/weekly_discovery.py --since 2026-07-23
    python scripts/weekly_discovery.py --mock-file m.json   # offline testing

Secrets: DEEPSEEK_API_KEY from env, or ~/Desktop/.ai_credentials.txt
(never printed). arXiv API base can be overridden via --arxiv-base-url or the
ARXIV_API_BASE env var (default https://export.arxiv.org/api/query).
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
import unicodedata
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.parse import quote_plus

import requests
import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from validate_entries import compile_validator, load_yaml_frontmatter  # noqa: E402

ARXIV_API_DEFAULT = "https://export.arxiv.org/api/query"
USER_AGENT = ("awesome-humanoid-robot weekly-discovery/1.0 "
              "(https://github.com/YansongW/awesome-humanoid-robot)")
POLITE_DELAY = 3.0          # seconds between arXiv API calls (arXiv asks for >=3)
MAX_RESULTS_PER_QUERY = 100
MAX_NEW_PER_WEEK = 30
MAX_SOURCE_CHARS = 6000
MIN_ABSTRACT_CHARS = 100   # below this the LLM would have to invent content -> drop
DEEPSEEK_URL = "https://api.deepseek.com/chat/completions"
DEEPSEEK_MODEL = "deepseek-chat"

PAPERS_DIR = ROOT / "research" / "papers"
REPORT_DIR = ROOT / ".staging" / "weekly_discovery"
# Write target for new cards (module-level so tests can redirect it).
WRITE_DIR = PAPERS_DIR

# Query terms covering the humanoid-robotics scope of the graph. Each is run
# as all:"<term>" AND cat:cs.RO, sorted by submittedDate descending.
QUERY_TERMS = [
    "humanoid robot",
    "legged locomotion",
    "loco-manipulation",
    "whole-body control humanoid",
    "vision-language-action robot",
    "robot learning manipulation humanoid",
]

SYSTEM_PROMPT = (
    "你是机器人学领域的中文技术编辑。基于用户提供的 arXiv 论文元数据（标题、作者、分类、摘要），"
    "为人形机器人知识图谱起草中文实体卡内容，用指定的分隔标记输出。\n"
    "要求：\n"
    "1. 专有名词（模型名、基准名、数据集名、公司/机构名、产品名、人名）保持英文原文不译；公式符号保留。\n"
    "2. 除专有名词外全部使用自然流畅的中文，禁止整句照搬英文。\n"
    "3. 严禁编造摘要中没有的数字、机构、实验设置或结论；摘要未涉及的方面不要写。\n"
    "4. 严格按以下格式输出，不要输出任何其他内容：\n"
    "<<<SUMMARY_ZH>>>\n（2-3 句中文精要：是什么、谁做的、核心贡献或关键参数）\n"
    "<<<OVERVIEW_ZH>>>\n（3-5 句中文精要段落，比 SUMMARY 略详，不要分点）\n"
    "<<<CONTENT_ZH>>>\n（完整中文编译：问题背景、方法、实验设置、关键结果、结论；"
    "可用 Markdown 列表与小标题（###），不要重复 OVERVIEW 的原文，不要遗漏关键数字）\n"
    "<<<TAGS>>>\n（3-6 个英文标签，小写 snake_case，逗号分隔，"
    "如 humanoid_locomotion, whole_body_control）"
)

MARK_SUMMARY = "<<<SUMMARY_ZH>>>"
MARK_OVERVIEW = "<<<OVERVIEW_ZH>>>"
MARK_CONTENT = "<<<CONTENT_ZH>>>"
MARK_TAGS = "<<<TAGS>>>"

ARXIV_ID_RE = re.compile(r"arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5})")
URL_RE = re.compile(r"https?://[^\s<>；，、）)\]]+")


# --------------------------------------------------------------------------- #
# Small helpers
# --------------------------------------------------------------------------- #

def slugify(text: str, max_len: int = 40) -> str:
    """Filesystem/ID-safe slug, same convention as ai4sci_lib.entry_builder."""
    text = unicodedata.normalize("NFKD", text)
    text = text.encode("ascii", "ignore").decode("ascii")
    text = re.sub(r"[^\w\s-]", "", text).strip().lower()
    text = re.sub(r"[-\s]+", "_", text)
    return text[:max_len].strip("_")


def normalize_title(title: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9 ]", " ", title.lower())).strip()


def cjk_count(text: str) -> int:
    return sum(1 for c in text if "一" <= c <= "鿿")


def zh_quality_ok(text: str) -> bool:
    """CJK must dominate over Latin letters (proper nouns stay English)."""
    latin = sum(1 for c in text if "a" <= c.lower() <= "z")
    cjk = cjk_count(text)
    return cjk > 0 and cjk / max(cjk + latin, 1) > 0.55


def load_api_key() -> str | None:
    key = os.environ.get("DEEPSEEK_API_KEY")
    if key:
        return key.strip()
    cred = Path.home() / "Desktop" / ".ai_credentials.txt"
    if cred.exists():
        m = re.search(r"DEEPSEEK_API_KEY=(\S+)", cred.read_text(encoding="utf-8"))
        if m:
            return m.group(1).strip()
    return None


# --------------------------------------------------------------------------- #
# arXiv fetching
# --------------------------------------------------------------------------- #

def parse_arxiv_feed(xml_text: str) -> list[dict]:
    ns = {"atom": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}
    root = ET.fromstring(xml_text)
    entries = []
    for entry in root.findall("atom:entry", ns):
        id_el = entry.find("atom:id", ns)
        title_el = entry.find("atom:title", ns)
        summary_el = entry.find("atom:summary", ns)
        published_el = entry.find("atom:published", ns)
        if id_el is None or not id_el.text or title_el is None or not title_el.text:
            continue
        m = ARXIV_ID_RE.search(id_el.text)
        if not m:
            continue
        comment_el = entry.find("arxiv:comment", ns)
        journal_el = entry.find("arxiv:journal_ref", ns)
        entries.append({
            "arxiv_id": m.group(1),
            "title": re.sub(r"\s+", " ", title_el.text).strip(),
            "abstract": re.sub(r"\s+", " ", summary_el.text).strip()
            if summary_el is not None and summary_el.text else "",
            "authors": [a.find("atom:name", ns).text.strip()
                        for a in entry.findall("atom:author", ns)
                        if a.find("atom:name", ns) is not None and a.find("atom:name", ns).text],
            "published": published_el.text.strip() if published_el is not None and published_el.text else "",
            "categories": [c.get("term", "") for c in entry.findall("atom:category", ns)],
            "comment": comment_el.text.strip() if comment_el is not None and comment_el.text else "",
            "journal_ref": journal_el.text.strip() if journal_el is not None and journal_el.text else "",
        })
    return entries


def fetch_query(term: str, api_base: str) -> tuple[list[dict], str | None]:
    """One arXiv API call for a search term. Returns (entries, error)."""
    query = f'all:"{term}" AND cat:cs.RO'
    url = (f"{api_base}?search_query={quote_plus(query)}"
           f"&start=0&max_results={MAX_RESULTS_PER_QUERY}"
           f"&sortBy=submittedDate&sortOrder=descending")
    headers = {"User-Agent": USER_AGENT}
    err = "unknown error"
    for attempt in range(3):
        try:
            resp = requests.get(url, headers=headers, timeout=60)
            if resp.status_code == 200:
                return parse_arxiv_feed(resp.text), None
            err = f"HTTP {resp.status_code}"
        except Exception as e:
            err = f"{type(e).__name__}: {e}"
        time.sleep(3 * (attempt + 1))
    return [], err


def load_mock_entries(path: Path) -> list[dict]:
    """Offline testing: load fake arXiv entries from a JSON file."""
    raw = json.loads(path.read_text(encoding="utf-8"))
    entries = []
    for r in raw:
        entries.append({
            "arxiv_id": r["arxiv_id"],
            "title": r.get("title", ""),
            "abstract": r.get("abstract", ""),
            "authors": r.get("authors", []),
            "published": r.get("published", ""),
            "categories": r.get("categories", ["cs.RO"]),
            "comment": r.get("comment", ""),
            "journal_ref": r.get("journal_ref", ""),
        })
    return entries


# --------------------------------------------------------------------------- #
# Dedup against existing cards
# --------------------------------------------------------------------------- #

def collect_existing() -> tuple[set[str], set[str], set[str]]:
    """Returns (existing_arxiv_ids, existing_norm_titles, existing_entity_ids)."""
    arxiv_ids: set[str] = set()
    titles: set[str] = set()
    ids: set[str] = set()
    for path in PAPERS_DIR.glob("*.md"):
        text = path.read_text(encoding="utf-8")
        arxiv_ids.update(ARXIV_ID_RE.findall(text))
        ids.add(path.stem)
        try:
            fm = load_yaml_frontmatter(path)
        except Exception:
            continue
        name_en = (fm.get("names") or {}).get("en")
        if name_en:
            titles.add(normalize_title(name_en))
        if fm.get("$id"):
            ids.add(fm["$id"])
    return arxiv_ids, titles, ids


# --------------------------------------------------------------------------- #
# DeepSeek drafting
# --------------------------------------------------------------------------- #

def call_deepseek(api_key: str, content: str, extra_instruction: str = "",
                  retries: int = 2) -> str | None:
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    payload = {
        "model": DEEPSEEK_MODEL,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT + extra_instruction},
            {"role": "user", "content": content},
        ],
        "temperature": 0.2,
    }
    for attempt in range(retries + 1):
        try:
            resp = requests.post(DEEPSEEK_URL, headers=headers, json=payload, timeout=180)
            if resp.status_code != 200:
                time.sleep(2 * (attempt + 1))
                continue
            return resp.json()["choices"][0]["message"]["content"].strip()
        except Exception:
            time.sleep(2 * (attempt + 1))
    return None


def parse_llm_output(out: str) -> dict | None:
    out = re.sub(r"^```(?:markdown|md)?\s*\n", "", out)
    out = re.sub(r"\n```\s*$", "", out)
    m = re.search(
        re.escape(MARK_SUMMARY) + r"\s*(.*?)\s*"
        + re.escape(MARK_OVERVIEW) + r"\s*(.*?)\s*"
        + re.escape(MARK_CONTENT) + r"\s*(.*?)\s*"
        + re.escape(MARK_TAGS) + r"\s*(.*)\Z",
        out, re.S,
    )
    if not m:
        return None
    parts = {"summary_zh": m.group(1).strip(), "overview_zh": m.group(2).strip(),
             "content_zh": m.group(3).strip(), "tags_raw": m.group(4).strip()}
    if not all([parts["summary_zh"], parts["overview_zh"], parts["content_zh"]]):
        return None
    return parts


def sanitize_tags(tags_raw: str, title: str) -> list[str]:
    tags = []
    for t in re.split(r"[,，;；\n]", tags_raw):
        slug = slugify(t, max_len=40)
        if slug and slug not in tags:
            tags.append(slug)
    if not tags:  # fallback: significant title words
        for w in title.split():
            slug = slugify(w, max_len=40)
            if len(slug) >= 4 and slug not in tags:
                tags.append(slug)
            if len(tags) >= 3:
                break
    return tags[:8] or ["arxiv_weekly"]


def draft_card_content(api_key: str, entry: dict) -> tuple[dict | None, str | None]:
    """LLM drafting with one stricter retry. Returns (parts, drop_reason)."""
    authors = entry["authors"]
    author_str = ", ".join(authors[:8]) + (" 等" if len(authors) > 8 else "")
    source = (
        f"标题: {entry['title']}\n"
        f"作者: {author_str or '未知'}\n"
        f"arXiv: {entry['arxiv_id']} ({', '.join(entry['categories'])})\n"
        f"发布日期: {entry['published'][:10]}\n\n"
        f"摘要:\n{entry['abstract'][:MAX_SOURCE_CHARS]}"
    )
    parts = parse_llm_output(call_deepseek(api_key, source) or "")
    if parts and not (zh_quality_ok(parts["overview_zh"]) and zh_quality_ok(parts["content_zh"])):
        parts2 = parse_llm_output(call_deepseek(
            api_key, source, "\n5. 上次输出含过多英文，请确保除专有名词外全部为中文。") or "")
        if parts2 and zh_quality_ok(parts2["overview_zh"]) and zh_quality_ok(parts2["content_zh"]):
            parts = parts2
    if not parts:
        return None, "llm_no_output"
    if not (zh_quality_ok(parts["overview_zh"]) and zh_quality_ok(parts["content_zh"])):
        return None, "llm_zh_quality"
    return parts, None


# --------------------------------------------------------------------------- #
# Card assembly
# --------------------------------------------------------------------------- #

def make_entry_id(entry: dict, existing_ids: set[str], planned_ids: set[str]) -> str:
    year = (entry["published"][:4] if entry["published"]
            else str(datetime.now(timezone.utc).year))
    surname = slugify(entry["authors"][0].split()[-1], max_len=20) if entry["authors"] else ""
    title_slug = slugify(entry["title"], max_len=30)
    stem = f"{surname}_{title_slug}" if surname else title_slug
    base = f"ent_paper_{stem}_{year}"
    eid, counter = base, 2
    while eid in existing_ids or eid in planned_ids:
        eid = f"{base}_{counter}"
        counter += 1
    return eid


def build_card(entry: dict, parts: dict, eid: str, today: str) -> str:
    title = entry["title"]
    aid = entry["arxiv_id"]
    arxiv_url = f"https://arxiv.org/abs/{aid}"
    abstract = entry["abstract"]
    summary_en = abstract[:400].rsplit(" ", 1)[0] + " ..." if len(abstract) > 400 else abstract

    complete = bool(entry["abstract"]) and bool(entry["authors"])
    confidence = "medium" if complete else "low"
    notes = (f"Weekly auto-discovery by scripts/weekly_discovery.py ({today}). "
             f"Bibliographic metadata from arXiv API ({aid}); zh content drafted by "
             f"DeepSeek ({DEEPSEEK_MODEL}) from the abstract. Unverified until human "
             f"review of the weekly discovery PR.")
    if not complete:
        notes += " Metadata incomplete (missing abstract or authors); confidence lowered."

    sources = [{
        "id": "src_001",
        "type": "paper",
        "title": f"arXiv:{aid} {title}",
        "url": arxiv_url,
        "date": entry["published"][:10] or today,
        "accessed_at": today,
    }]
    n = 2
    for u in dict.fromkeys(URL_RE.findall(entry["comment"] or "")):
        u = u.rstrip(".")
        if "arxiv.org" in u or u == arxiv_url:
            continue
        sources.append({"id": f"src_{n:03d}", "type": "website",
                        "title": "Project page", "url": u, "accessed_at": today})
        n += 1
        if n > 3:
            break

    fm = {
        "$id": eid,
        "$schema": "../../data/schema/v1/entry_schema.json",
        "$version": 1,
        "type": "paper",
        "names": {"en": title, "zh": title, "ko": title},
        "summary": {"en": summary_en, "zh": parts["summary_zh"], "ko": summary_en},
        "domains": ["07_ai_models_algorithms"],
        "layers": ["intelligence"],
        "functional_roles": ["knowledge", "intelligence"],
        "theoretical_depth": ["system"],
        "tags": sanitize_tags(parts["tags_raw"], title),
        "verification": {
            "status": "unverified",
            "reviewed_by": "ai",
            "reviewed_at": today,
            "confidence": confidence,
            "notes": notes,
        },
        "sources": sources,
    }

    body = [
        "## 概述", "", parts["overview_zh"], "",
        "## 核心内容", "", parts["content_zh"], "",
        "## Overview", "", abstract, "",
        "## 参考",
    ]
    for s in sources:
        body.append(f"- {s['url']}")

    text = ("---\n" + yaml.safe_dump(fm, allow_unicode=True, sort_keys=False, width=120)
            + "---\n\n" + "\n".join(body).strip() + "\n")

    # Round-trip check (AGENTS.md rule 4): the dumped frontmatter must parse
    # back with key fields intact.
    fm2 = yaml.safe_load(text.split("---", 2)[1])
    if fm2.get("$id") != eid or fm2.get("sources") != sources or fm2.get("tags") != fm["tags"]:
        raise ValueError("yaml round-trip mismatch")
    return text


# --------------------------------------------------------------------------- #
# Report
# --------------------------------------------------------------------------- #

def write_report(today: str, args: argparse.Namespace, query_stats: list[dict],
                 new_cards: list[dict], dropped: list[dict], dedup: dict,
                 errors: list[str]) -> Path:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    lines = [
        f"# 每周新论文发现报告 — {today}",
        "",
        f"- 运行时间 (UTC): {datetime.now(timezone.utc).isoformat(timespec='seconds')}",
        f"- 模式: {'**dry-run**（未写卡）' if args.dry_run else '写卡'}",
        f"- 时间窗: since {args.since}（published ≥ 该日期）",
        f"- 数据源: {'mock 文件 ' + str(args.mock_file) if args.mock_file else args.arxiv_base_url}",
        f"- 新增卡: **{len(new_cards)}** 篇（周上限 {args.max_new}）",
        f"- 丢弃: {len(dropped)} 篇；去重跳过: {dedup['arxiv']}（arXiv ID 撞库）"
        f" + {dedup['title']}（标题撞库）",
        "",
        "## arXiv 查询覆盖统计",
        "",
        "| 查询词 | 抓取 | 时间窗内 | 备注 |",
        "|--------|------|----------|------|",
    ]
    for s in query_stats:
        note = s.get("note", "")
        lines.append(f"| `{s['term']}` | {s['fetched']} | {s['kept']} | {note} |")
    if errors:
        lines += ["", "## 运行错误", ""]
        lines += [f"- {e}" for e in errors]
    lines += ["", "## 新增卡清单", ""]
    if new_cards:
        lines += ["| $id | arXiv | 标题 | confidence |", "|-----|-------|------|------------|"]
        for c in new_cards:
            lines.append(f"| `{c['id']}` | [{c['arxiv_id']}](https://arxiv.org/abs/{c['arxiv_id']})"
                         f" | {c['title']} | {c['confidence']} |")
    else:
        lines.append("（无）")
    lines += ["", "## 丢弃清单与原因", ""]
    if dropped:
        lines += ["| arXiv | 标题 | 阶段 | 原因 |", "|-------|------|------|------|"]
        for d in dropped:
            lines.append(f"| {d['arxiv_id']} | {d['title'][:60]} | {d['stage']} | {d['reason']} |")
    else:
        lines.append("（无）")
    lines += ["", "## 审查提示", "",
              "本批卡由 AI 自动起草，`verification.status: unverified`、`reviewed_by: ai`；"
              "合并 PR 前请抽查事实与来源。", ""]
    path = REPORT_DIR / f"report_{today}.md"
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


# --------------------------------------------------------------------------- #
# Main
# --------------------------------------------------------------------------- #

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--dry-run", action="store_true",
                        help="只出报告，不写卡文件")
    parser.add_argument("--since", default=None,
                        help="YYYY-MM-DD，只收 published ≥ 该日的论文（默认 7 天前）")
    parser.add_argument("--max-new", type=int, default=MAX_NEW_PER_WEEK,
                        help=f"每周新卡上限（默认 {MAX_NEW_PER_WEEK}）")
    parser.add_argument("--workers", type=int, default=4, help="DeepSeek 并发数")
    parser.add_argument("--mock-file", type=Path, default=None,
                        help="离线测试：从 JSON 文件读假 arXiv 条目，不访问网络")
    parser.add_argument("--arxiv-base-url",
                        default=os.environ.get("ARXIV_API_BASE", ARXIV_API_DEFAULT),
                        help="arXiv API base（可用镜像覆盖）")
    args = parser.parse_args()

    today = datetime.now(timezone.utc).date().isoformat()
    since_date = (datetime.strptime(args.since, "%Y-%m-%d").date() if args.since
                  else datetime.now(timezone.utc).date() - timedelta(days=7))
    args.since = since_date.isoformat()

    api_key = load_api_key()
    if not api_key:
        print("FATAL: DEEPSEEK_API_KEY not found (env or ~/Desktop/.ai_credentials.txt)")
        return 1

    # ---- 1. discover ------------------------------------------------------- #
    query_stats: list[dict] = []
    errors: list[str] = []
    candidates: dict[str, dict] = {}  # arxiv_id -> entry
    if args.mock_file:
        mock_entries = load_mock_entries(args.mock_file)
        kept = 0
        for e in mock_entries:
            try:
                pub = datetime.strptime(e["published"][:10], "%Y-%m-%d").date()
            except ValueError:
                continue
            if pub >= since_date and candidates.setdefault(e["arxiv_id"], e) is e:
                kept += 1
        query_stats.append({"term": "(mock file)", "fetched": len(mock_entries),
                            "kept": kept, "note": "离线测试数据"})
    else:
        for i, term in enumerate(QUERY_TERMS):
            if i:
                time.sleep(POLITE_DELAY)
            entries, err = fetch_query(term, args.arxiv_base_url)
            if err:
                errors.append(f"arXiv 查询失败 `{term}`: {err}")
                query_stats.append({"term": term, "fetched": 0, "kept": 0, "note": f"失败: {err}"})
                continue
            kept = 0
            for e in entries:
                try:
                    pub = datetime.strptime(e["published"][:10], "%Y-%m-%d").date()
                except ValueError:
                    continue
                if pub >= since_date:
                    if candidates.setdefault(e["arxiv_id"], e) is e:
                        kept += 1
            note = ""
            if len(entries) >= MAX_RESULTS_PER_QUERY:
                note = f"达到单查询上限 {MAX_RESULTS_PER_QUERY}，可能截断"
            query_stats.append({"term": term, "fetched": len(entries), "kept": kept, "note": note})
        if not candidates and errors and len(errors) == len(QUERY_TERMS):
            print("FATAL: all arXiv queries failed (network unreachable?). See report.")
            # still write the report so the CI log artifact explains the outage
            write_report(today, args, query_stats, [], [], {"arxiv": 0, "title": 0}, errors)
            return 1

    # ---- 2. dedup ---------------------------------------------------------- #
    existing_arxiv, existing_titles, existing_ids = collect_existing()
    dedup = {"arxiv": 0, "title": 0}
    fresh: list[dict] = []
    seen_titles: set[str] = set()
    for e in sorted(candidates.values(), key=lambda x: x["published"], reverse=True):
        if e["arxiv_id"] in existing_arxiv:
            dedup["arxiv"] += 1
            continue
        nt = normalize_title(e["title"])
        if nt in existing_titles or nt in seen_titles:
            dedup["title"] += 1
            continue
        seen_titles.add(nt)
        fresh.append(e)
    truncated = max(0, len(fresh) - args.max_new)
    fresh = fresh[: args.max_new]
    print(f"discovered {len(candidates)} unique, fresh {len(fresh)} "
          f"(dedup arxiv={dedup['arxiv']} title={dedup['title']}, truncated {truncated})")

    # ---- 3+4. draft & validate -------------------------------------------- #
    schema = json.loads((ROOT / "data" / "schema" / "v1" / "entry_schema.json").read_text())
    validator = compile_validator(schema)
    new_cards: list[dict] = []
    dropped: list[dict] = []
    planned: dict[str, str] = {}  # eid -> card text

    # Assign $ids in the main thread (collision-free, no worker race).
    planned_ids: set[str] = set()
    jobs: list[tuple[dict, str]] = []
    for e in fresh:
        eid = make_entry_id(e, existing_ids, planned_ids)
        planned_ids.add(eid)
        jobs.append((e, eid))

    def process(entry: dict, eid: str):
        # Anti-hallucination guard: never draft from a missing/stub abstract.
        if len(entry["abstract"]) < MIN_ABSTRACT_CHARS:
            return entry, eid, None, ("metadata",
                                      f"abstract too short ({len(entry['abstract'])} chars)")
        parts, reason = draft_card_content(api_key, entry)
        if reason:
            return entry, eid, None, ("llm", reason)
        try:
            text = build_card(entry, parts, eid, today)
        except Exception as exc:
            return entry, eid, None, ("roundtrip", str(exc))
        fm = yaml.safe_load(text.split("---", 2)[1])
        errs = sorted(validator.iter_errors(fm), key=lambda x: list(x.path))
        if errs:
            msg = "; ".join(f"{e.message} at {'/'.join(map(str, e.path)) or '<root>'}"
                            for e in errs[:3])
            return entry, eid, None, ("schema", msg)
        return entry, eid, text, None

    if jobs:
        with ThreadPoolExecutor(max_workers=args.workers) as pool:
            futures = [pool.submit(process, e, eid) for e, eid in jobs]
            for f in as_completed(futures):
                entry, eid, text, fail = f.result()
                if fail:
                    dropped.append({"arxiv_id": entry["arxiv_id"], "title": entry["title"],
                                    "stage": fail[0], "reason": fail[1]})
                    continue
                planned[eid] = text
                conf = yaml.safe_load(text.split("---", 2)[1])["verification"]["confidence"]
                new_cards.append({"id": eid, "arxiv_id": entry["arxiv_id"],
                                  "title": entry["title"], "confidence": conf})
    new_cards.sort(key=lambda c: c["id"])

    # ---- 5. write ---------------------------------------------------------- #
    if not args.dry_run:
        WRITE_DIR.mkdir(parents=True, exist_ok=True)
        for eid, text in sorted(planned.items()):
            (WRITE_DIR / f"{eid}.md").write_text(text, encoding="utf-8")
        if planned:
            print(f"wrote {len(planned)} cards to {WRITE_DIR}")
    report_path = write_report(today, args, query_stats, new_cards, dropped, dedup,
                               errors + ([f"超过周上限，截断 {truncated} 篇候选"] if truncated else []))
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    (REPORT_DIR / "last_run.json").write_text(json.dumps({
        "date": today, "dry_run": args.dry_run, "since": args.since,
        "new_cards": 0 if args.dry_run else len(new_cards),
        "candidates": len(candidates), "fresh": len(fresh),
        "dropped": len(dropped), "report": report_path.name,
    }, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"new cards: {len(new_cards)}, dropped: {len(dropped)}, report: {report_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
