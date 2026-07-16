---
$id: ent_paper_cervettini_a_framework_for_optimal_ankle_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: A Framework for Optimal Ankle Design of Humanoid Robots
  zh: 人形机器人踝关节最优设计框架
  ko: 휴머노이드 로봇을 위한 최적 발목 설계 프레임워크
summary:
  en: Proposes a unified methodology for designing and evaluating parallel ankle mechanisms for humanoid robots, using multi-objective
    optimization and a scalar cost function to compare SPU and RSU architectures, validated by redesigning an existing robot
    ankle.
  zh: The design of the humanoid ankle is critical for safe and efficient ground interaction. Key factors such as mechanical
    compliance and motor mass distribution have driven the adoption of parallel mechanism architectures. However, selecting
    the optimal configuration depends on both actuator availability and task requirements. We propose a unified methodology
    for the design and evaluation of parallel ankle mechanisms. A multi-objective optimization synthesizes the mechanism geometry,
    the resulting solutions are evaluated using a scalar cost function that aggregates key performance metrics for cro
  ko: 휴머노이드 로봇을 위한 병렬 발목 메커니즘의 설계 및 평가를 위한 통합 방법론을 제안하며, 다목적 최적화와 스칼라 비용 함수를 활용해 SPU 및 RSU 아키텍처를 비교하고 기존 로봇 발목의 재설계를 통해 검증한다.
domains:
- 02_components
- 06_design_engineering
layers:
- midstream
- upstream
functional_roles:
- knowledge
tags:
- parallel_ankle_mechanism
- spu_architecture
- rsu_architecture
- multi_objective_optimization
- ankle_design
- humanoid_locomotion
- kinematics
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.16469v1.
sources:
- id: src_001
  type: paper
  title: A Framework for Optimal Ankle Design of Humanoid Robots
  url: https://arxiv.org/abs/2509.16469
  date: '2025'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
---

## 概述
The design of the humanoid ankle is critical for safe and efficient ground interaction. Key factors such as mechanical compliance and motor mass distribution have driven the adoption of parallel mechanism architectures. However, selecting the optimal configuration depends on both actuator availability and task requirements. We propose a unified methodology for the design and evaluation of parallel ankle mechanisms. A multi-objective optimization synthesizes the mechanism geometry, the resulting solutions are evaluated using a scalar cost function that aggregates key performance metrics for cross-architecture comparison. We focus on two representative architectures: the Spherical-Prismatic-Universal (SPU) and the Revolute-Spherical-Universal (RSU). For both, we resolve the kinematics, and for the RSU, introduce a parameterization that ensures workspace feasibility and accelerates optimization. We validate our approach by redesigning the ankle of an existing humanoid robot. The optimized RSU consistently outperforms both the original serial design and a conventionally engineered RSU, reducing the cost function by up to 41% and 14%, respectively.

## 核心内容
The design of the humanoid ankle is critical for safe and efficient ground interaction. Key factors such as mechanical compliance and motor mass distribution have driven the adoption of parallel mechanism architectures. However, selecting the optimal configuration depends on both actuator availability and task requirements. We propose a unified methodology for the design and evaluation of parallel ankle mechanisms. A multi-objective optimization synthesizes the mechanism geometry, the resulting solutions are evaluated using a scalar cost function that aggregates key performance metrics for cross-architecture comparison. We focus on two representative architectures: the Spherical-Prismatic-Universal (SPU) and the Revolute-Spherical-Universal (RSU). For both, we resolve the kinematics, and for the RSU, introduce a parameterization that ensures workspace feasibility and accelerates optimization. We validate our approach by redesigning the ankle of an existing humanoid robot. The optimized RSU consistently outperforms both the original serial design and a conventionally engineered RSU, reducing the cost function by up to 41% and 14%, respectively.

## 参考
- http://arxiv.org/abs/2509.16469v1

