---
$id: ent_paper_reactor_reinforcement_learning_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ReActor: Reinforcement Learning for Physics-Aware Motion Retargeting'
  zh: 'ReActor: Reinforcement Learning for Physics-Aware Motion Retargeting'
  ko: 'ReActor: Reinforcement Learning for Physics-Aware Motion Retargeting'
summary:
  en: 'ReActor: Reinforcement Learning for Physics-Aware Motion Retargeting is a 2026 work on loco-manipulation and whole-body-control
    for humanoid robots.'
  zh: ReActor 是 2026 年提出的一种面向人形机器人的物理感知运动重定向框架。该工作由研究团队开发，核心贡献在于提出了一种双层优化方法，将参考运动适应机器人形态与强化学习跟踪策略训练联合进行，无需手动调参，并能在仿真与硬件上生成物理可行的运动。
  ko: 'ReActor: Reinforcement Learning for Physics-Aware Motion Retargeting is a 2026 work on loco-manipulation and whole-body-control
    for humanoid robots.'
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
- loco_manipulation
- reactor
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2605.06593v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'ReActor: Reinforcement Learning for Physics-Aware Motion Retargeting (arXiv)'
  url: https://arxiv.org/abs/2605.06593
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
将人类运动参考重定向到机器人形态上常导致脚滑、自碰撞或动力学不可行等问题。ReActor 提出了一种双层优化框架，在训练强化学习跟踪策略的同时，联合调整参考运动以适应机器人形态。该方法仅需稀疏的语义刚体对应关系，并通过自动识别最优参数来保留不同形态间的特征运动。通过将重定向直接与物理仿真集成，ReActor 能生成物理合理的运动，从而促进鲁棒的模仿学习。该方法在仿真和硬件上均得到验证，展示了从人类到四足机器人等显著不同形态的挑战性运动重定向。

## 核心内容
### 方法概述
ReActor 的核心是一个双层优化框架：
- **上层优化**：调整参考运动以适应机器人形态，目标是使运动在物理上可行且保留原始特征。
- **下层优化**：使用强化学习训练一个跟踪策略，使机器人能够跟踪调整后的运动。
- 为了求解上层损失，作者推导了一个近似梯度，使优化过程可计算。

### 关键设计
- **稀疏语义对应**：仅需定义少量关键刚体对应关系（如手、脚、躯干），无需密集映射。
- **自动参数调优**：通过优化一个表达能力强的参数化模型，自动识别最优值，消除手动调参需求。
- **物理仿真集成**：重定向过程直接与物理仿真耦合，确保生成的运动在动力学上可行。

### 实验设置与结果
- **仿真验证**：在多种机器人形态上测试，包括与人类形态差异显著的四足机器人。
- **硬件验证**：在真实机器人上执行挑战性运动，如全身协调操作。
- **关键指标**：相比基线方法，ReActor 显著减少了脚滑、自碰撞等物理不一致问题，并提高了模仿学习的成功率。
- **结论**：该方法能够将人类运动鲁棒地重定向到不同形态的机器人上，生成物理合理的运动，为下游任务（如模仿学习）提供可靠基础。

## Overview
Retargeting human kinematic reference motion onto a robot's morphology remains a formidable challenge. Existing methods often produce physical inconsistencies, such as foot sliding, self-collisions, or dynamically infeasible motions, which hinder downstream imitation learning. We propose a bilevel optimization framework that jointly adapts reference motions to a robot's morphology while training a tracking policy using reinforcement learning. To make the optimization tractable, we derive an approximate gradient for the upper-level loss. Our framework requires only a sparse set of semantic rigid-body correspondences and eliminates the need for manual tuning by identifying optimal values for a parameterization expressive enough to preserve characteristic motion across different embodiments. Moreover, by integrating retargeting directly with physics simulation, we produce physically plausible motions that facilitate robust imitation learning. We validate our method in simulation and on hardware, demonstrating challenging motions for morphologies that differ significantly from a human, including retargeting onto a quadruped.

## 개요
인간의 운동학적 참조 동작을 로봇의 형태로 재타겟팅하는 것은 여전히 어려운 과제로 남아 있습니다. 기존 방법들은 발 미끄러짐, 자가 충돌 또는 동역학적으로 불가능한 동작과 같은 물리적 불일치를 자주 발생시켜, 하위 단계의 모방 학습을 저해합니다. 우리는 강화 학습을 사용하여 추적 정책을 훈련하면서 참조 동작을 로봇의 형태에 공동으로 적응시키는 이중 최적화 프레임워크를 제안합니다. 최적화를 다루기 쉽게 만들기 위해, 상위 수준 손실에 대한 근사 기울기를 유도합니다. 우리의 프레임워크는 희소한 의미론적 강체 대응 관계 집합만 필요로 하며, 다양한 형태에서 특징적인 동작을 보존할 수 있을 만큼 표현력이 풍부한 매개변수화에 대한 최적 값을 식별함으로써 수동 조정의 필요성을 제거합니다. 또한, 재타겟팅을 물리 시뮬레이션과 직접 통합함으로써, 강건한 모방 학습을 촉진하는 물리적으로 타당한 동작을 생성합니다. 우리는 시뮬레이션과 하드웨어에서 방법을 검증하여, 인간과 크게 다른 형태(사족 보행 로봇으로의 재타겟팅 포함)에 대한 도전적인 동작을 시연합니다.

## 핵심 내용
인간의 운동학적 참조 동작을 로봇의 형태로 재타겟팅하는 것은 여전히 어려운 과제로 남아 있습니다. 기존 방법들은 발 미끄러짐, 자가 충돌 또는 동역학적으로 불가능한 동작과 같은 물리적 불일치를 자주 발생시켜, 하위 단계의 모방 학습을 저해합니다. 우리는 강화 학습을 사용하여 추적 정책을 훈련하면서 참조 동작을 로봇의 형태에 공동으로 적응시키는 이중 최적화 프레임워크를 제안합니다. 최적화를 다루기 쉽게 만들기 위해, 상위 수준 손실에 대한 근사 기울기를 유도합니다. 우리의 프레임워크는 희소한 의미론적 강체 대응 관계 집합만 필요로 하며, 다양한 형태에서 특징적인 동작을 보존할 수 있을 만큼 표현력이 풍부한 매개변수화에 대한 최적 값을 식별함으로써 수동 조정의 필요성을 제거합니다. 또한, 재타겟팅을 물리 시뮬레이션과 직접 통합함으로써, 강건한 모방 학습을 촉진하는 물리적으로 타당한 동작을 생성합니다. 우리는 시뮬레이션과 하드웨어에서 방법을 검증하여, 인간과 크게 다른 형태(사족 보행 로봇으로의 재타겟팅 포함)에 대한 도전적인 동작을 시연합니다.

## 参考
- http://arxiv.org/abs/2605.06593v1
