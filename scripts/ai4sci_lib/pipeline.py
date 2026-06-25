"""Reusable AI4Sci pipeline stages.

Stages:
  1. Discover candidate sources.
  2. Download/read full text.
  3. Extract metadata.
  4. Classify relevance.
  5. Generate entry draft + relationships.
  6. Write staged files.

This module is used by both `ai4sci_paper_pipeline.py` (single-paper CLI) and
`ai4sci_batch_pipeline.py` (workstream batch runner).
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any

from . import config, entry_builder, extraction, pdf, staging


@dataclass
class SourceCandidate:
    """A candidate paper or source to process."""

    input: str
    source_url: str
    pdf_url: str | None
    arxiv_id: str | None
    discovered_by: str = "manual"
    query: str | None = None


@dataclass
class PipelineResult:
    """Result of processing one source."""

    entry_path: Path | None = None
    rel_paths: list[Path] = field(default_factory=list)
    review_path: Path | None = None
    entry_id: str | None = None
    status: str = "pending"  # success, skipped, error, duplicate
    message: str = ""


def score_to_int(score: str) -> int:
    return {"low": 1, "medium": 2, "high": 3}.get(score.lower(), 0)


def threshold_to_int(threshold: str) -> int:
    return {"low": 1, "medium": 2, "high": 3}[threshold]


def process_source(
    source: SourceCandidate,
    output_dir: Path,
    relevance_threshold: str = "medium",
    model: str | None = None,
    preferred_type: str | None = None,
    dry_run: bool = False,
) -> PipelineResult:
    """Run the full AI4Sci pipeline for a single source and write staged files.

    Args:
        source: Candidate source to process.
        output_dir: Base directory for staged outputs (e.g., `.staging` or
            `.staging/workstreams/<name>`).
        relevance_threshold: Minimum relevance score to proceed.
        model: LLM model override.
        preferred_type: Preferred entity type if the LLM is uncertain.
        dry_run: If True, print drafts instead of writing files.

    Returns:
        PipelineResult with paths and status.
    """
    result = PipelineResult()

    try:
        text, meta = pdf.get_paper_text(source.input)
    except Exception as exc:
        result.status = "error"
        result.message = f"Error acquiring paper: {exc}"
        return result

    try:
        metadata = extraction.extract_paper_metadata(
            text,
            source_url=meta.get("source_url", source.source_url),
            pdf_url=meta.get("pdf_url") or source.pdf_url or source.source_url,
        )
    except Exception as exc:
        result.status = "error"
        result.message = f"Error extracting metadata: {exc}"
        return result

    try:
        relevance = extraction.classify_relevance(metadata)
    except Exception as exc:
        result.status = "error"
        result.message = f"Error classifying relevance: {exc}"
        return result

    if score_to_int(relevance.get("score", "low")) < threshold_to_int(relevance_threshold):
        result.status = "skipped"
        result.message = (
            f"Relevance score {relevance.get('score')} is below threshold {relevance_threshold}."
        )
        return result

    try:
        proposal = extraction.propose_entry(metadata, relevance, model=model)
    except Exception as exc:
        result.status = "error"
        result.message = f"Error generating entry proposal: {exc}"
        return result

    entry_data = proposal.get("entry", {})
    body_data = proposal.get("body", {})
    relationships = proposal.get("relationships", [])
    review_notes = proposal.get("review_notes", [])

    # Override type if requested and paper-type is uncertain.
    if preferred_type and entry_data.get("type") == "paper":
        entry_data["type"] = preferred_type

    # Build deterministic ID.
    first_author = metadata.get("authors", ["unknown"])[0]
    title = metadata.get("title", "untitled")
    year = metadata.get("year", datetime.now().year)
    entity_type = entry_data.get("type", "paper")
    entry_id = entry_builder.make_entry_id(entity_type, first_author, title, year)

    if entry_id in entry_builder.load_existing_ids():
        result.status = "duplicate"
        result.message = f"An entry with ID {entry_id} already exists."
        return result

    entry_data["$id"] = entry_id
    result.entry_id = entry_id

    # Ensure source record is present and accurate.
    source_record = {
        "id": "src_001",
        "type": "paper",
        "title": metadata.get("title", ""),
        "url": meta.get("source_url", source.source_url),
        "date": str(metadata.get("year", datetime.now().year)),
        "accessed_at": datetime.now().date().isoformat(),
    }
    if metadata.get("arxiv_id"):
        source_record["url"] = f"https://arxiv.org/abs/{metadata['arxiv_id']}"
    elif source.arxiv_id:
        source_record["url"] = f"https://arxiv.org/abs/{source.arxiv_id}"
    if metadata.get("doi"):
        source_record["doi"] = metadata["doi"]
    entry_data["sources"] = [source_record]

    # Sanitize domain codes.
    proposed_domains = entry_data.get("domains", [])
    valid_domains, invalid_domains = entry_builder.normalize_domains(proposed_domains)
    if invalid_domains:
        review_notes.append(
            f"Dropped invalid domain codes (not in schema): {', '.join(invalid_domains)}. "
            f"Valid domains retained: {', '.join(valid_domains) if valid_domains else 'none'}."
        )
    entry_data["domains"] = valid_domains

    # Infer layers if missing.
    if not entry_data.get("layers"):
        entry_data["layers"] = entry_builder.infer_layers(entry_data.get("domains", []))

    # Normalize related_entities and relationship types.
    for rel in entry_data.get("related_entities", []):
        desc = rel.get("description", "")
        if isinstance(desc, str):
            rel["description"] = {"en": desc, "zh": desc, "ko": desc}
        rel["relationship"] = entry_builder.normalize_relationship_type(rel.get("relationship", ""))

    for rel in relationships:
        rel["type"] = entry_builder.normalize_relationship_type(rel.get("type", ""))

    # Build body markdown.
    body_md = extraction.build_markdown_body(body_data)

    # Validate frontmatter.
    try:
        frontmatter = entry_builder.build_entry_frontmatter(entry_data)
    except ValueError as exc:
        result.status = "error"
        result.message = f"Invalid entry frontmatter: {exc}"
        return result

    if dry_run:
        result.status = "success"
        result.message = "Dry run completed."
        # Do not write files, but capture what would be written for reporting.
        return result

    # Determine output paths.
    research_base = output_dir / "research"
    relationships_base = output_dir / "data" / "relationships"
    review_base = output_dir / "review"
    subdir = entry_builder.infer_subdir(entity_type)
    filename = f"{entry_id}.md"

    staging.ensure_staging_dirs_for(output_dir)

    entry_path = entry_builder.write_entry_file(
        frontmatter, body_md, subdir, filename, base_dir=research_base
    )
    result.entry_path = entry_path

    rel_paths: list[Path] = []
    for rel in relationships:
        target_id = rel.get("target_id")
        rel_type = rel.get("type")
        if not target_id or not rel_type:
            continue
        rel_id = entry_builder.make_relationship_id(entry_id, rel_type, target_id)
        if rel_id in entry_builder.load_existing_ids():
            continue
        rel_frontmatter = entry_builder.build_relationship_frontmatter({
            "$id": rel_id,
            "type": rel_type,
            "source": {
                "id": entry_id,
                "name": {
                    "en": metadata.get("title", ""),
                    "zh": entry_data["names"].get("zh", ""),
                    "ko": entry_data["names"].get("ko", ""),
                },
            },
            "target": {
                "id": target_id,
                "name": rel.get("target_name", {"en": target_id}),
            },
            "domains": {
                "source_domain": entry_data["domains"][0] if entry_data.get("domains") else "07_ai_models_algorithms",
                "target_domain": rel.get("target_domain", "07_ai_models_algorithms"),
            },
            "description": rel.get("description", {"en": "", "zh": "", "ko": ""}),
            "verification": {
                "status": "partially_verified",
                "reviewed_by": "ai",
                "reviewed_at": datetime.now().date().isoformat(),
                "confidence": "medium",
                "notes": f"Proposed by AI extraction. Source citation: {rel.get('source_citation', 'N/A')}",
            },
            "sources": [source_record],
        })
        rel_path = entry_builder.write_relationship_file(rel_frontmatter, base_dir=relationships_base)
        rel_paths.append(rel_path)
    result.rel_paths = rel_paths

    # Write review report.
    review_base.mkdir(parents=True, exist_ok=True)
    review_path = review_base / f"{entry_id}.md"
    review_lines = [
        f"# Review: {metadata.get('title', '')}",
        "",
        f"- **Entry**: `{entry_id}`",
        f"- **Staged entry**: `{entry_path}`",
        f"- **Relevance**: {relevance.get('score', 'N/A')} — {relevance.get('reason', '')}",
        f"- **Generated at**: {datetime.now().isoformat()}",
        "",
        "## Proposed relationships",
        "",
    ]
    if rel_paths:
        for rp in rel_paths:
            review_lines.append(f"- `{rp.name}`")
    else:
        review_lines.append("- None")
    review_lines.extend([
        "",
        "## Review notes",
        "",
    ])
    if review_notes:
        for note in review_notes:
            review_lines.append(f"- {note}")
    else:
        review_lines.append("- No specific review notes from AI extraction.")
    review_lines.extend([
        "",
        "## Recommended action",
        "",
        "- [ ] Approve and move to production",
        "- [ ] Edit before approval",
        "- [ ] Reject",
        "",
        "## Verification checklist",
        "",
        "- [ ] Title, authors, year, and URL are correct",
        "- [ ] Summary accurately reflects the paper",
        "- [ ] Domains and layers are appropriate",
        "- [ ] All factual claims have source support",
        "- [ ] Proposed relationships are explicitly supported by the paper",
        "- [ ] Speculative claims are clearly labeled",
    ])
    review_path.write_text("\n".join(review_lines), encoding="utf-8")
    result.review_path = review_path

    result.status = "success"
    result.message = f"Staged entry + {len(rel_paths)} relationship(s)."
    return result
