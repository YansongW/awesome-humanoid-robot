---
$id: rel_ent_robot_system_berkeley_humanoid_lite_uses_ent_technology_quasi_direct_drive_actuator_2024
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_robot_system_berkeley_humanoid_lite
  name:
    en: Berkeley Humanoid Lite
    zh: 伯克利轻量人形机器人
target:
  id: ent_technology_quasi_direct_drive_actuator_2024
  name:
    en: Quasi Direct Drive Actuator
    zh: 准直驱执行器
domains:
  source_domain: 02_components
  target_domain: 07_ai_models_algorithms
description:
  en: Berkeley Humanoid Lite uses two self-designed quasi-direct-drive actuators (6512 x10 and 5010 x12)
    built around 3D-printed cycloidal reducers.
  zh: Berkeley Humanoid Lite 采用两种规格自研准直驱执行器（6512×10 与 5010×12），核心为 3D 打印摆线针轮减速器。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-01'
  confidence: medium
  notes: 来源档案 data/roadmap/research/berkeley-humanoid-lite.md 确认自研准直驱执行器方案。
sources:
- id: src_001
  type: website
  title: Berkeley Humanoid Lite paper arXiv:2504.17249
  url: https://arxiv.org/abs/2504.17249
  accessed_at: '2026-07-01'
---
