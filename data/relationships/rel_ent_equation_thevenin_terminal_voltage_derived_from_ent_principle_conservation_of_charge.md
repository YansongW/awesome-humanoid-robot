---
$id: rel_ent_equation_thevenin_terminal_voltage_derived_from_ent_principle_conservation_of_charge
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: derived_from
source:
  id: ent_equation_thevenin_terminal_voltage
  name:
    en: Thevenin Terminal Voltage Equation
target:
  id: ent_principle_conservation_of_charge
  name:
    en: Conservation of Charge
domains:
  source_domain: 00_foundations
  target_domain: 00_foundations
description:
  en: ent_equation_thevenin_terminal_voltage is derived from ent_principle_conservation_of_charge via Kirchhoff's current law.
  zh: ent_equation_thevenin_terminal_voltage 通过基尔霍夫电流定律从 ent_principle_conservation_of_charge 推导而来。
  ko: ent_equation_thevenin_terminal_voltage는 키르히호프 전류 법칙을 통해 ent_principle_conservation_of_charge에서 유도된다.
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-26'
  confidence: high
  notes: Created as part of the Li-ion battery knowledge-chain demonstration.
sources:
- id: src_dorf_svoboda_2017
  type: paper
  title: 'Dorf & Svoboda, Introduction to Electric Circuits, 9th ed.'
  url: https://www.wiley.com/en-us/Introduction+to+Electric+Circuits%2C+9th+Edition-p-9781118931897
  date: '2017-01-01'
  accessed_at: '2026-06-26'
---
