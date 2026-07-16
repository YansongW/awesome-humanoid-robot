---
$id: ent_paper_geometry_aware_predictive_safe_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Geometry-Aware Predictive Safety Filters on Humanoids
  zh: Geometry-Aware Predictive Safety Filters on Humanoids
  ko: Geometry-Aware Predictive Safety Filters on Humanoids
summary:
  en: Geometry-Aware Predictive Safety Filters on Humanoids is a 2025 work on locomotion for humanoid robots.
  zh: Geometry-Aware Predictive Safety Filters on Humanoids is a 2025 work on locomotion for humanoid robots.
  ko: Geometry-Aware Predictive Safety Filters on Humanoids is a 2025 work on locomotion for humanoid robots.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- geometry_aware_predictive_safe
- humanoid
- locomotion
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2508.11129v1.
sources:
- id: src_001
  type: paper
  title: Geometry-Aware Predictive Safety Filters on Humanoids (arXiv)
  url: https://arxiv.org/abs/2508.11129
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Autonomous navigation through unstructured and dynamically-changing environments is a complex task that continues to present many challenges for modern roboticists. In particular, legged robots typically possess manipulable asymmetric geometries which must be considered during safety-critical trajectory planning. This work proposes a predictive safety filter: a nonlinear model predictive control (MPC) algorithm for online trajectory generation with geometry-aware safety constraints based on control barrier functions (CBFs). Critically, our method leverages Poisson safety functions to numerically synthesize CBF constraints directly from perception data. We extend the theoretical framework for Poisson safety functions to incorporate temporal changes in the domain by reformulating the static Dirichlet problem for Poisson's equation as a parameterized moving boundary value problem. Furthermore, we employ Minkowski set operations to lift the domain into a configuration space that accounts for robot geometry. Finally, we implement our real-time predictive safety filter on humanoid and quadruped robots in various safety-critical scenarios. The results highlight the versatility of Poisson safety functions, as well as the benefit of CBF constrained model predictive safety-critical controllers.

## 核心内容
Autonomous navigation through unstructured and dynamically-changing environments is a complex task that continues to present many challenges for modern roboticists. In particular, legged robots typically possess manipulable asymmetric geometries which must be considered during safety-critical trajectory planning. This work proposes a predictive safety filter: a nonlinear model predictive control (MPC) algorithm for online trajectory generation with geometry-aware safety constraints based on control barrier functions (CBFs). Critically, our method leverages Poisson safety functions to numerically synthesize CBF constraints directly from perception data. We extend the theoretical framework for Poisson safety functions to incorporate temporal changes in the domain by reformulating the static Dirichlet problem for Poisson's equation as a parameterized moving boundary value problem. Furthermore, we employ Minkowski set operations to lift the domain into a configuration space that accounts for robot geometry. Finally, we implement our real-time predictive safety filter on humanoid and quadruped robots in various safety-critical scenarios. The results highlight the versatility of Poisson safety functions, as well as the benefit of CBF constrained model predictive safety-critical controllers.

## 参考
- http://arxiv.org/abs/2508.11129v1

## Overview
Autonomous navigation through unstructured and dynamically-changing environments is a complex task that continues to present many challenges for modern roboticists. In particular, legged robots typically possess manipulable asymmetric geometries which must be considered during safety-critical trajectory planning. This work proposes a predictive safety filter: a nonlinear model predictive control (MPC) algorithm for online trajectory generation with geometry-aware safety constraints based on control barrier functions (CBFs). Critically, our method leverages Poisson safety functions to numerically synthesize CBF constraints directly from perception data. We extend the theoretical framework for Poisson safety functions to incorporate temporal changes in the domain by reformulating the static Dirichlet problem for Poisson's equation as a parameterized moving boundary value problem. Furthermore, we employ Minkowski set operations to lift the domain into a configuration space that accounts for robot geometry. Finally, we implement our real-time predictive safety filter on humanoid and quadruped robots in various safety-critical scenarios. The results highlight the versatility of Poisson safety functions, as well as the benefit of CBF constrained model predictive safety-critical controllers.

