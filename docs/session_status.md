# Session Status: 2026-07-01

> **Project**: awesome-humanoid-robot  
> **Goal**: Build a knowledge base for going from 0 to 1 on humanoid robot mass production and industrial application.  
> **Current Phase**: Unified ingestion framework deployed; curated high-confidence sources on autopilot, AI4Sci workstreams paused.

---

## Where We Are

Resumed work after the previous session. The previous AI4Sci workstream daemon and hourly cron have been stopped. We shifted strategy from LLM-driven workstreams to a **unified ingestion framework** for curated high-confidence sources, with the daemon paused until the pipeline is stable and quality gates are redefined.

### Completed (this session)

- [x] Assessed current project state: 1586 entities, 841 relationships; validation passing.
- [x] Imported **Awesome-VLA** curated list: 385 new papers.
- [x] Imported **awesome-humanoid-robot-learning** curated list: 410 new papers.
- [x] Imported **Humanoid_Robot_Learning_Paper_Notebooks/progress.json**: 55 new papers (368 total, 313 duplicates).
- [x] Imported **arXiv cs.RO RSS**: 50 new papers.
- [x] Imported **Unitree official news API**: 8 report entries.
- [x] Imported **NVIDIA robotics blog RSS**: 10 report entries.
- [x] Added **NVIDIA ASPIRE paper**: 1 paper.
- [x] Graph totals updated from **1586 → 1715 entities**, 841 relationships.
- [x] Designed and implemented `scripts/ingestion/` unified framework:
  - `core.py`: shared `Source` / `ParsedItem` / `IngestionResult` models.
  - `registry.py`: `data/sources.yaml` source registry.
  - `dedup.py`: title/arXiv-ID/source-URL deduplication across production + staging.
  - `writer.py`: schema-compliant Markdown writer with automatic layer inference.
  - `adapters/`: curated JSON, progress.json, arXiv RSS, Unitree API, NVIDIA RSS, WeChat articles.
  - `pipeline.py`: CLI with `--all`, `--source`, `--dry-run`, and JSON output.
- [x] Migrated `scripts/ingest_all_sources.sh` to call `python -m ingestion.pipeline --all`.
- [x] Verified dry-run counts match current graph (no unexpected additions or missing duplicates).
- [x] Moved old ad-hoc `import_*.py` and `ingest_*.py` scripts to `scripts/legacy/`.
- [x] Stopped the old AI4Sci workstream daemon (`bash-9p3397v1`) and deleted its hourly cron (`b4f040f4`).
- [x] Updated `docs/session_status.md` to reflect new phase.

### In Progress

- [ ] WeChat 386-article backlog remains blocked without a URL list or WebBridge text dump.

### Pending

- [ ] Define quality gates and re-enable workstreams or LLM-driven enrichment on top of ingested entries.
- [ ] Re-run relationship backfill to connect newly ingested papers to existing entities.
- [ ] Continue expanding cross-layer knowledge chains for high-priority domains (actuation, perception, manufacturing processes).

---

## Active Background Tasks

| Task ID | Command | Status |
|---------|---------|--------|
| `b62efa54` | Daily cron: `bash scripts/ingest_all_sources.sh` | active |

---

## Approved Plan

See plan file for details. The four phases are:

1. **Phase 1**: Workflow engine refactor (pagination, global dedup, curated-list ingestion).
2. **Phase 2**: Layer model and cross-layer relationship norms (`theoretical_depth`, whitelist, prompt upgrades).
3. **Phase 3**: Fill `WORKSTREAM_TREE.md` coverage (done as stubs; execution in progress).
4. **Phase 4**: Relationship backfill, validation gates, coverage dashboard, and review queue.

---

## Key Reminders

- This project is **private until v0.1.0**.
- All entries must follow the YAML frontmatter + Markdown format defined in the schema.
- All entries and relationships must pass `scripts/validate_entries.py`.
- **Comprehensiveness rule**: external curated lists are imported in full, not as Top-N selections.
- The central question is: **How do we go from 0 to 1 on humanoid robot mass production and industrial application?**

