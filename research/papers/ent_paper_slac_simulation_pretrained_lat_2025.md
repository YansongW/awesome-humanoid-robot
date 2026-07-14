---
$id: ent_paper_slac_simulation_pretrained_lat_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'SLAC: Simulation-Pretrained Latent Action Space for Whole-Body Real-World Reinforcement Learning'
  zh: 'SLAC: Simulation-Pretrained Latent Action Space for Whole-Body Real-World Reinforcement Learning'
  ko: 'SLAC: Simulation-Pretrained Latent Action Space for Whole-Body Real-World Reinforcement Learning'
summary:
  en: 'SLAC: Simulation-Pretrained Latent Action Space for Whole-Body Real-World Reinforcement Learning is a 2025 work on
    loco-manipulation and whole-body-control for humanoid robots.'
  zh: 'SLAC: Simulation-Pretrained Latent Action Space for Whole-Body Real-World Reinforcement Learning is a 2025 work on
    loco-manipulation and whole-body-control for humanoid robots.'
  ko: 'SLAC: Simulation-Pretrained Latent Action Space for Whole-Body Real-World Reinforcement Learning is a 2025 work on
    loco-manipulation and whole-body-control for humanoid robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- loco_manipulation
- slac
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2506.04147v4.
sources:
- id: src_001
  type: paper
  title: 'SLAC: Simulation-Pretrained Latent Action Space for Whole-Body Real-World Reinforcement Learning (arXiv)'
  url: https://arxiv.org/abs/2506.04147
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'SLAC: Simulation-Pretrained Latent Action Space for Whole-Body Real-World Reinforcement Learning project page'
  url: https://robo-rl.github.io/
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Building capable household and industrial robots requires mastering the control of versatile, high-degree-of-freedom (DoF) systems such as mobile manipulators. While reinforcement learning (RL) holds promise for autonomously acquiring robot control policies, scaling it to high-DoF embodiments remains challenging. Direct RL in the real world demands both safe exploration and high sample efficiency, which are difficult to achieve in practice. Sim-to-real RL, on the other hand, is often brittle due to the reality gap. This paper introduces SLAC, a method that renders real-world RL feasible for complex embodiments by leveraging a low-fidelity simulator to pretrain a task-agnostic latent action space. SLAC trains this latent action space via a customized unsupervised skill discovery method designed to promote temporal abstraction, disentanglement, and safety, thereby facilitating efficient downstream learning. Once a latent action space is learned, SLAC uses it as the action interface for a novel off-policy RL algorithm to autonomously learn downstream tasks through real-world interactions. We evaluate SLAC against existing methods on a suite of bimanual mobile manipulation tasks, where it achieves state-of-the-art performance. Notably, SLAC learns contact-rich whole-body tasks in under an hour of real-world interactions, without relying on any demonstrations or hand-crafted behavior priors. More information and robot videos at robo-rl.github.io

## 核心内容
Building capable household and industrial robots requires mastering the control of versatile, high-degree-of-freedom (DoF) systems such as mobile manipulators. While reinforcement learning (RL) holds promise for autonomously acquiring robot control policies, scaling it to high-DoF embodiments remains challenging. Direct RL in the real world demands both safe exploration and high sample efficiency, which are difficult to achieve in practice. Sim-to-real RL, on the other hand, is often brittle due to the reality gap. This paper introduces SLAC, a method that renders real-world RL feasible for complex embodiments by leveraging a low-fidelity simulator to pretrain a task-agnostic latent action space. SLAC trains this latent action space via a customized unsupervised skill discovery method designed to promote temporal abstraction, disentanglement, and safety, thereby facilitating efficient downstream learning. Once a latent action space is learned, SLAC uses it as the action interface for a novel off-policy RL algorithm to autonomously learn downstream tasks through real-world interactions. We evaluate SLAC against existing methods on a suite of bimanual mobile manipulation tasks, where it achieves state-of-the-art performance. Notably, SLAC learns contact-rich whole-body tasks in under an hour of real-world interactions, without relying on any demonstrations or hand-crafted behavior priors. More information and robot videos at robo-rl.github.io

## 参考
- http://arxiv.org/abs/2506.04147v4

