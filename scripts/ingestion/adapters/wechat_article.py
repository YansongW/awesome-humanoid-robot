"""Adapter for WeChat articles.

Supports two modes:
1. A JSON file with extracted article text (data/curated/wechat_*.json).
2. A single mp.weixin.qq.com URL to be fetched via FetchURL / WebBridge.

When no URL list exists, the adapter returns an empty list and sets the source
status to pending.
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

from ai4sci_lib import entry_builder

from ..core import ParsedItem, Source


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


def _extract_arxiv_id(url: str) -> str:
    if not url:
        return ""
    m = re.search(r"arxiv\.org/abs/(\d+\.\d+)", url)
    return m.group(1) if m else ""


class WechatArticleAdapter:
    """Adapter for WeChat articles."""

    source_id = "wechat_articles"

    def fetch(self, source: Source) -> list[ParsedItem]:
        urls = source.extra.get("urls", []) if source.extra else []
        if not urls and source.url:
            urls = [source.url]
        if not urls:
            return []

        items: list[ParsedItem] = []
        for url in urls:
            if url.endswith(".json") and Path(url).exists():
                items.extend(self._parse_json_file(Path(url)))
            else:
                # URL-only mode: the pipeline must have fetched content separately.
                # This adapter expects extracted text in source.extra["texts"].
                text = source.extra.get("texts", {}).get(url, "") if source.extra else ""
                if text:
                    items.extend(self._parse_text(text, url))
        return items

    def _parse_json_file(self, path: Path) -> list[ParsedItem]:
        data = json.loads(path.read_text(encoding="utf-8"))
        papers = data.get("papers", [])
        return [self._paper_to_item(p, data.get("source", "")) for p in papers]

    def _parse_text(self, text: str, source_url: str) -> list[ParsedItem]:
        # Minimal parser: expects sections like "### 001 Title｜Subtitle" followed by metadata.
        items: list[ParsedItem] = []
        current_title: str | None = None
        current_texts: list[str] = []
        current_category = ""

        def flush() -> None:
            nonlocal current_title
            if not current_title:
                return
            title = self._normalize_title(current_title)
            if not title or len(title) < 8:
                current_title = None
                current_texts.clear()
                return
            body = "\n".join(current_texts)
            items.append(self._build_item(title, body, current_category, source_url))
            current_title = None
            current_texts.clear()

        for line in text.splitlines():
            line = line.strip()
            if not line:
                continue
            if re.match(r"^(\d{2}[\.、]|#+\s*)\s*[^：]+[:：]", line):
                maybe_cat = re.sub(r"^(\d{2}[\.、]|#+\s*)\s*", "", line).split("：")[0].strip()
                if maybe_cat and len(maybe_cat) < 40:
                    current_category = maybe_cat
                continue
            if re.match(r"^(###\s+|\d{3}\s+|\d{2}\s+|【.+?】)", line) or (
                len(line) < 150 and (line.startswith("001 ") or line.startswith("01 "))
            ):
                flush()
                current_title = line
                continue
            if current_title:
                current_texts.append(line)

        flush()
        return items

    def _build_item(self, title: str, body: str, category: str, source_url: str) -> ParsedItem:
        arxiv_id = ""
        project_url = ""
        for m in re.finditer(r"https?://[^\s<>\"')，。；：、\]]+", body):
            u = m.group(0).rstrip(".,;:'\")")
            if "arxiv.org" in u:
                arxiv_id = _extract_arxiv_id(u)
            elif not project_url:
                project_url = u
        year = self._extract_year(body, title)
        category = category or self._guess_category(body + " " + title)
        summary_match = re.search(r"(?:算法实现总结|一句话说明|核心内容)[:：]\s*(.+)", body, re.S)
        summary = summary_match.group(1).strip() if summary_match else f"{title} 是一篇关于{category}的人形机器人研究工作。"
        tags = {"humanoid", entry_builder._slugify(title.split(":")[0], max_len=30)}
        if category:
            tags.add(entry_builder._slugify(category, max_len=20))
        return ParsedItem(
            title=title,
            type="paper",
            year=year,
            names={"en": title, "zh": title, "ko": ""},
            summary={"en": summary, "zh": summary, "ko": ""},
            domains=["07_ai_models_algorithms"],
            tags=sorted(t for t in tags if t),
            arxiv_id=arxiv_id,
            source_url=arxiv_id or project_url or source_url,
            source_type="paper" if arxiv_id else "website",
            raw={"category": category},
        )

    @staticmethod
    def _normalize_title(title: str) -> str:
        title = re.sub(r"[\n\r\t]+", " ", title)
        title = re.sub(r"\s+", " ", title)
        title = title.strip("|•●◆▶\[\]（）()")
        title = re.sub(r"^\d+[\.、]\s*", "", title)
        return title.strip()

    @staticmethod
    def _extract_year(*texts: str) -> str:
        for text in texts:
            m = re.search(r"20\d{2}", text)
            if m:
                return m.group(0)
        return "2026"

    @staticmethod
    def _guess_category(text: str) -> str:
        text = text.lower()
        for hint, cat in CATEGORY_HINTS.items():
            if hint.lower() in text:
                return cat
        return ""
