---
$id: rel_ent_robot_system_toddlerbot_uses_ent_component_dynamixel_xm430_w210_t
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_robot_system_toddlerbot
  name:
    en: ToddlerBot
    zh: ToddlerBot 幼儿机器人
target:
  id: ent_component_dynamixel_xm430_w210_t
  name:
    en: ROBOTIS DYNAMIXEL XM430-W210-T
    zh: ROBOTIS DYNAMIXEL XM430-W210-T 舵机
domains:
  source_domain: 02_components
  target_domain: 02_components
description:
  en: ToddlerBot uses ROBOTIS Dynamixel bus servos as its actuators (five Dynamixel models selected per
    joint; the specific model list is in the paper's supplementary material).
  zh: ToddlerBot 采用 ROBOTIS Dynamixel 总线舵机作为执行器，共 5 种型号按关节空间/扭矩/成本选型（具体型号清单见论文补充材料 VIII-E）。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-01'
  confidence: medium
  notes: 来源档案 data/roadmap/research/toddlerbot.md 确认使用 ROBOTIS Dynamixel 总线舵机（5 种型号）；目标实体为知识图谱中 Dynamixel
    智能舵机代表条目（XM430-W210-T），档案未逐一列出具体型号，型号对应关系需以论文补充材料为准。
sources:
- id: src_001
  type: website
  title: hshi74/toddlerbot GitHub Repository
  url: https://github.com/hshi74/toddlerbot
  accessed_at: '2026-07-01'
---
