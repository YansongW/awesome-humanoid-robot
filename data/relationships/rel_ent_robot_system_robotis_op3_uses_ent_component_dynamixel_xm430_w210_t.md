---
$id: rel_ent_robot_system_robotis_op3_uses_ent_component_dynamixel_xm430_w210_t
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_robot_system_robotis_op3
  name:
    en: ROBOTIS OP3 (DARwIn-OP Series)
    zh: ROBOTIS OP3 人形机器人（DARwIn-OP 系列）
target:
  id: ent_component_dynamixel_xm430_w210_t
  name:
    en: ROBOTIS DYNAMIXEL XM430-W210-T
    zh: ROBOTIS DYNAMIXEL XM430-W210-T 舵机
domains:
  source_domain: 02_components
  target_domain: 02_components
description:
  en: ROBOTIS OP3 is driven by 20 DYNAMIXEL XM430-W350-R smart servos (4.1 N.m stall torque, DYNAMIXEL
    Protocol 2.0).
  zh: ROBOTIS OP3 由 20 台 DYNAMIXEL XM430-W350-R 智能舵机驱动（失速扭矩 4.1 N·m，DYNAMIXEL Protocol 2.0）。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-01'
  confidence: medium
  notes: 来源档案 data/roadmap/research/robotis-op3-darwin-op.md 确认 20 台 XM430-W350-R；目标实体为同系列代表条目 XM430-W210-T，与
    OP3 实际型号（W350-R）同属 XM430 家族但变体不同。
sources:
- id: src_001
  type: website
  title: ROBOTIS OP3 e-Manual
  url: https://emanual.robotis.com/docs/en/platform/op3/introduction/
  accessed_at: '2026-07-01'
---
