---
$id: ent_paper_mash_cooperative_heterogeneous_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'MASH: Cooperative-Heterogeneous Multi-Agent RL for Single Humanoid Robot Locomotion'
  zh: 'MASH: Cooperative-Heterogeneous Multi-Agent RL for Single Humanoid Robot Locomotion'
  ko: 'MASH: Cooperative-Heterogeneous Multi-Agent RL for Single Humanoid Robot Locomotion'
summary:
  en: 'MASH: Cooperative-Heterogeneous Multi-Agent RL for Single Humanoid Robot Locomotion is a 2025 work on locomotion for
    humanoid robots.'
  zh: 'MASH: Cooperative-Heterogeneous Multi-Agent RL for Single Humanoid Robot Locomotion is a 2025 work on locomotion for
    humanoid robots.'
  ko: 'MASH: Cooperative-Heterogeneous Multi-Agent RL for Single Humanoid Robot Locomotion is a 2025 work on locomotion for
    humanoid robots.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- locomotion
- mash
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2508.10423v1.
sources:
- id: src_001
  type: paper
  title: 'MASH: Cooperative-Heterogeneous Multi-Agent RL for Single Humanoid Robot Locomotion (arXiv)'
  url: https://arxiv.org/abs/2508.10423
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
This paper proposes a novel method to enhance locomotion for a single humanoid robot through cooperative-heterogeneous multi-agent deep reinforcement learning (MARL). While most existing methods typically employ single-agent reinforcement learning algorithms for a single humanoid robot or MARL algorithms for multi-robot system tasks, we propose a distinct paradigm: applying cooperative-heterogeneous MARL to optimize locomotion for a single humanoid robot. The proposed method, multi-agent reinforcement learning for single humanoid locomotion (MASH), treats each limb (legs and arms) as an independent agent that explores the robot's action space while sharing a global critic for cooperative learning. Experiments demonstrate that MASH accelerates training convergence and improves whole-body cooperation ability, outperforming conventional single-agent reinforcement learning methods. This work advances the integration of MARL into single-humanoid-robot control, offering new insights into efficient locomotion strategies.

## 核心内容
This paper proposes a novel method to enhance locomotion for a single humanoid robot through cooperative-heterogeneous multi-agent deep reinforcement learning (MARL). While most existing methods typically employ single-agent reinforcement learning algorithms for a single humanoid robot or MARL algorithms for multi-robot system tasks, we propose a distinct paradigm: applying cooperative-heterogeneous MARL to optimize locomotion for a single humanoid robot. The proposed method, multi-agent reinforcement learning for single humanoid locomotion (MASH), treats each limb (legs and arms) as an independent agent that explores the robot's action space while sharing a global critic for cooperative learning. Experiments demonstrate that MASH accelerates training convergence and improves whole-body cooperation ability, outperforming conventional single-agent reinforcement learning methods. This work advances the integration of MARL into single-humanoid-robot control, offering new insights into efficient locomotion strategies.

## 参考
- http://arxiv.org/abs/2508.10423v1

