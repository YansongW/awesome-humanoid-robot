#!/usr/bin/env python3
"""AI4Sci single-paper draft generator.

Downloads a paper (currently arXiv only), extracts full text, uses an LLM to
generate a structured entry draft + proposed relationships, and writes them to
.staging/ for human review.

Usage:
    export AI4SCI_API_KEY="your-api-key"
    source .venv/bin/activate
    python scripts/ai4sci_paper_pipeline.py https://arxiv.org/abs/2604.23001
    python scripts/ai4sci_paper_pipeline.py 2604.23001
    python scripts/ai4sci_paper_pipeline.py https://arxiv.org/abs/2605.12090 --type paper

After review, use scripts/ai4sci_review.py to approve or reject drafts.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from ai4sci_lib import config, pipeline


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate a draft knowledge-base entry from a paper URL or ID."
    )
    parser.add_argument(
        "input",
        help="arXiv URL/ID, or direct PDF URL (currently arXiv is best supported).",
    )
    parser.add_argument(
        "--type",
        default="paper",
        help="Preferred entity type if the LLM is uncertain (default: paper).",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=None,
        help="Override staging output directory.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the generated entry and relationships without writing files.",
    )
    parser.add_argument(
        "--relevance-threshold",
        choices=["low", "medium", "high"],
        default="medium",
        help="Minimum relevance score to proceed with draft generation (default: medium).",
    )
    parser.add_argument(
        "--model",
        default=None,
        help="LLM model name override.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    output_dir = args.output_dir or config.STAGING_DIR
    source = pipeline.SourceCandidate(
        input=args.input,
        source_url=args.input,
        pdf_url=None,
        arxiv_id=None,
        discovered_by="manual",
    )

    print(f"[pipeline] Processing: {args.input}")
    result = pipeline.process_source(
        source,
        output_dir=output_dir,
        relevance_threshold=args.relevance_threshold,
        model=args.model,
        preferred_type=args.type,
        dry_run=args.dry_run,
    )

    print(f"[pipeline] Status: {result.status} — {result.message}")
    if result.entry_path:
        print(f"           Entry: {result.entry_path}")
    if result.rel_paths:
        for rp in result.rel_paths:
            print(f"           Relationship: {rp}")
    if result.review_path:
        print(f"           Review: {result.review_path}")

    if result.status == "error":
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
