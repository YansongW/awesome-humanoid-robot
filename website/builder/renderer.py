"""Render static HTML pages using Jinja2 templates."""

from __future__ import annotations

import json
import re
import shutil
from pathlib import Path
from typing import Any

from jinja2 import Environment, FileSystemLoader, select_autoescape

from website.builder.loader import DOMAIN_LABELS, KGStore, Relationship, domain_label, type_label

BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = BASE_DIR / "templates"
SRC_DIR = BASE_DIR / "src"
DIST_DIR = BASE_DIR / "dist"


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
        "outgoing": "Outgoing",
        "incoming": "Incoming",
        "subgraph": "关系子图",
        "graph_hint": "拖拽节点可调整布局，滚轮缩放，点击查看实体详情。",
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
        "cluster_view": "큟뷰",
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
        "outgoing": "나가는",
        "incoming": "들어오는",
        "subgraph": "관계 하위 그래프",
        "graph_hint": "노드를 드래그하여 레이아웃을 조정하고, 휠로 확대/축소하며, 클릭하면 상세 정보를 볼 수 있습니다.",
    },
}


def ui_string(lang: str, key: str) -> str:
    return UI_STRINGS.get(lang, UI_STRINGS["zh"]).get(key, key)


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
    env.filters["plain_summary"] = plain_summary
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
        """Copy src/ static assets into dist/."""
        if self.dist_dir.exists():
            shutil.rmtree(self.dist_dir)
        self.dist_dir.mkdir(parents=True, exist_ok=True)
        if SRC_DIR.exists():
            shutil.copytree(SRC_DIR, self.dist_dir, dirs_exist_ok=True)
        (self.dist_dir / "data").mkdir(exist_ok=True)

    def render_home(self, stats: dict[str, Any]) -> None:
        template = self.env.get_template("index.html")
        domains = sorted({d for e in self.store.entries.values() for d in e.domains})
        types = sorted({e.type for e in self.store.entries.values()})
        featured = sorted(self.store.entries.values(), key=lambda e: e.name or e.id)[:12]
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

    def render_entry(self, entry: Any) -> None:
        template = self.env.get_template("entry.html")
        outgoing = self.store.outgoing.get(entry.id, [])
        incoming = self.store.incoming.get(entry.id, [])
        related = self.store.related_entries(entry.id)
        entry_name_lookup = {e.id: (e.name or e.id) for e in self.store.entries.values()}
        html = template.render(**self._ctx(
            title=f"{entry.name} · {self.ui['site_title']}",
            entry=entry,
            outgoing=outgoing,
            incoming=incoming,
            related=related,
            entry_name_lookup=entry_name_lookup,
        ))
        entry_dir = self.dist_dir / "entry" / entry.id
        ensure_dir(entry_dir)
        (entry_dir / "index.html").write_text(html, encoding="utf-8")

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

    def render_wiki_index(self, wiki_pages: list[dict]) -> None:
        template = self.env.get_template("wiki-index.html")
        html = template.render(**self._ctx(
            title=f"Wiki · {self.ui['site_title']}",
            wiki_pages=wiki_pages,
        ))
        wiki_dir = self.dist_dir / "wiki"
        ensure_dir(wiki_dir)
        (wiki_dir / "index.html").write_text(html, encoding="utf-8")

    def render_wiki_page(self, page: dict) -> None:
        template = self.env.get_template("wiki-page.html")
        html = template.render(**self._ctx(
            title=f"{page['title']} · Wiki · {self.ui['site_title']}",
            page=page,
        ))
        page_dir = self.dist_dir / page["url"].rstrip("/")
        ensure_dir(page_dir)
        (page_dir / "index.html").write_text(html, encoding="utf-8")

    def render_404(self) -> None:
        template = self.env.get_template("404.html")
        html = template.render(**self._ctx(
            title=f"{self.ui['not_found']} · {self.ui['site_title']}",
        ))
        (self.dist_dir / "404.html").write_text(html, encoding="utf-8")

    def write_json_data(self, data: dict, filename: str) -> None:
        path = self.dist_dir / "data" / filename
        path.write_text(json.dumps(data, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")

    def write_sitemap(self) -> None:
        lines = ['<?xml version="1.0" encoding="UTF-8"?>']
        lines.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')
        base = "https://kg.rounds-tech.com"
        prefix = f"/{self.lang}" if self.lang != "zh" else ""
        lines.append(f"  <url><loc>{base}{prefix}/</loc></url>")
        lines.append(f"  <url><loc>{base}{prefix}/search/</loc></url>")
        lines.append(f"  <url><loc>{base}{prefix}/graph/</loc></url>")
        lines.append(f"  <url><loc>{base}{prefix}/wiki/</loc></url>")
        for entry in self.store.entries.values():
            lines.append(f"  <url><loc>{base}{prefix}/{entry.url}</loc></url>")
        lines.append("</urlset>")
        (self.dist_dir / "sitemap.xml").write_text("\n".join(lines), encoding="utf-8")

    def render_all(
        self,
        search_index: dict,
        relations_data: dict,
        cluster_data: dict,
        stats: dict,
        wiki_pages: list[dict] | None = None,
    ) -> None:
        self.copy_static_assets()
        self.render_home(stats)
        self.render_search_page()
        self.render_graph_page(stats)
        self.render_404()
        for entry in self.store.entries.values():
            self.render_entry(entry)
        if wiki_pages:
            self.render_wiki_index(wiki_pages)
            for page in wiki_pages:
                self.render_wiki_page(page)
        self.write_json_data(search_index, "search-index.json")
        self.write_json_data(relations_data, "relations.json")
        self.write_json_data(cluster_data, "clusters.json")
        self.write_sitemap()
