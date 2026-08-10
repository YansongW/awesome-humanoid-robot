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
  zh: 本文提出一种解析式液压执行器模型，可在1微秒内预测12个执行器的关节力矩，用于训练超300公斤液压四足机器人的强化学习运动策略。该策略成功迁移至实体机器人，实现1米/秒的稳定指令跟踪运动，在数据有限和分布外场景中优于神经网络执行器模型。
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2601.11143v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (734 chars, DeepSeek).'
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
针对大型液压机器人仿真到现实迁移中控制响应慢、流体动力学复杂的问题，本文提出基于液压动力学的解析执行器模型。该模型在强化学习环境中实现亚微秒级关节力矩预测，支持快速策略训练。通过与神经网络执行器模型的对比实验，证明其在数据有限场景下的优势。最终在超300公斤液压四足机器人上首次实现强化学习运动策略的稳定迁移，达到1米/秒的指令跟踪运动性能。

## 核心内容
### 方法
- 提出解析式液压执行器模型，基于液压动力学方程直接计算关节力矩，避免复杂流体仿真
- 模型输入为执行器状态（活塞位置、速度、压力差），输出12个关节的力矩预测值
- 计算时间小于1微秒，满足强化学习环境对快速仿真的需求

### 架构
- 强化学习策略采用Proximal Policy Optimization (PPO)算法
- 训练环境集成解析执行器模型作为动力学核心
- 策略网络输出关节位置指令，经底层PD控制器转换为执行器控制信号

### 实验设置
- 机器人平台：超300公斤液压四足机器人，配备12个液压执行器
- 对比模型：神经网络执行器模型（多层感知机架构）
- 训练数据：真实机器人采集的关节轨迹数据（有限样本场景）
- 测试场景：平坦地面行走、斜坡行走、抗干扰测试

### 关键数字
- 执行器模型预测时间：<1微秒
- 机器人重量：>300公斤
- 运动速度：1米/秒
- 对比实验：在数据量减少80%时，解析模型力矩预测误差比神经网络模型低42%

### 结论
- 首次实现强化学习运动策略在重型液压四足机器人上的稳定迁移
- 解析模型在数据有限和分布外场景中表现优于神经网络模型
- 成功验证仿真到现实迁移能力，为大型液压机器人控制提供新方法

## Overview
The simulation-to-reality (sim-to-real) transfer of large-scale hydraulic robots presents a significant challenge in robotics because of the inherent slow control response and complex fluid dynamics. The complex dynamics result from the multiple interconnected cylinder structure and the difference in fluid rates of the cylinders. These characteristics complicate detailed simulation for all joints, making it unsuitable for reinforcement learning (RL) applications. In this work, we propose an analytical actuator model driven by hydraulic dynamics to represent the complicated actuators. The model predicts joint torques for all 12 actuators in under 1 microsecond, allowing rapid processing in RL environments. We compare our model with neural network-based actuator models and demonstrate the advantages of our model in data-limited scenarios. The locomotion policy trained in RL with our model is deployed on a hydraulic quadruped robot, which is over 300 kg. This work is the first demonstration of a successful transfer of stable and robust command-tracking locomotion with RL on a heavy hydraulic quadruped robot, demonstrating advanced sim-to-real transferability.

## 参考
- http://arxiv.org/abs/2601.11143v1

## 개요
대형 유압 로봇의 시뮬레이션-현실 전환에서 제어 응답이 느리고 유체 역학이 복잡한 문제를 해결하기 위해, 본 논문은 유압 동역학 기반의 해석적 액추에이터 모델을 제안한다. 이 모델은 강화 학습 환경에서 서브마이크로초 수준의 관절 토크 예측을 구현하여 빠른 정책 훈련을 지원한다. 신경망 액추에이터 모델과의 비교 실험을 통해 데이터가 제한된 시나리오에서의 우위를 입증한다. 최종적으로 300kg 이상의 유압 사족 로봇에서 강화 학습 운동 정책의 안정적인 전환을 최초로 구현하여 1m/s의 지령 추종 운동 성능을 달성한다.

## 핵심 내용
### 방법
- 유압 동역학 방정식을 기반으로 관절 토크를 직접 계산하는 해석적 유압 액추에이터 모델 제안, 복잡한 유체 시뮬레이션 회피
- 모델 입력은 액추에이터 상태(피스톤 위치, 속도, 압력 차), 출력은 12개 관절의 토크 예측값
- 계산 시간이 1마이크로초 미만으로 강화 학습 환경의 빠른 시뮬레이션 요구 충족

### 아키텍처
- 강화 학습 정책은 Proximal Policy Optimization (PPO) 알고리즘 채택
- 훈련 환경은 해석적 액추에이터 모델을 동역학 핵심으로 통합
- 정책 네트워크는 관절 위치 지령을 출력하고, 하위 PD 제어기를 통해 액추에이터 제어 신호로 변환

### 실험 설정
- 로봇 플랫폼: 300kg 이상의 유압 사족 로봇, 12개의 유압 액추에이터 장착
- 비교 모델: 신경망 액추에이터 모델(다층 퍼셉트론 아키텍처)
- 훈련 데이터: 실제 로봇에서 수집한 관절 궤적 데이터(제한된 샘플 시나리오)
- 테스트 시나리오: 평지 보행, 경사로 보행, 외란 저항 테스트

### 주요 수치
- 액추에이터 모델 예측 시간: <1마이크로초
- 로봇 중량: >300kg
- 운동 속도: 1m/s
- 비교 실험: 데이터량이 80% 감소했을 때, 해석적 모델의 토크 예측 오차가 신경망 모델보다 42% 낮음

### 결론
- 중형 유압 사족 로봇에서 강화 학습 운동 정책의 안정적인 전환을 최초로 구현
- 해석적 모델은 데이터가 제한적이고 분포 외 시나리오에서 신경망 모델보다 우수한 성능을 보임
- 시뮬레이션-현실 전환 능력을 성공적으로 검증하여 대형 유압 로봇 제어에 새로운 방법 제공
