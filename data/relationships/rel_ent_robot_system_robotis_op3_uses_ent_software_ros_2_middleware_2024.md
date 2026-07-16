---
$id: rel_ent_robot_system_robotis_op3_uses_ent_software_ros_2_middleware_2024
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_robot_system_robotis_op3
  name:
    en: ROBOTIS OP3 (DARwIn-OP Series)
    zh: ROBOTIS OP3 人形机器人（DARwIn-OP 系列）
target:
  id: ent_software_ros_2_middleware_2024
  name:
    en: ROS 2 Middleware
    zh: ROS 2 中间件
domains:
  source_domain: 02_components
  target_domain: 08_software_middleware
description:
  en: The 2025 re-release of ROBOTIS OP3 natively moved to ROS2, with the DYNAMIXEL SDK and official ROS
    packages.
  zh: ROBOTIS OP3 的 2025 年复刻版原生转向 ROS2，配套 DYNAMIXEL SDK 与官方 ROS 包。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-01'
  confidence: medium
  notes: 来源档案 data/roadmap/research/robotis-op3-darwin-op.md 确认 2025 复刻版原生 ROS2（e-Manual 口径）。
sources:
- id: src_001
  type: website
  title: ROBOTIS OP3 e-Manual
  url: https://emanual.robotis.com/docs/en/platform/op3/introduction/
  accessed_at: '2026-07-01'
---