---

# Session Status: 2026-06-26

> **Project**: awesome-humanoid-robot  
> **Goal**: Build a knowledge base for going from 0 to 1 on humanoid robot mass production and industrial application.  
> **Current Phase**: Structural overhaul — workflow engine, taxonomy coverage, and cross-layer knowledge links.

---

## Where We Are

Following user feedback that the workstreams were still too sampler-like and that the graph lacked robustness, granularity, and cross-layer links, we entered plan mode and began a four-phase structural overhaul.

### Completed (this session)

- [x] Entered plan mode and wrote an approved plan: **four-phase deep refactor** of the workstream engine, layer model, tree coverage, and validation gates.
- [x] Implemented `scripts/resolve_curated_arxiv.py`: resolves curated paper titles to arXiv IDs with caching and polite rate limiting.
- [x] Resolved **86/161** WeChat-list papers to arXiv IDs (`data/curated/wechat_161_arxiv_resolution_complete.json`).
- [x] Implemented `scripts/generate_workstream_from_curated.py`: generates workstream YAMLs seeded with resolved arXiv IDs and taxonomy-aligned seed queries.
- [x] Generated **10 curated workstreams** from the 161-paper list under `scripts/ai4sci_workstreams/curated/wechat_161/`.
- [x] Upgraded `scripts/ai4sci_lib/discovery.py`:
  - Added pagination support (`start` offset) for arXiv and Semantic Scholar.
  - Added `max_total` so workstreams can discover 50–200 candidates, decoupled from `max_papers`.
  - Added project-wide `.staging/tried_candidates.jsonl` deduplication across all workstreams.
- [x] Updated `scripts/ai4sci_batch_pipeline.py` to use `max_results_per_query`, `max_total`, and global tried logging.
- [x] Improved `dry-run` mode: it now discovers candidates without calling the LLM.
- [x] Enforced `theoretical_depth` in extraction prompts and entry frontmatter.
- [x] Added cross-layer relationship whitelist in `scripts/ai4sci_lib/config.py`.
- [x] Extended `scripts/validate_entries.py` to report cross-layer mismatches and dangling relationships as warnings.
- [x] Implemented `scripts/backfill_theoretical_depth.py` and backfilled **265 entries** with inferred `theoretical_depth`.
- [x] Implemented `scripts/generate_missing_workstreams.py` and generated **129 stub workstream YAMLs** for all unchecked `WORKSTREAM_TREE.md` leaves, with priority 1 for manufacturing/assembly/policy/raw-materials/foundations.
- [x] Workstream count went from **36 → 175** (148 tree leaves + 10 curated extras + existing overlaps).
- [x] Verified `scripts/validate_entries.py` still passes; cross-layer warnings reduced from ~400 to ~40 after backfill.
- [x] Manually landed the **Whole-Body Control (WBC) knowledge chain** as a cross-layer demonstration:
  - Created 9 new entities spanning `method → formalism → equation → operator → principle → foundation`.
  - Created 9 standalone typed relationships (`formalizes`, `includes`, `uses`, `derived_from`, `has_prerequisite`, `solves`).
  - New entity directories: `research/methods`, `research/formalisms`, `research/equations`, `research/operators`, `research/principles`, `research/foundations`.
  - Added type-to-subdirectory mappings in `scripts/ai4sci_lib/config.py`.
- [x] Updated README stats to **293 entries / 808 relationships / 175 workstreams** across all language versions.
- [x] Manually landed the **Li-ion battery knowledge chain** as a cross-layer L1–L5 demonstration:
  - Updated `research/technologies/li_battery_humanoid.md` (`theoretical_depth: system`).
  - Created 6 new entities: `ent_method_equivalent_circuit_battery_model`, `ent_formalism_thevenin_equivalent_circuit`, `ent_equation_thevenin_terminal_voltage`, `ent_operator_voltage_divider`, `ent_principle_conservation_of_charge`, `ent_foundation_electrochemistry`.
  - Created 9 standalone typed relationships (`uses`, `integrates`, `formalizes`, `includes`, `derived_from`, `has_prerequisite`).