## Overview
The design of the humanoid ankle is critical for safe and efficient ground interaction. Key factors such as mechanical compliance and motor mass distribution have driven the adoption of parallel mechanism architectures. However, selecting the optimal configuration depends on both actuator availability and task requirements. We propose a unified methodology for the design and evaluation of parallel ankle mechanisms. A multi-objective optimization synthesizes the mechanism geometry, and the resulting solutions are evaluated using a scalar cost function that aggregates key performance metrics for cross-architecture comparison. We focus on two representative architectures: the Spherical-Prismatic-Universal (SPU) and the Revolute-Spherical-Universal (RSU). For both, we resolve the kinematics, and for the RSU, introduce a parameterization that ensures workspace feasibility and accelerates optimization. We validate our approach by redesigning the ankle of an existing humanoid robot. The optimized RSU consistently outperforms both the original serial design and a conventionally engineered RSU, reducing the cost function by up to 41% and 14%, respectively.

## Content
The design of the humanoid ankle is critical for safe and efficient ground interaction. Key factors such as mechanical compliance and motor mass distribution have driven the adoption of parallel mechanism architectures. However, selecting the optimal configuration depends on both actuator availability and task requirements. We propose a unified methodology for the design and evaluation of parallel ankle mechanisms. A multi-objective optimization synthesizes the mechanism geometry, and the resulting solutions are evaluated using a scalar cost function that aggregates key performance metrics for cross-architecture comparison. We focus on two representative architectures: the Spherical-Prismatic-Universal (SPU) and the Revolute-Spherical-Universal (RSU). For both, we resolve the kinematics, and for the RSU, introduce a parameterization that ensures workspace feasibility and accelerates optimization. We validate our approach by redesigning the ankle of an existing humanoid robot. The optimized RSU consistently outperforms both the original serial design and a conventionally engineered RSU, reducing the cost function by up to 41% and 14%, respectively.

## 개요
인간형 로봇 발목의 설계는 안전하고 효율적인 지면 상호작용에 매우 중요합니다. 기계적 컴플라이언스와 모터 질량 분포와 같은 주요 요소들은 병렬 메커니즘 구조의 채택을 이끌었습니다. 그러나 최적의 구성을 선택하는 것은 액추에이터 가용성과 작업 요구사항 모두에 달려 있습니다. 우리는 병렬 발목 메커니즘의 설계 및 평가를 위한 통합 방법론을 제안합니다. 다중 목적 최적화가 메커니즘 형상을 종합하며, 결과 솔루션은 아키텍처 간 비교를 위한 주요 성능 지표를 집계하는 스칼라 비용 함수를 사용하여 평가됩니다. 우리는 두 가지 대표적인 아키텍처인 구형-프리즈매틱-유니버설(SPU)과 회전-구형-유니버설(RSU)에 초점을 맞춥니다. 두 경우 모두 운동학을 해결하고, RSU의 경우 작업 공간 실현 가능성을 보장하고 최적화를 가속화하는 매개변수화를 도입합니다. 우리는 기존 인간형 로봇의 발목을 재설계하여 접근 방식을 검증합니다. 최적화된 RSU는 원래의 직렬 설계와 기존 방식으로 설계된 RSU를 모두 일관되게 능가하며, 비용 함수를 각각 최대 41% 및 14%까지 줄입니다.

## 핵심 내용
인간형 로봇 발목의 설계는 안전하고 효율적인 지면 상호작용에 매우 중요합니다. 기계적 컴플라이언스와 모터 질량 분포와 같은 주요 요소들은 병렬 메커니즘 구조의 채택을 이끌었습니다. 그러나 최적의 구성을 선택하는 것은 액추에이터 가용성과 작업 요구사항 모두에 달려 있습니다. 우리는 병렬 발목 메커니즘의 설계 및 평가를 위한 통합 방법론을 제안합니다. 다중 목적 최적화가 메커니즘 형상을 종합하며, 결과 솔루션은 아키텍처 간 비교를 위한 주요 성능 지표를 집계하는 스칼라 비용 함수를 사용하여 평가됩니다. 우리는 두 가지 대표적인 아키텍처인 구형-프리즈매틱-유니버설(SPU)과 회전-구형-유니버설(RSU)에 초점을 맞춥니다. 두 경우 모두 운동학을 해결하고, RSU의 경우 작업 공간 실현 가능성을 보장하고 최적화를 가속화하는 매개변수화를 도입합니다. 우리는 기존 인간형 로봇의 발목을 재설계하여 접근 방식을 검증합니다. 최적화된 RSU는 원래의 직렬 설계와 기존 방식으로 설계된 RSU를 모두 일관되게 능가하며, 비용 함수를 각각 최대 41% 및 14%까지 줄입니다.
