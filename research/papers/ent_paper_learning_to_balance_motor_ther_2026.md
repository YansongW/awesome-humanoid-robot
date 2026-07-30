---
$id: ent_paper_learning_to_balance_motor_ther_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning to Balance Motor Thermal Safety and Quadrupedal Locomotion Performance with Residual Policy
  zh: Learning to Balance Motor Thermal Safety and Quadrupedal Locomotion Performance with Residual Policy
  ko: Learning to Balance Motor Thermal Safety and Quadrupedal Locomotion Performance with Residual Policy
summary:
  en: 'arXiv:2605.27046v3 Announce Type: replace Abstract: Motor thermal management is often overlooked in the context of
    electrically-actuated robots, particularly legged robots, but motor overheating is a key factor that limits long-duration
    locomotion especially under payload conditions. This paper integrates a whole-body thermal model of a quadruped robot
    into the reinforcement learning pipeline to update motor temperatures, and proposes a two-stage training framework for
    motor thermal management. In this framework, a nominal policy is first pre-trained as a locomotion baseline capable of
    traversing diverse terrains. A residual policy is then trained on top of the nominal policy to provide corrective actions
    based on the robot''s thermal state, ensuring high performance under low-temperature conditions and preventing motor overheating
    under high-temperature conditions. Simulation results demonstrate that the proposed policy achieves an effective balance
    between motor thermal safety and locomotion performance. Real-world experiments on a Unitree A1 quadruped robot further
    validate the approach: under a 3 kg payload, the robot achieves stable locomotion across multiple terrains for over 13
    minutes, while the nominal policy alone leads to motor overheating in about 5 minutes.'
  zh: 本文提出一种两阶段训练框架，将四足机器人的全身热模型集成到强化学习流程中，以平衡电机热安全与运动性能。该方法通过预训练标称策略作为运动基线，再训练残差策略根据热状态提供修正动作。在Unitree A1机器人上，3kg负载下实现多地形稳定运动超过13分钟，而单独标称策略仅约5分钟即过热。
  ko: 'arXiv:2605.27046v3 Announce Type: replace Abstract: Motor thermal management is often overlooked in the context of
    electrically-actuated robots, particularly legged robots, but motor overheating is a key factor that limits long-duration
    locomotion especially under payload conditions. This paper integrates a whole-body thermal model of a quadruped robot
    into the reinforcement learning pipeline to update motor temperatures, and proposes a two-stage training framework for
    motor thermal management. In this framework, a nominal policy is first pre-trained as a locomotion baseline capable of
    traversing diverse terrains. A residual policy is then trained on top of the nominal policy to provide corrective actions
    based on the robot''s thermal state, ensuring high performance under low-temperature conditions and preventing motor overheating
    under high-temperature conditions. Simulation results demonstrate that the proposed policy achieves an effective balance
    between motor thermal safety and locomotion performance. Real-world experiments on a Unitree A1 quadruped robot further
    validate the approach: under a 3 kg payload, the robot achieves stable locomotion across multiple terrains for over 13
    minutes, while the nominal policy alone leads to motor overheating in about 5 minutes.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- robotics
- learning_to_balance_motor_ther
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2605.27046v3. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: Learning to Balance Motor Thermal Safety and Quadrupedal Locomotion Performance with Residual Policy (arXiv)
  url: https://arxiv.org/abs/2605.27046
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
电机过热是限制电驱机器人（尤其是足式机器人）长时间运动的关键因素，但常被忽视。本文提出一种两阶段训练框架，首先将四足机器人的全身热模型集成到强化学习流程中实时更新电机温度，然后预训练标称策略作为能穿越多种地形的运动基线，再在其上训练残差策略，根据热状态提供修正动作。仿真结果表明该方法有效平衡了热安全与运动性能，真实实验在Unitree A1上验证：3kg负载下稳定运动超13分钟，而单独标称策略约5分钟即过热。

## 核心内容
### 方法
- 将四足机器人的全身热模型集成到强化学习流程中，用于实时更新电机温度。
- 提出两阶段训练框架：
  - **第一阶段**：预训练标称策略（nominal policy），作为能穿越多种地形的运动基线。
  - **第二阶段**：在标称策略之上训练残差策略（residual policy），根据机器人热状态提供修正动作，低温时保持高性能，高温时防止过热。

