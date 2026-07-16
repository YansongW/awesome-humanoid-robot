---
$id: rel_ent_robot_system_odri_bolt_uses_ent_technology_quasi_direct_drive_actuator_2024
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_robot_system_odri_bolt
  name:
    en: ODRI Bolt (Open Dynamic Robot Initiative)
    zh: ODRI Bolt 开源双足机器人
target:
  id: ent_technology_quasi_direct_drive_actuator_2024
  name:
    en: Quasi Direct Drive Actuator
    zh: 准直驱执行器
domains:
  source_domain: 02_components
  target_domain: 07_ai_models_algorithms
description:
  en: 'ODRI Bolt uses the initiative''s self-developed BLMC brushless force-controlled actuators: off-the-shelf
    frameless motors with dual encoders and a custom MicroDriver card, with a low gear ratio and high
    torque transparency for proprioceptive force control.'
  zh: ODRI Bolt 采用该计划自研的 BLMC 无刷力控执行器：现成无框电机 + 双编码器 + 自研 MicroDriver 驱动卡，低减速比、高扭矩透明度，支持本体感知力控。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-01'
  confidence: medium
  notes: 来源档案 data/roadmap/research/open-dynamic-robot-initiative.md 确认 BLMC 力控执行器方案，并将 ODRI 定位为'准直驱 +
    力控'技术路线的代表项目。
sources:
- id: src_001
  type: website
  title: open_robot_actuator_hardware GitHub Repository
  url: https://github.com/open-dynamic-robot-initiative/open_robot_actuator_hardware
  accessed_at: '2026-07-01'
---
