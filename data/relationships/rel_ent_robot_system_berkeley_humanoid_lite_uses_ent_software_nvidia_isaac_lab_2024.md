---
$id: rel_ent_robot_system_berkeley_humanoid_lite_uses_ent_software_nvidia_isaac_lab_2024
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_robot_system_berkeley_humanoid_lite
  name:
    en: Berkeley Humanoid Lite
    zh: 伯克利轻量人形机器人
target:
  id: ent_software_nvidia_isaac_lab_2024
  name:
    en: NVIDIA Isaac Lab
    zh: NVIDIA Isaac Lab
domains:
  source_domain: 02_components
  target_domain: 08_software_middleware
description:
  en: Berkeley Humanoid Lite organizes its training and simulation stack around NVIDIA Isaac Lab, with
    URDF/MJCF/USD descriptions and sim2sim validation.
  zh: Berkeley Humanoid Lite 基于 NVIDIA Isaac Lab 组织训练与仿真目录结构，提供 URDF/MJCF/USD 三种描述格式并支持 sim2sim 验证。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-01'
  confidence: medium
  notes: 来源档案 data/roadmap/research/berkeley-humanoid-lite.md 确认训练与仿真基于 NVIDIA Isaac Lab。
sources:
- id: src_001
  type: website
  title: HybridRobotics/Berkeley-Humanoid-Lite GitHub Repository
  url: https://github.com/HybridRobotics/Berkeley-Humanoid-Lite
  accessed_at: '2026-07-01'
---
