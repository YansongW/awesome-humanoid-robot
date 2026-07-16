---
$id: rel_ent_robot_system_toddlerbot_uses_ent_software_mujoco_physics_engine_2022
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_robot_system_toddlerbot
  name:
    en: ToddlerBot
    zh: ToddlerBot 幼儿机器人
target:
  id: ent_software_mujoco_physics_engine_2022
  name:
    en: MuJoCo Physics Engine
    zh: MuJoCo 物理引擎
domains:
  source_domain: 02_components
  target_domain: 08_software_middleware
description:
  en: ToddlerBot uses MuJoCo/MJX as its primary simulation stack for RL training (PPO) and keyframe animation,
    without depending on ROS.
  zh: ToddlerBot 以 MuJoCo/MJX 为仿真主力进行 RL 训练（PPO）与关键帧动画，不依赖 ROS。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-01'
  confidence: medium
  notes: 来源档案 data/roadmap/research/toddlerbot.md 明确记载仿真主力为 MuJoCo/MJX。
sources:
- id: src_001
  type: website
  title: hshi74/toddlerbot GitHub Repository
  url: https://github.com/hshi74/toddlerbot
  accessed_at: '2026-07-01'
---
