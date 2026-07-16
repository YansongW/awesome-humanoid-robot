---
$id: rel_ent_robot_system_odri_bolt_uses_ent_component_bldc_motor
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_robot_system_odri_bolt
  name:
    en: ODRI Bolt (Open Dynamic Robot Initiative)
    zh: ODRI Bolt 开源双足机器人
target:
  id: ent_component_bldc_motor
  name:
    en: Brushless DC Motor
    zh: 无刷直流电机
domains:
  source_domain: 02_components
  target_domain: 02_components
description:
  en: ODRI's BLMC actuators are built from off-the-shelf frameless brushless motors combined with dual
    encoders and the custom MicroDriver electronics.
  zh: ODRI 的 BLMC 执行器以现成无框无刷电机为基础，结合双编码器与自研 MicroDriver 驱动卡构成。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-01'
  confidence: medium
  notes: 来源档案 data/roadmap/research/open-dynamic-robot-initiative.md 确认执行器物料以现成无框电机构成（BLMC 无刷力控执行器）。
sources:
- id: src_001
  type: website
  title: open_robot_actuator_hardware GitHub Repository
  url: https://github.com/open-dynamic-robot-initiative/open_robot_actuator_hardware
  accessed_at: '2026-07-01'
---
