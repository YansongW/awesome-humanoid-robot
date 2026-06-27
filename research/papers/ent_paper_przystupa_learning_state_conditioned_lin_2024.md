---
$id: ent_paper_przystupa_learning_state_conditioned_lin_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning State Conditioned Linear Mappings for Low-Dimensional Control of Robotic
    Manipulators
  zh: 学习状态条件线性映射用于机械臂低维控制
  ko: 로봇 매니퓰레이터의 저차원 제어를 위한 상태 조건부 선형 매핑 학습
summary:
  en: This paper proposes State Conditioned Linear Maps (SCL maps), a method that
    uses neural networks to predict a state-dependent linear basis for controlling
    high-DOF robotic manipulators with low-DOF inputs, and validates it through user
    studies on a Kinova Gen-3 lite arm.
  zh: 本文提出状态条件线性映射（SCL映射），利用神经网络预测状态相关的线性基，以低自由度输入控制高自由度机械臂，并在Kinova Gen-3 lite机械臂上通过用户研究验证。
  ko: 본 논문은 신경망을 사용하여 상태 의존적 선형 기저를 예측하고 저자유도 입력으로 고자유도 로봇 매니퓰레이터를 제어하는 상태 조건부 선형
    매핑(SCL maps)을 제안하고 Kinova Gen-3 lite 매니퓰레이터를 통한 사용자 연구로 검증한다.
domains:
- 07_ai_models_algorithms
- 02_components
- 11_applications_markets
layers:
- intelligence
- upstream
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- state_conditioned_linear_maps
- teleoperation
- low_dimensional_control
- manipulator_control
- dimensionality_reduction
- kinova_gen3_lite
- humanoid_arms
- robot_learning
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from provided metadata; requires human review of the full arXiv
    text before verification.
sources:
- id: src_001
  type: paper
  title: Learning State Conditioned Linear Mappings for Low-Dimensional Control of
    Robotic Manipulators
  url: https://arxiv.org/abs/2410.21441
  date: '2024'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## Overview

The paper addresses the challenge of controlling high-degree-of-freedom (DOF) robotic manipulators using low-dimensional user inputs without sacrificing analytical tractability. It introduces State Conditioned Linear Maps (SCL maps), in which a neural network predicts a state-dependent matrix that linearly maps a low-DOF action space to high-DOF joint velocities. This combines the simplicity of linear mappings with the flexibility of nonlinear, state-dependent representations. The authors formulate a soft reversibility property for action mappings and prove that SCL maps satisfy this property by construction, although the proof assumes the mapping without the deployed Gram-Schmidt orthonormalization step.

Training proceeds as an autoencoding objective, with the neural network output constrained by a Gram-Schmidt orthonormalization step and Lipschitz continuity enforcement. Empirical validation is performed on a Kinova Gen-3 lite 7-DOF manipulator in two teleoperation user studies: a pick-and-place task and a more complex pouring task. Results show that SCL maps outperform conditional autoencoder and PCA baselines on pick-and-place and perform comparably to mode switching during pouring.

## Key Contributions

- Proposed State Conditioned Linear Maps (SCL maps) that combine local linearity with state-dependent neural-network bases.
- Formulated and proved a soft reversibility property for SCL maps by design.
- Empirically validated proportionality and soft reversibility on a Kinova Gen-3 lite manipulator.
- Demonstrated in two teleoperation user studies that SCL maps outperform PCA and conditional autoencoder baselines and are competitive with mode switching.

## Relevance to Humanoid Robotics

The method is directly relevant to humanoid robotics because it enables intuitive low-DOF control of high-DOF arms and hands, a central requirement for teleoperation and motion generation in humanoid systems. Humanoid robots typically possess many actuated joints, making direct joystick or wearable-device control challenging; SCL maps provide a learned, state-dependent linear basis that can map few user commands to many joint velocities. While the paper evaluates only a fixed-base 7-DOF arm, the underlying formalism can generalize to humanoid arms, dexterous hands, and whole-body manipulation tasks during development, testing, and deployment.
