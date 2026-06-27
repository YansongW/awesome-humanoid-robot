---
$id: rel_ent_formalism_thevenin_equivalent_circuit_includes_ent_equation_thevenin_terminal_voltage
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: includes
source:
  id: ent_formalism_thevenin_equivalent_circuit
  name:
    en: Thevenin Equivalent Circuit
target:
  id: ent_equation_thevenin_terminal_voltage
  name:
    en: Thevenin Terminal Voltage Equation
domains:
  source_domain: 00_foundations
  target_domain: 00_foundations
description:
  en: ent_formalism_thevenin_equivalent_circuit includes ent_equation_thevenin_terminal_voltage as its defining voltage-current relation.
  zh: ent_formalism_thevenin_equivalent_circuit 包含 ent_equation_thevenin_terminal_voltage 作为其定义的电压-电流关系。
  ko: ent_formalism_thevenin_equivalent_circuit은 정의하는 전압-전류 관계로 ent_equation_thevenin_terminal_voltage를 포함한다.
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
