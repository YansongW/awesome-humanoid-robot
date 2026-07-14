---
$id: ent_paper_learning_gait_aware_quadruped_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning Gait-Aware Quadruped Locomotion with Temporal Logic Specifications
  zh: Learning Gait-Aware Quadruped Locomotion with Temporal Logic Specifications
  ko: Learning Gait-Aware Quadruped Locomotion with Temporal Logic Specifications
summary:
  en: "arXiv:2607.00442v1 Announce Type: new \nAbstract: Reinforcement learning (RL)\
    \ for quadruped locomotion commonly depends on fixed, hand-crafted, and Markovian\
    \ reward functions that limit both interpretability of learned policies and lack\
    \ explicit control over gait behaviors. We introduce a framework where distinct\
    \ gaits are specified using parameterized constraints expressed in Signal Temporal\
    \ Logic (STL). These include safety bounds, gait synchronization constraints,\
    \ command tracking, and actuation bounds. From these specifications, we develop\
    \ a reward shaping mechanism that provides learning agents a dense, continuous\
    \ reward landscape that encodes desired behavior. We define parametric STL templates\
    \ for three speed regimes (walking-trot, trot, bound), calibrate their parameters\
    \ from reference rollouts, and compute rewards from using smooth approximations\
    \ of STL robustness over the rollouts. The generated rewards can be used to provide\
    \ shaped gradients compatible with Proximal Policy Optimization (PPO). We instantiate\
    \ the approach on Google's Barkour quadruped robot in MuJoCo XLA (MJX). We use\
    \ parallelization within the simulator to improve training speeds and use domain\
    \ randomization to robustify learned policies. We show that compared to a baseline\
    \ of hand-crafted rewards, the STL-shaped rewards yield tighter velocity tracking\
    \ and more stable training. Videos can be found on our project website: https://stl-locomotion.github.io/."
  zh: "arXiv:2607.00442v1 Announce Type: new \nAbstract: Reinforcement learning (RL)\
    \ for quadruped locomotion commonly depends on fixed, hand-crafted, and Markovian\
    \ reward functions that limit both interpretability of learned policies and lack\
    \ explicit control over gait behaviors. We introduce a framework where distinct\
    \ gaits are specified using parameterized constraints expressed in Signal Temporal\
    \ Logic (STL). These include safety bounds, gait synchronization constraints,\
    \ command tracking, and actuation bounds. From these specifications, we develop\
    \ a reward shaping mechanism that provides learning agents a dense, continuous\
    \ reward landscape that encodes desired behavior. We define parametric STL templates\
    \ for three speed regimes (walking-trot, trot, bound), calibrate their parameters\
    \ from reference rollouts, and compute rewards from using smooth approximations\
    \ of STL robustness over the rollouts. The generated rewards can be used to provide\
    \ shaped gradients compatible with Proximal Policy Optimization (PPO). We instantiate\
    \ the approach on Google's Barkour quadruped robot in MuJoCo XLA (MJX). We use\
    \ parallelization within the simulator to improve training speeds and use domain\
    \ randomization to robustify learned policies. We show that compared to a baseline\
    \ of hand-crafted rewards, the STL-shaped rewards yield tighter velocity tracking\
    \ and more stable training. Videos can be found on our project website: https://stl-locomotion.github.io/."
  ko: "arXiv:2607.00442v1 Announce Type: new \nAbstract: Reinforcement learning (RL)\
    \ for quadruped locomotion commonly depends on fixed, hand-crafted, and Markovian\
    \ reward functions that limit both interpretability of learned policies and lack\
    \ explicit control over gait behaviors. We introduce a framework where distinct\
    \ gaits are specified using parameterized constraints expressed in Signal Temporal\
    \ Logic (STL). These include safety bounds, gait synchronization constraints,\
    \ command tracking, and actuation bounds. From these specifications, we develop\
    \ a reward shaping mechanism that provides learning agents a dense, continuous\
    \ reward landscape that encodes desired behavior. We define parametric STL templates\
    \ for three speed regimes (walking-trot, trot, bound), calibrate their parameters\
    \ from reference rollouts, and compute rewards from using smooth approximations\
    \ of STL robustness over the rollouts. The generated rewards can be used to provide\
    \ shaped gradients compatible with Proximal Policy Optimization (PPO). We instantiate\
    \ the approach on Google's Barkour quadruped robot in MuJoCo XLA (MJX). We use\
    \ parallelization within the simulator to improve training speeds and use domain\
    \ randomization to robustify learned policies. We show that compared to a baseline\
    \ of hand-crafted rewards, the STL-shaped rewards yield tighter velocity tracking\
    \ and more stable training. Videos can be found on our project website: https://stl-locomotion.github.io/."
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
- robotics
- learning_gait_aware_quadruped
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-03'
  confidence: medium
  notes: Imported via ingestion framework from source_type=paper.
