---
$id: rel_ent_tech_li_battery_humanoid_uses_ent_method_equivalent_circuit_battery_model
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_tech_li_battery_humanoid
  name:
    en: Lithium-Ion Battery System for Humanoid Robots
target:
  id: ent_method_equivalent_circuit_battery_model
  name:
    en: Equivalent-Circuit Battery Model
domains:
  source_domain: 02_components
  target_domain: 00_foundations
description:
  en: ent_tech_li_battery_humanoid uses ent_method_equivalent_circuit_battery_model for state estimation and voltage prediction.
  zh: ent_tech_li_battery_humanoid 使用 ent_method_equivalent_circuit_battery_model 进行状态估计和电压预测。
  ko: ent_tech_li_battery_humanoid은 상태 추정 및 전압 예측을 위해 ent_method_equivalent_circuit_battery_model을 사용한다.
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-26'
  confidence: high
  notes: Created as part of the Li-ion battery knowledge-chain demonstration.
sources:
- id: src_hu_2012_ecm_soh
  type: paper
  title: 'A comparative study of equivalent circuit models for Li-ion batteries'
  url: https://doi.org/10.1016/j.jpowsour.2012.02.064
  date: '2012-07-15'
  accessed_at: '2026-06-26'
---
