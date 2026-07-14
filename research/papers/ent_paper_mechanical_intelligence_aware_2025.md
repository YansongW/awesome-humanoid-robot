---
$id: ent_paper_mechanical_intelligence_aware_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Mechanical Intelligence-Aware Curriculum RL for Humanoids with Parallel Actuation
  zh: Mechanical Intelligence-Aware Curriculum RL for Humanoids with Parallel Actuation
  ko: Mechanical Intelligence-Aware Curriculum RL for Humanoids with Parallel Actuation
summary:
  en: Mechanical Intelligence-Aware Curriculum RL for Humanoids with Parallel Actuation is a 2025 work on locomotion for humanoid
    robots.
  zh: Mechanical Intelligence-Aware Curriculum RL for Humanoids with Parallel Actuation is a 2025 work on locomotion for humanoid
    robots.
  ko: Mechanical Intelligence-Aware Curriculum RL for Humanoids with Parallel Actuation is a 2025 work on locomotion for humanoid
    robots.
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
- mechanical_intelligence_aware
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2507.00273v3.
sources:
- id: src_001
  type: paper
  title: Mechanical Intelligence-Aware Curriculum RL for Humanoids with Parallel Actuation (arXiv)
  url: https://arxiv.org/abs/2507.00273
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Reinforcement learning (RL) has enabled advances in humanoid robot locomotion, yet most learning frameworks do not account for mechanical intelligence embedded in parallel actuation mechanisms due to limitations in simulator support for closed kinematic chains. This omission can lead to inaccurate motion modeling and suboptimal policies, particularly for robots with high actuation complexity. This paper presents general formulations and simulation methods for three types of parallel mechanisms: a differential pulley, a five-bar linkage, and a four-bar linkage, and trains a parallel-mechanism aware policy through an end-to-end curriculum RL framework for BRUCE, a kid-sized humanoid robot. Unlike prior approaches that rely on simplified serial approximations, we simulate all closed-chain constraints natively using GPU-accelerated MuJoCo (MJX), preserving the hardware's mechanical nonlinear properties during training. We benchmark our RL approach against a model predictive controller (MPC), demonstrating better surface generalization and performance in real-world zero-shot deployment. This work highlights the computational approaches and performance benefits of fully simulating parallel mechanisms in end-to-end learning pipelines for legged humanoids. Project codes with parallel mechanisms: https://github.com/alvister88/og_bruce

## 核心内容
Reinforcement learning (RL) has enabled advances in humanoid robot locomotion, yet most learning frameworks do not account for mechanical intelligence embedded in parallel actuation mechanisms due to limitations in simulator support for closed kinematic chains. This omission can lead to inaccurate motion modeling and suboptimal policies, particularly for robots with high actuation complexity. This paper presents general formulations and simulation methods for three types of parallel mechanisms: a differential pulley, a five-bar linkage, and a four-bar linkage, and trains a parallel-mechanism aware policy through an end-to-end curriculum RL framework for BRUCE, a kid-sized humanoid robot. Unlike prior approaches that rely on simplified serial approximations, we simulate all closed-chain constraints natively using GPU-accelerated MuJoCo (MJX), preserving the hardware's mechanical nonlinear properties during training. We benchmark our RL approach against a model predictive controller (MPC), demonstrating better surface generalization and performance in real-world zero-shot deployment. This work highlights the computational approaches and performance benefits of fully simulating parallel mechanisms in end-to-end learning pipelines for legged humanoids. Project codes with parallel mechanisms: https://github.com/alvister88/og_bruce

## 参考
- http://arxiv.org/abs/2507.00273v3

