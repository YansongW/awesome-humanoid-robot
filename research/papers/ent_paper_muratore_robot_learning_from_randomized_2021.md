---
$id: ent_paper_muratore_robot_learning_from_randomized_2021
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Robot Learning from Randomized Simulations: A Review'
  zh: 基于随机化仿真的机器人学习：综述
  ko: '랜덤화된 시뮬레이션에서의 로봇 학습: 리뷰'
summary:
  en: A comprehensive review of sim-to-real transfer for robotics that focuses on
    domain randomization and categorizes current methods into static, adaptive, and
    adversarial approaches.
  zh: 一篇关于机器人仿真到现实迁移的综合综述，重点讨论域随机化，并将现有方法分为静态、自适应和对抗性三类。
  ko: 로보틱스를 위한 시뮬레이션에서 현실로의 전이에 대한 종합적인 리뷰로, 도메인 랜덤화에 중점을 두고 방법들을 정적, 적응적, 대抗性 접근으로
    분류한다.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- sim_to_real
- domain_randomization
- reinforcement_learning
- robot_learning
- physics_simulation
- policy_transfer
- sim2real
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-01'
  confidence: medium
  notes: AI-extracted from provided metadata and abstract; requires human review against
    the full paper before verification.
sources:
- id: src_001
  type: paper
  title: 'Robot Learning from Randomized Simulations: A Review'
  url: https://arxiv.org/abs/2111.00956
  date: '2021'
  accessed_at: '2026-07-01'
theoretical_depth:
- method
---

## Overview

This paper provides a comprehensive review of sim-to-real research for robotics, with a primary focus on domain randomization. The authors frame the central challenge as the "reality gap": the mismatch between simulation and physical reality caused by the fact that all simulators are imperfect model-based approximations. They argue that deep learning methods' appetite for large datasets makes simulation an essential training substrate, and that deliberately randomizing simulation parameters can produce policies robust enough to transfer to real robots.

The review introduces the mathematical fundamentals of sim-to-real transfer using Markov decision process and reinforcement learning formulations. It then covers foundational topics such as early sim-to-real methods, parametric simulators, design choices for randomization, and measures of transferability. Building on this foundation, the authors propose a taxonomy that divides domain randomization into static, adaptive, and adversarial methods. The paper also connects sim-to-real transfer to neighboring fields, including curriculum learning, meta-learning, transfer learning, knowledge distillation, and system identification, and concludes with a discussion of future research directions.

## Key Contributions

- Introduces the mathematical fundamentals of sim-to-real transfer using MDP and reinforcement learning formulations.
- Reviews foundational topics including early methods, parametric simulators, randomization design choices, and measures of transferability.
- Proposes a taxonomy that categorizes domain randomization into static, adaptive, and adversarial methods.
- Discusses connections between sim-to-real transfer and related fields such as curriculum learning, meta-learning, transfer learning, knowledge distillation, and system identification.
- Outlines future research directions including real-to-sim-to-real transfer, policy architectures with inductive biases, and dual control via likelihood-free inference.

## Relevance to Humanoid Robotics

The paper is highly relevant to humanoid robotics because humanoid systems are expensive, fragile, and data-hungry, making purely real-world training impractical at scale. The surveyed domain randomization and sim-to-real transfer techniques enable control policies for bipedal locomotion and manipulation to be learned cheaply in simulation and then transferred to physical hardware. This training paradigm is critical for scalable development, mass production, and deployment of humanoid robots. The review's coverage of physics engines, randomization strategies, and transferability metrics provides a methodological map that directly supports humanoid control-policy engineering.

## References

- [Robot Learning from Randomized Simulations: A Review](https://arxiv.org/abs/2111.00956) (accessed 2026-07-01)
