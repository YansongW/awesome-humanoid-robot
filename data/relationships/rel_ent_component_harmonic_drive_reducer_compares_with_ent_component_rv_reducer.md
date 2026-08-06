---
$id: rel_ent_component_harmonic_drive_reducer_compares_with_ent_component_rv_reducer
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: compares_with
source:
  id: ent_component_harmonic_drive_reducer
  name:
    en: Harmonic Drive Reducer
    zh: 谐波减速器
target:
  id: ent_component_rv_reducer
  name:
    en: RV Reducer
    zh: RV减速器
domains:
  source_domain: 02_components
  target_domain: 02_components
description:
  en: Harmonic Drive Reducer compares with RV Reducer.
  zh: 谐波减速器compares_withRV减速器。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-08-06'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 证据是一个对比表格，将谐波减速器与RV减速器进行维度比较。 | 证据: | Dimension
    | **Harmonic (Strain Wave)** | RV Reducer | Planetary Reducer | Cycloidal (Low Ratio) |'
sources:
- id: src_001
  type: other
  title: KG body of ent_component_harmonic_drive_reducer
  url: https://kg.rounds-tech.com/entry/ent_component_harmonic_drive_reducer/
  accessed_at: '2026-08-06'
---
