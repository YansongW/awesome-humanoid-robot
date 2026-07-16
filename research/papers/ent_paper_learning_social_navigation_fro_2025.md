---
$id: ent_paper_learning_social_navigation_fro_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning Social Navigation from Positive and Negative Demonstrations and Rule-Based Specifications
  zh: Learning Social Navigation from Positive and Negative Demonstrations and Rule-Based Specifications
  ko: Learning Social Navigation from Positive and Negative Demonstrations and Rule-Based Specifications
summary:
  en: Learning Social Navigation from Positive and Negative Demonstrations and Rule-Based Specifications is a 2025 work on
    navigation for humanoid robots.
  zh: Learning Social Navigation from Positive and Negative Demonstrations and Rule-Based Specifications is a 2025 work on
    navigation for humanoid robots.
  ko: Learning Social Navigation from Positive and Negative Demonstrations and Rule-Based Specifications is a 2025 work on
    navigation for humanoid robots.
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
- learning_social_navigation_fro
- navigation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2508.06779v1.
sources:
- id: src_001
  type: paper
  title: Learning Social Navigation from Positive and Negative Demonstrations and Rule-Based Specifications (arXiv)
  url: https://arxiv.org/abs/2508.06779
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Bipedal robots demonstrate potential in navigating challenging terrains through dynamic ground contact. However, current frameworks often depend solely on proprioception or use manually designed visual pipelines, which are fragile in real-world settings and complicate real-time footstep planning in unstructured environments. To address this problem, we present a vision-based hierarchical control framework that integrates a reinforcement learning high-level footstep planner, which generates footstep commands based on a local elevation map, with a low-level Operational Space Controller that tracks the generated trajectories. We utilize the Angular Momentum Linear Inverted Pendulum model to construct a low-dimensional state representation to capture an informative encoding of the dynamics while reducing complexity. We evaluate our method across different terrain conditions using the underactuated bipedal robot Cassie and investigate the capabilities and challenges of our approach through simulation and hardware experiments.

## 核心内容
Bipedal robots demonstrate potential in navigating challenging terrains through dynamic ground contact. However, current frameworks often depend solely on proprioception or use manually designed visual pipelines, which are fragile in real-world settings and complicate real-time footstep planning in unstructured environments. To address this problem, we present a vision-based hierarchical control framework that integrates a reinforcement learning high-level footstep planner, which generates footstep commands based on a local elevation map, with a low-level Operational Space Controller that tracks the generated trajectories. We utilize the Angular Momentum Linear Inverted Pendulum model to construct a low-dimensional state representation to capture an informative encoding of the dynamics while reducing complexity. We evaluate our method across different terrain conditions using the underactuated bipedal robot Cassie and investigate the capabilities and challenges of our approach through simulation and hardware experiments.

## 参考
- http://arxiv.org/abs/2508.06779v1

## Overview
Bipedal robots demonstrate potential in navigating challenging terrains through dynamic ground contact. However, current frameworks often depend solely on proprioception or use manually designed visual pipelines, which are fragile in real-world settings and complicate real-time footstep planning in unstructured environments. To address this problem, we present a vision-based hierarchical control framework that integrates a reinforcement learning high-level footstep planner, which generates footstep commands based on a local elevation map, with a low-level Operational Space Controller that tracks the generated trajectories. We utilize the Angular Momentum Linear Inverted Pendulum model to construct a low-dimensional state representation to capture an informative encoding of the dynamics while reducing complexity. We evaluate our method across different terrain conditions using the underactuated bipedal robot Cassie and investigate the capabilities and challenges of our approach through simulation and hardware experiments.

## Content
Bipedal robots demonstrate potential in navigating challenging terrains through dynamic ground contact. However, current frameworks often depend solely on proprioception or use manually designed visual pipelines, which are fragile in real-world settings and complicate real-time footstep planning in unstructured environments. To address this problem, we present a vision-based hierarchical control framework that integrates a reinforcement learning high-level footstep planner, which generates footstep commands based on a local elevation map, with a low-level Operational Space Controller that tracks the generated trajectories. We utilize the Angular Momentum Linear Inverted Pendulum model to construct a low-dimensional state representation to capture an informative encoding of the dynamics while reducing complexity. We evaluate our method across different terrain conditions using the underactuated bipedal robot Cassie and investigate the capabilities and challenges of our approach through simulation and hardware experiments.

## 개요
이족 보행 로봇은 동적 지면 접촉을 통해 험난한 지형을 탐색하는 잠재력을 보여줍니다. 그러나 현재의 프레임워크는 종종 고유 감각에만 의존하거나 수동으로 설계된 시각적 파이프라인을 사용하는데, 이는 실제 환경에서 취약하고 비정형 환경에서 실시간 발걸음 계획을 복잡하게 만듭니다. 이 문제를 해결하기 위해, 우리는 지역 고도 지도를 기반으로 발걸음 명령을 생성하는 강화 학습 기반의 고수준 발걸음 계획기와 생성된 궤적을 추적하는 저수준 작업 공간 제어기를 통합한 시각 기반 계층적 제어 프레임워크를 제시합니다. 우리는 각운동량 선형 역진자 모델을 활용하여 저차원 상태 표현을 구성함으로써 복잡성을 줄이면서 동역학의 정보적 인코딩을 포착합니다. 우리는 저구동 이족 보행 로봇 Cassie를 사용하여 다양한 지형 조건에서 방법을 평가하고, 시뮬레이션 및 하드웨어 실험을 통해 접근 방식의 능력과 과제를 조사합니다.

## 핵심 내용
이족 보행 로봇은 동적 지면 접촉을 통해 험난한 지형을 탐색하는 잠재력을 보여줍니다. 그러나 현재의 프레임워크는 종종 고유 감각에만 의존하거나 수동으로 설계된 시각적 파이프라인을 사용하는데, 이는 실제 환경에서 취약하고 비정형 환경에서 실시간 발걸음 계획을 복잡하게 만듭니다. 이 문제를 해결하기 위해, 우리는 지역 고도 지도를 기반으로 발걸음 명령을 생성하는 강화 학습 기반의 고수준 발걸음 계획기와 생성된 궤적을 추적하는 저수준 작업 공간 제어기를 통합한 시각 기반 계층적 제어 프레임워크를 제시합니다. 우리는 각운동량 선형 역진자 모델을 활용하여 저차원 상태 표현을 구성함으로써 복잡성을 줄이면서 동역학의 정보적 인코딩을 포착합니다. 우리는 저구동 이족 보행 로봇 Cassie를 사용하여 다양한 지형 조건에서 방법을 평가하고, 시뮬레이션 및 하드웨어 실험을 통해 접근 방식의 능력과 과제를 조사합니다.
