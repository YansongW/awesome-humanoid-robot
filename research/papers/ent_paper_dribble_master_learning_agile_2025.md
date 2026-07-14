---
$id: ent_paper_dribble_master_learning_agile_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Dribble Master: Learning Agile Humanoid Dribbling Through Legged Locomotion'
  zh: 'Dribble Master: Learning Agile Humanoid Dribbling Through Legged Locomotion'
  ko: 'Dribble Master: Learning Agile Humanoid Dribbling Through Legged Locomotion'
summary:
  en: 'Dribble Master: Learning Agile Humanoid Dribbling Through Legged Locomotion is a 2025 work on locomotion for humanoid
    robots.'
  zh: 'Dribble Master: Learning Agile Humanoid Dribbling Through Legged Locomotion is a 2025 work on locomotion for humanoid
    robots.'
  ko: 'Dribble Master: Learning Agile Humanoid Dribbling Through Legged Locomotion is a 2025 work on locomotion for humanoid
    robots.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- dribble_master
- humanoid
- locomotion
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.12679v3.
sources:
- id: src_001
  type: paper
  title: 'Dribble Master: Learning Agile Humanoid Dribbling Through Legged Locomotion (arXiv)'
  url: https://arxiv.org/abs/2505.12679
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Humanoid soccer dribbling is a highly challenging task that demands dexterous ball manipulation while maintaining dynamic balance. Traditional rule-based methods often struggle to achieve accurate ball control due to their reliance on fixed walking patterns and limited adaptability to real-time ball dynamics. To address these challenges, we propose a two-stage curriculum learning framework that enables a humanoid robot to acquire dribbling skills without explicit dynamics or predefined trajectories. In the first stage, the robot learns basic locomotion skills; in the second stage, we fine-tune the policy for agile dribbling maneuvers. We further introduce a virtual camera model in simulation that simulates the field of view and perception constraints of the real robot, enabling realistic ball perception during training. We also design heuristic rewards to encourage active sensing, promoting a broader visual range for continuous ball perception. The policy is trained in simulation and successfully transferred to a physical humanoid robot. Experiment results demonstrate that our method enables effective ball manipulation, achieving flexible and visually appealing dribbling behaviors across multiple environments. This work highlights the potential of reinforcement learning in developing agile humanoid soccer robots. Additional details and videos are available at https://zhuoheng0910.github.io/dribble-master/.

## 核心内容
Humanoid soccer dribbling is a highly challenging task that demands dexterous ball manipulation while maintaining dynamic balance. Traditional rule-based methods often struggle to achieve accurate ball control due to their reliance on fixed walking patterns and limited adaptability to real-time ball dynamics. To address these challenges, we propose a two-stage curriculum learning framework that enables a humanoid robot to acquire dribbling skills without explicit dynamics or predefined trajectories. In the first stage, the robot learns basic locomotion skills; in the second stage, we fine-tune the policy for agile dribbling maneuvers. We further introduce a virtual camera model in simulation that simulates the field of view and perception constraints of the real robot, enabling realistic ball perception during training. We also design heuristic rewards to encourage active sensing, promoting a broader visual range for continuous ball perception. The policy is trained in simulation and successfully transferred to a physical humanoid robot. Experiment results demonstrate that our method enables effective ball manipulation, achieving flexible and visually appealing dribbling behaviors across multiple environments. This work highlights the potential of reinforcement learning in developing agile humanoid soccer robots. Additional details and videos are available at https://zhuoheng0910.github.io/dribble-master/.

## 参考
- http://arxiv.org/abs/2505.12679v3

