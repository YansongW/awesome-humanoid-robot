---
$id: rel_ent_ddpm_reverse_process_uses_ent_score_matching
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_ddpm_reverse_process
  name:
    en: DDPM reverse process
    zh: DDPM 逆过程
target:
  id: ent_score_matching
  name:
    en: Score matching
    zh: 分数匹配
domains:
  source_domain: 00_foundations
  target_domain: 00_foundations
description:
  en: DDPM reverse process uses Score matching.
  zh: DDPM 逆过程使用分数匹配。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p0b_related_entities. Evidence: DDPM 使用去噪分数匹配目标训练其噪声预测网络。'
sources:
- id: src_001
  type: other
  title: KG frontmatter of ent_ddpm_reverse_process
  url: https://kg.rounds-tech.com/entry/ent_ddpm_reverse_process/
  accessed_at: '2026-07-16'
---
