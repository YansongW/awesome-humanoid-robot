# Workstream Design Reflection: From Sparse Sampling to Dense Taxonomy Coverage

## What Went Wrong

The first generation of workstreams behaved like **keyword-triggered samplers**:

- 4–5 free-text seed queries per workstream.
- `max_papers=15` hard cap, with `max_results_per_query=max_papers`.
- No explicit paper IDs, no survey anchors, no citation expansion.
- No coverage metric, so gaps were invisible until a curated list (161 papers) exposed them.

This design can bootstrap a graph, but it cannot deliver the **dense, branch-by-branch coverage** required by the comprehensiveness rule.

---

## Root-Cause Analysis

| Symptom | Root Cause |
|---------|-----------|
| Workstream produces 0–2 entries | Query set is too small; API returns only top-N results for a few keywords. |
| Same papers keep appearing across workstreams | No per-workstream `tried.json`; no cross-workstream duplicate suppression. |
| Large curated lists bypass workstreams entirely | No ingestion path from external curated lists to workstream YAMLs. |
| Relationship count lags behind entry count | Relationships are only generated inside the pipeline, not backfilled across the whole graph after a batch. |
| Missing hardware/software/test/policy branches | `WORKSTREAM_TREE.md` was treated as TODO, not as a mandatory coverage checklist. |
| No visibility into coverage | README only shows aggregate counts, not per-domain or per-tree-leaf coverage. |

---

## Design Principles for Dense Coverage

### 1. Taxonomy-first, not keyword-first

Every leaf of `WORKSTREAM_TREE.md` must map to a workstream YAML. If a leaf is missing, the coverage gap is explicit. The workstream name, domains, and tags should be derived from the ontology, not invented per run.

### 2. Curated-list ingestion as a first-class input

When a human-curated list appears (WeChat article, survey bibliography, conference proceedings), it should not be manually copied entry-by-entry. Instead:

1. Parse titles / URLs / project links.
2. Resolve arXiv IDs.
3. Generate or update a workstream YAML with those IDs as `paper_ids`.
4. Add category-aligned `seed_queries` so discovery can extend beyond the list.
5. Run the workstream and backfill relationships.

This guarantees that a dense curated set becomes a dense graph cluster.

### 3. Survey-anchor + citation expansion

For each branch, identify 2–5 recent survey or foundational papers and put their arXiv IDs in `paper_ids`. Then use their references / citations to grow the candidate pool. A single good survey can surface 50+ relevant papers.

### 4. Exhaustive discovery, not top-N sampling

- Increase `max_results_per_query` to 50–100.
- Implement API pagination (offset / pageToken) so a workstream can pull hundreds of candidates, not dozens.
- Use query expansion: combine taxonomy terms with method, robot platform, and task keywords (e.g. "humanoid whole-body control + reinforcement learning", "humanoid manipulation + diffusion policy").

### 5. Deduplication and provenance

- Maintain a project-wide `tried_candidates.jsonl` so the same arXiv ID is never processed twice by any workstream.
- Skip candidates whose entry ID already exists in production.
- Record which workstream produced each entry and relationship.

### 6. Mandatory relationship backfill

After every batch import, run `relationship_backfill.py` (or an equivalent LLM pass) to connect new entries to existing entities. Do not wait for the pipeline to propose relationships.

### 7. Coverage dashboard

Add a script that reports:

- `workstream tree coverage` = existing workstreams / `WORKSTREAM_TREE` leaves.
- `entries per ontology domain`.
- `relationships per entry` histogram.
- `unrun / exhausted / low-yield` workstreams.

Publish these numbers in README or session_status after each session.

---

## Immediate Engineering Changes

1. **Create `scripts/generate_workstream_from_curated.py`**
   - Input: a curated JSON (e.g. `data/curated/wechat_161_humanoid_papers.json`).
   - Resolves each title to arXiv ID via the arXiv API.
   - Outputs one YAML per category with `paper_ids`, `seed_queries`, `max_papers`, and taxonomy-derived domains/tags.

2. **Add pagination to `scripts/ai4sci_lib/discovery.py`**
   - `discover_candidates(..., start=0, max_total=200)`.
   - Loop over offsets until `max_total` or no more results.

3. **Expand `seed_queries` generation**
   - For each workstream, generate 10–20 queries from the taxonomy path + synonyms.
   - Store a `query_expansion` template in the workstream schema.

4. **Project-wide candidate deduplication**
   - Central `.staging/tried_candidates.jsonl` written by `ai4sci_batch_pipeline.py`.
   - All workstreams read it before processing.

5. **Coverage reporter**
   - `scripts/report_coverage.py` prints tree coverage, domain counts, and exhausted workstreams.

6. **Mandatory backfill hook**
   - Add a `--backfill` flag to `ai4sci_batch_pipeline.py` that runs relationship backfill after a successful batch.

---

## How the 161-Paper List Should Have Been Handled

The correct flow on receiving the list would have been:

1. Parse → 161 structured records.
2. Resolve arXiv IDs for all titles.
3. Generate 10 workstream YAMLs (one per category) seeded with those IDs.
4. Run each workstream with pagination and query expansion.
5. After promotion, run relationship backfill.
6. Update README coverage metrics.

Instead, the old design would have required 161 manual entries or a generic keyword workstream that would miss most of them.

---

## Success Criteria

A workstream design is good when:

- Every `WORKSTREAM_TREE` leaf has a YAML.
- Each workstream can surface ≥20 relevant candidates per run.
- Known curated lists can be converted to workstreams in one command.
- Relationship count grows automatically after every batch.
- Coverage dashboard shows no domain with 0 entries and no exhausted workstream due to narrow queries.
