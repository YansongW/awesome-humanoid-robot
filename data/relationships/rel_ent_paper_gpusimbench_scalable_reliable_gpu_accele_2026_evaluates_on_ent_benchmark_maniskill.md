---
$id: rel_ent_paper_gpusimbench_scalable_reliable_gpu_accele_2026_evaluates_on_ent_benchmark_maniskill
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: evaluates_on
source:
  id: ent_paper_gpusimbench_scalable_reliable_gpu_accele_2026
  name:
    en: 'GPUSimBench: Towards Scalable and Reliable GPU-Accelerated Simulators in Embodied AI'
    zh: 'GPUSimBench: Towards Scalable and Reliable GPU-Accelerated Simulators in Embodied AI'
target:
  id: ent_benchmark_maniskill
  name:
    en: ManiSkill
    zh: ManiSkill
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 10_evaluation_benchmarks
description:
  en: 'GPUSimBench: Towards Scalable and Reliable GPU-Accelerated Simulators in Embodied AI is evaluated on ManiSkill.'
  zh: 'GPUSimBench: Towards Scalable and Reliable GPU-Accelerated Simulators in Embodied AI评测于ManiSkill。'
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-08-06'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 该论文提出的基准用于评估包括ManiSkill在内的多个模拟器。 | 证据: GPUSimBench
    是一个面向具身智能 GPU 加速模拟器的标准化基准，由作者团队提出，用于系统评估主流模拟器（Isaac Lab、Genesis、Madrona、ManiSkill、MJX、MuJoCo Warp、Playground）在并行可扩展性、物理一致性和计算确定性三个维度的表现。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_gpusimbench_scalable_reliable_gpu_accele_2026
  url: https://kg.rounds-tech.com/entry/ent_paper_gpusimbench_scalable_reliable_gpu_accele_2026/
  accessed_at: '2026-08-06'
---
