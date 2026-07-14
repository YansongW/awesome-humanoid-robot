---
$id: ent_paper_whole_body_model_predictive_co_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Whole-Body Model-Predictive Control of Legged Robots with MuJoCo
  zh: Whole-Body Model-Predictive Control of Legged Robots with MuJoCo
  ko: Whole-Body Model-Predictive Control of Legged Robots with MuJoCo
summary:
  en: Whole-Body Model-Predictive Control of Legged Robots with MuJoCo is a 2025 work on loco-manipulation and whole-body-control
    for humanoid robots.
  zh: Whole-Body Model-Predictive Control of Legged Robots with MuJoCo is a 2025 work on loco-manipulation and whole-body-control
    for humanoid robots.
  ko: Whole-Body Model-Predictive Control of Legged Robots with MuJoCo is a 2025 work on loco-manipulation and whole-body-control
    for humanoid robots.
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
- whole_body_control
- whole_body_model_predictive_co
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2503.04613v3.
sources:
- id: src_001
  type: paper
  title: Whole-Body Model-Predictive Control of Legged Robots with MuJoCo (arXiv)
  url: https://arxiv.org/abs/2503.04613
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
We demonstrate the surprising real-world effectiveness of a very simple approach to whole-body model-predictive control (MPC) of quadruped and humanoid robots: the iterative LQR (iLQR) algorithm with MuJoCo dynamics and finite-difference approximated derivatives. Building upon the previous success of model-based behavior synthesis and control of locomotion and manipulation tasks with MuJoCo in simulation, we show that these policies can easily generalize to the real world with few sim-to-real considerations. Our baseline method achieves real-time whole-body MPC on a variety of hardware experiments, including dynamic quadruped locomotion, quadruped walking on two legs, and full-sized humanoid bipedal locomotion. We hope this easy-to-reproduce hardware baseline lowers the barrier to entry for real-world whole-body MPC research and contributes to accelerating research velocity in the community. Our code and experiment videos will be available online at:https://johnzhang3.github.io/mujoco_ilqr

## 核心内容
We demonstrate the surprising real-world effectiveness of a very simple approach to whole-body model-predictive control (MPC) of quadruped and humanoid robots: the iterative LQR (iLQR) algorithm with MuJoCo dynamics and finite-difference approximated derivatives. Building upon the previous success of model-based behavior synthesis and control of locomotion and manipulation tasks with MuJoCo in simulation, we show that these policies can easily generalize to the real world with few sim-to-real considerations. Our baseline method achieves real-time whole-body MPC on a variety of hardware experiments, including dynamic quadruped locomotion, quadruped walking on two legs, and full-sized humanoid bipedal locomotion. We hope this easy-to-reproduce hardware baseline lowers the barrier to entry for real-world whole-body MPC research and contributes to accelerating research velocity in the community. Our code and experiment videos will be available online at:https://johnzhang3.github.io/mujoco_ilqr

## 参考
- http://arxiv.org/abs/2503.04613v3

