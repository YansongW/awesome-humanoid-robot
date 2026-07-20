"""Render static HTML pages using Jinja2 templates."""

from __future__ import annotations

import json
import os
import re
import shutil
import xml.sax.saxutils as saxutils
from pathlib import Path
from typing import Any

from jinja2 import Environment, FileSystemLoader, select_autoescape

from website.builder.loader import DOMAIN_LABELS, KGStore, Relationship, domain_label, layer_label, type_label
from website.builder.minify import minify_assets
from website.builder.search_index import build_names_index

BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = BASE_DIR / "templates"
SRC_DIR = BASE_DIR / "src"
DIST_DIR = BASE_DIR / "dist"

# Base URL for sitemap and canonical links. Override via RTKG_SITE_URL env var.
SITE_BASE_URL = os.environ.get("RTKG_SITE_URL", "https://kg.rounds-tech.com").rstrip("/")


# UI strings for the three supported languages.
UI_STRINGS = {
    "zh": {
        "site_title": "人形机器人知识图谱",
        "site_subtitle": "从矿山到市场的人形机器人知识图谱",
        "nav_home": "首页",
        "nav_graph": "关系图谱",
        "nav_search": "搜索",
        "nav_wiki": "Wiki",
        "search_placeholder": "搜索实体、论文、公司…",
        "hero_title": "人形机器人：从矿山到市场的知识图谱",
        "hero_subtitle": "系统梳理人形机器人全产业链——材料、零部件、制造、设计、AI、软件、数据、测试、量产、应用、市场与政策。",
        "stat_entries": "实体",
        "stat_relationships": "关系",
        "stat_types": "实体类型",
        "stat_domains": "领域",
        "explore_by_domain": "按领域探索",
        "explore_by_type": "按类型浏览",
        "featured_entities": "精选实体",
        "view_all": "查看全部",
        "open_graph": "打开关系图谱",
        "graph_title": "关系图谱",
        "graph_summary": "探索 {entries} 个实体与 {relationships} 条关系",
        "search_entities": "搜索实体",
        "filter_by_domain": "按领域过滤",
        "legend": "图例",
        "reset_view": "重置视图",
        "fit_window": "适配窗口",
        "cluster_view": "聚类视图",
        "full_view": "全图视图",
        "recommended": "推荐",
        "search_title": "搜索知识图谱",
        "search_input_placeholder": "输入关键词，例如：减速器、特斯拉、VLA…",
        "filter_by_type": "按类型筛选：",
        "all": "全部",
        "results_title": "全部实体",
        "results_count": "共 {count} 条结果",
        "no_results_for": "未找到与 “{query}” 相关的实体。",
        "loading": "正在加载搜索索引…",
        "load_more": "加载更多",
        "not_found": "未找到",
        "wiki_banner_title": "Wiki 项目",
        "wiki_banner_text": "本知识图谱是《人形机器人：从矿山到市场》Wiki 的底层数据系统，按“物理层 → 感知层 → 决策层 → 执行层 → 系统层 → 产业层”展开。",
        "read_wiki_toc": "阅读 Wiki 目录",
        "nav_roadmap": "路线图",
        "roadmap_banner_title": "0→1 造一台人形机器人",
        "roadmap_banner_text": "面向零基础动手者的实操路线图：从基础筑基、造一个关节、双足平台到完整人形。每一步都链接知识卡片，告诉你做什么、为什么、怎么根据自己的情况分析选型。",
        "roadmap_banner_cta": "开始路线图",
        "nav_about": "关于",
        "summary": "摘要",
        "domains": "领域",
        "layers": "层级",
        "verification": "审校",
        "verified": "已审校",
        "pending": "待审校",
        "draft": "草稿",
        "aliases": "多语言名称",
        "sources": "来源与参考",
        "wiki_chapters": "Wiki 章节",
        "related_entities": "知识关联",
        "relations": "关系",
        "outgoing": "发出的关系",
        "incoming": "指向它的关系",
        "subgraph": "关系子图",
        "graph_hint": "拖拽节点可调整布局，滚轮缩放，点击查看实体详情。",
        "nav_aria_label": "主导航",
        "theme_aria_label": "切换主题",
        "menu_aria_label": "菜单",
        "breadcrumb_aria_label": "面包屑",
        "search_aria_label": "搜索",
        "theme_toggle_light": "浅色模式",
        "theme_toggle_dark": "深色模式",
        "graph_loading": "正在加载图谱…",
        "graph_empty": "没有可显示的关系数据。",
        "graph_no_relations": "暂无关系数据",
        "graph_cluster_count": "{name}\n{count} 个实体",
        "graph_cluster_pruned": "（显示前 {count} 个核心实体）",
        "graph_cluster_total": "（{count}）",
        "graph_confirm_full": "当前有 {total} 个节点，全图将只显示连接度最高的前 {count} 个节点以保持流畅。是否继续？",
        "graph_entity_count": "{count} 个实体",
        "search_empty": "输入关键词或选择类型以开始搜索。",
        "search_loading": "正在加载搜索索引…",
        "wiki_chapter": "第 {number} 章",
        "layer_foundations": "基础层",
        "layer_upstream": "上游",
        "layer_midstream": "中游",
        "layer_intelligence": "智能层",
        "layer_validation_markets": "验证与市场层",
        "skip_to_content": "跳转到主内容",
        "toc_title": "本页目录",
        "prev_page": "上一页",
        "next_page": "下一页",
        "untranslated_notice": "",
        "entries_of_type": "{count} 个实体",
        "back_to_top": "回到顶部",
        "roadmap_label": "0→1 路线图定位",
    },
    "en": {
        "site_title": "Humanoid Robot Knowledge Graph",
        "site_subtitle": "From Mine to Market: A Knowledge Graph for Humanoid Robots",
        "nav_home": "Home",
        "nav_graph": "Graph",
        "nav_search": "Search",
        "nav_wiki": "Wiki",
        "search_placeholder": "Search entities, papers, companies…",
        "hero_title": "Humanoid Robots: From Mine to Market",
        "hero_subtitle": "A systematic map of the humanoid robot value chain—materials, components, manufacturing, design, AI, software, data, testing, mass production, applications, markets, and policy.",
        "stat_entries": "Entities",
        "stat_relationships": "Relations",
        "stat_types": "Types",
        "stat_domains": "Domains",
        "explore_by_domain": "Explore by Domain",
        "explore_by_type": "Browse by Type",
        "featured_entities": "Featured Entities",
        "view_all": "View all",
        "open_graph": "Open Graph",
        "graph_title": "Relation Graph",
        "graph_summary": "Explore {entries} entities and {relationships} relations",
        "search_entities": "Search entities",
        "filter_by_domain": "Filter by domain",
        "legend": "Legend",
        "reset_view": "Reset view",
        "fit_window": "Fit window",
        "cluster_view": "Cluster view",
        "full_view": "Full graph",
        "recommended": "Recommended",
        "search_title": "Search Knowledge Graph",
        "search_input_placeholder": "Enter keywords, e.g. reducer, Tesla, VLA…",
        "filter_by_type": "Filter by type:",
        "all": "All",
        "results_title": "All entities",
        "results_count": "{count} results",
        "no_results_for": "No entities found for “{query}”.",
        "loading": "Loading search index…",
        "load_more": "Load more",
        "not_found": "Not Found",
        "wiki_banner_title": "Wiki Project",
        "wiki_banner_text": "This knowledge graph underpins the Humanoid Robots: From Mine to Market wiki, organized from physics → perception → decision → actuation → system → industry.",
        "read_wiki_toc": "Read Wiki TOC",
        "nav_roadmap": "Roadmap",
        "roadmap_banner_title": "Build a Humanoid from 0 to 1",
        "roadmap_banner_text": "A hands-on roadmap for complete beginners: foundations, one joint, a biped platform, then a full humanoid. Every step links to knowledge cards explaining what to do, why, and how to analyze your own case.",
        "roadmap_banner_cta": "Start the Roadmap",
        "nav_about": "About",
        "summary": "Summary",
        "domains": "Domains",
        "layers": "Layers",
        "verification": "Verification",
        "verified": "Verified",
        "pending": "Pending",
        "draft": "Draft",
        "aliases": "Names",
        "sources": "Sources",
        "wiki_chapters": "Wiki Chapters",
        "related_entities": "Related",
        "relations": "Relations",
        "outgoing": "Outgoing",
        "incoming": "Incoming",
        "subgraph": "Relation Subgraph",
        "graph_hint": "Drag nodes to adjust layout, scroll to zoom, click for details.",
        "nav_aria_label": "Main navigation",
        "theme_aria_label": "Toggle theme",
        "menu_aria_label": "Menu",
        "breadcrumb_aria_label": "Breadcrumb",
        "search_aria_label": "Search",
        "theme_toggle_light": "Light mode",
        "theme_toggle_dark": "Dark mode",
        "graph_loading": "Loading graph…",
        "graph_empty": "No relation data to display.",
        "graph_no_relations": "No relation data yet",
        "graph_cluster_count": "{name}\\n{count} entities",
        "graph_cluster_pruned": "(showing top {count} core entities)",
        "graph_cluster_total": "({count})",
        "graph_confirm_full": "There are {total} nodes; the full graph will show only the top {count} most-connected nodes to stay smooth. Continue?",
        "graph_entity_count": "{count} entities",
        "search_empty": "Enter keywords or select a type to start searching.",
        "search_loading": "Loading search index…",
        "wiki_chapter": "Chapter {number}",
        "layer_foundations": "Foundations",
        "layer_upstream": "Upstream",
        "layer_midstream": "Midstream",
        "layer_intelligence": "Intelligence",
        "layer_validation_markets": "Validation & Markets",
        "skip_to_content": "Skip to main content",
        "toc_title": "On this page",
        "prev_page": "Previous",
        "next_page": "Next",
        "untranslated_notice": "This page has not been translated yet — the original Chinese content is shown below.",
        "entries_of_type": "{count} entries",
        "back_to_top": "Back to top",
        "roadmap_label": "0→1 Roadmap",
    },
    "ko": {
        "site_title": "휴로봇 지식 그래프",
        "site_subtitle": "광산에서 시장까지: 휴로봇 지식 그래프",
        "nav_home": "홈",
        "nav_graph": "그래프",
        "nav_search": "검색",
        "nav_wiki": "Wiki",
        "search_placeholder": "개체, 논문, 기업 검색…",
        "hero_title": "휴로봇: 광산에서 시장까지",
        "hero_subtitle": "재료, 부품, 제조, 설계, AI, 소프트웨어, 데이터, 테스트, 양산, 응용, 시장, 정책을 포괄하는 휴로봇 산업 전반의 체계적 지도입니다.",
        "stat_entries": "개체",
        "stat_relationships": "관계",
        "stat_types": "유형",
        "stat_domains": "영역",
        "explore_by_domain": "영역별 탐색",
        "explore_by_type": "유형별 탐색",
        "featured_entities": "추천 개체",
        "view_all": "전체 보기",
        "open_graph": "그래프 열기",
        "graph_title": "관계 그래프",
        "graph_summary": "{entries}개 개체와 {relationships}개 관계 탐색",
        "search_entities": "개체 검색",
        "filter_by_domain": "영역 필터",
        "legend": "범례",
        "reset_view": "보기 초기화",
        "fit_window": "창에 맞춤",
        "cluster_view": "클리스터 뷰",
        "full_view": "전체 그래프",
        "recommended": "추천",
        "search_title": "지식 그래프 검색",
        "search_input_placeholder": "키워드 입력, 예: 감속기, Tesla, VLA…",
        "filter_by_type": "유형별 필터:",
        "all": "전체",
        "results_title": "전체 개체",
        "results_count": "{count}개 결과",
        "no_results_for": "“{query}”에 대한 개체를 찾을 수 없습니다.",
        "loading": "검색 색인 로드 중…",
        "load_more": "더 보기",
        "not_found": "찾을 수 없음",
        "wiki_banner_title": "Wiki 프로젝트",
        "wiki_banner_text": "이 지식 그래프는 '휴로봇: 광산에서 시장까지' Wiki의 데이터 기반이며, 물리 → 인식 → 의사결정 → 구동 → 시스템 → 산업 순으로 전개됩니다.",
        "read_wiki_toc": "Wiki 목차 보기",
        "nav_roadmap": "로드맵",
        "roadmap_banner_title": "0→1 휴로봇 만들기",
        "roadmap_banner_text": "완전 초보자를 위한 실습 로드맵: 기초 다지기, 관절 하나, 이족 플랫폼, 완전한 휴로봇까지. 각 단계는 무엇을, 왜, 어떻게 분석할지 알려주는 지식 카드로 연결됩니다.",
        "roadmap_banner_cta": "로드맵 시작",
        "nav_about": "소개",
        "summary": "요약",
        "domains": "영역",
        "layers": "계층",
        "verification": "검증",
        "verified": "검증됨",
        "pending": "대기 중",
        "draft": "초안",
        "aliases": "다국어 이름",
        "sources": "출처",
        "wiki_chapters": "Wiki 장",
        "related_entities": "관련 개체",
        "relations": "관계",
        "outgoing": "나가는 관계",
        "incoming": "들어오는 관계",
        "subgraph": "관계 하위 그래프",
        "graph_hint": "노드를 드래그하여 레이아웃을 조정하고, 휠로 확대/축소하며, 클릭하면 상세 정보를 볼 수 있습니다.",
        "nav_aria_label": "주요 탐색",
        "theme_aria_label": "테마 전환",
        "menu_aria_label": "메뉴",
        "breadcrumb_aria_label": "브레드크럼",
        "search_aria_label": "검색",
        "theme_toggle_light": "라이트 모드",
        "theme_toggle_dark": "다크 모드",
        "graph_loading": "그래프 로드 중…",
        "graph_empty": "표시할 관계 데이터가 없습니다.",
        "graph_no_relations": "관계 데이터가 없습니다",
        "graph_cluster_count": "{name}\\n{count}개 개체",
        "graph_cluster_pruned": "(상위 {count}개 핵심 개체 표시)",
        "graph_cluster_total": "({count})",
        "graph_confirm_full": "현재 {total}개 노드가 있습니다. 전체 그래프는 최상위 연결 {count}개 노드만 표시하여 부드럽게 유지합니다. 계속하시겠습니까?",
        "graph_entity_count": "{count}개 개체",
        "search_empty": "키워드를 입력하거나 유형을 선택하여 검색을 시작하세요.",
        "search_loading": "검색 색인 로드 중…",
        "wiki_chapter": "{number}장",
        "layer_foundations": "기초 계층",
        "layer_upstream": "상위",
        "layer_midstream": "중위",
        "layer_intelligence": "지능 계층",
        "layer_validation_markets": "검증 및 시장 계층",
        "skip_to_content": "주요 콘텐츠로 건너뛰기",
        "toc_title": "이 페이지 목차",
        "prev_page": "이전",
        "next_page": "다음",
        "untranslated_notice": "이 페이지는 아직 번역되지 않았습니다. 아래에 중국어 원문을 표시합니다.",
        "entries_of_type": "{count}개 개체",
        "back_to_top": "맨 위로",
        "roadmap_label": "0→1 로드맵",
    },
}


