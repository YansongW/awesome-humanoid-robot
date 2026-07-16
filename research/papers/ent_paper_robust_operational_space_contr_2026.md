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
  zh: 'arXiv:2607.00424v1 Announce Type: new Abstract: Redundant robotic manipulators operating in constrained and human-interactive
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.00424v1.
sources:
- id: src_001
  type: paper
  title: Robust Operational Space Control with Conformal Disturbance Bounds for Safe Redundant Manipulation (arXiv)
  url: https://arxiv.org/abs/2607.00424
  date: '2026'
  accessed_at: '2026-07-03'
---
## 概述
Redundant robotic manipulators operating in constrained and human-interactive environments require accurate task-space tracking together with rigorous safety guarantees under dynamic uncertainties. Classical operational space computed torque controller (OSCTC) relies on accurate dynamic models and degrades in the presence of disturbances. In contrast, the data-driven paradigm of residual learning approximates disturbances as functions learned from full-state measurements, which are often noisy in practice, lack rigorous theoretical guarantees, and introduce additional design complexity. This paper proposes a robust OSCTC framework that integrates an extended state observer (ESO) with conformal prediction to combine model-based robustness and data-driven adaptability. The ESO estimates lumped disturbances directly in operational space without requiring full-state measurements as in residual learning, and a robust control barrier function (CBF) is constructed to enforce safety under uncertainty. However, robust CBFs require a known disturbance-variation bound to guarantee absolute safety, which often leads to conservatism in practice. To address this limitation, we further employ a sliding-window conformal prediction mechanism to estimate the bound online in a distribution-free manner, thereby achieving practical probabilistic safety guarantees. Experiments on a 7-DoF Franka Research 3 manipulator demonstrate millimeter-level tracking accuracy and real-time safe control at 1~kHz under various disturbances.

## 核心内容
Redundant robotic manipulators operating in constrained and human-interactive environments require accurate task-space tracking together with rigorous safety guarantees under dynamic uncertainties. Classical operational space computed torque controller (OSCTC) relies on accurate dynamic models and degrades in the presence of disturbances. In contrast, the data-driven paradigm of residual learning approximates disturbances as functions learned from full-state measurements, which are often noisy in practice, lack rigorous theoretical guarantees, and introduce additional design complexity. This paper proposes a robust OSCTC framework that integrates an extended state observer (ESO) with conformal prediction to combine model-based robustness and data-driven adaptability. The ESO estimates lumped disturbances directly in operational space without requiring full-state measurements as in residual learning, and a robust control barrier function (CBF) is constructed to enforce safety under uncertainty. However, robust CBFs require a known disturbance-variation bound to guarantee absolute safety, which often leads to conservatism in practice. To address this limitation, we further employ a sliding-window conformal prediction mechanism to estimate the bound online in a distribution-free manner, thereby achieving practical probabilistic safety guarantees. Experiments on a 7-DoF Franka Research 3 manipulator demonstrate millimeter-level tracking accuracy and real-time safe control at 1~kHz under various disturbances.

## 参考
- http://arxiv.org/abs/2607.00424v1

## Overview
Redundant robotic manipulators operating in constrained and human-interactive environments require accurate task-space tracking together with rigorous safety guarantees under dynamic uncertainties. Classical operational space computed torque controller (OSCTC) relies on accurate dynamic models and degrades in the presence of disturbances. In contrast, the data-driven paradigm of residual learning approximates disturbances as functions learned from full-state measurements, which are often noisy in practice, lack rigorous theoretical guarantees, and introduce additional design complexity. This paper proposes a robust OSCTC framework that integrates an extended state observer (ESO) with conformal prediction to combine model-based robustness and data-driven adaptability. The ESO estimates lumped disturbances directly in operational space without requiring full-state measurements as in residual learning, and a robust control barrier function (CBF) is constructed to enforce safety under uncertainty. However, robust CBFs require a known disturbance-variation bound to guarantee absolute safety, which often leads to conservatism in practice. To address this limitation, we further employ a sliding-window conformal prediction mechanism to estimate the bound online in a distribution-free manner, thereby achieving practical probabilistic safety guarantees. Experiments on a 7-DoF Franka Research 3 manipulator demonstrate millimeter-level tracking accuracy and real-time safe control at 1~kHz under various disturbances.

