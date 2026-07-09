---
$id: rel_ent_equation_thevenin_terminal_voltage_uses_ent_operator_voltage_divider
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_equation_thevenin_terminal_voltage
  name:
    en: Thevenin Terminal Voltage Equation
    ko: ''
target:
  id: ent_operator_voltage_divider
  name:
    en: Voltage Divider
    ko: ''
domains:
  source_domain: 00_foundations
  target_domain: 00_foundations
description:
  en: ent_equation_thevenin_terminal_voltage uses ent_operator_voltage_divider to account for the voltage drop across internal
    and load resistances.
  zh: ent_equation_thevenin_terminal_voltage 使用 ent_operator_voltage_divider 来计算内阻和负载电阻上的压降。
  ko: ent_equation_thevenin_terminal_voltage은 낮은 저항과 부하 저항의 전압 강하를 설명하기 위해 ent_operator_voltage_divider를 사용한다.
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-26'
  confidence: high
  notes: Created as part of the Li-ion battery knowledge-chain demonstration.
sources:
- id: src_dorf_svoboda_2017
  type: paper
  title: Dorf & Svoboda, Introduction to Electric Circuits, 9th ed.
  url: https://www.wiley.com/en-us/Introduction+to+Electric+Circuits%2C+9th+Edition-p-9781118931897
  date: '2017-01-01'
  accessed_at: '2026-06-26'
---
