---
$id: rel_ent_paper_state_nav_stability_aware_trav_2025_uses_ent_method_model_predictive_control
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_state_nav_stability_aware_trav_2025
  name:
    en: 'STATE-NAV: Stability-Aware Traversability Estimation for Bipedal Navigation on Rough Terrain'
    zh: 'STATE-NAV: Stability-Aware Traversability Estimation for Bipedal Navigation on Rough Terrain'
target:
  id: ent_method_model_predictive_control
  name:
    en: Model Predictive Control (MPC)
    zh: 模型预测控制（MPC）
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: 'STATE-NAV: Stability-Aware Traversability Estimation for Bipedal Navigation on Rough Terrain uses Model Predictive
    Control (MPC).'
  zh: 'STATE-NAV: Stability-Aware Traversability Estimation for Bipedal Navigation on Rough Terrain使用模型预测控制（MPC）。'
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 该论文将模型预测控制（MPC）集成到分层规划器中用于安全执行，表明其使用了MPC。 |
    证据: This velocity-based traversability is integrated into a hierarchical planner that combines traversability-informed
    Rapid Random Tree Star (TravRRT*) for time-efficient planning and Model Predictive Control (MPC) for safe execution.'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_state_nav_stability_aware_trav_2025
  url: https://kg.rounds-tech.com/entry/ent_paper_state_nav_stability_aware_trav_2025/
  accessed_at: '2026-07-16'
---
