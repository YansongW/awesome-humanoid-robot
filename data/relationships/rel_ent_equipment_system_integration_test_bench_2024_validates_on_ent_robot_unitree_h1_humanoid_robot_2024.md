---
$id: rel_ent_equipment_system_integration_test_bench_2024_validates_on_ent_robot_unitree_h1_humanoid_robot_2024
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: validates_on
source:
  id: ent_equipment_system_integration_test_bench_2024
  name:
    en: System Integration Test Bench
    zh: 系统集成测试台
    ko: System Integration Test Bench
target:
  id: ent_robot_unitree_h1_humanoid_robot_2024
  name:
    en: Unitree H1 Humanoid Robot
    zh: 宇树 H1 人形机器人
    ko: Unitree H1 휨로봇
domains:
  source:
  - 04_assembly_integration_testing
  - 06_design_engineering
  target:
  - 06_design_engineering
  - 02_components
description:
  en: Integration test benches validate Unitree H1 joints and control loops.
  zh: 集成测试台验证Unitree H1的关节和控制回路。
  ko: 통합 테스트 벤치는 Unitree H1의 관절 및 제어 루프를 검증합니다.
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





