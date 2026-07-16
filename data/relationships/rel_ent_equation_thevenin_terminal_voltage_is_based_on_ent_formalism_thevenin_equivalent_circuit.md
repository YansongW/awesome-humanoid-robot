---
$id: rel_ent_equation_thevenin_terminal_voltage_is_based_on_ent_formalism_thevenin_equivalent_circuit
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: is_based_on
source:
  id: ent_equation_thevenin_terminal_voltage
  name:
    en: Thevenin Terminal Voltage Equation
    zh: Thevenin 端电压方程
target:
  id: ent_formalism_thevenin_equivalent_circuit
  name:
    en: Thevenin Equivalent Circuit
    zh: Thevenin 等效电路
domains:
  source_domain: 00_foundations
  target_domain: 00_foundations
description:
  en: Thevenin Terminal Voltage Equation is based on Thevenin Equivalent Circuit.
  zh: Thevenin 端电压方程基于Thevenin 等效电路。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: Thevenin端电压方程是基于Thevenin等效电路推导得出的。 | 证据: 给出
    Thevenin 等效电路端电压等于开路电压减去等效电阻上压降的方程。'
sources:
- id: src_001
  type: other
  title: KG body of ent_equation_thevenin_terminal_voltage
  url: https://kg.rounds-tech.com/entry/ent_equation_thevenin_terminal_voltage/
  accessed_at: '2026-07-16'
---
