---
$id: ent_paper_soccerdiffusion_toward_learnin_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'SoccerDiffusion: Toward Learning End-to-End Humanoid Robot Soccer from Gameplay Recordings'
  zh: 'SoccerDiffusion: Toward Learning End-to-End Humanoid Robot Soccer from Gameplay Recordings'
  ko: 'SoccerDiffusion: Toward Learning End-to-End Humanoid Robot Soccer from Gameplay Recordings'
summary:
  en: 'SoccerDiffusion: Toward Learning End-to-End Humanoid Robot Soccer from Gameplay Recordings is a 2025 work on locomotion
    for humanoid robots.'
  zh: 'SoccerDiffusion: Toward Learning End-to-End Humanoid Robot Soccer from Gameplay Recordings is a 2025 work on locomotion
    for humanoid robots.'
  ko: 'SoccerDiffusion: Toward Learning End-to-End Humanoid Robot Soccer from Gameplay Recordings is a 2025 work on locomotion
    for humanoid robots.'
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
- soccerdiffusion
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2504.20808v2.
sources:
- id: src_001
  type: paper
  title: 'SoccerDiffusion: Toward Learning End-to-End Humanoid Robot Soccer from Gameplay Recordings (arXiv)'
  url: https://arxiv.org/abs/2504.20808
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
This paper introduces SoccerDiffusion, a transformer-based diffusion model designed to learn end-to-end control policies for humanoid robot soccer directly from real-world gameplay recordings. Using data collected from RoboCup competitions, the model predicts joint command trajectories from multi-modal sensor inputs, including vision, proprioception, and game state. We employ a distillation technique to enable real-time inference on embedded platforms that reduces the multi-step diffusion process to a single step. Our results demonstrate the model's ability to replicate complex motion behaviors such as walking, kicking, and fall recovery both in simulation and on physical robots. Although high-level tactical behavior remains limited, this work provides a robust foundation for subsequent reinforcement learning or preference optimization methods. We release the dataset, pretrained models, and code under: https://bit-bots.github.io/SoccerDiffusion

## 核心内容
This paper introduces SoccerDiffusion, a transformer-based diffusion model designed to learn end-to-end control policies for humanoid robot soccer directly from real-world gameplay recordings. Using data collected from RoboCup competitions, the model predicts joint command trajectories from multi-modal sensor inputs, including vision, proprioception, and game state. We employ a distillation technique to enable real-time inference on embedded platforms that reduces the multi-step diffusion process to a single step. Our results demonstrate the model's ability to replicate complex motion behaviors such as walking, kicking, and fall recovery both in simulation and on physical robots. Although high-level tactical behavior remains limited, this work provides a robust foundation for subsequent reinforcement learning or preference optimization methods. We release the dataset, pretrained models, and code under: https://bit-bots.github.io/SoccerDiffusion

## 参考
- http://arxiv.org/abs/2504.20808v2

