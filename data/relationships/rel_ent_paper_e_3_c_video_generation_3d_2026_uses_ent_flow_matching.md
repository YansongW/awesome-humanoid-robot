---
$id: rel_ent_paper_e_3_c_video_generation_3d_2026_uses_ent_flow_matching
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_e_3_c_video_generation_3d_2026
  name:
    en: 'E$^3$C: Video Generation with 3D Environmental Memory and Ego-Exo Human Pose Control'
    zh: 'E$^3$C: Video Generation with 3D Environmental Memory and Ego-Exo Human Pose Control'
target:
  id: ent_flow_matching
  name:
    en: Flow matching
    zh: 流匹配
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 00_foundations
description:
  en: 'E$^3$C: Video Generation with 3D Environmental Memory and Ego-Exo Human Pose Control uses Flow matching.'
  zh: 'E$^3$C: Video Generation with 3D Environmental Memory and Ego-Exo Human Pose Control使用流匹配。'
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-08-06'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 论文使用Flow matching目标函数进行训练。 | 证据: - Flow matching
    objective: L = E[ w(t) ||(ε - z_0) - ε_θ(z_t, t; τ, C)||_2^2 ], with z_t = (1-σ_t)z_0 + σ_t ε.'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_e_3_c_video_generation_3d_2026
  url: https://kg.rounds-tech.com/entry/ent_paper_e_3_c_video_generation_3d_2026/
  accessed_at: '2026-08-06'
---