## Content
Autonomous navigation through unstructured and dynamically-changing environments is a complex task that continues to present many challenges for modern roboticists. In particular, legged robots typically possess manipulable asymmetric geometries which must be considered during safety-critical trajectory planning. This work proposes a predictive safety filter: a nonlinear model predictive control (MPC) algorithm for online trajectory generation with geometry-aware safety constraints based on control barrier functions (CBFs). Critically, our method leverages Poisson safety functions to numerically synthesize CBF constraints directly from perception data. We extend the theoretical framework for Poisson safety functions to incorporate temporal changes in the domain by reformulating the static Dirichlet problem for Poisson's equation as a parameterized moving boundary value problem. Furthermore, we employ Minkowski set operations to lift the domain into a configuration space that accounts for robot geometry. Finally, we implement our real-time predictive safety filter on humanoid and quadruped robots in various safety-critical scenarios. The results highlight the versatility of Poisson safety functions, as well as the benefit of CBF constrained model predictive safety-critical controllers.

## 개요
구조화되지 않고 동적으로 변화하는 환경에서의 자율 주행은 현대 로봇 공학자들에게 많은 도전 과제를 제시하는 복잡한 작업입니다. 특히, 보행 로봇은 일반적으로 조작 가능한 비대칭 형상을 가지며, 이는 안전이 중요한 궤적 계획 중에 고려되어야 합니다. 본 연구는 제어 장벽 함수(CBF)를 기반으로 형상을 인식하는 안전 제약 조건을 갖춘 온라인 궤적 생성을 위한 비선형 모델 예측 제어(MPC) 알고리즘인 예측 안전 필터를 제안합니다. 중요한 점은, 우리의 방법이 푸아송 안전 함수를 활용하여 인식 데이터로부터 직접 CBF 제약 조건을 수치적으로 합성한다는 것입니다. 우리는 푸아송 방정식에 대한 정적 디리클레 문제를 매개변수화된 이동 경계값 문제로 재구성하여 도메인의 시간적 변화를 통합하도록 푸아송 안전 함수의 이론적 프레임워크를 확장합니다. 또한, 민코프스키 집합 연산을 사용하여 로봇 형상을 고려한 구성 공간으로 도메인을 확장합니다. 마지막으로, 다양한 안전이 중요한 시나리오에서 인간형 및 사족 로봇에 실시간 예측 안전 필터를 구현합니다. 결과는 푸아송 안전 함수의 다용성과 CBF 제약 조건이 적용된 모델 예측 안전 중요 제어기의 이점을 강조합니다.

## 핵심 내용
구조화되지 않고 동적으로 변화하는 환경에서의 자율 주행은 현대 로봇 공학자들에게 많은 도전 과제를 제시하는 복잡한 작업입니다. 특히, 보행 로봇은 일반적으로 조작 가능한 비대칭 형상을 가지며, 이는 안전이 중요한 궤적 계획 중에 고려되어야 합니다. 본 연구는 제어 장벽 함수(CBF)를 기반으로 형상을 인식하는 안전 제약 조건을 갖춘 온라인 궤적 생성을 위한 비선형 모델 예측 제어(MPC) 알고리즘인 예측 안전 필터를 제안합니다. 중요한 점은, 우리의 방법이 푸아송 안전 함수를 활용하여 인식 데이터로부터 직접 CBF 제약 조건을 수치적으로 합성한다는 것입니다. 우리는 푸아송 방정식에 대한 정적 디리클레 문제를 매개변수화된 이동 경계값 문제로 재구성하여 도메인의 시간적 변화를 통합하도록 푸아송 안전 함수의 이론적 프레임워크를 확장합니다. 또한, 민코프스키 집합 연산을 사용하여 로봇 형상을 고려한 구성 공간으로 도메인을 확장합니다. 마지막으로, 다양한 안전이 중요한 시나리오에서 인간형 및 사족 로봇에 실시간 예측 안전 필터를 구현합니다. 결과는 푸아송 안전 함수의 다용성과 CBF 제약 조건이 적용된 모델 예측 안전 중요 제어기의 이점을 강조합니다.
