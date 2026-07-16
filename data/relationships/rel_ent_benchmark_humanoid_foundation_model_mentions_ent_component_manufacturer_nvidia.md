---
$id: rel_ent_benchmark_humanoid_foundation_model_mentions_ent_component_manufacturer_nvidia
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: mentions
source:
  id: ent_benchmark_humanoid_foundation_model
  name:
    en: Humanoid Foundation Model Benchmark
    zh: 人形机器人基础模型基准
target:
  id: ent_component_manufacturer_nvidia
  name:
    en: NVIDIA
    zh: 英伟达
domains:
  source_domain: 10_evaluation_benchmarks
  target_domain: 02_components
description:
  en: Humanoid Foundation Model Benchmark mentions NVIDIA.
  zh: 人形机器人基础模型基准提及英伟达。
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: low
  notes: 'Mined by build_latent_relationships.py rule p5b_acronym. Evidence: It evaluates 40+ models from organizations such
    as NVIDIA, Google DeepMind, Tesla, Physical Intelligence, Figure AI, and Unitree.'
sources:
- id: src_001
  type: other
  title: KG body of ent_benchmark_humanoid_foundation_model
  url: https://kg.rounds-tech.com/entry/ent_benchmark_humanoid_foundation_model/
  accessed_at: '2026-07-16'
---
