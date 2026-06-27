---
$id: ent_paper_liu_dexrepnet_learning_dexterous_r_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'DexRepNet++: Learning Dexterous Robotic Manipulation with Geometric and Spatial
    Hand-Object Representations'
  zh: DexRepNet++：基于几何与空间手-物表征学习灵巧机器人操作
  ko: 'DexRepNet++: 기하학적 및 공간적 손-물체 표현을 활용한 능숙한 로봇 조작 학습'
summary:
  en: This paper proposes DexRep, a structured hand-object interaction representation
    that fuses occupancy, surface, and local-geometry features, and integrates it
    with deep reinforcement learning to achieve generalizable dexterous grasping,
    in-hand reorientation, and bimanual handover with real-world sim-to-real transfer.
  zh: 本文提出DexRep，一种将占用、表面和局部几何特征融合的结构化手-物交互表征，并将其与深度强化学习结合，以实现可泛化的灵巧抓取、手中重定向和双手递接，且具有真实世界的仿真到现实迁移能力。
  ko: 본 논문은 점유, 표면 및 국부 기하 특징을 융합한 구조화된 손-물체 상호작용 표현인 DexRep을 제안하고, 이를 심층 강화학습과 통합하여
    일반화 가능한 능숙한 파지, 손 내 재배향, 양손 전달을 실현하고 실제 환경으로의 시뮬레이션-투-리얼 전이를 보여준다.
domains:
- 07_ai_models_algorithms
- 02_components
layers:
- intelligence
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- dexterous_manipulation
- hand_object_representation
- reinforcement_learning
- sim_to_real
- point_cloud
- multi_fingered_hand
- bimanual_handover
- in_hand_reorientation
- grasping
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from metadata and abstract; full-text review is required before
    final verification.
sources:
- id: src_001
  type: paper
  title: 'DexRepNet++: Learning Dexterous Robotic Manipulation with Geometric and
    Spatial Hand-Object Representations'
  url: https://arxiv.org/abs/2602.21811
  date: '2026'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
related_entities:
- id: ent_component_allegro_hand
  relationship: evaluates_on
  description:
    en: Deploys real-world grasp policies on an Allegro Hand.
    zh: 在Allegro Hand上部署真实世界抓取策略。
    ko: Allegro Hand에 실제 환경 파지 정책을 배포함.
---

## Overview

Dexterous robotic manipulation remains difficult because high-DoF multi-fingered hands generate complex, contact-rich interactions that are hard to represent compactly. This paper introduces DexRep, a structured hand-object interaction representation that combines a coarse occupancy feature, a fine-grained surface feature, and a local-geometry feature. DexRep captures object surface properties and spatial relations between hands and objects, and is fed into deep reinforcement-learning policies to learn grasping, in-hand reorientation, and bimanual handover.

The authors train grasp policies with 40 objects and report an 87.9% success rate on more than 5,000 unseen objects spanning diverse categories, outperforming prior work that used thousands of training objects. For in-hand reorientation and handover, policies using DexRep improve success rates and related metrics by 20% to 40% over existing hand-object representations. The learned grasp policies are transferred to a real robot composed of an Allegro Hand, a Unitree Z1 arm, and Azure Kinect DK cameras under both multi-camera and single-camera setups, demonstrating a small sim-to-real gap.

## Key Contributions

- A compact, structured DexRep representation that fuses coarse global occupancy with fine-grained local surface geometry and hand-object spatial relations.
- Strong generalization across grasping, in-hand reorientation, and bimanual handover, including transfer to unseen objects and across 2- to 5-finger hand morphologies.
- Real-world deployment on an Allegro Hand + Unitree Z1 arm + Azure Kinect system with a small sim-to-real gap under both multi-view and single-view partial observations.
- Extensive ablation and analysis of feature components, pretraining data scale, partial point-cloud robustness, multi-hand morphology, friction, and hyperparameter sensitivity.

## Relevance to Humanoid Robotics

Dexterous hands are a primary end-effector for humanoid robots, and reliable grasping, in-hand manipulation, and bimanual handover are prerequisites for useful operation in unstructured environments. DexRep addresses a key bottleneck in these skills by providing a compact, generalizable representation of hand-object interaction that can be learned from point-cloud observations and transferred to real hardware. The demonstrated sim-to-real transfer on a multi-fingered hand mounted on a robotic arm directly supports the development of robust manipulation capabilities for humanoid platforms.
