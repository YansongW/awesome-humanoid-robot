---
$id: rel_ent_paper_deniz_identification_of_a_physics_ba_2026_integrates_ent_component_main_board_power_sensor
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: integrates
source:
  id: ent_paper_deniz_identification_of_a_physics_ba_2026
  name:
    en: Identification of a Physics-Based Electrical Power Consumption Model for the Unitree G1 Humanoid Arm
    zh: Unitree G1人形机器人手臂基于物理的电力消耗模型辨识
    ko: Unitree G1 휴머노이드 팔의 물리 기반 전력 소비 모델 식별
target:
  id: ent_component_main_board_power_sensor
  name:
    en: Main-board power sensor
    ko: ''
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 02_components
description:
  en: The main-board power sensor provides the onboard power measurements used as the regression target.
  zh: 主板功率传感器提供用作回归目标的车载功率测量。
  ko: 메인보드 전력 센서는 회귀 목표로 사용되는 온보드 전력 측정을 제공합니다.
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-22'
  confidence: medium
  notes: 'Proposed by AI extraction. Source citation: Model parameters are identified from experimental data collected on
    a physical Unitree G1 using onboard power measurements as the regression target.'
sources:
- id: src_001
  type: paper
  title: Identification of a Physics-Based Electrical Power Consumption Model for the Unitree G1 Humanoid Arm
  url: https://arxiv.org/abs/2606.15915
  date: '2026'
  accessed_at: '2026-06-22'
---
