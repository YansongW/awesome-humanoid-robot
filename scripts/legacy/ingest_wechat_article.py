#!/usr/bin/env python3
"""Fetch a WeChat article, extract paper metadata, and optionally import into the graph.

Usage:
    python scripts/ingest_wechat_article.py --url https://mp.weixin.qq.com/s/xxxxx --output data/curated/wechat_article_xx.json
    python scripts/ingest_wechat_article.py --url https://mp.weixin.qq.com/s/xxxxx --import-graph
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date
from pathlib import Path
from typing import Any
from urllib.parse import urljoin, urlparse

import requests
import yaml
from bs4 import BeautifulSoup

from ai4sci_lib import config, entry_builder


ROOT = config.ROOT
RESEARCH_DIR = config.RESEARCH_DIR
DEFAULT_OUTPUT_DIR = ROOT / "data" / "curated"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
}

CATEGORY_HINTS: dict[str, str] = {
    "运控": "运控基座与通用全身跟踪",
    "全身跟踪": "运控基座与通用全身跟踪",
    "移动操作": "视觉感知驱动的人形移动操作",
    "语言控制": "生成式运动、语言控制与轨迹规划",
    "轨迹规划": "生成式运动、语言控制与轨迹规划",
    "生成式": "生成式运动、语言控制与轨迹规划",
    "动捕": "动捕、人类视频与交互动作规划",
    "人类视频": "动捕、人类视频与交互动作规划",
    "遥操作": "数据采集与遥操作系统",
    "数据采集": "数据采集与遥操作系统",
    "硬件": "硬件平台、感知配置与部署扩展",
    "VLA": "人形 VLA、世界模型与通用操作",
    "世界模型": "人形 VLA、世界模型与通用操作",
    "第一视角": "从人类第一视角视频学习",
    "egocentric": "从人类第一视角视频学习",
    "强化学习": "动作数据、重定向、遥操作和交互保真",
    "重定向": "动作数据、重定向、遥操作和交互保真",
    "课程学习": "强化学习奖励、课程学习与鲁棒策略",
    "鲁棒策略": "强化学习奖励、课程学习与鲁棒策略",
    "足式": "全身或足式运动策略与Sim-to-Real",
    "Sim-to-Real": "全身或足式运动策略与Sim-to-Real",
    "多接触": "全身多接触任务与运动合成",
}


def fetch_article(url: str) -> str:
    resp = requests.get(url, headers=HEADERS, timeout=30)
    resp.raise_for_status()
    resp.encoding = resp.apparent_encoding or "utf-8"
    return resp.text


def normalize_title(title: str) -> str:
    title = re.sub(r"[\n\r\t]+", " ", title)
    title = re.sub(r"\s+", " ", title)
    title = title.strip("|•●◆▶\[\]（）()")
    # remove leading numbering like 001, 01, 1.
    title = re.sub(r"^\d+[\.、]\s*", "", title)
    return title.strip()


def _extract_year(text: str) -> str | None:
    m = re.search(r"20\d{2}", text)
    return m.group(0) if m else None


def _arxiv_id_from(url: str) -> str | None:
    m = re.search(r"arxiv\.org/abs/(\d+\.\d+)", url)
    return m.group(1) if m else None


def guess_category(text: str) -> str:
    text = text.lower()
    for hint, cat in CATEGORY_HINTS.items():
        if hint.lower() in text:
            return cat
    return ""


def parse_papers(html: str) -> list[dict[str, Any]]:
    soup = BeautifulSoup(html, "html.parser")
    content = soup.find(id="js_content") or soup.body
    if not content:
        return []

    papers: list[dict[str, Any]] = []
    seen_titles: set[str] = set()

    # Each paper block is usually a section starting with a bold title heading followed by metadata.
    # We iterate over all elements and detect headings.
    current_title: str | None = None
    current_category: str = ""
    current_text: list[str] = []

    def flush() -> None:
        nonlocal current_title
        if not current_title:
            return
        title = normalize_title(current_title)
        if not title or len(title) < 8:
            current_title = None
            current_text.clear()
            return
        body = "\n".join(current_text)
        # find project/arxiv/code urls
        project_url = ""
        arxiv_url = ""
        code_url = ""
        for m in re.finditer(r"https?://[^\s<>\"')，。；：、\]]+", body):
            u = m.group(0).rstrip(".,;:'\")")
            if "arxiv.org" in u:
                arxiv_url = u
            elif any(x in u.lower() for x in ["github.com", "gitlab"]):
                code_url = u
            elif not project_url and any(x in u for x in [".github.io", "sites.google", "project", "web", "page"]):
                project_url = u
            elif not project_url:
                project_url = u
        year = _extract_year(body) or _extract_year(title) or str(date.today().year)
        category = current_category or guess_category(body) or guess_category(title)
        summary_match = re.search(r"(?:算法实现总结|一句话说明|核心内容)[:：]\s*(.+)", body, re.S)
        summary = summary_match.group(1).strip() if summary_match else ""
        institution_match = re.search(r"(?:机构|单位)[:：]\s*(.+)", body)
        institution = institution_match.group(1).strip() if institution_match else ""

        key = title.lower()
        if key not in seen_titles:
            seen_titles.add(key)
            papers.append({
                "title": title,
                "year": year,
                "category": category,
                "institution": institution,
                "summary": summary,
                "arxiv_url": arxiv_url,
                "arxiv_id": _arxiv_id_from(arxiv_url) or "",
                "project_url": project_url,
                "code_url": code_url,
            })
        current_title = None
        current_text.clear()

    for elem in content.find_all(["p", "section", "h1", "h2", "h3", "h4", "li"]):
        text = elem.get_text(" ", strip=True)
        if not text:
            continue
        # category headings
        if re.match(r"^(\d{2}[\.、]|#+\s*)\s*[^：]+[:：]", text):
            maybe_cat = re.sub(r"^(\d{2}[\.、]|#+\s*)\s*", "", text).split("：")[0].strip()
            if maybe_cat and len(maybe_cat) < 40:
                current_category = maybe_cat
            continue
        # paper title headings often look like "### 001 Title｜Subtitle" or bold short name
        if re.match(r"^(###\s+|\d{3}\s+|\d{2}\s+|【.+?】)", text) or (
            elem.name in ("h1", "h2", "h3", "h4") and len(text) < 150
        ):
            flush()
            current_title = text
            continue
        if current_title:
            current_text.append(text)

    flush()
    return papers


def load_existing_titles_and_arxiv() -> tuple[set[str], set[str]]:
    titles: set[str] = set()
    arxiv_ids: set[str] = set()
    for path in RESEARCH_DIR.rglob("*.md"):
        try:
            text = path.read_text(encoding="utf-8")
            if not text.startswith("---"):
                continue
            _, rest = text.split("---", 1)
            yaml_text, _ = rest.split("---", 1)
            data = yaml.safe_load(yaml_text) or {}
            names = data.get("names", {})
            if isinstance(names, dict):
                titles.add(names.get("en", "").strip().lower())
                titles.add(names.get("zh", "").strip().lower())
            for src in data.get("sources", []):
                url = src.get("url", "")
                m = re.search(r"arxiv\.org/abs/(\d+\.\d+)", str(url))
                if m:
                    arxiv_ids.add(m.group(1))
        except Exception:
            continue
    return titles, arxiv_ids


def build_entry(
    paper: dict[str, Any],
    existing_titles: set[str],
    existing_arxiv: set[str],
    existing_ids: set[str],
) -> dict[str, Any] | None:
    title = paper["title"].strip()
    if not title:
        return None
    key = title.lower()
    if key in existing_titles:
        print(f"[skip duplicate title] {title}")
        return None
    arxiv_id = paper.get("arxiv_id", "")
    if arxiv_id and arxiv_id in existing_arxiv:
        print(f"[skip duplicate arxiv] {arxiv_id} - {title}")
        return None

    year = str(paper.get("year", date.today().year))
    title_slug = entry_builder._slugify(title, max_len=30)
    ent_id = f"ent_paper_{title_slug}_{year}"
    candidate_id = ent_id
    counter = 1
    while candidate_id in existing_ids:
        candidate_id = f"{ent_id}_{counter}"
        counter += 1
    ent_id = candidate_id
    existing_ids.add(ent_id)
    existing_titles.add(key)
    if arxiv_id:
        existing_arxiv.add(arxiv_id)

    names = {"en": title, "zh": title, "ko": ""}
    summary_text = paper.get("summary", "") or f"{title} 是一篇 {year} 年人形机器人相关论文。"
    summary = {"en": summary_text, "zh": summary_text, "ko": ""}

    tags = set(["humanoid", entry_builder._slugify(title.split(":")[0], max_len=30)])
    category = paper.get("category", "")
    if category:
        tags.add(entry_builder._slugify(category, max_len=20))
    tags = sorted(t for t in tags if t)

    today = str(date.today())
    sources: list[dict[str, Any]] = []
    if arxiv_id:
        sources.append({
            "id": "src_001",
            "type": "paper",
            "title": f"{title} (arXiv)",
            "url": f"https://arxiv.org/abs/{arxiv_id}",
            "date": year,
            "accessed_at": today,
        })
    project_url = paper.get("project_url", "")
    if project_url:
        src_id = "src_002" if arxiv_id else "src_001"
        sources.append({
            "id": src_id,
            "type": "website",
            "title": f"{title} project page",
            "url": project_url,
            "date": year,
            "accessed_at": today,
        })
    if not sources:
        sources.append({
            "id": "src_001",
            "type": "website",
            "title": title,
            "url": "",
            "date": year,
            "accessed_at": today,
        })

    notes = "Imported from WeChat article using ingest_wechat_article.py."
    if category:
        notes += f" Category: {category}."
    if arxiv_id:
        notes += f" arXiv: {arxiv_id}."

    return {
        "$id": ent_id,
        "$schema": "../../data/schema/v1/entry_schema.json",
        "$version": 1,
        "type": "paper",
        "names": names,
        "summary": summary,
        "domains": ["07_ai_models_algorithms"],
        "layers": ["intelligence"],
        "functional_roles": ["knowledge", "intelligence"],
        "tags": tags,
        "theoretical_depth": ["system"],
        "verification": {
            "status": "partially_verified" if arxiv_id else "unverified",
            "reviewed_by": "ai",
            "reviewed_at": today,
            "confidence": "medium" if arxiv_id else "low",
            "notes": notes,
        },
        "sources": sources,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Ingest paper metadata from a WeChat article.")
    parser.add_argument("--url", required=True, help="WeChat article URL")
    parser.add_argument("--output", help="Output JSON path (optional)")
    parser.add_argument("--import-graph", action="store_true", help="Write entries directly to research/papers/")
    parser.add_argument("--dry-run", action="store_true", help="Preview without writing")
    args = parser.parse_args()

    print(f"Fetching {args.url} ...")
    html = fetch_article(args.url)
    papers = parse_papers(html)
    print(f"Extracted {len(papers)} paper entries.")

    if args.output:
        out_path = Path(args.output)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(json.dumps({"source": args.url, "papers": papers}, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"Wrote extracted metadata to {out_path}")

    if args.import_graph or args.dry_run:
        existing_titles, existing_arxiv = load_existing_titles_and_arxiv()
        existing_ids = entry_builder.load_existing_ids()
        added = 0
        skipped = 0
        for paper in papers:
            fm = build_entry(paper, existing_titles, existing_arxiv, existing_ids)
            if fm is None:
                skipped += 1
                continue
            if args.dry_run:
                print(f"[dry-run] {fm['$id']}: {fm['names']['en'][:80]}")
            else:
                path = entry_builder.write_entry_file(fm, fm["summary"]["en"] or "", "papers", f"{fm['$id']}.md")
                print(f"[wrote] {path.name}")
            added += 1
        print(f"\nTotal: {len(papers)} | Added: {added} | Skipped: {skipped}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
