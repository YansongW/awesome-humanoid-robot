---
$id: rel_ent_bayesian_filtering_builds_on_ent_ddpm_reverse_process
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: builds_on
source:
  id: ent_bayesian_filtering
  name:
    en: Bayesian filtering
    zh: 贝叶斯滤波
target:
  id: ent_ddpm_reverse_process
  name:
    en: DDPM reverse process
    zh: DDPM 逆过程
domains:
  source_domain: 00_foundations
  target_domain: 00_foundations
description:
  en: Bayesian filtering builds on DDPM reverse process.
  zh: 贝叶斯滤波builds_onDDPM 逆过程。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p0b_related_entities. Evidence: 贝叶斯滤波与 DDPM 逆过程都利用条件信息递归地精化分布，只是后者用于生成而非估计。'
sources:
- id: src_001
  type: other
  title: KG frontmatter of ent_bayesian_filtering
  url: https://kg.rounds-tech.com/entry/ent_bayesian_filtering/
  accessed_at: '2026-07-16'
---
