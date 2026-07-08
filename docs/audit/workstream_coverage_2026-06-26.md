# Workstream Coverage Audit — 2026-06-26

## Executive Summary

The current 36 workstreams are **exploratory samples, not exhaustive surveys**. They rely on 4–5 seed queries each and a `max_papers` cap of 15, which means they discover only the top-ranked results for a handful of keywords. This is sufficient for bootstrapping the graph but does **not** satisfy the comprehensiveness requirement.

## Findings

### 1. Output is sparse

| Area | Workstreams | Total successes | Avg success per workstream |
|------|-------------|----------------|---------------------------|
| design/hardware | 9 | ~14 | 1.6 |
| manufacturing/* | 4 | 0 | 0.0 |
| applications/* | 4 | 3 | 0.8 |
| mass_production/supply_chain | 5 | 2 | 0.4 |
| policy/safety | 2 | 5 | 2.5 |
| foundations | 4 | 8 | 2.0 |
| definition/algorithm_survey | 3 | 7 | 2.3 |
| infra/software | 2 | 0 | 0.0 |

Many workstreams have **0 staged successes** (`assistive_rehabilitation`, `industrial_inspection`, `warehouse_logistics`, `cameras_vision`, `imu_inertial_sensors`, `actuator_assembly`, `precision_machining`, `functional_safety`, `system_integration_test`, `quality_control`, `critical_minerals`, `global_supply_chain_risk`, `rare_earth_magnets`, `raw_materials`, `simulation_platforms`, `ros2_middleware`).

### 2. Seed queries are narrow

Almost every config uses only 4–5 free-text seed queries and **no explicit paper IDs**. Examples of typical coverage:

- `actuator_module_design`: 4 queries, max 15 papers → 2 successes, 1 duplicate, 7 runs before exhaustion.
- `battery_cells`: 5 queries, max 15 papers → 0 successes after 3 runs.
- `vla`: 4 queries, max 15 papers → 2 successes, 1 duplicate.

This is keyword-driven sampling, not a systematic literature review.

### 3. Taxonomy coverage is incomplete

Comparing the 36 configs against `docs/ai4sci/WORKSTREAM_TREE.md` shows large gaps:

- **Definition / requirements**: use cases, system architecture, business models missing.
- **Algorithm surveys**: VLM for robotics, world models, WAM, imitation learning, RL locomotion, sim-to-real, manipulation policies, loco-manipulation missing.
- **Hardware**: linear actuators, hand actuators, vision/depth/lidar/encoder sensors, BMS/thermal, charging, edge/real-time/communication compute, structural materials missing.
- **Software & AI architecture**: perception/planning/control/learning stacks missing.
- **Mechanical design**: morphology/DOF, kinematics/dynamics, DfX missing.
- **Testing**: joint/balance/calibration/environmental test benches missing.
- **MVP / EVT / PVT / mass production**: almost entirely missing.
- **Policy / regulation / markets**: only `safety_standards` and `iso_13482` present.

### 4. Relationship generation is downstream-limited

The pipeline only proposes relationships when it processes a source. Because many workstreams produce 0–2 entries, relationship counts stay low unless a separate backfill pass is run.

## Root Cause

1. **Scope was content-first sprint**, not full taxonomy coverage.
2. **Discovery is capped** (`max_papers=15`, `max_results_per_query=max_papers`) with no pagination or exhaustive keyword expansion.
3. **No seed paper lists** were provided, so the LLM/search API decides what to retrieve.
4. **Workstream tree existed as TODO but was not fully implemented**; only a subset of leaves became YAML files.

## Recommended Corrective Actions

1. **Convert the 161-paper WeChat curated list into explicit workstream seeds**  
   Resolve each paper's arXiv ID and add them as `paper_ids` to 10 category-aligned workstreams. This guarantees the curated set is represented in the graph (already imported as entries; now also traceable via workstream provenance).

2. **Expand low-yield workstreams**  
   - Increase `max_papers` to 50+ and add 10–20 diverse seed queries per workstream.  
   - Add `paper_ids` from known surveys/review papers in each area.  
   - Use the duplicate-skip fix in `ai4sci_batch_pipeline.py` so repeated runs exhaust the candidate pool instead of looping.

3. **Fill taxonomy gaps from `WORKSTREAM_TREE.md`**  
   Create YAML configs for the unchecked leaves, prioritizing:  
   - use cases / system architecture / business models  
   - missing algorithm surveys (world models, imitation learning, sim-to-real, manipulation policies)  
   - missing hardware stacks (vision/depth/lidar, BMS/thermal, edge compute, structural materials)  
   - missing test/MVP/EVT/PVT/mass-production workstreams  
   - policy, regulation, market, and certification workstreams

4. **Run relationship backfill after every bulk import**  
   Do not wait for the pipeline to propose relationships; run `relationship_backfill.py` to connect new entries to existing entities.

5. **Add a coverage metric**  
   Track `(workstream_count / WORKSTREAM_TREE leaf count)` and `(entries per ontology domain)` in README stats to make gaps visible.
