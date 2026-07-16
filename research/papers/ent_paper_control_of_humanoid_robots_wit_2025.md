---
$id: ent_paper_control_of_humanoid_robots_wit_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Control of Humanoid Robots with Parallel Mechanisms using Kinematic Actuation Models
  zh: Control of Humanoid Robots with Parallel Mechanisms using Kinematic Actuation Models
  ko: Control of Humanoid Robots with Parallel Mechanisms using Kinematic Actuation Models
summary:
  en: Control of Humanoid Robots with Parallel Mechanisms using Kinematic Actuation Models is a 2025 work on hardware design
    for humanoid robots.
  zh: Control of Humanoid Robots with Parallel Mechanisms using Kinematic Actuation Models is a 2025 work on hardware design
    for humanoid robots.
  ko: Control of Humanoid Robots with Parallel Mechanisms using Kinematic Actuation Models is a 2025 work on hardware design
    for humanoid robots.
domains:
- 06_design_engineering
- 02_components
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
- system
tags:
- control_of_humanoid_robots_wit
- hardware_design
- humanoid
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2503.22459v2.
sources:
- id: src_001
  type: paper
  title: Control of Humanoid Robots with Parallel Mechanisms using Kinematic Actuation Models (arXiv)
  url: https://arxiv.org/abs/2503.22459
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Several recently released humanoid robots, inspired by the mechanical design of Cassie, employ actuator configurations in which the motors are displaced from the joints to reduce leg inertia. While studies accounting for the full kinematic complexity have demonstrated the benefits of these designs, the associated loop-closure constraints greatly increase computational cost and limit their use in control and learning. As a result, the non-linear transmission is often approximated by a constant reduction ratio, preventing exploitation of the mechanism's full capabilities. This paper introduces a compact analytical formulation for the two standard knee and ankle mechanisms that captures the exact non-linear transmission while remaining computationally efficient. The model is fully differentiable up to second order with a minimal formulation, enabling low-cost evaluation of dynamic derivatives for trajectory optimization and of the apparent transmission impedance for reinforcement learning. We integrate this formulation into trajectory optimization and locomotion policy learning, and compare it against simplified constant-ratio approaches. Hardware experiments demonstrate improved accuracy and robustness, showing that the proposed method provides a practical means to incorporate parallel actuation into modern control algorithms.

## 核心内容
Several recently released humanoid robots, inspired by the mechanical design of Cassie, employ actuator configurations in which the motors are displaced from the joints to reduce leg inertia. While studies accounting for the full kinematic complexity have demonstrated the benefits of these designs, the associated loop-closure constraints greatly increase computational cost and limit their use in control and learning. As a result, the non-linear transmission is often approximated by a constant reduction ratio, preventing exploitation of the mechanism's full capabilities. This paper introduces a compact analytical formulation for the two standard knee and ankle mechanisms that captures the exact non-linear transmission while remaining computationally efficient. The model is fully differentiable up to second order with a minimal formulation, enabling low-cost evaluation of dynamic derivatives for trajectory optimization and of the apparent transmission impedance for reinforcement learning. We integrate this formulation into trajectory optimization and locomotion policy learning, and compare it against simplified constant-ratio approaches. Hardware experiments demonstrate improved accuracy and robustness, showing that the proposed method provides a practical means to incorporate parallel actuation into modern control algorithms.

## 参考
- http://arxiv.org/abs/2503.22459v2

## Overview
Several recently released humanoid robots, inspired by the mechanical design of Cassie, employ actuator configurations in which the motors are displaced from the joints to reduce leg inertia. While studies accounting for the full kinematic complexity have demonstrated the benefits of these designs, the associated loop-closure constraints greatly increase computational cost and limit their use in control and learning. As a result, the non-linear transmission is often approximated by a constant reduction ratio, preventing exploitation of the mechanism's full capabilities. This paper introduces a compact analytical formulation for the two standard knee and ankle mechanisms that captures the exact non-linear transmission while remaining computationally efficient. The model is fully differentiable up to second order with a minimal formulation, enabling low-cost evaluation of dynamic derivatives for trajectory optimization and of the apparent transmission impedance for reinforcement learning. We integrate this formulation into trajectory optimization and locomotion policy learning, and compare it against simplified constant-ratio approaches. Hardware experiments demonstrate improved accuracy and robustness, showing that the proposed method provides a practical means to incorporate parallel actuation into modern control algorithms.

