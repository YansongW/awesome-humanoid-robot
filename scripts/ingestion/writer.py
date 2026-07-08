"""Write normalized ParsedItem objects into the research graph."""

from __future__ import annotations

import re
from datetime import date
from pathlib import Path
from typing import Any

from ai4sci_lib import config, entry_builder

from .core import ParsedItem


class EntryWriter:
    """Convert ParsedItem to schema-compliant Markdown entries."""

    def __init__(self, base_dir: Path | None = None, existing_ids: set[str] | None = None) -> None:
        self.base_dir = base_dir or config.RESEARCH_DIR
        self._existing_ids = existing_ids
        self._new_ids: set[str] = set()

    @staticmethod
    def _extract_year(title: str, fallback: str | int | None = None) -> str:
        m = re.search(r"20\d{2}", title)
        if m:
            return m.group(0)
        if fallback:
            return str(fallback)
        return str(date.today().year)

    @staticmethod
    def _infer_layers(domains: list[str]) -> list[str]:
        layers = sorted({config.LAYER_MAP[d] for d in domains if d in config.LAYER_MAP})
        return layers or ["intelligence"]

    def write(self, item: ParsedItem) -> Path:
        year = self._extract_year(item.title, item.year)
        title_slug = entry_builder._slugify(item.title, max_len=30)

        prefix_map = {
            "report": "ent_report",
            "paper": "ent_paper",
            "company": "ent_company",
            "oem": "ent_company",
            "tier1_supplier": "ent_company",
            "tier2_supplier": "ent_company",
            "component_manufacturer": "ent_company",
            "material_supplier": "ent_company",
            "software_vendor": "ent_company",
            "research_institution": "ent_company",
            "standards_body": "ent_company",
            "industry_consortium": "ent_company",
            "market_segment": "ent_market",
            "application_scenario": "ent_market",
            "business_model": "ent_market",
            "regulation": "ent_regulation",
            "component": "ent_component",
            "robot_system": "ent_robot",
            "material": "ent_material",
            "technology": "ent_technology",
            "software_platform": "ent_software",
            "tool_equipment": "ent_equipment",
            "facility": "ent_facility",
            "standard": "ent_standard",
            "certification": "ent_certification",
            "dataset": "ent_dataset",
            "benchmark": "ent_benchmark",
        }
        prefix = prefix_map.get(item.type, "ent_paper")
        if item.type == "report":
            ns = item.tags[0] if item.tags else "src"
            ent_id = f"{prefix}_{ns}_{title_slug}_{year}"
        else:
            ent_id = f"{prefix}_{title_slug}_{year}"

        if self._existing_ids is None:
            existing_ids = entry_builder.load_existing_ids()
        else:
            existing_ids = self._existing_ids
        candidate_id = ent_id
        counter = 1
        while candidate_id in existing_ids or candidate_id in self._new_ids:
            candidate_id = f"{ent_id}_{counter}"
            counter += 1
        ent_id = candidate_id
        self._new_ids.add(ent_id)

        today = str(date.today())
        sources: list[dict[str, Any]] = []
        if item.arxiv_id:
            sources.append({
                "id": "src_001",
                "type": "paper",
                "title": f"{item.title} (arXiv)",
                "url": f"https://arxiv.org/abs/{item.arxiv_id}",
                "date": str(year),
                "accessed_at": today,
            })
        if item.source_url and (not item.arxiv_id or item.source_url != f"https://arxiv.org/abs/{item.arxiv_id}"):
            src_id = "src_002" if item.arxiv_id else "src_001"
            sources.append({
                "id": src_id,
                "type": item.source_type,
                "title": item.title,
                "url": item.source_url,
                "date": item.source_date or str(year),
                "accessed_at": today,
            })
        if not sources:
            sources.append({
                "id": "src_001",
                "type": item.source_type,
                "title": item.title,
                "url": "",
                "date": str(year),
                "accessed_at": today,
            })

        verified = bool(item.arxiv_id) or bool(item.source_url)
        frontmatter = {
            "$id": ent_id,
            "$schema": "../../data/schema/v1/entry_schema.json",
            "$version": 1,
            "type": item.type,
            "names": item.names,
            "summary": item.summary,
            "domains": item.domains,
            "layers": item.layers or self._infer_layers(item.domains),
            "functional_roles": item.functional_roles,
            "tags": item.tags,
            "theoretical_depth": item.theoretical_depth,
            "verification": {
                "status": "partially_verified" if verified else "unverified",
                "reviewed_by": "ai",
                "reviewed_at": today,
                "confidence": "medium" if verified else "low",
                "notes": f"Imported via ingestion framework from source_type={item.source_type}.",
            },
            "sources": sources,
        }

        subdir = entry_builder.infer_subdir(item.type)
        filename = f"{ent_id}.md"
        body = item.summary.get("en", "") or item.title
        return entry_builder.write_entry_file(frontmatter, body, subdir, filename, self.base_dir)
