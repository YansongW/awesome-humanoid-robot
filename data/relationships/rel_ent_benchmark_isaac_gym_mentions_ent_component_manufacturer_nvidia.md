---
$id: rel_ent_benchmark_isaac_gym_mentions_ent_component_manufacturer_nvidia
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: mentions
source:
  id: ent_benchmark_isaac_gym
  name:
    en: Isaac Gym Benchmarks
    zh: Isaac Gym基准
target:
  id: ent_component_manufacturer_nvidia
  name:
    en: NVIDIA
    zh: 英伟达
domains:
  source_domain: 10_evaluation_benchmarks
  target_domain: 02_components
description:
  en: Isaac Gym Benchmarks mentions NVIDIA.
  zh: Isaac Gym基准提及英伟达。
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: low
  notes: 'Mined by build_latent_relationships.py rule p5b_acronym. Evidence: A collection of GPU-accelerated reinforcement-learning
    benchmarks built on NVIDIA Isaac Gym for high-throughput robot policy training and evaluation.'
sources:
- id: src_001
  type: other
  title: KG body of ent_benchmark_isaac_gym
  url: https://kg.rounds-tech.com/entry/ent_benchmark_isaac_gym/
  accessed_at: '2026-07-16'
---
