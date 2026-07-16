---
$id: ent_paper_lee_learning_quadrupedal_locomotio_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning Quadrupedal Locomotion for a Heavy Hydraulic Robot Using an Actuator Model
  zh: 基于执行器模型的大型液压四足机器人运动学习
  ko: 액추에이터 모델을 활용한 대형 유압 사족 보행 로봇의 보행 학습
summary:
  en: This paper presents an analytical hydraulic actuator model that predicts joint torques for 12 actuators in under one
    microsecond, enabling reinforcement-learning training of a locomotion policy for a hydraulic quadruped robot weighing
    over 300 kg. The trained policy is transferred to hardware, achieving stable, command-tracking locomotion at 1 m/s and
    outperforming neural-network actuator models in data-limited and out-of-distribution settings.
  zh: 本文提出了一种解析液压执行器模型，可在不到1微秒内预测12个执行器的关节扭矩，从而为超过300公斤的液压四足机器人训练强化学习运动策略。训练的策略被迁移到实体硬件，实现了1米/秒的稳定指令跟踪运动，并在数据有限和分布外场景中优于神经网络执行器模型。
  ko: 본 논문은 12개의 액추에이터에 대한 관절 토크를 1마이크로초 이내에 예측하는 해석적 유압 액추에이터 모델을 제안하여 300kg이 넘는 유압 사족 보행 로봇의 강화학습 보행 정책 학습을 가능하게 한다. 학습된
    정책은 하드웨어로 이전되어 1m/s의 안정적인 명령 추종 보행을 달성했으며, 데이터가 제한되거나 분포 외 시나리오에서 신경망 기반 액추에이터 모델보다 우수한 성능을 보였다.
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
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2601.11143v1.
sources:
- id: src_001
  type: paper
  title: Learning Quadrupedal Locomotion for a Heavy Hydraulic Robot Using an Actuator Model
  url: https://arxiv.org/abs/2601.11143
  date: '2026'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
The simulation-to-reality (sim-to-real) transfer of large-scale hydraulic robots presents a significant challenge in robotics because of the inherent slow control response and complex fluid dynamics. The complex dynamics result from the multiple interconnected cylinder structure and the difference in fluid rates of the cylinders. These characteristics complicate detailed simulation for all joints, making it unsuitable for reinforcement learning (RL) applications. In this work, we propose an analytical actuator model driven by hydraulic dynamics to represent the complicated actuators. The model predicts joint torques for all 12 actuators in under 1 microsecond, allowing rapid processing in RL environments. We compare our model with neural network-based actuator models and demonstrate the advantages of our model in data-limited scenarios. The locomotion policy trained in RL with our model is deployed on a hydraulic quadruped robot, which is over 300 kg. This work is the first demonstration of a successful transfer of stable and robust command-tracking locomotion with RL on a heavy hydraulic quadruped robot, demonstrating advanced sim-to-real transferability.

## 核心内容
The simulation-to-reality (sim-to-real) transfer of large-scale hydraulic robots presents a significant challenge in robotics because of the inherent slow control response and complex fluid dynamics. The complex dynamics result from the multiple interconnected cylinder structure and the difference in fluid rates of the cylinders. These characteristics complicate detailed simulation for all joints, making it unsuitable for reinforcement learning (RL) applications. In this work, we propose an analytical actuator model driven by hydraulic dynamics to represent the complicated actuators. The model predicts joint torques for all 12 actuators in under 1 microsecond, allowing rapid processing in RL environments. We compare our model with neural network-based actuator models and demonstrate the advantages of our model in data-limited scenarios. The locomotion policy trained in RL with our model is deployed on a hydraulic quadruped robot, which is over 300 kg. This work is the first demonstration of a successful transfer of stable and robust command-tracking locomotion with RL on a heavy hydraulic quadruped robot, demonstrating advanced sim-to-real transferability.

## 参考
- http://arxiv.org/abs/2601.11143v1

