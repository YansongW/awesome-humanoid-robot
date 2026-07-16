---
$id: rel_ent_paper_xu_stare_vla_progressive_stage_aw_2025_evaluates_on_ent_benchmark_maniskill
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: evaluates_on
source:
  id: ent_paper_xu_stare_vla_progressive_stage_aw_2025
  name:
    en: 'STARE-VLA: Progressive Stage-Aware Reinforcement for Fine-Tuning Vision-Language-Action Models'
    zh: STARE-VLA
target:
  id: ent_benchmark_maniskill
  name:
    en: ManiSkill
    zh: ManiSkill
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 10_evaluation_benchmarks
description:
  en: 'STARE-VLA: Progressive Stage-Aware Reinforcement for Fine-Tuning Vision-Language-Action Models is evaluated on ManiSkill.'
  zh: STARE-VLA评测于ManiSkill。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: STARE-VLA在ManiSkill3上进行了实验，ManiSkill3是一个基准测试平台。
    | 证据: Experiments on SimplerEnv and ManiSkill3 demonstrate substantial gains, achieving state-of-the-art success rates
    of 98.'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_xu_stare_vla_progressive_stage_aw_2025
  url: https://kg.rounds-tech.com/entry/ent_paper_xu_stare_vla_progressive_stage_aw_2025/
  accessed_at: '2026-07-16'
---
