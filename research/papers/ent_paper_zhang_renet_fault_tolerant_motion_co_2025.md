---
$id: ent_paper_zhang_renet_fault_tolerant_motion_co_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RENet: Fault-Tolerant Motion Control for Quadruped Robots via Redundant Estimator
    Networks under Visual Collapse'
  zh: RENet：视觉崩溃下基于冗余估计器网络的四足机器人容错运动控制
  ko: 'RENet: 시각 붕괴 하에서 중복 추정기 네트워크를 통한 사족 로봇의 결허용 운동 제어'
summary:
  en: This paper proposes RENet, a single-stage end-to-end framework that trains a
    vision-plus-proprioception estimator and a proprioception-only estimator jointly
    with a low-level policy, and switches between them online using a CNN autoencoder
    anomaly detector when depth images become unreliable. Real-world outdoor experiments
    on a Unitree GO1 robot demonstrate direct sim-to-real transfer without fine-tuning.
  zh: 本文提出RENet，一种单阶段端到端框架，联合训练视觉-本体感知估计器与纯本体感知估计器及底层策略，并通过CNN自编码器异常检测器在深度图像不可靠时在线切换估计器。在Unitree
    GO1机器人上的真实室外实验验证了无需微调的直接仿真到现实迁移。
  ko: 본 논문은 시각-고유수용성 추정기와 고유수용성 전용 추정기를 저수준 정책과 함께 단일 단계로 종단간 학습하고, 깊이 이미지가 불안정해질
    때 CNN 오토인코더 이상 탐지기를 통해 온라인으로 전환하는 RENet을 제안한다. Unitree GO1 로봇을 이용한 실제 야외 실험에서
    미세 조정 없는 시뮬레이션-현실 직접 전이를 검증하였다.
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
- vision_based_locomotion
- quadruped_robot
- state_estimation
- sensor_fusion
- fault_tolerance
- sim_to_real
- reinforcement_learning
- depth_perception
- humanoid_transfer
- outdoor_navigation
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from supplied metadata and abstract; full-text review needed
    to confirm section-level citations and exact technical claims before verification.
sources:
- id: src_001
  type: paper
  title: 'RENet: Fault-Tolerant Motion Control for Quadruped Robots via Redundant
    Estimator Networks under Visual Collapse'
  url: https://arxiv.org/abs/2509.09283
  date: '2025'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## Overview

RENet addresses the problem of vision-based quadruped locomotion in outdoor environments, where depth sensor noise and vision failures can degrade state estimation and destabilize the controller. The framework employs a dual-estimator architecture: one estimator fuses vision and proprioception, while the second relies solely on proprioception. Both estimators are trained jointly with the low-level locomotion policy in a single end-to-end stage. During deployment, an anomaly detector monitors the depth image stream and triggers an online switch to the proprioceptive estimator when visual input becomes unreliable.

The online adaptation mechanism is built around a CNN autoencoder that reconstructs depth images and a low-pass filtered selector that decides which estimator to trust. This design avoids abrupt switching and maintains deployment stability under visual collapse. The authors report direct sim-to-real transfer without additional real-world fine-tuning, and they validate the approach in complex outdoor scenarios including degraded visual perception.

The paper situates its contribution as a practical solution for reliable robotic deployment in challenging field conditions. Although the experiments focus on a quadruped platform, the authors explicitly identify humanoid robots as a future target for the redundant estimator architecture, because robust state estimation under sensor degradation is equally critical for bipedal systems operating in unstructured environments.

## Key Contributions

- Single-stage end-to-end training framework that fuses vision and proprioception for fault-tolerant quadruped locomotion with online estimator adaptation.
- Self-adaptive estimator switching mechanism that detects depth sensor noise and automatically selects the appropriate estimator.
- Direct sim-to-real transfer validated by extensive outdoor experiments on a real robot without fine-tuning.

## Relevance to Humanoid Robotics

The redundant estimator architecture and automatic vision-failure switching mechanism are directly transferable to humanoid robots. In unstructured environments, humanoids must maintain reliable state estimation despite sensor degradation, making fault-tolerant estimation a prerequisite for safe mass deployment.

The authors explicitly identify humanoids as a future target for this framework, noting that applicability to humanoids with more intricate structures remains to be explored. This indicates a recognized but not yet validated extension path from quadruped to humanoid systems.
