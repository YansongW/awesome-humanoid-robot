---
$id: ent_paper_ai_towards_embodiment_scaling_law_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Towards Embodiment Scaling Laws in Robot Locomotion
  zh: 机器人运动中的具身规模定律研究
  ko: 로봇 보행에서의 구현체 스케일링 법칙을 향하여
summary:
  en: Investigates embodiment scaling laws by training a single URMA policy on approximately
    1,000 procedurally generated robot morphologies (GENBOT-1K), demonstrating zero-shot
    transfer to unseen simulated and real robots including the Unitree Go2 and H1.
  zh: 通过在大约1000个程序生成的机器人形态（GENBOT-1K）上训练单一URMA策略，研究具身规模定律，并展示对包括宇树Go2和H1在内的全新仿真与真实机器人的零样本迁移。
  ko: 약 1,000개의 절차적 생성 로봇 형태(GENBOT-1K)로 단일 URMA 정책을 훈련하여 구현체 스케일링 법칙을 연구하고, Unitree
    Go2 및 H1을 포함한 새로운 시뮬레이션 및 실제 로봇으로의 제로샷 전이를 보인다.
domains:
- 07_ai_models_algorithms
- 09_data_datasets
- 10_evaluation_benchmarks
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- cross_embodiment_generalization
- embodiment_scaling_laws
- locomotion
- reinforcement_learning
- behavior_cloning
- sim_to_real
- urma
- genbot_1k
- procedural_generation
- unitree_h1
- unitree_go2
- robot_morphology
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from provided metadata and abstract; full-paper verification
    and human review are required before promotion to verified status.
sources:
- id: src_001
  type: paper
  title: Towards Embodiment Scaling Laws in Robot Locomotion
  url: https://arxiv.org/abs/2505.05753
  date: '2025'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## Overview

This paper studies embodiment scaling laws—the hypothesis that increasing the number and diversity of training robot embodiments improves generalization to unseen morphologies—using robot locomotion as a test bed. The authors procedurally generate GENBOT-1K, a dataset of approximately 1,000 robot embodiments spanning humanoid, quadruped, and hexapod classes with topological, geometric, and joint-level kinematic variations. They train single-embodiment reinforcement-learning experts with Proximal Policy Optimization (PPO) and distill these experts into a single embodiment-aware Unified Robot Morphology Attention (URMA) policy via behavior cloning, scaling the architecture with multi-head attention.

Empirically, the authors observe positive scaling trends: policies trained on larger and more diverse sets of embodiments generalize better to novel morphologies than policies trained on fewer embodiments. They further find that embodiment scaling enables substantially broader generalization than simply scaling the amount of training data on a fixed set of embodiments. The best policy, trained on the full GENBOT-1K dataset, transfers zero-shot to novel embodiments in both simulation and the real world, including the Unitree Go2 quadruped and the Unitree H1 humanoid, even when joint constraints are modified.

The results are framed as a step toward general embodied intelligence, with downstream relevance to adaptive control for configurable robots, morphology co-design, and the development of scalable generalist locomotion controllers.

## Key Contributions

- Conceptualize and empirically validate embodiment scaling laws in robot locomotion.
- Introduce GENBOT-1K, a procedurally generated dataset of approximately 1,000 diverse humanoid, quadruped, and hexapod embodiments.
- Extend URMA with multi-head attention and a two-stage RL-plus-behavior-cloning pipeline to scale to approximately 1,000 embodiments.
- Demonstrate zero-shot sim-to-real transfer to Unitree Go2 and H1, including modified joint constraints.
- Show that scaling embodiments outperforms pure data scaling on fixed embodiments for broad generalization.

## Relevance to Humanoid Robotics

The work is directly relevant to humanoid robotics because it demonstrates that a single policy, trained on a large and diverse set of simulated morphologies, can zero-shot control the Unitree H1 humanoid in the real world. This suggests a path toward scalable generalist controllers that reduce the need for per-humanoid engineering during mass production and deployment. If embodiment scaling laws continue to hold at larger scales, future humanoid platforms could leverage shared, morphology-conditioned policies rather than requiring bespoke controllers for each design.
