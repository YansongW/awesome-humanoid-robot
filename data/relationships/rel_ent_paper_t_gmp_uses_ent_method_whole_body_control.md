---
$id: rel_ent_paper_t_gmp_uses_ent_method_whole_body_control
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_t_gmp
  name:
    en: T-GMP
    zh: 地形条件生成式运动先验的人形自然多地形行走
target:
  id: ent_method_whole_body_control
  name:
    en: Whole-Body Control (WBC)
    zh: 全身控制（WBC）
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: T-GMP uses Whole-Body Control (WBC).
  zh: 地形条件生成式运动先验的人形自然多地形行走使用全身控制（WBC）。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p6_llm_link. Evidence: 人形机器人控制通常需要全身控制。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_t_gmp
  url: https://kg.rounds-tech.com/entry/ent_paper_t_gmp/
  accessed_at: '2026-07-31'
---
