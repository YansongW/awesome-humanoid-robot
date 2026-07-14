---
$id: ent_paper_predictive_sampling_real_time_2022
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Predictive Sampling: Real-time Behaviour Synthesis with MuJoCo'
  zh: 'Predictive Sampling: Real-time Behaviour Synthesis with MuJoCo'
  ko: 'Predictive Sampling: Real-time Behaviour Synthesis with MuJoCo'
summary:
  en: 'Predictive Sampling: Real-time Behaviour Synthesis with MuJoCo is a 2022 work on loco-manipulation and whole-body-control
    for humanoid robots.'
  zh: 'Predictive Sampling: Real-time Behaviour Synthesis with MuJoCo is a 2022 work on loco-manipulation and whole-body-control
    for humanoid robots.'
  ko: 'Predictive Sampling: Real-time Behaviour Synthesis with MuJoCo is a 2022 work on loco-manipulation and whole-body-control
    for humanoid robots.'
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
- predictive_sampling
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2212.00541v2.
sources:
- id: src_001
  type: paper
  title: 'Predictive Sampling: Real-time Behaviour Synthesis with MuJoCo (arXiv)'
  url: https://arxiv.org/abs/2212.00541
  date: '2022'
  accessed_at: '2026-07-01'
---
## 概述
We introduce MuJoCo MPC (MJPC), an open-source, interactive application and software framework for real-time predictive control, based on MuJoCo physics. MJPC allows the user to easily author and solve complex robotics tasks, and currently supports three shooting-based planners: derivative-based iLQG and Gradient Descent, and a simple derivative-free method we call Predictive Sampling. Predictive Sampling was designed as an elementary baseline, mostly for its pedagogical value, but turned out to be surprisingly competitive with the more established algorithms. This work does not present algorithmic advances, and instead, prioritises performant algorithms, simple code, and accessibility of model-based methods via intuitive and interactive software. MJPC is available at: github.com/deepmind/mujoco_mpc, a video summary can be viewed at: dpmd.ai/mjpc.

## 核心内容
We introduce MuJoCo MPC (MJPC), an open-source, interactive application and software framework for real-time predictive control, based on MuJoCo physics. MJPC allows the user to easily author and solve complex robotics tasks, and currently supports three shooting-based planners: derivative-based iLQG and Gradient Descent, and a simple derivative-free method we call Predictive Sampling. Predictive Sampling was designed as an elementary baseline, mostly for its pedagogical value, but turned out to be surprisingly competitive with the more established algorithms. This work does not present algorithmic advances, and instead, prioritises performant algorithms, simple code, and accessibility of model-based methods via intuitive and interactive software. MJPC is available at: github.com/deepmind/mujoco_mpc, a video summary can be viewed at: dpmd.ai/mjpc.

## 参考
- http://arxiv.org/abs/2212.00541v2