def ui_string(lang: str, key: str) -> str:
    return UI_STRINGS.get(lang, UI_STRINGS["zh"]).get(key, key)


# Relationship type display labels by language.
REL_TYPE_LABELS = {
    "zh": {
        "addresses": "应对", "analyzes": "分析", "applies_to": "应用于",
        "cites": "引用", "combines_with": "结合", "constrains": "约束",
        "derived_from": "衍生自", "enables": "使能", "evaluates": "评估",
        "evaluates_on": "评测于", "formalizes": "形式化", "has_prerequisite": "前置依赖",
        "implemented_on": "实现于", "includes": "包含", "instantiates": "实例化",
        "integrates": "集成", "is_alternative_to": "可替代", "is_based_on": "基于",
        "is_part_of": "属于", "is_regulated_by": "受制于", "is_version_of": "版本",
        "manufacturer_of": "制造", "mentions": "提及", "models": "建模",
        "produces": "生产", "requires": "依赖", "serves": "服务",
        "solves": "解决", "sources_from": "采购自", "supplies": "供应",
        "tested_with": "测试于", "uses": "使用", "uses_data": "使用数据",
        "uses_dataset": "使用数据集", "uses_product_of": "使用其产品", "uses_technology": "采用技术",
        "validates_on": "验证于", "verified_by": "验证于",
    },
    "en": {
        "addresses": "addresses", "analyzes": "analyzes", "applies_to": "applies to",
        "cites": "cites", "combines_with": "combines with", "constrains": "constrains",
        "derived_from": "derived from", "enables": "enables", "evaluates": "evaluates",
        "evaluates_on": "evaluates on", "formalizes": "formalizes", "has_prerequisite": "has prerequisite",
        "implemented_on": "implemented on", "includes": "includes", "instantiates": "instantiates",
        "integrates": "integrates", "is_alternative_to": "alternative to", "is_based_on": "based on",
        "is_part_of": "part of", "is_regulated_by": "regulated by", "is_version_of": "version of",
        "manufacturer_of": "manufacturer of", "mentions": "mentions", "models": "models",
        "produces": "produces", "requires": "requires", "serves": "serves",
        "solves": "solves", "sources_from": "sources from", "supplies": "supplies",
        "tested_with": "tested with", "uses": "uses", "uses_data": "uses data",
        "uses_dataset": "uses dataset", "uses_product_of": "uses product of", "uses_technology": "uses technology",
        "validates_on": "validates on", "verified_by": "verified by",
    },
    "ko": {
        "addresses": "대응", "analyzes": "분석", "applies_to": "적용",
        "cites": "인용", "combines_with": "결합", "constrains": "제약",
        "derived_from": "파생", "enables": "가능하게 함", "evaluates": "평가",
        "evaluates_on": "평가 대상", "formalizes": "형식화", "has_prerequisite": "선행 조건",
        "implemented_on": "구현 대상", "includes": "포함", "instantiates": "인스턴스화",
        "integrates": "통합", "is_alternative_to": "대체 가능", "is_based_on": "기반",
        "is_part_of": "일부", "is_regulated_by": "규제 대상", "is_version_of": "버전",
        "manufacturer_of": "제조", "mentions": "언급", "models": "모델링",
        "produces": "생산", "requires": "필요", "serves": "서비스",
        "solves": "해결", "sources_from": "조달처", "supplies": "공급",
        "tested_with": "테스트 대상", "uses": "사용", "uses_data": "데이터 사용",
        "uses_dataset": "데이터셋 사용", "uses_product_of": "제품 사용", "uses_technology": "기술 채택",
        "validates_on": "검증 대상", "verified_by": "검증 주체",
    },
}


