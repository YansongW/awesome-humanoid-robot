---
$id: rel_ent_component_lidar_livox_mid360_uses_ent_method_sim_to_real
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_component_lidar_livox_mid360
  name:
    en: Solid-State LiDAR (e.g., Livox Mid-360)
    zh: 固态激光雷达
target:
  id: ent_method_sim_to_real
  name:
    en: Sim-to-Real Transfer
    zh: Sim-to-Real迁移
domains:
  source_domain: 02_components
  target_domain: 07_ai_models_algorithms
description:
  en: Solid-State LiDAR (e.g., Livox Mid-360) uses Sim-to-Real Transfer.
  zh: 固态激光雷达使用Sim-to-Real迁移。
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-17'
  confidence: low
  notes: 'Mined by build_latent_relationships.py rule p6_llm_link_retry. Evidence: 激光雷达感知数据有助于缩小仿真与现实的差距。'
sources:
- id: src_001
  type: other
  title: KG body of ent_component_lidar_livox_mid360
  url: https://kg.rounds-tech.com/entry/ent_component_lidar_livox_mid360/
  accessed_at: '2026-07-17'
---
