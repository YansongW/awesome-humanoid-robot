"""Main entry point for building the static knowledge graph website."""

from __future__ import annotations

import sys
from pathlib import Path

# Make project root importable
ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT))

from website.builder.loader import KGStore
from website.builder.renderer import render_all
from website.builder.search_index import build_relations_data, build_search_index


def main() -> int:
    print("Loading knowledge graph...")
    store = KGStore()
    store.load()

    stats = {
        "entries": len(store.entries),
        "relationships": len(store.relationships),
        "domains": len({d for e in store.entries.values() for d in e.domains}),
        "types": len({e.type for e in store.entries.values()}),
    }
    print(f"Loaded {stats['entries']} entries, {stats['relationships']} relationships.")

    print("Building search index and relation graph...")
    search_index = build_search_index(store.entries)
    relations_data = build_relations_data(store.entries, store.relationships)

    print("Rendering static pages...")
    render_all(store, search_index, relations_data, stats)

    print("Build complete.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
