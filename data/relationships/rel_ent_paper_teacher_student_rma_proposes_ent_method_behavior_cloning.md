---
$id: rel_ent_paper_teacher_student_rma_proposes_ent_method_behavior_cloning
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: proposes
source:
  id: ent_paper_teacher_student_rma
  name:
    en: 特权信息训练（Teacher-Student / RMA）核心论文
    zh: 特权信息训练（Teacher-Student / RMA）核心论文
target:
  id: ent_method_behavior_cloning
  name:
    en: Behavior Cloning
    zh: 行为克隆
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: 特权信息训练（Teacher-Student / RMA）核心论文 proposes Behavior Cloning.
  zh: 特权信息训练（Teacher-Student / RMA）核心论文提出行为克隆。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p6_llm_link. Evidence: Teacher-Student框架中教师策略通过行为克隆训练学生策略。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_teacher_student_rma
  url: https://kg.rounds-tech.com/entry/ent_paper_teacher_student_rma/
  accessed_at: '2026-07-31'
---