sources:
- id: src_001
  type: paper
  title: Learning Gait-Aware Quadruped Locomotion with Temporal Logic Specifications
    (arXiv)
  url: https://arxiv.org/abs/2607.00442
  date: '2026'
  accessed_at: '2026-07-03'
---

## 概述
arXiv:2607.00442v1 Announce Type: new 
Abstract: Reinforcement learning (RL) for quadruped locomotion commonly depends on fixed, hand-crafted, and Markovian reward functions that limit both interpretability of learned policies and lack explicit control over gait behaviors. We introduce a framework where distinct gaits are specified using parameterized constraints expressed in Signal Temporal Logic (STL). These include safety bounds, gait synchronization constraints, command tracking, and actuation bounds. From these specifications, we develop a reward shaping mechanism that provides learning agents a dense, continuous reward landscape that encodes desired behavior. We define parametric STL templates for three speed regimes (walking-trot, trot, bound), calibrate their parameters from reference rollouts, and compute rewards from using smooth approximations of STL robustness over the rollouts. The generated rewards can be used to provide shaped gradients compatible with Proximal Policy Optimization (PPO). We instantiate the approach on Google's Barkour quadruped robot in MuJoCo XLA (MJX). We use parallelization within the simulator to improve training speeds and use domain randomization to robustify learned policies. We show that compared to a baseline of hand-crafted rewards, the STL-shaped rewards yield tighter velocity tracking and more stable training. Videos can be found on our project website: https://stl-locomotion.github.io/.

## Overview
arXiv:2607.00442v1 Announce Type: new 
Abstract: Reinforcement learning (RL) for quadruped locomotion commonly depends on fixed, hand-crafted, and Markovian reward functions that limit both interpretability of learned policies and lack explicit control over gait behaviors. We introduce a framework where distinct gaits are specified using parameterized constraints expressed in Signal Temporal Logic (STL). These include safety bounds, gait synchronization constraints, command tracking, and actuation bounds. From these specifications, we develop a reward shaping mechanism that provides learning agents a dense, continuous reward landscape that encodes desired behavior. We define parametric STL templates for three speed regimes (walking-trot, trot, bound), calibrate their parameters from reference rollouts, and compute rewards from using smooth approximations of STL robustness over the rollouts. The generated rewards can be used to provide shaped gradients compatible with Proximal Policy Optimization (PPO). We instantiate the approach on Google's Barkour quadruped robot in MuJoCo XLA (MJX). We use parallelization within the simulator to improve training speeds and use domain randomization to robustify learned policies. We show that compared to a baseline of hand-crafted rewards, the STL-shaped rewards yield tighter velocity tracking and more stable training. Videos can be found on our project website: https://stl-locomotion.github.io/.

## 개요
arXiv:2607.00442v1 Announce Type: new 
Abstract: Reinforcement learning (RL) for quadruped locomotion commonly depends on fixed, hand-crafted, and Markovian reward functions that limit both interpretability of learned policies and lack explicit control over gait behaviors. We introduce a framework where distinct gaits are specified using parameterized constraints expressed in Signal Temporal Logic (STL). These include safety bounds, gait synchronization constraints, command tracking, and actuation bounds. From these specifications, we develop a reward shaping mechanism that provides learning agents a dense, continuous reward landscape that encodes desired behavior. We define parametric STL templates for three speed regimes (walking-trot, trot, bound), calibrate their parameters from reference rollouts, and compute rewards from using smooth approximations of STL robustness over the rollouts. The generated rewards can be used to provide shaped gradients compatible with Proximal Policy Optimization (PPO). We instantiate the approach on Google's Barkour quadruped robot in MuJoCo XLA (MJX). We use parallelization within the simulator to improve training speeds and use domain randomization to robustify learned policies. We show that compared to a baseline of hand-crafted rewards, the STL-shaped rewards yield tighter velocity tracking and more stable training. Videos can be found on our project website: https://stl-locomotion.github.io/.
