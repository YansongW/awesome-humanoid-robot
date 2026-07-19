---
$id: rel_ent_component_lidar_livox_mid360_uses_ent_concept_digital_twin
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_component_lidar_livox_mid360
  name:
    en: Solid-State LiDAR (e.g., Livox Mid-360)
    zh: 固态激光雷达
target:
  id: ent_concept_digital_twin
  name:
    en: Digital Twin
    zh: 数字孪生
domains:
  source_domain: 02_components
  target_domain: 08_software_middleware
description:
  en: Solid-State LiDAR (e.g., Livox Mid-360) uses Digital Twin.
  zh: 固态激光雷达使用数字孪生。
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-17'
  confidence: low
  notes: 'Mined by build_latent_relationships.py rule p6_llm_link_retry. Evidence: 激光雷达扫描数据可用于构建机器人的数字孪生环境。'
sources:
- id: src_001
  type: other
  title: KG body of ent_component_lidar_livox_mid360
  url: https://kg.rounds-tech.com/entry/ent_component_lidar_livox_mid360/
  accessed_at: '2026-07-17'
---
