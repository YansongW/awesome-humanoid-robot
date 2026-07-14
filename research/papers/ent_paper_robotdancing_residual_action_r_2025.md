---
$id: ent_paper_robotdancing_residual_action_r_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RobotDancing: Residual-Action RL Enables Robust Long-Horizon Humanoid Motion Tracking'
  zh: 'RobotDancing: Residual-Action RL Enables Robust Long-Horizon Humanoid Motion Tracking'
  ko: 'RobotDancing: Residual-Action RL Enables Robust Long-Horizon Humanoid Motion Tracking'
summary:
  en: 'RobotDancing: Residual-Action RL Enables Robust Long-Horizon Humanoid Motion Tracking is a 2025 work on physics-based
    character animation for humanoid robots.'
  zh: 'RobotDancing: Residual-Action RL Enables Robust Long-Horizon Humanoid Motion Tracking is a 2025 work on physics-based
    character animation for humanoid robots.'
  ko: 'RobotDancing: Residual-Action RL Enables Robust Long-Horizon Humanoid Motion Tracking is a 2025 work on physics-based
    character animation for humanoid robots.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- character_animation
- humanoid
- physics_based
- robotdancing
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.20717v1.
sources:
- id: src_001
  type: paper
  title: 'RobotDancing: Residual-Action RL Enables Robust Long-Horizon Humanoid Motion Tracking (arXiv)'
  url: https://arxiv.org/abs/2509.20717
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Long-horizon, high-dynamic motion tracking on humanoids remains brittle because absolute joint commands cannot compensate model-plant mismatch, leading to error accumulation. We propose RobotDancing, a simple, scalable framework that predicts residual joint targets to explicitly correct dynamics discrepancies. The pipeline is end-to-end--training, sim-to-sim validation, and zero-shot sim-to-real--and uses a single-stage reinforcement learning (RL) setup with a unified observation, reward, and hyperparameter configuration. We evaluate primarily on Unitree G1 with retargeted LAFAN1 dance sequences and validate transfer on H1/H1-2. RobotDancing can track multi-minute, high-energy behaviors (jumps, spins, cartwheels) and deploys zero-shot to hardware with high motion tracking quality.

## 核心内容
Long-horizon, high-dynamic motion tracking on humanoids remains brittle because absolute joint commands cannot compensate model-plant mismatch, leading to error accumulation. We propose RobotDancing, a simple, scalable framework that predicts residual joint targets to explicitly correct dynamics discrepancies. The pipeline is end-to-end--training, sim-to-sim validation, and zero-shot sim-to-real--and uses a single-stage reinforcement learning (RL) setup with a unified observation, reward, and hyperparameter configuration. We evaluate primarily on Unitree G1 with retargeted LAFAN1 dance sequences and validate transfer on H1/H1-2. RobotDancing can track multi-minute, high-energy behaviors (jumps, spins, cartwheels) and deploys zero-shot to hardware with high motion tracking quality.

## 参考
- http://arxiv.org/abs/2509.20717v1

