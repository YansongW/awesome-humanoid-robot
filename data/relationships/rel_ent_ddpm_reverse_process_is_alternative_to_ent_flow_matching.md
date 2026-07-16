---
$id: rel_ent_ddpm_reverse_process_is_alternative_to_ent_flow_matching
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: is_alternative_to
source:
  id: ent_ddpm_reverse_process
  name:
    en: DDPM reverse process
    zh: DDPM 逆过程
target:
  id: ent_flow_matching
  name:
    en: Flow matching
    zh: 流匹配
domains:
  source_domain: 00_foundations
  target_domain: 00_foundations
description:
  en: DDPM reverse process is alternative to Flow matching.
  zh: DDPM 逆过程is_alternative_to流匹配。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p0b_related_entities. Evidence: 流匹配提供了一种替代生成框架，直接学习确定性的概率流而非随机逆扩散链。'
sources:
- id: src_001
  type: other
  title: KG frontmatter of ent_ddpm_reverse_process
  url: https://kg.rounds-tech.com/entry/ent_ddpm_reverse_process/
  accessed_at: '2026-07-16'
---
