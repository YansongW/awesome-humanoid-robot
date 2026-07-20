---
$id: rel_ent_component_livox_mid_360_lidar_2024_uses_ent_process_p12_1_2
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_component_livox_mid_360_lidar_2024
  name:
    en: Livox Mid-360 LiDAR
    zh: Livox Mid-360 激光雷达
target:
  id: ent_process_p12_1_2
  name:
    en: SLAM and Scene Understanding
    zh: SLAM 与场景理解
domains:
  source_domain: 02_components
  target_domain: 07_ai_models_algorithms
description:
  en: Livox Mid-360 LiDAR uses SLAM and Scene Understanding.
  zh: Livox Mid-360 激光雷达使用SLAM 与场景理解。
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-17'
  confidence: low
  notes: 'Mined by build_latent_relationships.py rule p6_llm_link_retry. Evidence: 固态激光雷达用于SLAM和场景理解，提供3D测距数据。 [merged on 2026-07-20: duplicate entity ent_component_lidar_livox_mid360 merged into ent_component_livox_mid_360_lidar_2024; endpoint migrated; original evidence from the merged card body]'
sources:
- id: src_001
  type: other
  title: KG body of ent_component_livox_mid_360_lidar_2024
  url: https://kg.rounds-tech.com/entry/ent_component_livox_mid_360_lidar_2024/
  accessed_at: '2026-07-17'
---
