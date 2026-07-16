---
$id: rel_ent_paper_lift_towards_bridging_the_gap_2026_uses_ent_newton_euler_equations
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_lift_towards_bridging_the_gap_2026
  name:
    en: 'LIFT: Towards Bridging the Gap between Large-Scale Pretraining and Efficient Finetuning for Humanoid Control'
    zh: LIFT：用大批量 SAC 预训练 + 物理先验世界模型微调，把人形 sim-to-real 压到 1 小时
target:
  id: ent_newton_euler_equations
  name:
    en: Newton-Euler equations
    zh: 牛顿-欧拉方程
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 00_foundations
description:
  en: 'LIFT: Towards Bridging the Gap between Large-Scale Pretraining and Efficient Finetuning for Humanoid Control uses Newton-Euler
    equations.'
  zh: LIFT：用大批量 SAC 预训练 + 物理先验世界模型微调，把人形 sim-to-real 压到 1 小时使用牛顿-欧拉方程。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 论文LIFT将牛顿-欧拉方程作为归纳偏置使用。 | 证据: , Newton-Euler
    equations) as inductive biases, significantly reducing its reliance on large amounts of real data.'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_lift_towards_bridging_the_gap_2026
  url: https://kg.rounds-tech.com/entry/ent_paper_lift_towards_bridging_the_gap_2026/
  accessed_at: '2026-07-16'
---
