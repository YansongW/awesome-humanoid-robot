---
$id: ent_paper_jeong_your_vision_language_action_mo_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Your Vision-Language-Action Model Already Has Attention Heads For Path Deviation
    Detection
  zh: 你的视觉-语言-动作模型已具备路径偏离检测的注意力头
  ko: 당신의 비전-언어-액션 모델에는 이미 경로 편차 탐지를 위한 어텐션 헤드가 있다
summary:
  en: This paper identifies sparse 'Navigation Heads' in a frozen Vision-Language-Action
    model whose attention-entropy signals indicate trajectory deviations, enabling
    a training-free anomaly detector and lightweight RL rollback for navigation. It
    reports a 44.6% deviation-detection rate with an 11.7% false-positive rate on
    VLN-CE R2R and RxR, and validates the full detection-to-recovery pipeline on an
    AgileX Scout 2.0 mobile robot.
  zh: 本文在冻结的视觉-语言-动作模型中识别出稀疏的“导航头”，其注意力熵信号可指示轨迹偏离，从而实现了无需训练的异常检测器和轻量强化学习回退机制。在VLN-CE
    R2R与RxR上达到44.6%的偏离检测率和11.7%的误检率，并在AgileX Scout 2.0移动机器人上验证了完整的检测-恢复流程。
  ko: 본 논문은 고정된 비전-언어-액션(VLA) 모델 내 어텐션 엔트로피 신호가 궤적 편차를 나타내는 소수의 '네비게이션 헤드(Navigation
    Heads)'를 식별하여, 학습 불필요 이상 탐지기와 경량 RL 롤백을 제안한다. VLN-CE R2R 및 RxR에서 44.6%의 편차 탐지율과
    11.7%의 오탐률을 보였으며, AgileX Scout 2.0 이동 로봇에서 탐지-회복 파이프라인을 검증했다.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
- 11_applications_markets
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- vla
- vision_language_action
- navigation_heads
- attention_entropy
- hallucination_detection
- anomaly_detection
- reinforcement_learning
- robot_navigation
- vln_ce
- r2r
- rxr
- navila
- ros2
- mobile_robot
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-26'
  confidence: medium
  notes: AI-extracted from arXiv abstract and supplied metadata; requires human review
    against the full PDF before final verification.
sources:
- id: src_001
  type: paper
  title: Your Vision-Language-Action Model Already Has Attention Heads For Path Deviation
    Detection
  url: https://arxiv.org/abs/2603.13782
  date: '2026'
  accessed_at: '2026-06-26'
---


## Overview

Vision-Language-Action (VLA) models can predict semantic actions from language instructions and visual observations, but they are prone to visual-reasoning hallucinations that cause the robot to leave the intended path. The authors address this by showing that a small, sparse set of internal attention heads in a frozen VLA already encodes spatiotemporal causality between historical visual sequences and linguistic instructions. They name these heads Navigation Heads (Hnav) and use their attention-entropy signals as a training-free, real-time anomaly detector.

The detector monitors only three heads out of more than a thousand and reports a 44.6% path-deviation detection rate with an 11.7% false-positive rate on the VLN-CE R2R and RxR navigation benchmarks. When a deviation is detected, the heavy VLA model is bypassed and a lightweight Reinforcement Learning (RL) policy takes over to execute collision-free obstacle avoidance and a shortest-path rollback to the last safe state.

The complete detection-to-recovery pipeline is implemented on an AgileX Scout 2.0 mobile robot equipped with an NVIDIA Jetson AGX Orin, a ZED 2i stereo camera, a RoboSense Helios RS-32 LiDAR, and an IMU, integrated through ROS 2. This demonstrates that the approach can run with near-zero extra computation and recover from real-world deviations on a physical platform.

## Key Contributions

- Discovery of Navigation Heads (Hnav), a sparse set of attention heads in a frozen VLA that encode spatiotemporal alignment between visual observations and navigation instructions.
- Training-free, real-time anomaly-detection framework that monitors the entropy of only three heads with near-zero computational overhead.
- Integration of the detection signal with a lightweight RL low-level controller for collision-free obstacle avoidance and shortest-path rollback.
- Validation on a physical mobile robot through ROS 2, including real-world path-deviation detection and recovery.

## Relevance to Humanoid Robotics

Although the experiments are performed on a wheeled mobile robot, the core finding is directly relevant to humanoid robotics. Future humanoids will increasingly rely on VLA models for natural-language instruction following in unstructured environments, where hallucination-induced deviations are a critical reliability risk. The ability to detect these deviations from the model's own attention heads—without extra training or compute—provides a built-in safety signal.

When paired with a fast low-level recovery policy, this mechanism can improve deployment reliability of humanoid systems without increasing inference cost. However, generalization to humanoid embodiments and other VLA architectures remains to be validated, as the current study evaluates a single backbone (NaVILA) in a mobile navigation domain.
