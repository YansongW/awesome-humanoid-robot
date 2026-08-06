---
$id: rel_ent_paper_flap_fov_constrained_active_perception_p_2026_uses_ent_component_livox_mid_360_lidar_2024
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_flap_fov_constrained_active_perception_p_2026
  name:
    en: 'FLAP: FOV-Constrained Active Perception Planning for Prior-Map-Free 3D Navigation'
    zh: 'FLAP: FOV-Constrained Active Perception Planning for Prior-Map-Free 3D Navigation'
target:
  id: ent_component_livox_mid_360_lidar_2024
  name:
    en: Livox Mid-360 LiDAR
    zh: Livox Mid-360 激光雷达
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 02_components
description:
  en: 'FLAP: FOV-Constrained Active Perception Planning for Prior-Map-Free 3D Navigation uses Livox Mid-360 LiDAR.'
  zh: 'FLAP: FOV-Constrained Active Perception Planning for Prior-Map-Free 3D Navigation使用Livox Mid-360 激光雷达。'
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-08-06'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 论文在真实世界实验中使用Livox Mid-360 LiDAR作为传感器。 | 证据:
    仿真部分覆盖水平窄空间、头顶障碍物、U形迷宫与垂直管道四个场景，传感器配置涵盖全向LiDAR（水平FOV 360°）与前向深度相机（水平FOV约78°、垂直FOV约64°）两种代表性设置；真实世界实验使用Livox Mid-360 LiDAR（水平FOV
    360°，垂直FOV向上约52°、向下约7°）与Orbbec Gemini 335深度相机。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_flap_fov_constrained_active_perception_p_2026
  url: https://kg.rounds-tech.com/entry/ent_paper_flap_fov_constrained_active_perception_p_2026/
  accessed_at: '2026-08-06'
---
