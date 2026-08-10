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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2605.06593v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (755 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2605.06593v1

## 개요
인간의 운동 참조를 로봇 형태로 리타게팅하면 종종 발 미끄러짐, 자체 충돌 또는 동역학적 비실현 가능성과 같은 문제가 발생합니다. ReActor는 강화 학습 추적 정책을 훈련하면서 참조 운동을 로봇 형태에 맞게 공동으로 조정하는 이중 최적화 프레임워크를 제안합니다. 이 방법은 희소한 의미론적 강체 대응만 필요로 하며, 최적 매개변수를 자동으로 식별하여 서로 다른 형태 간의 특징적인 운동을 보존합니다. 리타게팅을 물리 시뮬레이션과 직접 통합함으로써 ReActor는 물리적으로 타당한 운동을 생성하여 강건한 모방 학습을 촉진합니다. 이 방법은 시뮬레이션과 하드웨어 모두에서 검증되었으며, 인간에서 사족 로봇에 이르는 현저히 다른 형태로의 도전적인 운동 리타게팅을 보여줍니다.

## 핵심 내용
### 방법 개요
ReActor의 핵심은 이중 최적화 프레임워크입니다:
- **상위 최적화**: 참조 운동을 로봇 형태에 맞게 조정하며, 운동이 물리적으로 실현 가능하고 원래 특징을 보존하는 것을 목표로 합니다.
- **하위 최적화**: 강화 학습을 사용하여 조정된 운동을 추적할 수 있는 추적 정책을 훈련합니다.
- 상위 손실을 풀기 위해 저자는 근사 기울기를 유도하여 최적화 과정을 계산 가능하게 만듭니다.

### 핵심 설계
- **희소 의미론적 대응**: 손, 발, 몸통과 같은 소수의 핵심 강체 대응만 정의하면 되며, 밀집 매핑이 필요하지 않습니다.
- **자동 매개변수 튜닝**: 표현력이 뛰어난 매개변수화 모델을 최적화하여 최적 값을 자동으로 식별하고, 수동 튜닝의 필요성을 제거합니다.
- **물리 시뮬레이션 통합**: 리타게팅 과정이 물리 시뮬레이션과 직접 결합되어 생성된 운동이 동역학적으로 실현 가능함을 보장합니다.

### 실험 설정 및 결과
- **시뮬레이션 검증**: 인간과 현저히 다른 형태인 사족 로봇을 포함한 다양한 로봇 형태에서 테스트되었습니다.
- **하드웨어 검증**: 전신 협조 조작과 같은 도전적인 운동을 실제 로봇에서 실행했습니다.
- **핵심 지표**: 기준 방법과 비교하여 ReActor는 발 미끄러짐, 자체 충돌과 같은 물리적 불일치 문제를 현저히 줄이고 모방 학습의 성공률을 향상시켰습니다.
- **결론**: 이 방법은 인간의 운동을 서로 다른 형태의 로봇에 강건하게 리타게팅하여 물리적으로 타당한 운동을 생성하며, 모방 학습과 같은 하위 작업에 신뢰할 수 있는 기반을 제공합니다.
