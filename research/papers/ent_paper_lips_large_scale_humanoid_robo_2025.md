---
$id: ent_paper_lips_large_scale_humanoid_robo_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'LiPS: Large-Scale Humanoid Robot RL with Parallel-Series Structures'
  zh: 'LiPS: Large-Scale Humanoid Robot RL with Parallel-Series Structures'
  ko: 'LiPS: Large-Scale Humanoid Robot RL with Parallel-Series Structures'
summary:
  en: 'LiPS: Large-Scale Humanoid Robot RL with Parallel-Series Structures is a 2025 work on locomotion for humanoid robots.'
  zh: 'LiPS: Large-Scale Humanoid Robot RL with Parallel-Series Structures is a 2025 work on locomotion for humanoid robots.'
  ko: 'LiPS: Large-Scale Humanoid Robot RL with Parallel-Series Structures is a 2025 work on locomotion for humanoid robots.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- lips
- locomotion
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2503.08349v1.
sources:
- id: src_001
  type: paper
  title: 'LiPS: Large-Scale Humanoid Robot RL with Parallel-Series Structures (arXiv)'
  url: https://arxiv.org/abs/2503.08349
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
In recent years, research on humanoid robots has garnered significant attention, particularly in reinforcement learning based control algorithms, which have achieved major breakthroughs. Compared to traditional model-based control algorithms, reinforcement learning based algorithms demonstrate substantial advantages in handling complex tasks. Leveraging the large-scale parallel computing capabilities of GPUs, contemporary humanoid robots can undergo extensive parallel training in simulated environments. A physical simulation platform capable of large-scale parallel training is crucial for the development of humanoid robots. As one of the most complex robot forms, humanoid robots typically possess intricate mechanical structures, encompassing numerous series and parallel mechanisms. However, many reinforcement learning based humanoid robot control algorithms currently employ open-loop topologies during training, deferring the conversion to series-parallel structures until the sim2real phase. This approach is primarily due to the limitations of physics engines, as current GPU-based physics engines often only support open-loop topologies or have limited capabilities in simulating multi-rigid-body closed-loop topologies. For enabling reinforcement learning-based humanoid robot control algorithms to train in large-scale parallel environments, we propose a novel training method LiPS. By incorporating multi-rigid-body dynamics modeling in the simulation environment, we significantly reduce the sim2real gap and the difficulty of converting to parallel structures during model deployment, thereby robustly supporting large-scale reinforcement learning for humanoid robots.

## 核心内容
In recent years, research on humanoid robots has garnered significant attention, particularly in reinforcement learning based control algorithms, which have achieved major breakthroughs. Compared to traditional model-based control algorithms, reinforcement learning based algorithms demonstrate substantial advantages in handling complex tasks. Leveraging the large-scale parallel computing capabilities of GPUs, contemporary humanoid robots can undergo extensive parallel training in simulated environments. A physical simulation platform capable of large-scale parallel training is crucial for the development of humanoid robots. As one of the most complex robot forms, humanoid robots typically possess intricate mechanical structures, encompassing numerous series and parallel mechanisms. However, many reinforcement learning based humanoid robot control algorithms currently employ open-loop topologies during training, deferring the conversion to series-parallel structures until the sim2real phase. This approach is primarily due to the limitations of physics engines, as current GPU-based physics engines often only support open-loop topologies or have limited capabilities in simulating multi-rigid-body closed-loop topologies. For enabling reinforcement learning-based humanoid robot control algorithms to train in large-scale parallel environments, we propose a novel training method LiPS. By incorporating multi-rigid-body dynamics modeling in the simulation environment, we significantly reduce the sim2real gap and the difficulty of converting to parallel structures during model deployment, thereby robustly supporting large-scale reinforcement learning for humanoid robots.

## 参考
- http://arxiv.org/abs/2503.08349v1

