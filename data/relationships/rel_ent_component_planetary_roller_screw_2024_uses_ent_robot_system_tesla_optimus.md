---
$id: rel_ent_component_planetary_roller_screw_2024_uses_ent_robot_system_tesla_optimus
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_component_planetary_roller_screw_2024
  name:
    en: Planetary Roller Screw
    zh: 行星滚柱丝杠
target:
  id: ent_robot_system_tesla_optimus
  name:
    en: Tesla Optimus
    zh: Tesla Optimus
domains:
  source_domain: 02_components
  target_domain: 05_mass_production
description:
  en: Planetary Roller Screw uses Tesla Optimus.
  zh: 行星滚柱丝杠使用Tesla Optimus。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 证据表明Tesla Optimus采用行星滚柱丝杠，即源被目标使用。 | 证据: 例如，Tesla
    Optimus 线性关节 reportedly 采用行星滚柱丝杠，若需输出 $F=8000\ \text{N}$，丝杠导程 $l=5\ \text{mm}=0.'
sources:
- id: src_001
  type: other
  title: KG body of ent_component_planetary_roller_screw_2024
  url: https://kg.rounds-tech.com/entry/ent_component_planetary_roller_screw_2024/
  accessed_at: '2026-07-16'
---
