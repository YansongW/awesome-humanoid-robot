---
$id: rel_ent_software_genesis_generative_physics_eng_2024_has_prerequisite_ent_method_domain_randomization
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: has_prerequisite
source:
  id: ent_software_genesis_generative_physics_eng_2024
  name:
    en: Genesis Generative Physics Engine
    zh: Genesis 生成式物理引擎
target:
  id: ent_method_domain_randomization
  name:
    en: Domain Randomization
    zh: 域随机化
domains:
  source_domain: 08_software_middleware
  target_domain: 07_ai_models_algorithms
description:
  en: Genesis Generative Physics Engine has prerequisite Domain Randomization.
  zh: Genesis 生成式物理引擎前置依赖域随机化。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-17'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p7_learning_chain. Evidence: 域随机化是生成式物理引擎中常用的技术，用于提高仿真到现实的迁移能力。'
sources:
- id: src_001
  type: other
  title: 0→1 路线图学习链
  url: https://kg.rounds-tech.com/wiki/roadmap/
  accessed_at: '2026-07-17'
---
