---
$id: rel_ent_paper_teacher_student_rma_uses_ent_algorithm_ppo
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_teacher_student_rma
  name:
    en: 特权信息训练（Teacher-Student / RMA）核心论文
    zh: 特权信息训练（Teacher-Student / RMA）核心论文
target:
  id: ent_algorithm_ppo
  name:
    en: Proximal Policy Optimization (PPO)
    zh: 近端策略优化（PPO）
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: 特权信息训练（Teacher-Student / RMA）核心论文 uses Proximal Policy Optimization (PPO).
  zh: 特权信息训练（Teacher-Student / RMA）核心论文使用近端策略优化（PPO）。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p6_llm_link. Evidence: 教师策略通常使用PPO等强化学习算法训练。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_teacher_student_rma
  url: https://kg.rounds-tech.com/entry/ent_paper_teacher_student_rma/
  accessed_at: '2026-07-31'
---
