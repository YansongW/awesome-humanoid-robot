---
$id: rel_ent_robot_system_bruce_uses_ent_technology_quasi_direct_drive_actuator_2024
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_robot_system_bruce
  name:
    en: BRUCE (Bipedal Robot Unit with Compliance Enhanced)
    zh: BRUCE 儿童尺寸人形机器人
target:
  id: ent_technology_quasi_direct_drive_actuator_2024
  name:
    en: Quasi Direct Drive Actuator
    zh: 准直驱执行器
domains:
  source_domain: 02_components
  target_domain: 07_ai_models_algorithms
description:
  en: BRUCE uses self-developed Koala BEAR proprioceptive quasi-direct-drive actuators (250 g each, 10.5
    N.m peak torque) with liquid cooling on key joints.
  zh: BRUCE 采用自研 Koala BEAR 本体感知准直驱执行器（单台 250 g、峰值扭矩 10.5 N·m），关键关节液态冷却。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-01'
  confidence: medium
  notes: 来源档案 data/roadmap/research/bruce-westwood.md 确认 Koala BEAR 准直驱执行器与液冷方案（半直驱/QDD 路线）。
sources:
- id: src_001
  type: website
  title: BRUCE at World Robot Conference
  url: https://www.worldrobotconference.com/ex/product/244.html
  accessed_at: '2026-07-01'
---
