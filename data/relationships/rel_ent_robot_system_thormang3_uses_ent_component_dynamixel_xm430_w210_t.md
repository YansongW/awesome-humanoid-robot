---
$id: rel_ent_robot_system_thormang3_uses_ent_component_dynamixel_xm430_w210_t
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_robot_system_thormang3
  name:
    en: THORMANG3
    zh: THORMANG3 全尺寸人形机器人
target:
  id: ent_component_dynamixel_xm430_w210_t
  name:
    en: ROBOTIS DYNAMIXEL XM430-W210-T
    zh: ROBOTIS DYNAMIXEL XM430-W210-T 舵机
domains:
  source_domain: 02_components
  target_domain: 02_components
description:
  en: THORMANG3 is driven by 29 DYNAMIXEL-P series integrated servos (PH54-200 x10, PH54-100 x11, PH42-020
    x8).
  zh: THORMANG3 由 29 台 DYNAMIXEL-P 系列一体化伺服驱动（PH54-200×10、PH54-100×11、PH42-020×8）。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-01'
  confidence: medium
  notes: 来源档案 data/roadmap/research/thormang3.md 确认 29 台 DYNAMIXEL-P 系列；目标实体为知识图谱 Dynamixel 智能舵机代表条目（XM430-W210-T，X
    系列），与 THORMANG3 实际所用 P 系列非同一系列。
sources:
- id: src_001
  type: website
  title: THORMANG3 e-Manual
  url: https://emanual.robotis.com/docs/en/platform/thormang3/introduction/
  accessed_at: '2026-07-01'
---
