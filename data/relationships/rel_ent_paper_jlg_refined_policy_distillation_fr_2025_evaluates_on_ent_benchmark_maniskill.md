---
$id: rel_ent_paper_jlg_refined_policy_distillation_fr_2025_evaluates_on_ent_benchmark_maniskill
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: evaluates_on
source:
  id: ent_paper_jlg_refined_policy_distillation_fr_2025
  name:
    en: 'Refined Policy Distillation: From VLA Generalists to RL Experts'
    zh: RPD
target:
  id: ent_benchmark_maniskill
  name:
    en: ManiSkill
    zh: ManiSkill
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 10_evaluation_benchmarks
description:
  en: 'Refined Policy Distillation: From VLA Generalists to RL Experts is evaluated on ManiSkill.'
  zh: RPD评测于ManiSkill。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 论文使用ManiSkill3仿真环境来评估RPD方法。 | 证据: We complement
    our method by fine-tuned versions of Octo and OpenVLA for ManiSkill3 to evaluate RPD in simulation.'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_jlg_refined_policy_distillation_fr_2025
  url: https://kg.rounds-tech.com/entry/ent_paper_jlg_refined_policy_distillation_fr_2025/
  accessed_at: '2026-07-16'
---
