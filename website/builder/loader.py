"""Load entries and relationships from the knowledge graph Markdown files."""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, List, Optional, Tuple

import yaml

ROOT = Path(__file__).resolve().parent.parent.parent
RESEARCH_DIR = ROOT / "research"
RELATIONSHIPS_DIR = ROOT / "data" / "relationships"

# Domain display labels by language
DOMAIN_LABELS = {
    "zh": {
        "00_foundations": "基础学科",
        "01_raw_materials": "原材料",
        "02_components": "零部件",
        "03_manufacturing_processes": "制造工艺",
        "04_assembly_integration_testing": "组装集成测试",
        "05_mass_production": "量产制造",
        "06_design_engineering": "设计工程",
        "07_ai_models_algorithms": "AI 模型与算法",
        "08_software_middleware": "软件中间件",
        "09_data_datasets": "数据与数据集",
        "10_evaluation_benchmarks": "评测基准",
        "10_benchmarks_evaluation": "评测基准",
        "11_applications_markets": "应用与市场",
        "12_policy_regulation_ethics": "政策法规伦理",
    },
    "en": {
        "00_foundations": "Foundations",
        "01_raw_materials": "Raw Materials",
        "02_components": "Components",
        "03_manufacturing_processes": "Manufacturing Processes",
        "04_assembly_integration_testing": "Assembly, Integration & Testing",
        "05_mass_production": "Mass Production",
        "06_design_engineering": "Design Engineering",
        "07_ai_models_algorithms": "AI Models & Algorithms",
        "08_software_middleware": "Software & Middleware",
        "09_data_datasets": "Data & Datasets",
        "10_evaluation_benchmarks": "Evaluation & Benchmarks",
        "10_benchmarks_evaluation": "Evaluation & Benchmarks",
        "11_applications_markets": "Applications & Markets",
        "12_policy_regulation_ethics": "Policy, Regulation & Ethics",
    },
    "ko": {
        "00_foundations": "기초 학문",
        "01_raw_materials": "원자재",
        "02_components": "부품",
        "03_manufacturing_processes": "제조 공정",
        "04_assembly_integration_testing": "조립 통합 테스트",
        "05_mass_production": "대량 생산",
        "06_design_engineering": "설계 공학",
        "07_ai_models_algorithms": "AI 모델 및 알고리즘",
        "08_software_middleware": "소프트웨어 미들웨어",
        "09_data_datasets": "데이터 및 데이터셋",
        "10_evaluation_benchmarks": "평가 및 벤치마크",
        "10_benchmarks_evaluation": "평가 및 벤치마크",
        "11_applications_markets": "응용 및 시장",
        "12_policy_regulation_ethics": "정책 규제 윤리",
    },
}


# Entity type display labels by language
TYPE_LABELS = {
    "zh": {
        "algorithm": "算法",
        "benchmark": "评测基准",
        "company": "公司",
        "component": "零部件",
        "component_manufacturer": "零部件制造商",
        "concept": "概念",
        "dataset": "数据集",
        "equation": "方程",
        "formalism": "形式化方法",
        "foundation": "基础学科",
        "material": "材料",
        "method": "方法",
        "oem": "整机厂商",
        "operator": "运营商",
        "paper": "论文",
        "principle": "原理",
        "report": "报告",
        "robot_system": "机器人系统",
        "software_platform": "软件平台",
        "standard": "标准",
        "technology": "技术",
        "theorem": "定理",
        "tier1_supplier": "Tier 1 供应商",
        "tool_equipment": "工具设备",
        "application_scenario": "应用场景",
        "market_segment": "市场细分",
    },
    "en": {
        "algorithm": "Algorithm",
        "benchmark": "Benchmark",
        "company": "Company",
        "component": "Component",
        "component_manufacturer": "Component Manufacturer",
        "concept": "Concept",
        "dataset": "Dataset",
        "equation": "Equation",
        "formalism": "Formalism",
        "foundation": "Foundation",
        "material": "Material",
        "method": "Method",
        "oem": "OEM",
        "operator": "Operator",
        "paper": "Paper",
        "principle": "Principle",
        "report": "Report",
        "robot_system": "Robot System",
        "software_platform": "Software Platform",
        "standard": "Standard",
        "technology": "Technology",
        "theorem": "Theorem",
        "tier1_supplier": "Tier 1 Supplier",
        "tool_equipment": "Tool / Equipment",
        "application_scenario": "Application Scenario",
        "market_segment": "Market Segment",
    },
    "ko": {
        "algorithm": "알고리즘",
        "benchmark": "벤치마크",
        "company": "기업",
        "component": "부품",
        "component_manufacturer": "부품 제조사",
        "concept": "개념",
        "dataset": "데이터셋",
        "equation": "방정식",
        "formalism": "형식화 방법",
        "foundation": "기초 학문",
        "material": "재료",
        "method": "방법",
        "oem": "완제품 업체",
        "operator": "운영사",
        "paper": "논문",
        "principle": "원리",
        "report": "보고서",
        "robot_system": "로봇 시스템",
        "software_platform": "소프트웨어 플랫폼",
        "standard": "표준",
        "technology": "기술",
        "theorem": "정리",
        "tier1_supplier": "Tier 1 공급업체",
        "tool_equipment": "도구/장비",
        "application_scenario": "응용 시나리오",
        "market_segment": "시장 세그먼트",
    },
}


