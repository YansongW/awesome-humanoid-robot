---
$id: rel_ent_paper_latent_dynamics_planning_pixels_2018_evaluates_on_ent_paper_deepmind_control_suite_2018
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: evaluates_on
source:
  id: ent_paper_latent_dynamics_planning_pixels_2018
  name:
    en: Learning Latent Dynamics for Planning from Pixels
    zh: Learning Latent Dynamics for Planning from Pixels
target:
  id: ent_paper_deepmind_control_suite_2018
  name:
    en: DeepMind Control Suite
    zh: DeepMind Control Suite
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: Learning Latent Dynamics for Planning from Pixels is evaluated on DeepMind Control Suite.
  zh: Learning Latent Dynamics for Planning from Pixels评测于DeepMind Control Suite。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-08-06'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 论文在DeepMind Control Suite上评估其方法性能。 | 证据: 它在
    DeepMind Control Suite 的六个连续控制任务上，以 1000 个回合的样本量达到或超过无模型基线（D4PG）在 100000 个回合下的性能，数据效率提升 40 至 500 倍以上。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_latent_dynamics_planning_pixels_2018
  url: https://kg.rounds-tech.com/entry/ent_paper_latent_dynamics_planning_pixels_2018/
  accessed_at: '2026-08-06'
---
