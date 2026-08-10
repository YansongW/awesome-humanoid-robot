---
$id: ent_paper_robust_operational_space_contr_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Robust Operational Space Control with Conformal Disturbance Bounds for Safe Redundant Manipulation
  zh: Robust Operational Space Control with Conformal Disturbance Bounds for Safe Redundant Manipulation
  ko: Robust Operational Space Control with Conformal Disturbance Bounds for Safe Redundant Manipulation
summary:
  en: 'arXiv:2607.00424v1 Announce Type: new Abstract: Redundant robotic manipulators operating in constrained and human-interactive
    environments require accurate task-space tracking together with rigorous safety guarantees under dynamic uncertainties.
    Classical operational space computed torque controller (OSCTC) relies on accurate dynamic models and degrades in the presence
    of disturbances. In contrast, the data-driven paradigm of residual learning approximates disturbances as functions learned
    from full-state measurements, which are often noisy in practice, lack rigorous theoretical guarantees, and introduce additional
    design complexity. This paper proposes a robust OSCTC framework that integrates an extended state observer (ESO) with
    conformal prediction to combine model-based robustness and data-driven adaptability. The ESO estimates lumped disturbances
    directly in operational space without requiring full-state measurements as in residual learning, and a robust control
    barrier function (CBF) is constructed to enforce safety under uncertainty. However, robust CBFs require a known disturbance-variation
    bound to guarantee absolute safety, which often leads to conservatism in practice. To address this limitation, we further
    employ a sliding-window conformal prediction mechanism to estimate the bound online in a distribution-free manner, thereby
    achieving practical probabilistic safety guarantees. Experiments on a 7-DoF Franka Research 3 manipulator demonstrate
    millimeter-level tracking accuracy and real-time safe control at 1~kHz under various disturbances.'
  zh: 本文提出一种鲁棒操作空间控制框架，将扩展状态观测器（ESO）与保形预测相结合，用于冗余机械臂的安全控制。该框架在7-DoF Franka Research 3机械臂上实现了毫米级跟踪精度和1 kHz实时安全控制，无需全状态测量即可处理动态不确定性。
  ko: 'arXiv:2607.00424v1 Announce Type: new Abstract: Redundant robotic manipulators operating in constrained and human-interactive
    environments require accurate task-space tracking together with rigorous safety guarantees under dynamic uncertainties.
    Classical operational space computed torque controller (OSCTC) relies on accurate dynamic models and degrades in the presence
    of disturbances. In contrast, the data-driven paradigm of residual learning approximates disturbances as functions learned
    from full-state measurements, which are often noisy in practice, lack rigorous theoretical guarantees, and introduce additional
    design complexity. This paper proposes a robust OSCTC framework that integrates an extended state observer (ESO) with
    conformal prediction to combine model-based robustness and data-driven adaptability. The ESO estimates lumped disturbances
    directly in operational space without requiring full-state measurements as in residual learning, and a robust control
    barrier function (CBF) is constructed to enforce safety under uncertainty. However, robust CBFs require a known disturbance-variation
    bound to guarantee absolute safety, which often leads to conservatism in practice. To address this limitation, we further
    employ a sliding-window conformal prediction mechanism to estimate the bound online in a distribution-free manner, thereby
    achieving practical probabilistic safety guarantees. Experiments on a 7-DoF Franka Research 3 manipulator demonstrate
    millimeter-level tracking accuracy and real-time safe control at 1~kHz under various disturbances.'
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
- robust_operational_space_contr
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.00424v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (734 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Robust Operational Space Control with Conformal Disturbance Bounds for Safe Redundant Manipulation (arXiv)
  url: https://arxiv.org/abs/2607.00424
  date: '2026'
  accessed_at: '2026-07-03'
---
## 概述
针对冗余机械臂在约束与人机交互环境中的任务空间跟踪与安全需求，本文提出一种融合扩展状态观测器（ESO）与保形预测的鲁棒操作空间控制框架。ESO直接在操作空间估计集总扰动，避免了残差学习对全状态测量的依赖；同时构建鲁棒控制屏障函数（CBF）以保障不确定性下的安全性。为解决鲁棒CBF需已知扰动变化边界导致的保守性问题，采用滑动窗口保形预测机制在线估计该边界，实现无分布假设下的实用概率安全保证。

## 核心内容
### 方法架构
- **核心问题**：经典操作空间计算力矩控制器（OSCTC）依赖精确动力学模型，在扰动下性能退化；残差学习需全状态测量且缺乏理论保证。
- **ESO设计**：扩展状态观测器直接在操作空间估计集总扰动，无需全状态测量，保留模型基鲁棒性。
- **鲁棒CBF**：构建鲁棒控制屏障函数，在不确定性下强制执行安全约束，但需已知扰动变化边界以避免保守性。
- **保形预测机制**：采用滑动窗口保形预测在线估计扰动变化边界，无需分布假设，实现实用概率安全保证。

### 实验设置
- **平台**：7-DoF Franka Research 3机械臂
- **扰动类型**：多种动态不确定性（未具体说明）
- **控制频率**：1 kHz实时控制
- **性能指标**：毫米级跟踪精度

### 关键结果
- 在各类扰动下实现毫米级任务空间跟踪精度
- 实时安全控制频率达1 kHz
- 保形预测机制有效降低鲁棒CBF的保守性，同时维持安全保证

### 结论
该框架通过ESO与保形预测的协同，在无需全状态测量和分布假设的前提下，兼顾了模型基鲁棒性与数据驱动适应性，为冗余机械臂在动态不确定环境中的安全操作提供了实用解决方案。

## Overview
Redundant robotic manipulators operating in constrained and human-interactive environments require accurate task-space tracking together with rigorous safety guarantees under dynamic uncertainties. Classical operational space computed torque controller (OSCTC) relies on accurate dynamic models and degrades in the presence of disturbances. In contrast, the data-driven paradigm of residual learning approximates disturbances as functions learned from full-state measurements, which are often noisy in practice, lack rigorous theoretical guarantees, and introduce additional design complexity. This paper proposes a robust OSCTC framework that integrates an extended state observer (ESO) with conformal prediction to combine model-based robustness and data-driven adaptability. The ESO estimates lumped disturbances directly in operational space without requiring full-state measurements as in residual learning, and a robust control barrier function (CBF) is constructed to enforce safety under uncertainty. However, robust CBFs require a known disturbance-variation bound to guarantee absolute safety, which often leads to conservatism in practice. To address this limitation, we further employ a sliding-window conformal prediction mechanism to estimate the bound online in a distribution-free manner, thereby achieving practical probabilistic safety guarantees. Experiments on a 7-DoF Franka Research 3 manipulator demonstrate millimeter-level tracking accuracy and real-time safe control at 1~kHz under various disturbances.

## 参考
- http://arxiv.org/abs/2607.00424v1

## 개요
구속 및 인간-로봇 상호작용 환경에서의 중복 매니퓰레이터의 작업 공간 추적 및 안전 요구를 위해, 본 논문은 확장 상태 관측기(ESO)와 등각 예측(Conformal Prediction)을 융합한 강건한 작업 공간 제어 프레임워크를 제안한다. ESO는 작업 공간에서 직접 집중 외란을 추정하여 전 상태 측정에 대한 잔차 학습의 의존성을 피하며, 동시에 불확실성 하에서 안전성을 보장하기 위한 강건한 제어 장벽 함수(CBF)를 구축한다. 강건한 CBF가 요구하는 외란 변화 경계의 사전 지식으로 인한 보수성을 해결하기 위해, 슬라이딩 윈도우 등각 예측 메커니즘을 통해 해당 경계를 온라인으로 추정하여 분포 가정 없이 실용적인 확률적 안전 보장을 구현한다.

## 핵심 내용
### 방법 구조
- **핵심 문제**: 고전적 작업 공간 계산 토크 제어기(OSCTC)는 정밀한 동역학 모델에 의존하며, 외란 하에서 성능이 저하된다. 잔차 학습은 전 상태 측정을 필요로 하고 이론적 보장이 부족하다.
- **ESO 설계**: 확장 상태 관측기는 작업 공간에서 직접 집중 외란을 추정하며, 전 상태 측정 없이 모델 기반 강건성을 유지한다.
- **강건한 CBF**: 불확실성 하에서 안전 제약을 강제로 이행하는 강건한 제어 장벽 함수를 구축하지만, 보수성을 피하기 위해 외란 변화 경계에 대한 사전 지식이 필요하다.
- **등각 예측 메커니즘**: 슬라이딩 윈도우 등각 예측을 통해 외란 변화 경계를 온라인으로 추정하며, 분포 가정 없이 실용적인 확률적 안전 보장을 구현한다.

### 실험 설정
- **플랫폼**: 7-DoF Franka Research 3 매니퓰레이터
- **외란 유형**: 다양한 동적 불확실성 (구체적으로 명시되지 않음)
- **제어 주파수**: 1 kHz 실시간 제어
- **성능 지표**: 밀리미터급 추적 정밀도

### 주요 결과
- 다양한 외란 하에서 밀리미터급 작업 공간 추적 정밀도 달성
- 실시간 안전 제어 주파수 1 kHz 달성
- 등각 예측 메커니즘이 강건한 CBF의 보수성을 효과적으로 낮추면서 안전 보장을 유지

### 결론
본 프레임워크는 ESO와 등각 예측의 협력을 통해 전 상태 측정 및 분포 가정 없이 모델 기반 강건성과 데이터 기반 적응성을 동시에 확보하여, 동적 불확실성 환경에서 중복 매니퓰레이터의 안전한 작업을 위한 실용적 해결책을 제공한다.
