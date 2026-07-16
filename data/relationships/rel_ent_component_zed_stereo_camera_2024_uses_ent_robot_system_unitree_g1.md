---
$id: rel_ent_component_zed_stereo_camera_2024_uses_ent_robot_system_unitree_g1
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_component_zed_stereo_camera_2024
  name:
    en: ZED Stereo Camera
    zh: ZED 立体相机
target:
  id: ent_robot_system_unitree_g1
  name:
    en: Unitree G1 Humanoid Robot
    zh: Unitree G1 人形机器人
domains:
  source_domain: 02_components
  target_domain: 02_components
description:
  en: ZED Stereo Camera uses Unitree G1 Humanoid Robot.
  zh: ZED 立体相机使用Unitree G1 人形机器人。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p6_llm_link. Evidence: ZED立体相机可用于Unitree G1人形机器人的导航和空间AI任务。'
sources:
- id: src_001
  type: other
  title: KG body of ent_component_zed_stereo_camera_2024
  url: https://kg.rounds-tech.com/entry/ent_component_zed_stereo_camera_2024/
  accessed_at: '2026-07-16'
---