LAYER_LABELS = {
    "zh": {
        "foundations": "基础层",
        "upstream": "上游",
        "midstream": "中游",
        "intelligence": "智能层",
        "validation_markets": "验证与市场层",
    },
    "en": {
        "foundations": "Foundations",
        "upstream": "Upstream",
        "midstream": "Midstream",
        "intelligence": "Intelligence",
        "validation_markets": "Validation & Markets",
    },
    "ko": {
        "foundations": "기초 계층",
        "upstream": "상위",
        "midstream": "중위",
        "intelligence": "지능 계층",
        "validation_markets": "검증 및 시장 계층",
    },
}


def domain_label(domain: str, lang: str = "zh") -> str:
    """Return a human-readable domain label in the requested language."""
    return DOMAIN_LABELS.get(lang, DOMAIN_LABELS["zh"]).get(domain, domain)


def type_label(type_name: str, lang: str = "zh") -> str:
    """Return a human-readable entity type label in the requested language."""
    return TYPE_LABELS.get(lang, TYPE_LABELS["zh"]).get(type_name, type_name)


def layer_label(layer_name: str, lang: str = "zh") -> str:
    """Return a human-readable value-chain layer label in the requested language."""
    key = (layer_name or "").strip().lower().replace(" ", "_").replace("-", "_")
    return LAYER_LABELS.get(lang, LAYER_LABELS["zh"]).get(key, layer_name)


def split_frontmatter(text: str, source: str = "<unknown>") -> tuple[dict[str, Any], str]:
    """Split Markdown frontmatter from body."""
    if not text.startswith("---"):
        return {}, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}, text
    try:
        front = yaml.safe_load(parts[1]) or {}
    except Exception as exc:
        import sys
        print(f"[warning] YAML parse error in {source}: {exc}", file=sys.stderr)
        front = {}
    return front, parts[2].strip()


def pick_lang(value: Any, lang: str = "zh") -> str:
    """Pick a language value from a dict or return string.

    Fallback order ensures every language site has usable content rather than
    empty fields when a translation is missing:
      - zh: zh -> en -> ko -> ""
      - en: en -> zh -> ko -> ""
      - ko: ko -> en -> zh -> ""
    """
    if isinstance(value, dict):
        order = {
            "zh": ["zh", "en", "ko"],
            "en": ["en", "zh", "ko"],
            "ko": ["ko", "en", "zh"],
        }.get(lang, [lang, "en", "zh", "ko"])
        for key in order:
            v = value.get(key)
            if v:
                return v
        return ""
    return str(value or "")


