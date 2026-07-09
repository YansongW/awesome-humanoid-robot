---
$id: rel_ent_method_equivalent_circuit_battery_model_formalizes_ent_formalism_thevenin_equivalent_circuit
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: formalizes
source:
  id: ent_method_equivalent_circuit_battery_model
  name:
    en: Equivalent-Circuit Battery Model
    ko: ''
target:
  id: ent_formalism_thevenin_equivalent_circuit
  name:
    en: Thevenin Equivalent Circuit
    ko: ''
domains:
  source_domain: 02_components
  target_domain: 00_foundations
description:
  en: ent_method_equivalent_circuit_battery_model formalizes ent_formalism_thevenin_equivalent_circuit for battery state estimation.
  zh: ent_method_equivalent_circuit_battery_model 为电池状态估计实例化了 ent_formalism_thevenin_equivalent_circuit。
  ko: ent_method_equivalent_circuit_battery_model은 배터리 상태 추정을 위해 ent_formalism_thevenin_equivalent_circuit을 공식화한다.
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-26'
  confidence: high
  notes: Created as part of the Li-ion battery knowledge-chain demonstration.
sources:
- id: src_hu_2012_ecm_soh
  type: paper
  title: A comparative study of equivalent circuit models for Li-ion batteries
  url: https://doi.org/10.1016/j.jpowsour.2012.02.064
  date: '2012-07-15'
  accessed_at: '2026-06-26'
---
