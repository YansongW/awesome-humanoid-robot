---
$id: rel_ent_component_battery_management_system_is_part_of_ent_robot_system_tesla_optimus
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: is_part_of
source:
  id: ent_component_battery_management_system
  name:
    en: Battery Management System
    zh: 电池管理系统
    ko: 배터리 관리 시스템
target:
  id: ent_robot_system_tesla_optimus
  name:
    en: Tesla Optimus
    zh: Tesla Optimus
    ko: 테슬라 옵티머스
domains:
  source:
  - 02_components
  - 06_design_engineering
  - 04_assembly_integration_testing
  target:
  - 05_mass_production
  - 06_design_engineering
  - 11_applications_markets
description:
  en: BMS manages the torso battery pack of Tesla Optimus.
  zh: BMS管理Tesla Optimus的躯干电池包。
  ko: BMS는 Tesla Optimus의 몸통 배터리 팩을 관리합니다.
verification:
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





