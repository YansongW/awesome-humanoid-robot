---
$id: rel_ent_component_lidar_livox_mid360_uses_ent_process_p12_1_2
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_component_lidar_livox_mid360
  name:
    en: Solid-State LiDAR (e.g., Livox Mid-360)
    zh: 固态激光雷达
target:
  id: ent_process_p12_1_2
  name:
    en: SLAM and Scene Understanding
    zh: SLAM 与场景理解
domains:
  source_domain: 02_components
  target_domain: 07_ai_models_algorithms
description:
  en: Solid-State LiDAR (e.g., Livox Mid-360) uses SLAM and Scene Understanding.
  zh: 固态激光雷达使用SLAM 与场景理解。
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-17'
  confidence: low
  notes: 'Mined by build_latent_relationships.py rule p6_llm_link_retry. Evidence: 固态激光雷达用于SLAM和场景理解，提供3D测距数据。'
sources:
- id: src_001
  type: other
  title: KG body of ent_component_lidar_livox_mid360
  url: https://kg.rounds-tech.com/entry/ent_component_lidar_livox_mid360/
  accessed_at: '2026-07-17'
---