- [x] Manually landed the **Vision-Language-Action (VLA) knowledge chain** as a cross-layer L1–L5 demonstration:
  - Updated `research/technologies/on_device_vla_inference.md` and `research/foundations/ent_self_attention_equation.md`.
  - Created 5 new entities: `ent_method_action_token_prediction`, `ent_formalism_transformer_action_decoder`, `ent_operator_softmax_function`, `ent_principle_maximum_likelihood_estimation`, `ent_foundation_probability_theory`.
  - Created 9 standalone typed relationships.
  - Extended `CROSS_LAYER_RELATIONSHIPS` in `scripts/ai4sci_lib/config.py` with `formalism → foundation` and `formalism → principle`.
- [x] Implemented `scripts/backfill_cross_layer_relationships.py`: LLM-driven proposal of cross-layer/engineering relationships for system-level entities, with caching, whitelist validation, and staging output for human review.
- [x] Implemented `scripts/coverage_dashboard.py`: generates `docs/coverage_dashboard.md`, `.staging/review/human_review_queue.md`, and `.staging/review/dashboard_summary.json`.
- [x] Updated README stats to **304 entries / 826 relationships / 175 workstreams** across all language versions.
- [x] Root-caused and fixed the low hit-rate in foundational/economics workstreams:
  - Found that `generate_missing_workstreams.py` was appending `.yaml` to seed queries, producing malformed arXiv searches like `economics cost analysis.yaml`.
  - Fixed the generator to use `Path.stem` and cleaned its topic extraction (drop numeric domain prefixes, map `or_ie` → `operations research`).
  - Added optional `relevance_context` support to `extraction.classify_relevance`, `pipeline.process_source`, and `ai4sci_batch_pipeline.py`.
  - Created and ran `scripts/refine_generated_workstreams.py`, which rewrote seed queries and added `relevance_context` for **129** generated stubs.
  - Cleared stale exhaustion logs for affected workstreams so the daemon re-runs them.
  - Verified with dry-run and end-to-end tests: `cost_analysis` now discovers **100 candidates** (was near-zero) and successfully staged an entry + 6 relationships on a single-paper run.

### In Progress

- [ ] Daemon `bash-dpgco1uk` is running and will pick up new priority workstreams automatically.
- [ ] Hourly cron reminder (`4f944d7a`) reports task status.

### Pending

- [ ] Run and promote outputs from the new curated and stub workstreams.
- [ ] Run `scripts/backfill_cross_layer_relationships.py` on the 199 system-level entities that currently lack cross-layer links, then review and promote high-confidence proposals.
- [ ] Address the 39 pre-existing dangling relationships (mostly `proposed_*` entities from earlier pipeline runs).
- [ ] Continue expanding cross-layer knowledge chains for other high-priority domains (actuation, perception, manufacturing processes).

---

## Active Background Tasks

| Task ID | Command | Status |
|---------|---------|--------|
| `bash-dpgco1uk` | Workstream daemon loop 5-minute interval (`ai4sci_run_next_workstream.py`) | running |
| `4f944d7a` | Hourly cron reminder to check `TaskOutput` | active |

---

## Approved Plan

See plan file for details. The four phases are:

1. **Phase 1**: Workflow engine refactor (pagination, global dedup, curated-list ingestion).
2. **Phase 2**: Layer model and cross-layer relationship norms (`theoretical_depth`, whitelist, prompt upgrades).
3. **Phase 3**: Fill `WORKSTREAM_TREE.md` coverage (done as stubs; execution in progress).
4. **Phase 4**: Relationship backfill, validation gates, coverage dashboard, and review queue.

---

## Key Reminders

- This project is **private until v0.1.0**.
- All entries must follow the YAML frontmatter + Markdown format defined in the schema.
- All entries and relationships must pass `scripts/validate_entries.py`.
- **Comprehensiveness rule**: external curated lists are imported in full, not as Top-N selections.
- The central question is: **How do we go from 0 to 1 on humanoid robot mass production and industrial application?**

