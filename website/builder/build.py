"""Main entry point for building the static knowledge graph website."""

from __future__ import annotations

import sys
from pathlib import Path

# Make project root importable
ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT))

from website.builder.loader import KGStore
from website.builder.renderer import Renderer
from website.builder.search_index import build_cluster_data, build_relations_data, build_search_index, build_subgraph_data
from website.builder.wiki_loader import build_wiki_pages, build_wiki_tree


LANGUAGES = ["zh", "en", "ko"]


def build_language(lang: str, dist_dir: Path, wiki_pages: list | None = None, wiki_tree: dict | None = None) -> None:
    print(f"\nBuilding language: {lang}")
    store = KGStore(lang=lang)
    store.load()

    stats = {
        "entries": len(store.entries),
        "relationships": len(store.relationships),
        "domains": len({d for e in store.entries.values() for d in e.domains}),
        "types": len({e.type for e in store.entries.values()}),
    }
    print(f"Loaded {stats['entries']} entries, {stats['relationships']} relationships.")

    print("Building search index, relation graph, and clusters...")
    search_index = build_search_index(store.entries, lang)
    relations_data = build_relations_data(store.entries, store.relationships)
    cluster_data = build_cluster_data(store.entries, store.relationships)

    print("Building per-entry subgraphs...")
    subgraphs = {
        eid: build_subgraph_data(eid, store.entries, store.relationships)
        for eid in store.entries
    }

    print("Rendering static pages...")
    renderer = Renderer(store, lang, dist_dir)
    renderer.render_all(search_index, relations_data, cluster_data, stats, wiki_pages, subgraphs, wiki_tree)


def main() -> int:
    try:
        print("Loading wiki pages...")
        wiki_pages = build_wiki_pages()
        wiki_tree = build_wiki_tree(wiki_pages) if wiki_pages else None
        print(f"Loaded {len(wiki_pages)} wiki pages.")
    except Exception as exc:
        print(f"Failed to load wiki pages: {exc}", file=sys.stderr)
        return 1

    base_dist = Path(__file__).resolve().parent.parent / "dist"

    for lang in LANGUAGES:
        dist_dir = base_dist if lang == "zh" else base_dist / lang
        try:
            build_language(lang, dist_dir, wiki_pages, wiki_tree)
        except Exception as exc:
            print(f"Failed to build language '{lang}': {exc}", file=sys.stderr)
            return 1

    print("\nBuild complete.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