def _detect_heading_language(heading: str) -> Optional[str]:
    """Detect the dominant script of a Markdown heading.

    Returns 'zh', 'en', 'ko', or None if no language-specific characters are found.
    English headings may contain numbers and punctuation.
    """
    text = heading.strip()
    # Strip leading heading markers and whitespace.
    text = re.sub(r"^#+\s*", "", text).strip()
    if not text:
        return None

    has_zh = bool(re.search(r"[\u4e00-\u9fff]", text))
    has_ko = bool(re.search(r"[\uac00-\ud7af]", text))
    has_en = bool(re.search(r"[a-zA-Z]", text))

    if has_zh and not has_ko and not has_en:
        return "zh"
    if has_ko and not has_zh and not has_en:
        return "ko"
    if has_en and not has_zh and not has_ko:
        return "en"

    # Mixed or ambiguous headings (e.g., "PID 控制") are treated as Chinese
    # because the primary content in this project is Chinese.
    if has_zh:
        return "zh"
    if has_ko:
        return "ko"
    if has_en:
        return "en"
    return None


def _detect_text_language(text: str) -> Optional[str]:
    """Detect dominant script of arbitrary text, treating code/math as neutral."""
    # Remove inline code/backticks and common markup before detection.
    cleaned = re.sub(r"`[^`]*`", "", text)
    cleaned = re.sub(r"\$[^$]*\$", "", cleaned)
    cleaned = re.sub(r"\$\$[^$]*\$\$", "", cleaned)
    return _detect_heading_language(cleaned)


def filter_body_by_language(body: str, lang: str) -> str:
    """Return only the body sections matching the requested language.

    Sections are split by headings (lines starting with #), while fenced code
    blocks are ignored so that ``#`` characters inside code are not treated as
    headings. For the Chinese site we keep Chinese and unknown-language
    sections; for English/Korean we keep only sections whose heading is clearly
    in that language. Lead paragraphs without a heading are kept unless they
    are clearly written in a different language.
    """
    lines = body.splitlines()
    sections: List[Tuple[Optional[str], List[str]]] = []
    current_heading: Optional[str] = None
    current_lines: List[str] = []
    in_code_block = False
    code_fence = ""

    for line in lines:
        stripped = line.strip()
        # Track fenced code blocks (``` or ~~~) so # inside them is ignored.
        fence_match = re.match(r"^(```+|~~~+)(\w*)\s*$", stripped)
        if fence_match:
            if not in_code_block:
                in_code_block = True
                code_fence = fence_match.group(1)
            elif stripped.startswith(code_fence) and len(stripped) >= len(code_fence):
                in_code_block = False
                code_fence = ""
            current_lines.append(line)
            continue

        if in_code_block:
            current_lines.append(line)
            continue

        if re.match(r"^#{1,6}\s+", line):
            if current_heading is not None or current_lines:
                sections.append((current_heading, current_lines))
            current_heading = line
            current_lines = []
        else:
            current_lines.append(line)
    if current_heading is not None or current_lines:
        sections.append((current_heading, current_lines))

    def _keep(heading: Optional[str], content: List[str]) -> bool:
        if heading is None:
            # Lead paragraph: keep if empty or not clearly in a different language.
            text = "\n".join(content)
            if not text.strip():
                return True
            detected = _detect_text_language(text)
            if detected is None:
                return True
            return detected == lang

        heading_lang = _detect_heading_language(heading)
        if heading_lang is None:
            # Unknown script headings are kept only on the Chinese site
            # because the majority of existing rich content is Chinese.
            return lang == "zh"
        return heading_lang == lang

    keep_sections = [(h, c) for h, c in sections if _keep(h, c)]

    if not keep_sections:
        return ""

    # The template already renders entry.name as <h1>, so drop the redundant
    # first-level heading from the body to avoid duplicating the title across
    # the top of the page.
    if keep_sections and keep_sections[0][0] and keep_sections[0][0].startswith("# "):
        keep_sections = keep_sections[1:]

    out_lines: List[str] = []
    for heading, content in keep_sections:
        if heading:
            out_lines.append(heading)
        out_lines.extend(content)
    return "\n".join(out_lines).strip()