## Content
Several recently released humanoid robots, inspired by the mechanical design of Cassie, employ actuator configurations in which the motors are displaced from the joints to reduce leg inertia. While studies accounting for the full kinematic complexity have demonstrated the benefits of these designs, the associated loop-closure constraints greatly increase computational cost and limit their use in control and learning. As a result, the non-linear transmission is often approximated by a constant reduction ratio, preventing exploitation of the mechanism's full capabilities. This paper introduces a compact analytical formulation for the two standard knee and ankle mechanisms that captures the exact non-linear transmission while remaining computationally efficient. The model is fully differentiable up to second order with a minimal formulation, enabling low-cost evaluation of dynamic derivatives for trajectory optimization and of the apparent transmission impedance for reinforcement learning. We integrate this formulation into trajectory optimization and locomotion policy learning, and compare it against simplified constant-ratio approaches. Hardware experiments demonstrate improved accuracy and robustness, showing that the proposed method provides a practical means to incorporate parallel actuation into modern control algorithms.

## 개요
최근 출시된 여러 휴머노이드 로봇은 Cassie의 기계적 설계에서 영감을 받아, 다리 관성(lower leg inertia)을 줄이기 위해 모터를 관절에서 이격시킨 액추에이터 구성을 채택하고 있습니다. 전체 운동학적 복잡성을 고려한 연구들이 이러한 설계의 이점을 입증했지만, 관련된 폐쇄 루프 제약 조건(loop-closure constraints)은 계산 비용을 크게 증가시켜 제어 및 학습에서의 사용을 제한합니다. 그 결과, 비선형 전달(non-linear transmission)은 종종 일정한 감속비(constant reduction ratio)로 근사되어 메커니즘의 전체 성능을 활용하지 못하게 됩니다. 본 논문은 두 가지 표준 무릎 및 발목 메커니즘에 대한 간결한 해석적 공식을 도입하여, 계산 효율성을 유지하면서 정확한 비선형 전달을 포착합니다. 이 모델은 최소한의 공식으로 2차까지 완전히 미분 가능하여, 궤적 최적화를 위한 동적 도함수(dynamic derivatives)와 강화 학습을 위한 겉보기 전달 임피던스(apparent transmission impedance)를 저비용으로 평가할 수 있습니다. 우리는 이 공식을 궤적 최적화 및 보행 정책 학습에 통합하고, 단순화된 일정 비율 접근법과 비교합니다. 하드웨어 실험을 통해 개선된 정확성과 견고성을 입증하였으며, 제안된 방법이 병렬 액추에이션(parallel actuation)을 현대 제어 알고리즘에 통합하는 실용적인 수단을 제공함을 보여줍니다.

## 핵심 내용
최근 출시된 여러 휴머노이드 로봇은 Cassie의 기계적 설계에서 영감을 받아, 다리 관성을 줄이기 위해 모터를 관절에서 이격시킨 액추에이터 구성을 채택하고 있습니다. 전체 운동학적 복잡성을 고려한 연구들이 이러한 설계의 이점을 입증했지만, 관련된 폐쇄 루프 제약 조건은 계산 비용을 크게 증가시켜 제어 및 학습에서의 사용을 제한합니다. 그 결과, 비선형 전달은 종종 일정한 감속비로 근사되어 메커니즘의 전체 성능을 활용하지 못하게 됩니다. 본 논문은 두 가지 표준 무릎 및 발목 메커니즘에 대한 간결한 해석적 공식을 도입하여, 계산 효율성을 유지하면서 정확한 비선형 전달을 포착합니다. 이 모델은 최소한의 공식으로 2차까지 완전히 미분 가능하여, 궤적 최적화를 위한 동적 도함수와 강화 학습을 위한 겉보기 전달 임피던스를 저비용으로 평가할 수 있습니다. 우리는 이 공식을 궤적 최적화 및 보행 정책 학습에 통합하고, 단순화된 일정 비율 접근법과 비교합니다. 하드웨어 실험을 통해 개선된 정확성과 견고성을 입증하였으며, 제안된 방법이 병렬 액추에이션을 현대 제어 알고리즘에 통합하는 실용적인 수단을 제공함을 보여줍니다.
