---
$id: ent_paper_radosavovic_learning_humanoid_locomotion_o_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning Humanoid Locomotion over Challenging Terrain
  zh: 挑战性地形上的人形机器人运动学习
  ko: 어려운 지형에서의 휴머노이드 보행 학습
summary:
  en: Presents a transformer-based blind locomotion controller for the Digit humanoid
    robot, pre-trained with sequence modeling on flat-ground trajectories and fine-tuned
    with reinforcement learning on uneven terrain, enabling zero-shot sim-to-real
    traversal of natural and urban environments.
  zh: 提出一种基于Transformer的Digit人形机器人盲态运动控制器，先通过序列建模在平地轨迹上预训练，再通过强化学习在不平坦地形上微调，实现从仿真到现实的零样本迁移，跨越自然与城市环境。
  ko: Digit 휴머노이드 로봇을 위한 Transformer 기반의 시각 정보 없는 보행 컨트롤러를 제안한다. 평지 궤적에 대한 시퀀스 모델링으로
    사전 학습하고 불규칙한 지형에 대해 강화 학습으로 미세 조정하여, 시뮬레이션에서 현실로의 제로샷 전이를 통해 자연 및 도시 환경을 주행할 수
    있게 한다.
domains:
- 07_ai_models_algorithms
- 11_applications_markets
- 02_components
layers:
- intelligence
- upstream
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- humanoid_locomotion
- blind_locomotion
- transformer
- sequence_modeling
- reinforcement_learning
- sim_to_real
- digit_robot
- agility_robotics
- terrain_traversal
- domain_randomization
- outdoor_navigation
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-28'
  confidence: medium
  notes: AI-extracted from the supplied abstract and metadata; quantitative claims
    and dataset usage should be cross-checked against the full paper.
sources:
- id: src_001
  type: paper
  title: Learning Humanoid Locomotion over Challenging Terrain
  url: https://arxiv.org/abs/2410.03654
  date: '2024'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
---

## Overview

This paper addresses the challenge of deploying humanoid robots on difficult real-world terrain. It proposes a fully learning-based, blind locomotion controller that uses only proprioceptive history (joint positions, joint velocities, and IMU data) to decide actions. A causal transformer is first pre-trained on a large corpus of flat-ground walking trajectories using sequence modeling, then fine-tuned on procedurally generated uneven terrain with reinforcement learning. The resulting policy transfers zero-shot from MuJoCo simulation to a physical Digit robot.

The two-stage training recipe is central to the approach. Sequence modeling on diverse prior trajectories—including outputs from model-based controllers, prior learned policies, and human motion capture—provides a strong prior for natural locomotion. Reinforcement-learning fine-tuning on rough, sloped, and varied terrain then adapts this prior to challenging conditions while retaining sample efficiency.

Real-world evaluation spans multiple natural and man-made environments, including hiking trails in Berkeley and steep streets in San Francisco. The authors report robust traversal over rough, deformable, wet, muddy, and sandy surfaces, and observe emergent capabilities such as in-context slope adaptation and unsupervised terrain clustering in the transformer’s latent representations.

## Key Contributions

- A single transformer-based neural network controller for blind humanoid locomotion over steep, rough, rutted, rocky, wet, muddy, and sandy terrain.
- A two-stage training recipe that combines sequence-modeling pre-training on flat-ground trajectories with reinforcement-learning fine-tuning on challenging terrains, improving sample efficiency and final performance over training from scratch.
- Real-world validation on a Digit robot, including over 4 miles of hiking trails in Berkeley and traversal of 31%-grade streets in San Francisco.
- Empirical evidence of emergent behavior: unsupervised terrain clustering in latent space, in-context kinematic adaptation to slope, and dynamic adaptation to terrain material.
- Systematic comparisons and ablations demonstrating that pre-training improves sample efficiency and that fine-tuning substantially outperforms both the pre-trained and from-scratch policies.

## Relevance to Humanoid Robotics

The work is directly relevant to humanoid robotics because it demonstrates a scalable learned locomotion stack that operates outside controlled laboratory environments. By enabling a real humanoid robot to walk over unstructured outdoor and urban terrain, it addresses a key capability gap for deployment in logistics, inspection, and personal assistance scenarios.
