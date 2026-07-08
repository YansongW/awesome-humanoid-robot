# Agent Instructions for Awesome Humanoid Robot

## Core Principle: Comprehensiveness, Not Top-N

When curating the knowledge graph, **always prioritize comprehensiveness**.

- **External curated lists** (e.g., paper surveys, WeChat collections, conference proceedings) should be imported **in full**, not reduced to a "Top N" selection.
- **Taxonomy coverage** matters: every paper, component, company, dataset, benchmark, or concept that belongs in the humanoid-robot industry chain should have a place in the graph.
- Only skip entries that are exact duplicates of existing production entities or fall outside the project's scope (non-humanoid, non-robotics).

## Verification Stance

- New entries may start as `unverified` or `speculative` and be promoted after review.
- Do not block bulk imports purely because individual sources are not yet independently verified.
- Preserve source links and provenance so claims remain traceable.

## Relationship Philosophy

- Relationships are first-class citizens. After adding a batch of entities, backfill relationships among existing entities rather than waiting for the pipeline to propose them.
- Use direct textual evidence (mentions, shared domains, known product links) to justify relationships.

## Minimal Intrusiveness

- Make minimal changes to existing validated files.
- Run `scripts/validate_entries.py` after any bulk import or relationship backfill.
