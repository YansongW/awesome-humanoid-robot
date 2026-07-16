---
$id: rel_ent_process_p11_2_1_uses_ent_principle_force_closure
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_process_p11_2_1
  name:
    en: Grasp Pose Generation and Force Closure Analysis
    zh: 抓取姿态生成与力闭合分析
target:
  id: ent_principle_force_closure
  name:
    en: Force Closure
    zh: 力闭合
domains:
  source_domain: 02_components
  target_domain: 07_ai_models_algorithms
description:
  en: Grasp Pose Generation and Force Closure Analysis uses Force Closure.
  zh: 抓取姿态生成与力闭合分析使用力闭合。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 源使用目标作为方法/工具。 | 证据: **Methods/Tools**: GraspIt
    / OpenRAVE, Force Closure Criterion, Adversarial Grasping'
sources:
- id: src_001
  type: other
  title: KG body of ent_process_p11_2_1
  url: https://kg.rounds-tech.com/entry/ent_process_p11_2_1/
  accessed_at: '2026-07-16'
---
