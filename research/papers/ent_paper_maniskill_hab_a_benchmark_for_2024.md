---
$id: ent_paper_maniskill_hab_a_benchmark_for_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ManiSkill-HAB: A Benchmark for Low-Level Manipulation in Home Rearrangement Tasks'
  zh: 'ManiSkill-HAB: A Benchmark for Low-Level Manipulation in Home Rearrangement Tasks'
  ko: 'ManiSkill-HAB: A Benchmark for Low-Level Manipulation in Home Rearrangement Tasks'
summary:
  en: 'ManiSkill-HAB: A Benchmark for Low-Level Manipulation in Home Rearrangement Tasks is a 2024 work on simulation benchmark
    for humanoid robots.'
  zh: 'ManiSkill-HAB: A Benchmark for Low-Level Manipulation in Home Rearrangement Tasks is a 2024 work on simulation benchmark
    for humanoid robots.'
  ko: 'ManiSkill-HAB: A Benchmark for Low-Level Manipulation in Home Rearrangement Tasks is a 2024 work on simulation benchmark
    for humanoid robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
- 10_evaluation_benchmarks
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- benchmark
- humanoid
- maniskill_hab
- simulation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2412.13211v3.
sources:
- id: src_001
  type: paper
  title: 'ManiSkill-HAB: A Benchmark for Low-Level Manipulation in Home Rearrangement Tasks (arXiv)'
  url: https://arxiv.org/abs/2412.13211
  date: '2024'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'ManiSkill-HAB: A Benchmark for Low-Level Manipulation in Home Rearrangement Tasks project page'
  url: https://arth-shukla.github.io/mshab/
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
High-quality benchmarks are the foundation for embodied AI research, enabling significant advancements in long-horizon navigation, manipulation and rearrangement tasks. However, as frontier tasks in robotics get more advanced, they require faster simulation speed, more intricate test environments, and larger demonstration datasets. To this end, we present MS-HAB, a holistic benchmark for low-level manipulation and in-home object rearrangement. First, we provide a GPU-accelerated implementation of the Home Assistant Benchmark (HAB). We support realistic low-level control and achieve over 3x the speed of prior magical grasp implementations at a fraction of the GPU memory usage. Second, we train extensive reinforcement learning (RL) and imitation learning (IL) baselines for future work to compare against. Finally, we develop a rule-based trajectory filtering system to sample specific demonstrations from our RL policies which match predefined criteria for robot behavior and safety. Combining demonstration filtering with our fast environments enables efficient, controlled data generation at scale.

## 核心内容
High-quality benchmarks are the foundation for embodied AI research, enabling significant advancements in long-horizon navigation, manipulation and rearrangement tasks. However, as frontier tasks in robotics get more advanced, they require faster simulation speed, more intricate test environments, and larger demonstration datasets. To this end, we present MS-HAB, a holistic benchmark for low-level manipulation and in-home object rearrangement. First, we provide a GPU-accelerated implementation of the Home Assistant Benchmark (HAB). We support realistic low-level control and achieve over 3x the speed of prior magical grasp implementations at a fraction of the GPU memory usage. Second, we train extensive reinforcement learning (RL) and imitation learning (IL) baselines for future work to compare against. Finally, we develop a rule-based trajectory filtering system to sample specific demonstrations from our RL policies which match predefined criteria for robot behavior and safety. Combining demonstration filtering with our fast environments enables efficient, controlled data generation at scale.

## 参考
- http://arxiv.org/abs/2412.13211v3

