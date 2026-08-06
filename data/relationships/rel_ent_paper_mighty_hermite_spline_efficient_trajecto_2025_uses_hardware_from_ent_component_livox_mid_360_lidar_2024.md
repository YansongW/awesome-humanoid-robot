---
$id: rel_ent_paper_mighty_hermite_spline_efficient_trajecto_2025_uses_hardware_from_ent_component_livox_mid_360_lidar_2024
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses_hardware_from
source:
  id: ent_paper_mighty_hermite_spline_efficient_trajecto_2025
  name:
    en: 'MIGHTY: Hermite Spline-based Efficient Trajectory Planning'
    zh: 'MIGHTY: Hermite Spline-based Efficient Trajectory Planning'
target:
  id: ent_component_livox_mid_360_lidar_2024
  name:
    en: Livox Mid-360 LiDAR
    zh: Livox Mid-360 激光雷达
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 02_components
description:
  en: 'MIGHTY: Hermite Spline-based Efficient Trajectory Planning uses hardware from Livox Mid-360 LiDAR.'
  zh: 'MIGHTY: Hermite Spline-based Efficient Trajectory Planninguses_hardware_fromLivox Mid-360 激光雷达。'
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-08-06'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 论文在硬件测试中使用了Livox Mid-360 LiDAR作为传感器。 | 证据: 最后在动态环境（含
    100 个动态障碍物，以及动态+静态混合场景）中验证避障能力，并在硬件上（机载 Intel NUC 13，Livox Mid-360 LiDAR，PX4 飞控）进行长时、高速及动态障碍物飞行测试。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_mighty_hermite_spline_efficient_trajecto_2025
  url: https://kg.rounds-tech.com/entry/ent_paper_mighty_hermite_spline_efficient_trajecto_2025/
  accessed_at: '2026-08-06'
---