def tokenize(text: str) -> list[str]:
    """Tokenize text for search; English words and CJK characters."""
    text = text or ""
    tokens: list[str] = []
    for part in re.findall(r"[a-zA-Z0-9]+|[\u4e00-\u9fff\uac00-\ud7af]", text):
        if part[0].isascii():
            tokens.append(part.lower())
        else:
            tokens.extend(list(part.lower()))
    return tokens


@dataclass
class Entry:
    id: str
    type: str
    name: str
    name_en: str
    summary: str
    domains: list[str]
    layers: list[str]
    tags: list[str]
    body: str
    body_html: str
    frontmatter: dict[str, Any]
    path: Path

    @property
    def url(self) -> str:
        return f"entry/{self.id}/"


@dataclass
class Relationship:
    id: str
    type: str
    source_id: str
    target_id: str
    source_name: str
    target_name: str
    description: str


@dataclass
class KGStore:
    entries: dict[str, Entry] = field(default_factory=dict)
    relationships: list[Relationship] = field(default_factory=list)
    outgoing: dict[str, list[Relationship]] = field(default_factory=dict)
    incoming: dict[str, list[Relationship]] = field(default_factory=dict)
    lang: str = "zh"

    def load(self, lang: str | None = None) -> None:
        if lang:
            self.lang = lang
        self.entries.clear()
        self.relationships.clear()
        self.outgoing.clear()
        self.incoming.clear()

        import markdown

        md = markdown.Markdown(
            extensions=["extra", "toc", "tables", "pymdownx.arithmatex"],
            extension_configs={"pymdownx.arithmatex": {"generic": True}},
        )

        for path in RESEARCH_DIR.rglob("*.md"):
            text = path.read_text(encoding="utf-8")
            front, body = split_frontmatter(text, source=str(path))
            eid = front.get("$id")
            if not eid:
                continue

            names = front.get("names", {})
            summaries = front.get("summary", {})
            filtered_body = filter_body_by_language(body, self.lang)
            entry = Entry(
                id=str(eid),
                type=front.get("type", "unknown"),
                name=pick_lang(names, self.lang),
                name_en=pick_lang(names, "en"),
                summary=pick_lang(summaries, self.lang),
                domains=front.get("domains", []) or [],
                layers=front.get("layers", []) or [],
                tags=front.get("tags", []) or [],
                body=filtered_body,
                body_html=md.convert(filtered_body),
                frontmatter=front,
                path=path,
            )
            md.reset()
            self.entries[entry.id] = entry

        if RELATIONSHIPS_DIR.exists():
            for path in RELATIONSHIPS_DIR.rglob("*.md"):
                text = path.read_text(encoding="utf-8")
                front, _ = split_frontmatter(text, source=str(path))
                rid = front.get("$id")
                if not rid:
                    continue
                source = front.get("source", {}) or {}
                target = front.get("target", {}) or {}
                source_id = source.get("id", "") if isinstance(source, dict) else ""
                target_id = target.get("id", "") if isinstance(target, dict) else ""
                description = pick_lang(front.get("description", {}), self.lang)

                rel = Relationship(
                    id=str(rid),
                    type=front.get("type", "unknown"),
                    source_id=source_id,
                    target_id=target_id,
                    source_name=self.entries.get(source_id, Entry(id=source_id, type="", name=source_id, name_en="", summary="", domains=[], layers=[], tags=[], body="", body_html="", frontmatter={}, path=Path())).name,
                    target_name=self.entries.get(target_id, Entry(id=target_id, type="", name=target_id, name_en="", summary="", domains=[], layers=[], tags=[], body="", body_html="", frontmatter={}, path=Path())).name,
                    description=description,
                )
                self.relationships.append(rel)
                self.outgoing.setdefault(source_id, []).append(rel)
                self.incoming.setdefault(target_id, []).append(rel)

    def related_entries(self, eid: str) -> list[Entry]:
        ids = set()
        for rel in self.outgoing.get(eid, []) + self.incoming.get(eid, []):
            ids.add(rel.source_id if rel.source_id != eid else rel.target_id)
        return [self.entries[i] for i in ids if i in self.entries and i != eid]