### 实验设置
- 仿真环境：验证策略在热安全与运动性能间的平衡。
- 真实实验：使用Unitree A1四足机器人，负载3kg，测试多地形稳定运动。

### 关键结果
- 仿真中，所提策略有效平衡电机热安全与运动性能。
- 真实实验中：
  - 所提策略：3kg负载下，多地形稳定运动超过13分钟。
  - 单独标称策略：约5分钟即导致电机过热。

### 结论
本文方法通过残差策略结合热模型，显著延长了四足机器人在负载下的运动时长，为电机热管理提供了有效方案。

## Overview
Motor thermal management is often overlooked in the context of electrically-actuated robots, particularly legged robots, but motor overheating is a key factor that limits long-duration locomotion especially under payload conditions. This paper integrates a whole-body thermal model of a quadruped robot into the reinforcement learning pipeline to update motor temperatures, and proposes a two-stage training framework for motor thermal management. In this framework, a nominal policy is first pre-trained as a locomotion baseline capable of traversing diverse terrains. A residual policy is then trained on top of the nominal policy to provide corrective actions based on the robot's thermal state, ensuring high performance under low-temperature conditions and preventing motor overheating under high-temperature conditions. Simulation results demonstrate that the proposed policy achieves an effective balance between motor thermal safety and locomotion performance. Real-world experiments on a Unitree A1 quadruped robot further validate the approach: under a 3 kg payload, the robot achieves stable locomotion across multiple terrains for over 13 minutes, while the nominal policy alone leads to motor overheating in about 5 minutes.

## 개요
전기 구동 로봇, 특히 보행 로봇의 맥락에서 모터 열 관리는 종종 간과되지만, 모터 과열은 특히 탑재 하중 조건에서 장시간 보행을 제한하는 핵심 요소입니다. 본 논문은 사족 보행 로봇의 전신 열 모델을 강화 학습 파이프라인에 통합하여 모터 온도를 업데이트하고, 모터 열 관리를 위한 2단계 훈련 프레임워크를 제안합니다. 이 프레임워크에서 기본 정책은 먼저 다양한 지형을 횡단할 수 있는 보행 기준선으로 사전 훈련됩니다. 그런 다음 잔차 정책이 기본 정책 위에 훈련되어 로봇의 열 상태에 기반한 교정 동작을 제공하며, 저온 조건에서 높은 성능을 보장하고 고온 조건에서 모터 과열을 방지합니다. 시뮬레이션 결과는 제안된 정책이 모터 열 안전성과 보행 성능 사이의 효과적인 균형을 달성함을 보여줍니다. Unitree A1 사족 보행 로봇을 사용한 실제 실험은 이 접근 방식을 추가로 검증합니다: 3kg 탑재 하중 조건에서 로봇은 여러 지형에서 13분 이상 안정적인 보행을 달성하는 반면, 기본 정책만으로는 약 5분 만에 모터 과열이 발생합니다.

## 핵심 내용
전기 구동 로봇, 특히 보행 로봇의 맥락에서 모터 열 관리는 종종 간과되지만, 모터 과열은 특히 탑재 하중 조건에서 장시간 보행을 제한하는 핵심 요소입니다. 본 논문은 사족 보행 로봇의 전신 열 모델을 강화 학습 파이프라인에 통합하여 모터 온도를 업데이트하고, 모터 열 관리를 위한 2단계 훈련 프레임워크를 제안합니다. 이 프레임워크에서 기본 정책은 먼저 다양한 지형을 횡단할 수 있는 보행 기준선으로 사전 훈련됩니다. 그런 다음 잔차 정책이 기본 정책 위에 훈련되어 로봇의 열 상태에 기반한 교정 동작을 제공하며, 저온 조건에서 높은 성능을 보장하고 고온 조건에서 모터 과열을 방지합니다. 시뮬레이션 결과는 제안된 정책이 모터 열 안전성과 보행 성능 사이의 효과적인 균형을 달성함을 보여줍니다. Unitree A1 사족 보행 로봇을 사용한 실제 실험은 이 접근 방식을 추가로 검증합니다: 3kg 탑재 하중 조건에서 로봇은 여러 지형에서 13분 이상 안정적인 보행을 달성하는 반면, 기본 정책만으로는 약 5분 만에 모터 과열이 발생합니다.

## 参考
- http://arxiv.org/abs/2605.27046v3
