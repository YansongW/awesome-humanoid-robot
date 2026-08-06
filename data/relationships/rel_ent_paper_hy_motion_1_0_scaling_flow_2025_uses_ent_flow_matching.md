---
$id: rel_ent_paper_hy_motion_1_0_scaling_flow_2025_uses_ent_flow_matching
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_hy_motion_1_0_scaling_flow_2025
  name:
    en: 'HY-Motion 1.0: Scaling Flow Matching Models for Text-To-Motion Generation'
    zh: 'HY-Motion 1.0: Scaling Flow Matching Models for Text-To-Motion Generation'
target:
  id: ent_flow_matching
  name:
    en: Flow matching
    zh: 流匹配
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 00_foundations
description:
  en: 'HY-Motion 1.0: Scaling Flow Matching Models for Text-To-Motion Generation uses Flow matching.'
  zh: 'HY-Motion 1.0: Scaling Flow Matching Models for Text-To-Motion Generation使用流匹配。'
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-08-06'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 论文采用Flow matching目标函数进行训练。 | 证据: - **Flow matching
    objective**: Optimal transport path x_t = (1−t)x₀ + tx₁, loss L_FM = E[||v_θ(x_t, c, t) − (x₁−x₀)||²].'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_hy_motion_1_0_scaling_flow_2025
  url: https://kg.rounds-tech.com/entry/ent_paper_hy_motion_1_0_scaling_flow_2025/
  accessed_at: '2026-08-06'
---