def rel_type_label(rel_type: str, lang: str = "zh") -> str:
    return REL_TYPE_LABELS.get(lang, REL_TYPE_LABELS["zh"]).get(rel_type, rel_type)


def is_english_boilerplate(text: str) -> bool:
    """Detect English-only boilerplate descriptions unsuitable for zh/ko pages."""
    if not text:
        return False
    ascii_ratio = sum(1 for c in text if ord(c) < 128) / max(len(text), 1)
    return ascii_ratio > 0.85


def plain_summary(text: str, max_len: int = 120) -> str:
    """Return a plain-text, line-break-normalized summary for cards."""
    text = text or ""
    # Collapse line breaks and extra whitespace.
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) <= max_len:
        return text
    # Truncate at the last space before max_len.
    cut = text.rfind(" ", 0, max_len + 1)
    if cut <= 0:
        cut = max_len
    return text[:cut].rstrip() + "…"


def get_jinja_env() -> Environment:
    env = Environment(
        loader=FileSystemLoader(str(TEMPLATES_DIR)),
        autoescape=select_autoescape(["html", "xml"]),
    )
    env.filters["domain_label"] = domain_label
    env.filters["type_label"] = type_label
    env.filters["layer_label"] = layer_label
    env.filters["plain_summary"] = plain_summary
    env.filters["rel_type_label"] = rel_type_label
    return env


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


