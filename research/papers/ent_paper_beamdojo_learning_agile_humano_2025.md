---
$id: ent_paper_beamdojo_learning_agile_humano_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'BeamDojo: Learning Agile Humanoid Locomotion on Sparse Footholds'
  zh: 'BeamDojo: Learning Agile Humanoid Locomotion on Sparse Footholds'
  ko: 'BeamDojo: Learning Agile Humanoid Locomotion on Sparse Footholds'
summary:
  en: 'BeamDojo: Learning Agile Humanoid Locomotion on Sparse Footholds is a 2025 work on locomotion for humanoid robots.'
  zh: 'BeamDojo: Learning Agile Humanoid Locomotion on Sparse Footholds is a 2025 work on locomotion for humanoid robots.'
  ko: 'BeamDojo: Learning Agile Humanoid Locomotion on Sparse Footholds is a 2025 work on locomotion for humanoid robots.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- beamdojo
- humanoid
- locomotion
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2502.10363v3.
sources:
- id: src_001
  type: paper
  title: 'BeamDojo: Learning Agile Humanoid Locomotion on Sparse Footholds (arXiv)'
  url: https://arxiv.org/abs/2502.10363
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'BeamDojo: Learning Agile Humanoid Locomotion on Sparse Footholds project page'
  url: https://why618188.github.io/beamdojo/
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Traversing risky terrains with sparse footholds poses a significant challenge for humanoid robots, requiring precise foot placements and stable locomotion. Existing learning-based approaches often struggle on such complex terrains due to sparse foothold rewards and inefficient learning processes. To address these challenges, we introduce BeamDojo, a reinforcement learning (RL) framework designed for enabling agile humanoid locomotion on sparse footholds. BeamDojo begins by introducing a sampling-based foothold reward tailored for polygonal feet, along with a double critic to balancing the learning process between dense locomotion rewards and sparse foothold rewards. To encourage sufficient trial-and-error exploration, BeamDojo incorporates a two-stage RL approach: the first stage relaxes the terrain dynamics by training the humanoid on flat terrain while providing it with task-terrain perceptive observations, and the second stage fine-tunes the policy on the actual task terrain. Moreover, we implement a onboard LiDAR-based elevation map to enable real-world deployment. Extensive simulation and real-world experiments demonstrate that BeamDojo achieves efficient learning in simulation and enables agile locomotion with precise foot placement on sparse footholds in the real world, maintaining a high success rate even under significant external disturbances.

## 核心内容
Traversing risky terrains with sparse footholds poses a significant challenge for humanoid robots, requiring precise foot placements and stable locomotion. Existing learning-based approaches often struggle on such complex terrains due to sparse foothold rewards and inefficient learning processes. To address these challenges, we introduce BeamDojo, a reinforcement learning (RL) framework designed for enabling agile humanoid locomotion on sparse footholds. BeamDojo begins by introducing a sampling-based foothold reward tailored for polygonal feet, along with a double critic to balancing the learning process between dense locomotion rewards and sparse foothold rewards. To encourage sufficient trial-and-error exploration, BeamDojo incorporates a two-stage RL approach: the first stage relaxes the terrain dynamics by training the humanoid on flat terrain while providing it with task-terrain perceptive observations, and the second stage fine-tunes the policy on the actual task terrain. Moreover, we implement a onboard LiDAR-based elevation map to enable real-world deployment. Extensive simulation and real-world experiments demonstrate that BeamDojo achieves efficient learning in simulation and enables agile locomotion with precise foot placement on sparse footholds in the real world, maintaining a high success rate even under significant external disturbances.

## 参考
- http://arxiv.org/abs/2502.10363v3

