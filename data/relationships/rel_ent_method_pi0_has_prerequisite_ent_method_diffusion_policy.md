---
$id: rel_ent_method_pi0_has_prerequisite_ent_method_diffusion_policy
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: has_prerequisite
source:
  id: ent_method_pi0
  name:
    en: π0 (Pi Zero)
    zh: π0
target:
  id: ent_method_diffusion_policy
  name:
    en: Diffusion Policy
    zh: 扩散策略
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: π0 (Pi Zero) has prerequisite Diffusion Policy.
  zh: π0前置依赖扩散策略。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-17'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p7_learning_chain. Evidence: π0可能使用扩散策略作为其核心生成模型，理解扩散过程有助于掌握其工作原理。'
sources:
- id: src_001
  type: other
  title: 0→1 路线图学习链
  url: https://kg.rounds-tech.com/wiki/roadmap/
  accessed_at: '2026-07-17'
---
