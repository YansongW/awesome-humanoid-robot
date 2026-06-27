---
$id: rel_ent_method_equivalent_circuit_battery_model_uses_ent_butler_volmer_equation
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_method_equivalent_circuit_battery_model
  name:
    en: Equivalent-Circuit Battery Model
target:
  id: ent_butler_volmer_equation
  name:
    en: Butler-Volmer Equation
domains:
  source_domain: 02_components
  target_domain: 00_foundations
description:
  en: ent_method_equivalent_circuit_battery_model uses ent_butler_volmer_equation to parameterize charge-transfer polarization resistance.
  zh: ent_method_equivalent_circuit_battery_model 使用 ent_butler_volmer_equation 来参数化电荷转移极化电阻。
  ko: ent_method_equivalent_circuit_battery_model은 전하 이동 분극 저항을 매개변수화하기 위해 ent_butler_volmer_equation을 사용한다.
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-26'
  confidence: high
  notes: Created as part of the Li-ion battery knowledge-chain demonstration.
sources:
- id: src_bard_faulkner_2001
  type: other
  title: 'A. J. Bard and L. R. Faulkner, Electrochemical Methods: Fundamentals and Applications, 2nd ed.'
  url: https://www.wiley.com/en-us/Electrochemical+Methods%3A+Fundamentals+and+Applications%2C+2nd+Edition-p-9780471043720
  date: '2001-01-01'
  accessed_at: '2026-06-26'
---
