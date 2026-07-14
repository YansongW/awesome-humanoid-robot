---
$id: ent_paper_learning_smooth_humanoid_locom_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning Smooth Humanoid Locomotion through Lipschitz-Constrained Policies
  zh: Learning Smooth Humanoid Locomotion through Lipschitz-Constrained Policies
  ko: Learning Smooth Humanoid Locomotion through Lipschitz-Constrained Policies
summary:
  en: Learning Smooth Humanoid Locomotion through Lipschitz-Constrained Policies is a 2024 work on locomotion for humanoid
    robots, with open-source code available.
  zh: Learning Smooth Humanoid Locomotion through Lipschitz-Constrained Policies is a 2024 work on locomotion for humanoid
    robots, with open-source code available.
  ko: Learning Smooth Humanoid Locomotion through Lipschitz-Constrained Policies is a 2024 work on locomotion for humanoid
    robots, with open-source code available.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- learning_smooth_humanoid_locom
- locomotion
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2410.11825v3.
sources:
- id: src_001
  type: paper
  title: Learning Smooth Humanoid Locomotion through Lipschitz-Constrained Policies (arXiv)
  url: https://arxiv.org/abs/2410.11825
  date: '2024'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Learning Smooth Humanoid Locomotion through Lipschitz-Constrained Policies project page
  url: https://lipschitz-constrained-policy.github.io/
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
Reinforcement learning combined with sim-to-real transfer offers a general framework for developing locomotion controllers for legged robots. To facilitate successful deployment in the real world, smoothing techniques, such as low-pass filters and smoothness rewards, are often employed to develop policies with smooth behaviors. However, because these techniques are non-differentiable and usually require tedious tuning of a large set of hyperparameters, they tend to require extensive manual tuning for each robotic platform. To address this challenge and establish a general technique for enforcing smooth behaviors, we propose a simple and effective method that imposes a Lipschitz constraint on a learned policy, which we refer to as Lipschitz-Constrained Policies (LCP). We show that the Lipschitz constraint can be implemented in the form of a gradient penalty, which provides a differentiable objective that can be easily incorporated with automatic differentiation frameworks. We demonstrate that LCP effectively replaces the need for smoothing rewards or low-pass filters and can be easily integrated into training frameworks for many distinct humanoid robots. We extensively evaluate LCP in both simulation and real-world humanoid robots, producing smooth and robust locomotion controllers. All simulation and deployment code, along with complete checkpoints, is available on our project page: https://lipschitz-constrained-policy.github.io.

## 核心内容
Reinforcement learning combined with sim-to-real transfer offers a general framework for developing locomotion controllers for legged robots. To facilitate successful deployment in the real world, smoothing techniques, such as low-pass filters and smoothness rewards, are often employed to develop policies with smooth behaviors. However, because these techniques are non-differentiable and usually require tedious tuning of a large set of hyperparameters, they tend to require extensive manual tuning for each robotic platform. To address this challenge and establish a general technique for enforcing smooth behaviors, we propose a simple and effective method that imposes a Lipschitz constraint on a learned policy, which we refer to as Lipschitz-Constrained Policies (LCP). We show that the Lipschitz constraint can be implemented in the form of a gradient penalty, which provides a differentiable objective that can be easily incorporated with automatic differentiation frameworks. We demonstrate that LCP effectively replaces the need for smoothing rewards or low-pass filters and can be easily integrated into training frameworks for many distinct humanoid robots. We extensively evaluate LCP in both simulation and real-world humanoid robots, producing smooth and robust locomotion controllers. All simulation and deployment code, along with complete checkpoints, is available on our project page: https://lipschitz-constrained-policy.github.io.

## 参考
- http://arxiv.org/abs/2410.11825v3

