---
$id: ent_paper_full_order_sampling_based_mpc_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Full-Order Sampling-Based MPC for Torque-Level Locomotion Control via Diffusion-Style Annealing
  zh: Full-Order Sampling-Based MPC for Torque-Level Locomotion Control via Diffusion-Style Annealing
  ko: Full-Order Sampling-Based MPC for Torque-Level Locomotion Control via Diffusion-Style Annealing
summary:
  en: Full-Order Sampling-Based MPC for Torque-Level Locomotion Control via Diffusion-Style Annealing is a 2024 work on loco-manipulation
    and whole-body-control for humanoid robots.
  zh: Full-Order Sampling-Based MPC for Torque-Level Locomotion Control via Diffusion-Style Annealing is a 2024 work on loco-manipulation
    and whole-body-control for humanoid robots.
  ko: Full-Order Sampling-Based MPC for Torque-Level Locomotion Control via Diffusion-Style Annealing is a 2024 work on loco-manipulation
    and whole-body-control for humanoid robots.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- full_order_sampling_based_mpc
- humanoid
- loco_manipulation
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2409.15610v1.
sources:
- id: src_001
  type: paper
  title: Full-Order Sampling-Based MPC for Torque-Level Locomotion Control via Diffusion-Style Annealing (arXiv)
  url: https://arxiv.org/abs/2409.15610
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
Due to high dimensionality and non-convexity, real-time optimal control using full-order dynamics models for legged robots is challenging. Therefore, Nonlinear Model Predictive Control (NMPC) approaches are often limited to reduced-order models. Sampling-based MPC has shown potential in nonconvex even discontinuous problems, but often yields suboptimal solutions with high variance, which limits its applications in high-dimensional locomotion. This work introduces DIAL-MPC (Diffusion-Inspired Annealing for Legged MPC), a sampling-based MPC framework with a novel diffusion-style annealing process. Such an annealing process is supported by the theoretical landscape analysis of Model Predictive Path Integral Control (MPPI) and the connection between MPPI and single-step diffusion. Algorithmically, DIAL-MPC iteratively refines solutions online and achieves both global coverage and local convergence. In quadrupedal torque-level control tasks, DIAL-MPC reduces the tracking error of standard MPPI by $13.4$ times and outperforms reinforcement learning (RL) policies by $50\%$ in challenging climbing tasks without any training. In particular, DIAL-MPC enables precise real-world quadrupedal jumping with payload. To the best of our knowledge, DIAL-MPC is the first training-free method that optimizes over full-order quadruped dynamics in real-time.

## 核心内容
Due to high dimensionality and non-convexity, real-time optimal control using full-order dynamics models for legged robots is challenging. Therefore, Nonlinear Model Predictive Control (NMPC) approaches are often limited to reduced-order models. Sampling-based MPC has shown potential in nonconvex even discontinuous problems, but often yields suboptimal solutions with high variance, which limits its applications in high-dimensional locomotion. This work introduces DIAL-MPC (Diffusion-Inspired Annealing for Legged MPC), a sampling-based MPC framework with a novel diffusion-style annealing process. Such an annealing process is supported by the theoretical landscape analysis of Model Predictive Path Integral Control (MPPI) and the connection between MPPI and single-step diffusion. Algorithmically, DIAL-MPC iteratively refines solutions online and achieves both global coverage and local convergence. In quadrupedal torque-level control tasks, DIAL-MPC reduces the tracking error of standard MPPI by $13.4$ times and outperforms reinforcement learning (RL) policies by $50\%$ in challenging climbing tasks without any training. In particular, DIAL-MPC enables precise real-world quadrupedal jumping with payload. To the best of our knowledge, DIAL-MPC is the first training-free method that optimizes over full-order quadruped dynamics in real-time.

## 参考
- http://arxiv.org/abs/2409.15610v1

