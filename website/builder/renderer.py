"""Render static HTML pages using Jinja2 templates."""

from __future__ import annotations

import json
import shutil
from pathlib import Path
from typing import Any

from jinja2 import Environment, FileSystemLoader, select_autoescape

from website.builder.loader import Entry, KGStore, Relationship

BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = BASE_DIR / "templates"
SRC_DIR = BASE_DIR / "src"
DIST_DIR = BASE_DIR / "dist"


def get_jinja_env() -> Environment:
    return Environment(
        loader=FileSystemLoader(str(TEMPLATES_DIR)),
        autoescape=select_autoescape(["html", "xml"]),
    )


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def copy_static_assets() -> None:
    """Copy src/ static assets into dist/."""
    if DIST_DIR.exists():
        shutil.rmtree(DIST_DIR)
    DIST_DIR.mkdir(parents=True, exist_ok=True)
    if SRC_DIR.exists():
        shutil.copytree(SRC_DIR, DIST_DIR, dirs_exist_ok=True)
    (DIST_DIR / "data").mkdir(exist_ok=True)


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


def render_home(store: KGStore, stats: dict[str, Any]) -> None:
    env = get_jinja_env()
    template = env.get_template("index.html")
    domains = sorted({d for e in store.entries.values() for d in e.domains})
    types = sorted({e.type for e in store.entries.values()})
    featured = sorted(store.entries.values(), key=lambda e: e.name or e.id)[:12]
    domain_colors = {d: domain_color(d) for d in domains}
    html = template.render(
        title="人形机器人知识图谱",
        stats=stats,
        domains=domains,
        domain_colors=domain_colors,
        types=types,
        featured=featured,
    )
    (DIST_DIR / "index.html").write_text(html, encoding="utf-8")


def render_entry(store: KGStore, entry: Entry) -> None:
    env = get_jinja_env()
    template = env.get_template("entry.html")
    outgoing = store.outgoing.get(entry.id, [])
    incoming = store.incoming.get(entry.id, [])
    related = store.related_entries(entry.id)
    html = template.render(
        title=f"{entry.name} · 人形机器人知识图谱",
        entry=entry,
        outgoing=outgoing,
        incoming=incoming,
        related=related,
    )
    entry_dir = DIST_DIR / "entry" / entry.id
    ensure_dir(entry_dir)
    (entry_dir / "index.html").write_text(html, encoding="utf-8")


def render_search_page(store: KGStore) -> None:
    env = get_jinja_env()
    template = env.get_template("search.html")
    domains = sorted({d for e in store.entries.values() for d in e.domains})
    types = sorted({e.type for e in store.entries.values()})
    html = template.render(
        title="搜索 · 人形机器人知识图谱",
        domains=domains,
        types=types,
    )
    search_dir = DIST_DIR / "search"
    ensure_dir(search_dir)
    (search_dir / "index.html").write_text(html, encoding="utf-8")


def render_graph_page(store: KGStore, stats: dict) -> None:
    env = get_jinja_env()
    template = env.get_template("graph.html")
    domains = sorted({d for e in store.entries.values() for d in e.domains})
    html = template.render(
        title="关系图谱 · 人形机器人知识图谱",
        domains=domains,
        stats=stats,
    )
    graph_dir = DIST_DIR / "graph"
    ensure_dir(graph_dir)
    (graph_dir / "index.html").write_text(html, encoding="utf-8")


def render_404() -> None:
    env = get_jinja_env()
    template = env.get_template("404.html")
    html = template.render(title="未找到 · 人形机器人知识图谱")
    (DIST_DIR / "404.html").write_text(html, encoding="utf-8")


def write_json_data(data: dict, filename: str) -> None:
    path = DIST_DIR / "data" / filename
    path.write_text(json.dumps(data, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")


def write_sitemap(store: KGStore) -> None:
    lines = ['<?xml version="1.0" encoding="UTF-8"?>']
    lines.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')
    base = "https://rounds-tech.com"
    lines.append(f"  <url><loc>{base}/</loc></url>")
    lines.append(f"  <url><loc>{base}/search/</loc></url>")
    lines.append(f"  <url><loc>{base}/graph/</loc></url>")
    for entry in store.entries.values():
        lines.append(f"  <url><loc>{base}/{entry.url}</loc></url>")
    lines.append("</urlset>")
    (DIST_DIR / "sitemap.xml").write_text("\n".join(lines), encoding="utf-8")


def render_all(store: KGStore, search_index: dict, relations_data: dict, cluster_data: dict, stats: dict) -> None:
    copy_static_assets()
    render_home(store, stats)
    render_search_page(store)
    render_graph_page(store, stats)
    render_404()
    for entry in store.entries.values():
        render_entry(store, entry)
    write_json_data(search_index, "search-index.json")
    write_json_data(relations_data, "relations.json")
    write_json_data(cluster_data, "clusters.json")
    write_sitemap(store)