## Content
Redundant robotic manipulators operating in constrained and human-interactive environments require accurate task-space tracking together with rigorous safety guarantees under dynamic uncertainties. Classical operational space computed torque controller (OSCTC) relies on accurate dynamic models and degrades in the presence of disturbances. In contrast, the data-driven paradigm of residual learning approximates disturbances as functions learned from full-state measurements, which are often noisy in practice, lack rigorous theoretical guarantees, and introduce additional design complexity. This paper proposes a robust OSCTC framework that integrates an extended state observer (ESO) with conformal prediction to combine model-based robustness and data-driven adaptability. The ESO estimates lumped disturbances directly in operational space without requiring full-state measurements as in residual learning, and a robust control barrier function (CBF) is constructed to enforce safety under uncertainty. However, robust CBFs require a known disturbance-variation bound to guarantee absolute safety, which often leads to conservatism in practice. To address this limitation, we further employ a sliding-window conformal prediction mechanism to estimate the bound online in a distribution-free manner, thereby achieving practical probabilistic safety guarantees. Experiments on a 7-DoF Franka Research 3 manipulator demonstrate millimeter-level tracking accuracy and real-time safe control at 1~kHz under various disturbances.

## 개요
제약이 있는 환경과 인간 상호작용 환경에서 작동하는 리던던트 로봇 매니퓰레이터는 동적 불확실성 하에서 정확한 작업 공간 추적과 엄격한 안전 보장을 필요로 합니다. 고전적인 작업 공간 계산 토크 제어기(OSCTC)는 정확한 동적 모델에 의존하며 외란이 존재할 때 성능이 저하됩니다. 반면, 잔차 학습의 데이터 기반 패러다임은 전 상태 측정값으로부터 학습된 함수로 외란을 근사화하지만, 실제로는 종종 잡음이 많고 엄격한 이론적 보장이 부족하며 추가적인 설계 복잡성을 초래합니다. 본 논문은 확장 상태 관측기(ESO)와 컨포멀 예측을 통합하여 모델 기반 강건성과 데이터 기반 적응성을 결합한 강건한 OSCTC 프레임워크를 제안합니다. ESO는 잔차 학습에서처럼 전 상태 측정값을 필요로 하지 않고 작업 공간에서 직접 집합 외란을 추정하며, 불확실성 하에서 안전을 강제하기 위해 강건한 제어 장벽 함수(CBF)가 구축됩니다. 그러나 강건한 CBF는 절대적 안전을 보장하기 위해 알려진 외란 변동 경계를 필요로 하며, 이는 실제로 보수성을 초래하는 경우가 많습니다. 이 한계를 해결하기 위해, 우리는 슬라이딩 윈도우 컨포멀 예측 메커니즘을 추가로 사용하여 분포 무관 방식으로 온라인에서 경계를 추정함으로써 실용적인 확률적 안전 보장을 달성합니다. 7-DOF Franka Research 3 매니퓰레이터에 대한 실험은 다양한 외란 하에서 밀리미터 수준의 추적 정확도와 1kHz에서의 실시간 안전 제어를 입증합니다.

## 핵심 내용
제약이 있는 환경과 인간 상호작용 환경에서 작동하는 리던던트 로봇 매니퓰레이터는 동적 불확실성 하에서 정확한 작업 공간 추적과 엄격한 안전 보장을 필요로 합니다. 고전적인 작업 공간 계산 토크 제어기(OSCTC)는 정확한 동적 모델에 의존하며 외란이 존재할 때 성능이 저하됩니다. 반면, 잔차 학습의 데이터 기반 패러다임은 전 상태 측정값으로부터 학습된 함수로 외란을 근사화하지만, 실제로는 종종 잡음이 많고 엄격한 이론적 보장이 부족하며 추가적인 설계 복잡성을 초래합니다. 본 논문은 확장 상태 관측기(ESO)와 컨포멀 예측을 통합하여 모델 기반 강건성과 데이터 기반 적응성을 결합한 강건한 OSCTC 프레임워크를 제안합니다. ESO는 잔차 학습에서처럼 전 상태 측정값을 필요로 하지 않고 작업 공간에서 직접 집합 외란을 추정하며, 불확실성 하에서 안전을 강제하기 위해 강건한 제어 장벽 함수(CBF)가 구축됩니다. 그러나 강건한 CBF는 절대적 안전을 보장하기 위해 알려진 외란 변동 경계를 필요로 하며, 이는 실제로 보수성을 초래하는 경우가 많습니다. 이 한계를 해결하기 위해, 우리는 슬라이딩 윈도우 컨포멀 예측 메커니즘을 추가로 사용하여 분포 무관 방식으로 온라인에서 경계를 추정함으로써 실용적인 확률적 안전 보장을 달성합니다. 7-DOF Franka Research 3 매니퓰레이터에 대한 실험은 다양한 외란 하에서 밀리미터 수준의 추적 정확도와 1kHz에서의 실시간 안전 제어를 입증합니다.