---

# Session Status: 2026-06-25

> **Project**: awesome-humanoid-robot  
> **Goal**: Build a knowledge base for going from 0 to 1 on humanoid robot mass production and industrial application.  
> **Current Phase**: Option A — Content-first industry-chain sprint (hardware → manufacturing → applications).

---

## Where We Are

We are executing the **approved Option A plan**: a 4-week content sprint to grow the knowledge graph from ~80 entries toward 120–150, with a focus on the industry chain rather than tooling refactoring.

The arXiv discovery bug (`submittedDate` → `relevance`) is fixed, the hourly workstream daemon is running, and the first hardware workstream (`motor_selection`) is being processed. New hardware and downstream workstream configs have been committed.

### Completed (this session)

- [x] Created and committed three hardware workstreams:
  - `scripts/ai4sci_workstreams/design/hardware/actuation/motor_selection.yaml`
  - `scripts/ai4sci_workstreams/design/hardware/actuation/reducer_selection.yaml`
  - `scripts/ai4sci_workstreams/design/hardware/power/battery_cells.yaml`
- [x] Fixed invalid target domain `02_components_supply_chain` → `02_components` in four existing workstreams.
- [x] Created and committed four downstream workstreams:
  - `manufacturing/processes/actuator_assembly.yaml`
  - `manufacturing/testing/system_integration_test.yaml`
  - `applications/logistics/warehouse.yaml`
  - `applications/domestic/home_assistive.yaml`
