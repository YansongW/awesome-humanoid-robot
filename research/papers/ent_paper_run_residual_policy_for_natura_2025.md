---
$id: ent_paper_run_residual_policy_for_natura_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RuN: Residual Policy for Natural Humanoid Locomotion'
  zh: 'RuN: Residual Policy for Natural Humanoid Locomotion'
  ko: 'RuN: Residual Policy for Natural Humanoid Locomotion'
summary:
  en: 'RuN: Residual Policy for Natural Humanoid Locomotion is a 2025 work on locomotion for humanoid robots.'
  zh: 'RuN: Residual Policy for Natural Humanoid Locomotion is a 2025 work on locomotion for humanoid robots.'
  ko: 'RuN: Residual Policy for Natural Humanoid Locomotion is a 2025 work on locomotion for humanoid robots.'
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
- run
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.20696v1.
sources:
- id: src_001
  type: paper
  title: 'RuN: Residual Policy for Natural Humanoid Locomotion (arXiv)'
  url: https://arxiv.org/abs/2509.20696
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Enabling humanoid robots to achieve natural and dynamic locomotion across a wide range of speeds, including smooth transitions from walking to running, presents a significant challenge. Existing deep reinforcement learning methods typically require the policy to directly track a reference motion, forcing a single policy to simultaneously learn motion imitation, velocity tracking, and stability maintenance. To address this, we introduce RuN, a novel decoupled residual learning framework. RuN decomposes the control task by pairing a pre-trained Conditional Motion Generator, which provides a kinematically natural motion prior, with a reinforcement learning policy that learns a lightweight residual correction to handle dynamical interactions. Experiments in simulation and reality on the Unitree G1 humanoid robot demonstrate that RuN achieves stable, natural gaits and smooth walk-run transitions across a broad velocity range (0-2.5 m/s), outperforming state-of-the-art methods in both training efficiency and final performance.

## 核心内容
Enabling humanoid robots to achieve natural and dynamic locomotion across a wide range of speeds, including smooth transitions from walking to running, presents a significant challenge. Existing deep reinforcement learning methods typically require the policy to directly track a reference motion, forcing a single policy to simultaneously learn motion imitation, velocity tracking, and stability maintenance. To address this, we introduce RuN, a novel decoupled residual learning framework. RuN decomposes the control task by pairing a pre-trained Conditional Motion Generator, which provides a kinematically natural motion prior, with a reinforcement learning policy that learns a lightweight residual correction to handle dynamical interactions. Experiments in simulation and reality on the Unitree G1 humanoid robot demonstrate that RuN achieves stable, natural gaits and smooth walk-run transitions across a broad velocity range (0-2.5 m/s), outperforming state-of-the-art methods in both training efficiency and final performance.

## 参考
- http://arxiv.org/abs/2509.20696v1

