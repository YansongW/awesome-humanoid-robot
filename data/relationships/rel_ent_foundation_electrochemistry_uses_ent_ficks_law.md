---
$id: rel_ent_foundation_electrochemistry_uses_ent_ficks_law
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_foundation_electrochemistry
  name:
    en: Electrochemistry
    zh: 电化学
target:
  id: ent_ficks_law
  name:
    en: Fick's law
    zh: 菲克定律
domains:
  source_domain: 00_foundations
  target_domain: 00_foundations
description:
  en: Electrochemistry uses Fick's law.
  zh: 电化学使用菲克定律。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 电化学使用菲克定律描述扩散规律。 | 证据: - **菲克定律（Fick''s law）**：描述物质从高浓度区向低浓度区扩散的规律。'
sources:
- id: src_001
  type: other
  title: KG body of ent_foundation_electrochemistry
  url: https://kg.rounds-tech.com/entry/ent_foundation_electrochemistry/
  accessed_at: '2026-07-16'
---
