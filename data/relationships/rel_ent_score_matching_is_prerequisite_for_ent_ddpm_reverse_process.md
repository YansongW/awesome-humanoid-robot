---
$id: rel_ent_score_matching_is_prerequisite_for_ent_ddpm_reverse_process
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: is_prerequisite_for
source:
  id: ent_score_matching
  name:
    en: Score matching
    zh: 分数匹配
target:
  id: ent_ddpm_reverse_process
  name:
    en: DDPM reverse process
    zh: DDPM 逆过程
domains:
  source_domain: 00_foundations
  target_domain: 00_foundations
description:
  en: Score matching is prerequisite for DDPM reverse process.
  zh: 分数匹配is_prerequisite_forDDPM 逆过程。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p0b_related_entities. Evidence: DDPM 通过去噪分数匹配训练类分数的噪声模型，并用其逆转扩散过程。'
sources:
- id: src_001
  type: other
  title: KG frontmatter of ent_score_matching
  url: https://kg.rounds-tech.com/entry/ent_score_matching/
  accessed_at: '2026-07-16'
---
