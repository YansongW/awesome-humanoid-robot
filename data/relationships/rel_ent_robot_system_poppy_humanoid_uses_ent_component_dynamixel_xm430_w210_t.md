---
$id: rel_ent_robot_system_poppy_humanoid_uses_ent_component_dynamixel_xm430_w210_t
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_robot_system_poppy_humanoid
  name:
    en: Poppy Humanoid
    zh: Poppy 人形机器人
target:
  id: ent_component_dynamixel_xm430_w210_t
  name:
    en: ROBOTIS DYNAMIXEL XM430-W210-T
    zh: ROBOTIS DYNAMIXEL XM430-W210-T 舵机
domains:
  source_domain: 02_components
  target_domain: 02_components
description:
  en: Poppy Humanoid is driven by 25 ROBOTIS Dynamixel smart servos on a TTL serial bus, mixing AX-series
    (small joints) and MX-series (high-torque joints) models.
  zh: Poppy Humanoid 由 25 台 ROBOTIS Dynamixel 智能舵机经 TTL 串行总线驱动，按关节扭矩需求混用 AX 系列与 MX 系列。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-01'
  confidence: medium
  notes: 来源档案 data/roadmap/research/poppy-humanoid.md 确认 25 台 Dynamixel（AX/MX 系列）；目标实体为知识图谱中 Dynamixel
    智能舵机代表条目（XM430-W210-T），与 Poppy 实际所用 AX/MX 系列非同一型号。
sources:
- id: src_001
  type: website
  title: Poppy Humanoid assembly guide
  url: https://docs.poppy-project.org/en/assembly-guides/poppy-humanoid/
  accessed_at: '2026-07-01'
---
