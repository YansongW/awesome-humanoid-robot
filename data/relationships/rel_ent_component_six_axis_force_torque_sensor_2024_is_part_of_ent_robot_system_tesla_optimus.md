---
$id: rel_ent_component_six_axis_force_torque_sensor_2024_is_part_of_ent_robot_system_tesla_optimus
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: is_part_of
source:
  id: ent_component_six_axis_force_torque_sensor_2024
  name:
    en: Six Axis Force Torque Sensor
    zh: 六维力传感器
    ko: Six Axis Force Torque Sensor
target:
  id: ent_robot_system_tesla_optimus
  name:
    en: Tesla Optimus
    zh: Tesla Optimus
    ko: 테슬라 옵티머스
domains:
  source:
  - 02_components
  target:
  - 05_mass_production
  - 06_design_engineering
  - 11_applications_markets
description:
  en: Wrist/ankle force-torque sensors enable contact control in Tesla Optimus.
  zh: 腕部/踝部力矩传感器使Tesla Optimus能够实现接触控制。
  ko: 손목/발목 힘-토크 센서는 Tesla Optimus의 접촉 제어를 가능하게 합니다.
verification:
  confidence: medium
  notes: bulk-added confidence on 2026-07-17 by backfill_rel_confidence.py; pending human review
  status: partially_verified
  sources: []
  reviewed_by: ai_autonomous
  reviewed_at: '2026-07-02T00:21:22.207515+00:00'
sources:
- type: website
  url: ''
  description: Workflow relationship curated from public project pages and literature.
  id: curated_workflow_relationship
---