## Overview
The simulation-to-reality (sim-to-real) transfer of large-scale hydraulic robots presents a significant challenge in robotics because of the inherent slow control response and complex fluid dynamics. The complex dynamics result from the multiple interconnected cylinder structure and the difference in fluid rates of the cylinders. These characteristics complicate detailed simulation for all joints, making it unsuitable for reinforcement learning (RL) applications. In this work, we propose an analytical actuator model driven by hydraulic dynamics to represent the complicated actuators. The model predicts joint torques for all 12 actuators in under 1 microsecond, allowing rapid processing in RL environments. We compare our model with neural network-based actuator models and demonstrate the advantages of our model in data-limited scenarios. The locomotion policy trained in RL with our model is deployed on a hydraulic quadruped robot, which is over 300 kg. This work is the first demonstration of a successful transfer of stable and robust command-tracking locomotion with RL on a heavy hydraulic quadruped robot, demonstrating advanced sim-to-real transferability.

## Content
The simulation-to-reality (sim-to-real) transfer of large-scale hydraulic robots presents a significant challenge in robotics because of the inherent slow control response and complex fluid dynamics. The complex dynamics result from the multiple interconnected cylinder structure and the difference in fluid rates of the cylinders. These characteristics complicate detailed simulation for all joints, making it unsuitable for reinforcement learning (RL) applications. In this work, we propose an analytical actuator model driven by hydraulic dynamics to represent the complicated actuators. The model predicts joint torques for all 12 actuators in under 1 microsecond, allowing rapid processing in RL environments. We compare our model with neural network-based actuator models and demonstrate the advantages of our model in data-limited scenarios. The locomotion policy trained in RL with our model is deployed on a hydraulic quadruped robot, which is over 300 kg. This work is the first demonstration of a successful transfer of stable and robust command-tracking locomotion with RL on a heavy hydraulic quadruped robot, demonstrating advanced sim-to-real transferability.

## 개요
대규모 유압 로봇의 시뮬레이션-현실(sim-to-real) 전환은 본질적으로 느린 제어 응답과 복잡한 유체 역학으로 인해 로봇 공학에서 중요한 도전 과제입니다. 이러한 복잡한 역학은 다중 상호 연결된 실린더 구조와 실린더 간 유체 속도 차이에서 비롯됩니다. 이러한 특성은 모든 관절에 대한 상세 시뮬레이션을 복잡하게 만들어 강화 학습(RL) 응용에 부적합하게 만듭니다. 본 연구에서는 복잡한 액추에이터를 표현하기 위해 유압 역학에 기반한 해석적 액추에이터 모델을 제안합니다. 이 모델은 1마이크로초 미만의 시간 내에 12개 액추에이터의 관절 토크를 예측하여 RL 환경에서 빠른 처리를 가능하게 합니다. 우리는 이 모델을 신경망 기반 액추에이터 모델과 비교하고 데이터가 제한된 시나리오에서 우리 모델의 장점을 입증합니다. 우리 모델로 RL에서 훈련된 보행 정책은 300kg이 넘는 유압 사족 로봇에 배포됩니다. 이 연구는 중형 유압 사족 로봇에서 RL을 통한 안정적이고 강건한 명령 추적 보행의 성공적인 전환을 최초로 시연하며, 고급 시뮬레이션-현실 전환 가능성을 보여줍니다.

## 핵심 내용
대규모 유압 로봇의 시뮬레이션-현실(sim-to-real) 전환은 본질적으로 느린 제어 응답과 복잡한 유체 역학으로 인해 로봇 공학에서 중요한 도전 과제입니다. 이러한 복잡한 역학은 다중 상호 연결된 실린더 구조와 실린더 간 유체 속도 차이에서 비롯됩니다. 이러한 특성은 모든 관절에 대한 상세 시뮬레이션을 복잡하게 만들어 강화 학습(RL) 응용에 부적합하게 만듭니다. 본 연구에서는 복잡한 액추에이터를 표현하기 위해 유압 역학에 기반한 해석적 액추에이터 모델을 제안합니다. 이 모델은 1마이크로초 미만의 시간 내에 12개 액추에이터의 관절 토크를 예측하여 RL 환경에서 빠른 처리를 가능하게 합니다. 우리는 이 모델을 신경망 기반 액추에이터 모델과 비교하고 데이터가 제한된 시나리오에서 우리 모델의 장점을 입증합니다. 우리 모델로 RL에서 훈련된 보행 정책은 300kg이 넘는 유압 사족 로봇에 배포됩니다. 이 연구는 중형 유압 사족 로봇에서 RL을 통한 안정적이고 강건한 명령 추적 보행의 성공적인 전환을 최초로 시연하며, 고급 시뮬레이션-현실 전환 가능성을 보여줍니다.
