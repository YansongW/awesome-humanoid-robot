---
$id: ent_paper_lee_learning_quadrupedal_locomotio_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning Quadrupedal Locomotion for a Heavy Hydraulic Robot Using an Actuator
    Model
  zh: 基于执行器模型的大型液压四足机器人运动学习
  ko: 액추에이터 모델을 활용한 대형 유압 사족 보행 로봇의 보행 학습
summary:
  en: This paper presents an analytical hydraulic actuator model that predicts joint
    torques for 12 actuators in under one microsecond, enabling reinforcement-learning
    training of a locomotion policy for a hydraulic quadruped robot weighing over
    300 kg. The trained policy is transferred to hardware, achieving stable, command-tracking
    locomotion at 1 m/s and outperforming neural-network actuator models in data-limited
    and out-of-distribution settings.
  zh: 本文提出了一种解析液压执行器模型，可在不到1微秒内预测12个执行器的关节扭矩，从而为超过300公斤的液压四足机器人训练强化学习运动策略。训练的策略被迁移到实体硬件，实现了1米/秒的稳定指令跟踪运动，并在数据有限和分布外场景中优于神经网络执行器模型。
  ko: 본 논문은 12개의 액추에이터에 대한 관절 토크를 1마이크로초 이내에 예측하는 해석적 유압 액추에이터 모델을 제안하여 300kg이 넘는
    유압 사족 보행 로봇의 강화학습 보행 정책 학습을 가능하게 한다. 학습된 정책은 하드웨어로 이전되어 1m/s의 안정적인 명령 추종 보행을 달성했으며,
    데이터가 제한되거나 분포 외 시나리오에서 신경망 기반 액추에이터 모델보다 우수한 성능을 보였다.
domains:
- 02_components
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
- upstream
functional_roles:
- knowledge
- intelligence
- system
tags:
- hydraulic_actuator
- sim_to_real
- reinforcement_learning
- quadruped_locomotion
- heavy_robot
- actuator_model
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from provided metadata and abstract; full-text review is required
    before final verification.
sources:
- id: src_001
  type: paper
  title: Learning Quadrupedal Locomotion for a Heavy Hydraulic Robot Using an Actuator
    Model
  url: https://arxiv.org/abs/2601.11143
  date: '2026'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## Overview

Large-scale hydraulic robots are difficult to simulate accurately for reinforcement learning because of slow control response and complex fluid dynamics arising from multiple interconnected cylinders and differing fluid rates. This paper introduces an analytical actuator model derived from hydraulic dynamics that predicts joint torques for all 12 actuators in less than one microsecond. The model is used inside a reinforcement-learning environment to train a quadrupedal locomotion policy for a hydraulic robot weighing more than 300 kg. The authors also compare the analytical model against neural-network actuator models based on MLP, LSTM, and GRU architectures, showing that the analytical approach is more accurate in data-limited and out-of-distribution cases and trains more than three times faster.

Training uses 400 parallel simulated environments and concurrent policy-estimator training. The learned policy is deployed on the physical hydraulic quadruped, where it achieves stable, command-tracking locomotion at approximately 1 m/s. The authors state that this is the first demonstration of successful reinforcement-learning-based locomotion transferred to a heavy hydraulic quadruped robot. The work was supported by KAIST, HYUNDAI Rotem, KITECH, KRIT, and DAPA.

The core technical contribution is therefore a fast, physics-based actuator representation that makes reinforcement learning practical for heavy hydraulic legged systems, together with a complete sim-to-real training and deployment pipeline.

## Key Contributions

- Analytical hydraulic actuator model that predicts joint torques for all 12 actuators in under one microsecond.
- Reinforcement-learning locomotion controller trained and deployed on a hydraulic quadruped robot weighing over 300 kg.
- First reported stable, command-tracking RL locomotion at 1 m/s on a heavy hydraulic quadruped robot.
- Demonstrated advantages over neural-network actuator models (MLP, LSTM, GRU) in data-limited and out-of-distribution scenarios.
- Training runtime more than three times faster than neural-network-based actuator models.

## Relevance to Humanoid Robotics

Although the experiments are performed on a quadruped, the actuator modeling problem is directly relevant to heavy humanoid robots that use hydraulic actuation for high-load, high-fidelity joint control. The analytical actuator model reduces the computational cost of simulating complex hydraulic dynamics, which is a prerequisite for applying reinforcement learning to large humanoids. The sim-to-real pipeline—including concurrent policy-estimator training and parallel simulation—can be adapted to bipedal locomotion and whole-body control for humanoid systems. Therefore, the paper contributes enabling component and algorithmic technologies for hydraulic humanoid development.
