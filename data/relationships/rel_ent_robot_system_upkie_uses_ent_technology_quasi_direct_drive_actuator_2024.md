---
$id: rel_ent_robot_system_upkie_uses_ent_technology_quasi_direct_drive_actuator_2024
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_robot_system_upkie
  name:
    en: Upkie Wheeled Biped Robot
    zh: Upkie 轮足双足机器人
target:
  id: ent_technology_quasi_direct_drive_actuator_2024
  name:
    en: Quasi Direct Drive Actuator
    zh: 准直驱执行器
domains:
  source_domain: 02_components
  target_domain: 07_ai_models_algorithms
description:
  en: Upkie uses four mjbots qdd100 quasi-direct-drive brushless servos (hip/knee) plus moteus drivers
    (wheels), all with open-source firmware and force control capability.
  zh: Upkie 采用 4 台 mjbots qdd100 准直驱无刷伺服（髋/膝）加 moteus 驱动器（轮），固件全开源、可力控。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-01'
  confidence: medium
  notes: 来源档案 data/roadmap/research/upkie.md 确认 mjbots qdd100 准直驱伺服方案。
sources:
- id: src_001
  type: website
  title: upkie/upkie GitHub Repository
  url: https://github.com/upkie/upkie
  accessed_at: '2026-07-01'
---
