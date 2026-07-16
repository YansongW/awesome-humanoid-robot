---
$id: rel_ent_flow_matching_is_alternative_to_ent_ddpm_reverse_process
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: is_alternative_to
source:
  id: ent_flow_matching
  name:
    en: Flow matching
    zh: 流匹配
target:
  id: ent_ddpm_reverse_process
  name:
    en: DDPM reverse process
    zh: DDPM 逆过程
domains:
  source_domain: 00_foundations
  target_domain: 00_foundations
description:
  en: Flow matching is alternative to DDPM reverse process.
  zh: 流匹配is_alternative_toDDPM 逆过程。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p0b_related_entities. Evidence: 流匹配为 DDPM 使用的随机逆扩散链提供了一种基于确定性 ODE 的替代方案。'
sources:
- id: src_001
  type: other
  title: KG frontmatter of ent_flow_matching
  url: https://kg.rounds-tech.com/entry/ent_flow_matching/
  accessed_at: '2026-07-16'
---