DOMAIN_COLORS = {
    "00_foundations": "#7c8798",
    "01_raw_materials": "#2a9d8f",
    "02_components": "#5d8c48",
    "03_manufacturing_processes": "#c38e3c",
    "04_assembly_integration_testing": "#b3592a",
    "05_mass_production": "#a84442",
    "06_design_engineering": "#7d5a8a",
    "07_ai_models_algorithms": "#3d7ea6",
    "08_software_middleware": "#5a8fbd",
    "09_data_datasets": "#2d5a7b",
    "10_evaluation_benchmarks": "#c9a227",
    "10_benchmarks_evaluation": "#c9a227",
    "11_applications_markets": "#b34d73",
    "12_policy_regulation_ethics": "#6b5b4f",
    "unknown": "#6b7280",
}


def domain_color(domain: str) -> str:
    return DOMAIN_COLORS.get(domain, DOMAIN_COLORS["unknown"])


class Renderer:
    """Render the static site for a single language."""

    def __init__(self, store: KGStore, lang: str, dist_dir: Path):
        self.store = store
        self.lang = lang
        self.dist_dir = dist_dir
        self.env = get_jinja_env()
        self.ui = UI_STRINGS.get(lang, UI_STRINGS["zh"])
        self.entry_name_lookup = {e.id: (e.name or e.id) for e in self.store.entries.values()}

    def _ctx(self, **kwargs) -> dict[str, Any]:
        """Common template context."""
        ctx = {
            "lang": self.lang,
            "ui": self.ui,
            "languages": [
                {"code": "zh", "name": "简体中文"},
                {"code": "en", "name": "English"},
                {"code": "ko", "name": "한국어"},
            ],
            "domain_label": domain_label,
            "domain_color": domain_color,
            "type_label": type_label,
        }
        ctx.update(kwargs)
        return ctx

    def copy_static_assets(self) -> None:
        """Copy src/ static assets into dist/.

        All templates reference /css, /js and /lib with root-absolute paths, so
        only the zh (root) build needs them — the en/ko copies were dead weight
        (~3.8 MB of vendored JS each).
        """
        if self.dist_dir.exists():
            shutil.rmtree(self.dist_dir)
        self.dist_dir.mkdir(parents=True, exist_ok=True)
        if SRC_DIR.exists():
            if self.lang == "zh":
                shutil.copytree(SRC_DIR, self.dist_dir, dirs_exist_ok=True)
            else:
                for item in SRC_DIR.iterdir():
                    if item.name in ("css", "js", "lib"):
                        continue
                    if item.is_dir():
                        shutil.copytree(item, self.dist_dir / item.name, dirs_exist_ok=True)
                    else:
                        shutil.copy2(item, self.dist_dir / item.name)
        if self.lang == "zh":
            minify_assets(self.dist_dir)
        (self.dist_dir / "data").mkdir(exist_ok=True)

    def render_home(self, stats: dict[str, Any]) -> None:
        template = self.env.get_template("index.html")
        domains = sorted({d for e in self.store.entries.values() for d in e.domains})
        types = sorted({e.type for e in self.store.entries.values()})

        def rel_count(eid: str) -> int:
            return len(self.store.outgoing.get(eid, [])) + len(self.store.incoming.get(eid, []))

        # Feature well-connected, well-described entities instead of the first
        # alphabetical ones (which surfaced data-quality warts on the home page).
        candidates = [e for e in self.store.entries.values() if e.summary and rel_count(e.id) > 0]
        featured = sorted(candidates, key=lambda e: (-rel_count(e.id), e.name or e.id))[:12]
        domain_colors = {d: domain_color(d) for d in domains}
        html = template.render(**self._ctx(
            title=self.ui["site_title"],
            stats=stats,
            domains=domains,
            domain_colors=domain_colors,
            types=types,
            featured=featured,
        ))
        (self.dist_dir / "index.html").write_text(html, encoding="utf-8")

    def render_types_pages(self) -> None:
        """Generate /types/<type>/ listing pages for browsing by entity type."""
        template = self.env.get_template("types.html")
        types = sorted({e.type for e in self.store.entries.values()})
        for t in types:
            entries = sorted(
                (e for e in self.store.entries.values() if e.type == t),
                key=lambda e: e.name or e.id,
            )
            html = template.render(**self._ctx(
                title=f"{type_label(t, self.lang)} · {self.ui['site_title']}",
                type_name=t,
                entries=entries,
            ))
            type_dir = self.dist_dir / "types" / t
            ensure_dir(type_dir)
            (type_dir / "index.html").write_text(html, encoding="utf-8")

    def render_entry(self, entry: Any) -> None:
        template = self.env.get_template("entry.html")
        outgoing = self.store.outgoing.get(entry.id, [])
        incoming = self.store.incoming.get(entry.id, [])
        related = self.store.related_entries(entry.id)
        roadmap_badges = self._roadmap_badges(entry.id)

        def view(rels: list[Relationship], direction: str) -> list[dict]:
            out = []
            for rel in rels:
                desc = rel.description or ""
                # Hide English boilerplate descriptions on zh/ko pages.
                if self.lang != "en" and is_english_boilerplate(desc):
                    desc = ""
                out.append({"rel": rel, "description": desc, "direction": direction})
            return out

        html = template.render(**self._ctx(
            title=f"{entry.name} · {self.ui['site_title']}",
            entry=entry,
            outgoing=view(outgoing, "out"),
            incoming=view(incoming, "in"),
            related=related,
            roadmap_badges=roadmap_badges,
            entry_name_lookup=self.entry_name_lookup,
        ))
        entry_dir = self.dist_dir / "entry" / entry.id
        ensure_dir(entry_dir)
        (entry_dir / "index.html").write_text(html, encoding="utf-8")

    def _roadmap_badges(self, entry_id: str) -> list[dict]:
        """Roadmap stage badges bound to this entity via roadmap_mapping.yaml."""
        roadmap = getattr(self.store, "roadmap", None) or {}
        bindings = (roadmap.get("entities") or {}).get(entry_id) or []
        stages = roadmap.get("stages") or {}
        roles = roadmap.get("roles") or {}
        badges = []
        for b in bindings:
            stage = stages.get(b.get("stage", ""), {})
            role = roles.get(b.get("role", ""), {})
            title = stage.get("title", {})
            badges.append({
                "url": stage.get("url", ""),
                "stage": title.get(self.lang) or title.get("zh") or b.get("stage", ""),
                "role": role.get(self.lang) or role.get("zh") or b.get("role", ""),
                "role_key": b.get("role", ""),
                "step": b.get("step", ""),
            })
        return badges

    def render_search_page(self) -> None:
        template = self.env.get_template("search.html")
        domains = sorted({d for e in self.store.entries.values() for d in e.domains})
        types = sorted({e.type for e in self.store.entries.values()})
        html = template.render(**self._ctx(
            title=f"{self.ui['search_title']} · {self.ui['site_title']}",
            domains=domains,
            types=types,
        ))
        search_dir = self.dist_dir / "search"
        ensure_dir(search_dir)
        (search_dir / "index.html").write_text(html, encoding="utf-8")

    def render_graph_page(self, stats: dict) -> None:
        template = self.env.get_template("graph.html")
        domains = sorted({d for e in self.store.entries.values() for d in e.domains})
        html = template.render(**self._ctx(
            title=f"{self.ui['graph_title']} · {self.ui['site_title']}",
            domains=domains,
            stats=stats,
        ))
        graph_dir = self.dist_dir / "graph"
        ensure_dir(graph_dir)
        (graph_dir / "index.html").write_text(html, encoding="utf-8")

    def render_wiki_index(self, wiki_pages: list[dict], wiki_tree: dict | None = None) -> None:
        template = self.env.get_template("wiki-index.html")
        html = template.render(**self._ctx(
            title=f"Wiki · {self.ui['site_title']}",
            wiki_pages=wiki_pages,
            wiki_tree=wiki_tree,
        ))
        wiki_dir = self.dist_dir / "wiki"
        ensure_dir(wiki_dir)
        (wiki_dir / "index.html").write_text(html, encoding="utf-8")

    def render_wiki_page(self, page: dict) -> None:
        template = self.env.get_template("wiki-page.html")
        html = template.render(**self._ctx(
            title=f"{page['title']} · Wiki · {self.ui['site_title']}",
            page=page,
            # Pages still in zh under a non-zh build get an honest notice.
            untranslated=page.get("page_lang", "zh") != self.lang,
        ))
        page_dir = self.dist_dir / page["url"].rstrip("/")
        ensure_dir(page_dir)
        (page_dir / "index.html").write_text(html, encoding="utf-8")

    def render_roadmap_index(self, roadmap_pages: list[dict], roadmap_tree: dict | None = None) -> None:
        template = self.env.get_template("roadmap-index.html")
        html = template.render(**self._ctx(
            title=f"{self.ui['nav_roadmap']} · {self.ui['site_title']}",
            roadmap_pages=roadmap_pages,
            roadmap_tree=roadmap_tree,
        ))
        roadmap_dir = self.dist_dir / "roadmap"
        ensure_dir(roadmap_dir)
        (roadmap_dir / "index.html").write_text(html, encoding="utf-8")

    def render_roadmap_page(self, page: dict) -> None:
        template = self.env.get_template("wiki-page.html")
        html = template.render(**self._ctx(
            title=f"{page['title']} · {self.ui['nav_roadmap']} · {self.ui['site_title']}",
            page=page,
            # Pages still in zh under a non-zh build get an honest notice.
            untranslated=page.get("page_lang", "zh") != self.lang,
            active_nav="roadmap",
            section_name=self.ui["nav_roadmap"],
            section_url="roadmap",
        ))
        page_dir = self.dist_dir / page["url"].rstrip("/")
        ensure_dir(page_dir)
        (page_dir / "index.html").write_text(html, encoding="utf-8")

    def render_roadmap_redirects(self, roadmap_pages: list[dict]) -> None:
        """Meta-refresh placeholders at the old /wiki/roadmap/** URLs."""
        bp = "" if self.lang == "zh" else f"/{self.lang}"
        moved = {
            "zh": "本页已迁移至路线图独立站点",
            "en": "This page has moved to the standalone roadmap site",
            "ko": "이 페이지는 독립 로드맵 사이트로 이동되었습니다",
        }.get(self.lang, "This page has moved")

        def write_redirect(old_rel: str, new_path: str) -> None:
            target_dir = self.dist_dir / old_rel
            ensure_dir(target_dir)
            html = (
                "<!doctype html>\n"
                f'<html lang="{"zh-CN" if self.lang == "zh" else ("ko-KR" if self.lang == "ko" else "en-US")}">\n'
                "<head>\n"
                '<meta charset="utf-8">\n'
                f'<meta http-equiv="refresh" content="0; url={new_path}">\n'
                f'<link rel="canonical" href="{SITE_BASE_URL}{new_path}">\n'
                f"<title>{moved} · Rounds Tech KG</title>\n"
                "</head>\n"
                "<body>\n"
                f'<p>{moved}: <a href="{new_path}">{new_path}</a></p>\n'
                "</body>\n"
                "</html>\n"
            )
            (target_dir / "index.html").write_text(html, encoding="utf-8")

        for page in roadmap_pages:
            slug = page["url"][len("roadmap/"):]
            write_redirect(f"wiki/roadmap/{slug}", f"{bp}/roadmap/{slug}/")
        # The old bare /wiki/roadmap/ URL (linked from the old nav) has no page
        # slug of its own; redirect it to the new roadmap index.
        write_redirect("wiki/roadmap", f"{bp}/roadmap/")

    def render_404(self) -> None:
        template = self.env.get_template("404.html")
        html = template.render(**self._ctx(
            title=f"{self.ui['not_found']} · {self.ui['site_title']}",
        ))
        (self.dist_dir / "404.html").write_text(html, encoding="utf-8")

    def render_about(self, stats: dict[str, Any]) -> None:
        template = self.env.get_template("about.html")
        html = template.render(**self._ctx(
            title=f"{self.ui['nav_about']} · {self.ui['site_title']}",
            stats=stats,
            active_nav="about",
        ))
        about_dir = self.dist_dir / "about"
        ensure_dir(about_dir)
        (about_dir / "index.html").write_text(html, encoding="utf-8")

    def write_json_data(self, data: dict, filename: str) -> None:
        path = self.dist_dir / "data" / filename
        path.write_text(json.dumps(data, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")

    def write_subgraphs(self, subgraphs: dict[str, dict]) -> None:
        sg_dir = self.dist_dir / "data" / "subgraphs"
        sg_dir.mkdir(parents=True, exist_ok=True)
        for eid, data in subgraphs.items():
            (sg_dir / f"{eid}.json").write_text(
                json.dumps(data, ensure_ascii=False, separators=(",", ":")),
                encoding="utf-8",
            )

    def write_sitemap(self, wiki_pages: list[dict] | None = None, roadmap_pages: list[dict] | None = None) -> None:
        from datetime import datetime, timezone

        lines = ['<?xml version="1.0" encoding="UTF-8"?>']
        lines.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')
        base = SITE_BASE_URL
        prefix = f"/{self.lang}" if self.lang != "zh" else ""
        lastmod = datetime.now(timezone.utc).strftime("%Y-%m-%d")

        def _url(loc: str, priority: str = "0.5") -> None:
            full = saxutils.escape(f"{base}{prefix}{loc}")
            lines.append(
                f"  <url>"
                f"<loc>{full}</loc>"
                f"<lastmod>{lastmod}</lastmod>"
                f"<priority>{priority}</priority>"
                f"</url>"
            )

        _url("/", "1.0")
        _url("/search/", "0.8")
        _url("/graph/", "0.8")
        _url("/wiki/", "0.9")
        _url("/roadmap/", "0.9")
        for t in sorted({e.type for e in self.store.entries.values()}):
            _url(f"/types/{t}/", "0.5")
        for entry in self.store.entries.values():
            _url(f"/{entry.url}", "0.6")
        if wiki_pages:
            for page in wiki_pages:
                _url(f"/{page['url']}", "0.7")
        if roadmap_pages:
            for page in roadmap_pages:
                _url(f"/{page['url']}", "0.7")
        lines.append("</urlset>")
        (self.dist_dir / "sitemap.xml").write_text("\n".join(lines), encoding="utf-8")

    def render_all(
        self,
        search_index: dict,
        relations_data: dict,
        cluster_data: dict,
        stats: dict,
        wiki_pages: list[dict] | None = None,
        subgraphs: dict[str, dict] | None = None,
        wiki_tree: dict | None = None,
        roadmap_pages: list[dict] | None = None,
        roadmap_tree: dict | None = None,
    ) -> None:
        self.copy_static_assets()
        self.render_home(stats)
        self.render_about(stats)
        self.render_search_page()
        self.render_graph_page(stats)
        self.render_404()
        self.render_types_pages()
        for entry in self.store.entries.values():
            self.render_entry(entry)
        if wiki_pages:
            self.render_wiki_index(wiki_pages, wiki_tree)
            for page in wiki_pages:
                self.render_wiki_page(page)
        if roadmap_pages:
            self.render_roadmap_index(roadmap_pages, roadmap_tree)
            for page in roadmap_pages:
                self.render_roadmap_page(page)
            self.render_roadmap_redirects(roadmap_pages)
        self.write_json_data(search_index, "search-index.json")
        self.write_json_data(relations_data, "relations.json")
        self.write_json_data(cluster_data, "clusters.json")
        self.write_json_data(build_names_index(self.store.entries), "names.json")
        if subgraphs:
            self.write_subgraphs(subgraphs)
        self.write_sitemap(wiki_pages, roadmap_pages)