- [x] Started a foreground run of `motor_selection` (task `bash-xnup903m`) to validate the new hardware configs.
- [x] Improved `scripts/ai4sci_run_next_workstream.py`: sorts by `priority`, uses config `name` for output tracking, and skips workstreams after two all-error runs.
- [x] Added `priority` to hardware (1), manufacturing/supply-chain (2), and application (3) workstreams.
- [x] Renamed `cross_domain_relationships.yaml` → `cross_domain.yaml` to align filename with config name.
- [x] Added `scripts/clean_staging_dangling.py` to remove dangling edges from staged workstreams before promotion.
- [x] Updated `scripts/ai4sci_lib/pipeline.py` to filter dangling edges at generation time.
- [x] Promoted `motor_selection` outputs: **2 entries, 1 relationship**.
- [x] Promoted `ai_to_hardware_requirements` daemon outputs: **2 entries**.
- [x] Promoted `reducer_selection` outputs: **3 entries**.
- [x] Promoted `battery_cells` output: **1 entry** (1 duplicate, 1 LLM JSON error).
- [x] Promoted daemon outputs: **force_torque_sensors** 2 entries, **actuator_assembly** 1 entry, **system_integration_test** 1 entry, **companies** 2 entries, **rare_earth_magnets** 1 entry, **raw_materials** 1 entry, **home_assistive** 2 entries, **warehouse_logistics** 1 entry.
- [x] Updated README stats to **99 entries / 58 relationships / 23 workstreams**; validation passing.
- [x] Restarted workstream daemon (task `bash-qhu214g1`) with 60s interval, no timeout, and `PYTHONUNBUFFERED=1`.
- [x] Updated hourly cron reminder to monitor new daemon (`bash-qhu214g1`).
- [x] Daemon completed full pass over all 23 workstreams; stopped because all have produced staged outputs.
- [x] Promoted final batch: **cross_domain** 3 entries, **model_predictive_control** 2 entries, **whole_body_control** 3 entries, **vla** 1 entry, **simulation_platforms** 1 entry, **iso_13482** 3 entries (1 duplicate skipped).
- [x] Fixed validation error: mapped `uses_product_of` → `uses` in `RELATIONSHIP_TYPE_MAP`.
- [x] Final stats: **112 entries / 58 relationships / 23 workstreams**, validation passing.
- [x] Created 6 new workstreams for underrepresented domains: `critical_minerals`, `quality_control`, `precision_machining`, `functional_safety`, `safety_standards`, `assistive_rehabilitation`.
- [x] Updated README workstream count to 29.
- [x] Restarted daemon (task `bash-jm85j3bv`) with 60s interval to run new workstreams.
- [x] Recreated hourly cron reminder (`d4d0c5b1`) to monitor new daemon.
- [x] Daemon completed all new workstreams; stopped due to idle.
- [x] Cleaned and promoted new outputs: **precision_machining** 1 entry, **functional_safety** 1 entry, **quality_control** 1 entry, **assistive_rehabilitation** 1 entry, **safety_standards** 2 entries. `critical_minerals` produced 0 usable entries (exhausted).
- [x] Removed accidentally committed temporary `paper.*` files and updated `.gitignore`.
- [x] Final stats: **118 entries / 58 relationships / 29 workstreams**, validation passing.
- [x] Created 7 new workstreams for underrepresented domains: `cameras_vision`, `imu_inertial_sensors`, `tactile_sensors`, `edge_compute`, `ros2_middleware`, `industrial_inspection`, `global_supply_chain_risk`.
- [x] Raised `max_papers` to **15** on all existing workstream configs.
- [x] Cleared low-yield staging summaries so under-performing workstreams can re-run.
- [x] Implemented `scripts/relationship_backfill.py` to add relationships among existing entities.
- [x] Ran backfill: **+216 relationships**, bringing the graph to **118 entries / 274 relationships / 36 workstreams**, validation passing.
- [x] Updated README stats across `README.md`, `README.zh.md`, and `README.ko.md`.
- [x] Restarted workstream daemon (task `bash-oyptjn50`) with 5-minute interval to run new and re-run workstreams.
- [x] Recreated hourly cron reminder (`87620067`) to monitor the new daemon.
- [x] Fixed daemon env issue: `AI4SCI_USE_KIMI_CLI` was not exported, causing "No LLM API key found" errors in `actuator_module_design`.
- [x] Cleared the failed `actuator_module_design` staging summary so it can retry.
- [x] Restarted daemon with corrected environment (task `bash-baaw35x9`).
- [x] Updated hourly cron reminder (`175967a7`) to monitor the corrected daemon.
- [x] Read and parsed the WeChat curated list of 161 humanoid mobile-manipulation papers.
- [x] Saved structured data to `data/curated/wechat_161_humanoid_papers.json` and a human-readable summary to `data/curated/wechat_161_humanoid_papers.md`.
- [x] Analyzed the list: 10 categories, heavy concentration in 2025–2026, top contributors include NVIDIA, Stanford, CMU, UC San Diego.
- [x] Imported all 161 papers into the production graph (159 new entries, 2 exact duplicates skipped), mapped each to schema-compliant domains/layers/tags based on the article's 10 categories.
- [x] Fixed validation issue (`ai_proposed` → `unverified`) for all imported entries.
- [x] Updated README stats to **277 entries / 274 relationships / 36 workstreams** across all language versions.
- [x] Added `AGENTS.md` codifying the comprehensiveness rule: external curated lists are imported in full, not as Top-N selections.
- [x] Ran relationship backfill after import: **+482 relationships**, bringing the graph to **277 entries / 756 relationships / 36 workstreams**, validation passing.
- [x] Updated README stats again to **277 entries / 756 relationships / 36 workstreams** across all language versions.
- [x] Audited existing workstream coverage and produced `docs/audit/workstream_coverage_2026-06-26.md`.
- [x] Confirmed that previous workstreams were keyword-limited samples, not full quantitative surveys; identified taxonomy gaps against `WORKSTREAM_TREE.md`.
- [x] Wrote `docs/ai4sci/workstream_design_reflection.md` with root-cause analysis and redesign principles for dense taxonomy coverage.
- [x] Added `scripts/auto_promote_staging.py` to bulk-promote staged daemon outputs; promoted 7 entries and 38 relationships from current daemon runs.
- [x] Added `scripts/report_coverage.py` and published first coverage report: 36/148 workstream tree leaves (24.3%), heavy concentration in `07_ai_models_algorithms` and `06_design_engineering`, weak coverage in `03_manufacturing_processes`, `04_assembly_integration_testing`, `12_policy_regulation_ethics`, `01_raw_materials`.
- [x] Extended `RELATIONSHIP_TYPE_MAP` to normalize `implements_on`, `introduces`, `affiliated_with`, etc., and fixed promoted relationship validation errors.
- [x] Updated README stats to **284 entries / 794 relationships / 36 workstreams** across all language versions.
- [x] Fixed duplicate-candidate loop in `scripts/ai4sci_batch_pipeline.py`: added per-workstream `tried.json` so each run processes fresh candidates instead of re-attempting the same already-existing papers.
- [x] Cleared the exhausted `actuator_module_design` summary and seeded `tried.json` with the 3 duplicate arXiv IDs so it can move on to remaining candidates.
- [x] Restarted daemon with the duplicate fix (task `bash-0etvcdd4`).
- [x] Updated hourly cron reminder (`77c13b07`) to monitor the fixed daemon.
- [x] Fixed `is_exhausted` logic: workstreams with no successes after ≥3 runs are now skipped, preventing infinite loops on tiny candidate pools (e.g. `battery_cells`).
- [x] Restarted daemon with exhaustion fix (task `bash-dpgco1uk`).
- [x] Updated hourly cron reminder (`4f944d7a`) to monitor the new daemon.
- [x] Auto-promoted additional staged relationships (+5), bringing graph to **284 entries / 799 relationships / 36 workstreams**.
- [x] Updated README stats to **284 entries / 799 relationships / 36 workstreams** across all language versions.

