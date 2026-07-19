---
$id: rel_ent_oem_unitree_robotics_has_prerequisite_ent_principle_current_velocity_position_loops
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: has_prerequisite
source:
  id: ent_oem_unitree_robotics
  name:
    en: Unitree Robotics
    zh: 宇树科技
target:
  id: ent_principle_current_velocity_position_loops
  name:
    en: Current / Velocity / Position Control Loops
    zh: 电流环/速度环/位置环
domains:
  source_domain: 02_components
  target_domain: 02_components
description:
  en: Unitree Robotics has prerequisite Current / Velocity / Position Control Loops.
  zh: 宇树科技前置依赖电流环/速度环/位置环。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-17'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p7_learning_chain. Evidence: Unitree的高扭矩执行器依赖电流-速度-位置环控制，这是伺服驱动的基础。'
sources:
- id: src_001
  type: other
  title: 0→1 路线图学习链
  url: https://kg.rounds-tech.com/wiki/roadmap/
  accessed_at: '2026-07-17'
---
