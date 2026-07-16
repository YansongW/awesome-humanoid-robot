---
$id: rel_ent_ddpm_reverse_process_is_prerequisite_for_ent_continuity_equation
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: is_prerequisite_for
source:
  id: ent_ddpm_reverse_process
  name:
    en: DDPM reverse process
    zh: DDPM 逆过程
target:
  id: ent_continuity_equation
  name:
    en: Continuity equation
    zh: 连续性方程
domains:
  source_domain: 00_foundations
  target_domain: 00_foundations
description:
  en: DDPM reverse process is prerequisite for Continuity equation.
  zh: DDPM 逆过程is_prerequisite_for连续性方程。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p0b_related_entities. Evidence: DDPM 的连续时间极限由反向时间随机微分方程描述，其概率流满足连续性方程。'
sources:
- id: src_001
  type: other
  title: KG frontmatter of ent_ddpm_reverse_process
  url: https://kg.rounds-tech.com/entry/ent_ddpm_reverse_process/
  accessed_at: '2026-07-16'
---
