---
$id: ent_paper_hord_robust_humanoid_control_v_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'HoRD: Robust Humanoid Control via History-Conditioned Reinforcement Learning and Online Distillation'
  zh: 'HoRD: Robust Humanoid Control via History-Conditioned Reinforcement Learning and Online Distillation'
  ko: 'HoRD: Robust Humanoid Control via History-Conditioned Reinforcement Learning and Online Distillation'
summary:
  en: 'HoRD: Robust Humanoid Control via History-Conditioned Reinforcement Learning and Online Distillation is a 2026 work
    on locomotion for humanoid robots.'
  zh: 'HoRD: Robust Humanoid Control via History-Conditioned Reinforcement Learning and Online Distillation is a 2026 work
    on locomotion for humanoid robots.'
  ko: 'HoRD: Robust Humanoid Control via History-Conditioned Reinforcement Learning and Online Distillation is a 2026 work
    on locomotion for humanoid robots.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- hord
- humanoid
- locomotion
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.04412v3.
sources:
- id: src_001
  type: paper
  title: 'HoRD: Robust Humanoid Control via History-Conditioned Reinforcement Learning and Online Distillation (arXiv)'
  url: https://arxiv.org/abs/2602.04412
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Humanoid robots can suffer significant performance drops under small changes in dynamics, task specifications, or environment setup. We propose HoRD, a two-stage learning framework for robust humanoid control under domain shift. First, we train a high-performance teacher policy via history-conditioned reinforcement learning, where the policy infers latent dynamics context from recent state--action trajectories to adapt online to diverse randomized dynamics. Second, we perform online distillation to transfer the teacher's robust control capabilities into a transformer-based student policy that operates on sparse root-relative 3D joint keypoint trajectories. By combining history-conditioned adaptation with online distillation, HoRD enables a single policy to adapt zero-shot to unseen domains without per-domain retraining. Extensive experiments show HoRD outperforms strong baselines in robustness and transfer, especially under unseen domains and external perturbations. Code and project page are available at https://tonywang-0517.github.io/hord/.

## 核心内容
Humanoid robots can suffer significant performance drops under small changes in dynamics, task specifications, or environment setup. We propose HoRD, a two-stage learning framework for robust humanoid control under domain shift. First, we train a high-performance teacher policy via history-conditioned reinforcement learning, where the policy infers latent dynamics context from recent state--action trajectories to adapt online to diverse randomized dynamics. Second, we perform online distillation to transfer the teacher's robust control capabilities into a transformer-based student policy that operates on sparse root-relative 3D joint keypoint trajectories. By combining history-conditioned adaptation with online distillation, HoRD enables a single policy to adapt zero-shot to unseen domains without per-domain retraining. Extensive experiments show HoRD outperforms strong baselines in robustness and transfer, especially under unseen domains and external perturbations. Code and project page are available at https://tonywang-0517.github.io/hord/.

## 参考
- http://arxiv.org/abs/2602.04412v3

