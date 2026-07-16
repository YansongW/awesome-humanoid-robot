---
$id: rel_ent_process_p10_uses_ent_method_domain_randomization
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_process_p10
  name:
    en: Motion Control Algorithm Development and Validation
    zh: 运动控制算法开发与验证（Motion Control）
target:
  id: ent_method_domain_randomization
  name:
    en: Domain Randomization
    zh: 域随机化
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: Motion Control Algorithm Development and Validation uses Domain Randomization.
  zh: 运动控制算法开发与验证（Motion Control）使用域随机化。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 源方法在描述中使用了Domain Randomization作为方法/工具 | 证据:
    - **方法 / 工具**：Domain Randomization、系统噪声注入、地形/负载变化'
sources:
- id: src_001
  type: other
  title: KG body of ent_process_p10
  url: https://kg.rounds-tech.com/entry/ent_process_p10/
  accessed_at: '2026-07-16'
---