### In Progress

- [ ] Daemon processing new/re-run workstreams (`bash-dpgco1uk`).
- [ ] Hourly cron reminder (`4f944d7a`) reports task status.

### Pending

- [ ] Review daemon outputs each hour and promote valid entries/relationships.
- [ ] Fill taxonomy gaps from `WORKSTREAM_TREE.md` (manufacturing, assembly/testing, policy, mass production, hardware stacks).
- [ ] Periodically check daemon logs and re-enable/restart if it stalls.

---

## Active Background Tasks

| Task ID | Command | Status |
|---------|---------|--------|
| `bash-dpgco1uk` | Workstream daemon loop 5-minute interval (`ai4sci_run_next_workstream.py`) | running |
| `bash-0etvcdd4` | Previous daemon loop (exhaustion-loop bug, stopped) | stopped |
| `bash-baaw35x9` | Previous daemon loop (duplicate loop, stopped) | stopped |
| `bash-oyptjn50` | Previous daemon loop (env issue, stopped) | stopped |
| `bash-jm85j3bv` | Previous daemon loop | completed |
| `bash-qhu214g1` | Previous daemon loop | completed |
| `4f944d7a` | Hourly cron reminder to check `TaskOutput` | active |

---

## Approved Plan (Option A)

1. **Week 1**: Hardware — motors, reducers, battery cells, sensors, actuator module design.
2. **Week 2**: Manufacturing & supply chain — assembly, testing, raw materials, mass production.
3. **Week 3**: Applications & markets — logistics, home assistance, industrial inspection, policy/safety.
4. **Week 4**: Cross-cutting AI/software integration and graph integrity cleanup.

Productization remains a **planning-only** topic until explicitly discussed and approved.

---

## Key Reminders

- This project is **private until v0.1.0**.
- All entries must follow the YAML frontmatter + Markdown format defined in `information_model.md`.
- All entries and relationships must pass `scripts/validate_entries.py`.
- No external awesome-list references should appear in project content.
- **AI4Sci source requirement**: every factual claim must cite a peer-reviewed paper, official report, standard, or reputable industry analysis; speculative claims must be explicitly labeled.
- The central question is: **How do we go from 0 to 1 on humanoid robot mass production and industrial application?**
