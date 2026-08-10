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
  zh: 本文提出一种用于人形机器人并联踝关节设计的统一方法论，通过多目标优化与标量成本函数比较SPU与RSU两种架构，并在现有机器人踝关节的重新设计中验证，优化后的RSU架构将成本函数降低高达41%。
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.16469v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (738 chars, DeepSeek).'
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
人形机器人踝关节设计对安全高效的地面交互至关重要，机械柔顺性与电机质量分布促使并联机构被广泛采用。本文提出一种统一方法论，通过多目标优化综合机构几何参数，并利用标量成本函数聚合关键性能指标，实现跨架构比较。研究聚焦于SPU与RSU两种代表性架构，解析其运动学，并为RSU引入参数化方法以确保工作空间可行性并加速优化。通过重新设计现有机器人踝关节，验证了该方法的有效性。

## 核心内容
### 背景与动机
人形机器人踝关节的设计直接影响地面交互的安全性与效率。关键因素如机械柔顺性和电机质量分布，推动了并联机构架构的采用。然而，最优配置的选择取决于执行器可用性与任务需求。

### 方法论
- 提出一种统一方法论，用于并联踝关节机构的设计与评估。
- 通过多目标优化综合机构几何参数，生成多种设计方案。
- 使用标量成本函数聚合关键性能指标，实现跨架构比较。

### 架构分析
- 聚焦两种代表性架构：Spherical-Prismatic-Universal (SPU) 与 Revolute-Spherical-Universal (RSU)。
- 对两种架构均解析其运动学。
- 针对RSU架构，引入参数化方法，确保工作空间可行性并加速优化过程。

### 实验验证
- 通过重新设计现有的人形机器人踝关节，验证该方法的有效性。
- 优化后的RSU架构在性能上持续优于原始串联设计，成本函数降低高达41%。
- 与常规工程设计的RSU相比，优化后的RSU将成本函数进一步降低14%。

### 结论
本文提出的统一方法论为并联踝关节设计提供了系统化框架，优化后的RSU架构在性能上显著优于传统设计，验证了多目标优化与标量成本函数在跨架构比较中的有效性。

## Overview
The design of the humanoid ankle is critical for safe and efficient ground interaction. Key factors such as mechanical compliance and motor mass distribution have driven the adoption of parallel mechanism architectures. However, selecting the optimal configuration depends on both actuator availability and task requirements. We propose a unified methodology for the design and evaluation of parallel ankle mechanisms. A multi-objective optimization synthesizes the mechanism geometry, the resulting solutions are evaluated using a scalar cost function that aggregates key performance metrics for cross-architecture comparison. We focus on two representative architectures: the Spherical-Prismatic-Universal (SPU) and the Revolute-Spherical-Universal (RSU). For both, we resolve the kinematics, and for the RSU, introduce a parameterization that ensures workspace feasibility and accelerates optimization. We validate our approach by redesigning the ankle of an existing humanoid robot. The optimized RSU consistently outperforms both the original serial design and a conventionally engineered RSU, reducing the cost function by up to 41% and 14%, respectively.

## Overview
The design of the humanoid ankle is critical for safe and efficient ground interaction. Key factors such as mechanical compliance and motor mass distribution have driven the adoption of parallel mechanism architectures. However, selecting the optimal configuration depends on both actuator availability and task requirements. We propose a unified methodology for the design and evaluation of parallel ankle mechanisms. A multi-objective optimization synthesizes the mechanism geometry, and the resulting solutions are evaluated using a scalar cost function that aggregates key performance metrics for cross-architecture comparison. We focus on two representative architectures: the Spherical-Prismatic-Universal (SPU) and the Revolute-Spherical-Universal (RSU). For both, we resolve the kinematics, and for the RSU, introduce a parameterization that ensures workspace feasibility and accelerates optimization. We validate our approach by redesigning the ankle of an existing humanoid robot. The optimized RSU consistently outperforms both the original serial design and a conventionally engineered RSU, reducing the cost function by up to 41% and 14%, respectively.

## Content
The design of the humanoid ankle is critical for safe and efficient ground interaction. Key factors such as mechanical compliance and motor mass distribution have driven the adoption of parallel mechanism architectures. However, selecting the optimal configuration depends on both actuator availability and task requirements. We propose a unified methodology for the design and evaluation of parallel ankle mechanisms. A multi-objective optimization synthesizes the mechanism geometry, and the resulting solutions are evaluated using a scalar cost function that aggregates key performance metrics for cross-architecture comparison. We focus on two representative architectures: the Spherical-Prismatic-Universal (SPU) and the Revolute-Spherical-Universal (RSU). For both, we resolve the kinematics, and for the RSU, introduce a parameterization that ensures workspace feasibility and accelerates optimization. We validate our approach by redesigning the ankle of an existing humanoid robot. The optimized RSU consistently outperforms both the original serial design and a conventionally engineered RSU, reducing the cost function by up to 41% and 14%, respectively.

## 参考
- http://arxiv.org/abs/2509.16469v1

## 개요
휴머노이드 로봇 발목 관절 설계는 안전하고 효율적인 지면 상호작용에至关重要하며, 기계적 유연성과 모터 질량 분포로 인해 병렬 메커니즘이 널리 채택되고 있습니다. 본 논문은 다목적 최적화를 통해 메커니즘 기하 파라미터를 종합하고, 스칼라 비용 함수로 핵심 성능 지표를 집계하여 아키텍처 간 비교를 가능하게 하는 통합 방법론을 제안합니다. 연구는 SPU와 RSU 두 가지 대표적 아키텍처에 초점을 맞추어 운동학을 해석하고, RSU에 파라미터화 방법을 도입하여 작업 공간 실현 가능성을 보장하고 최적화를 가속화합니다. 기존 로봇 발목 관절을 재설계함으로써 이 방법의 유효성을 검증합니다.

## 핵심 내용
### 배경 및 동기
휴머노이드 로봇 발목 관절의 설계는 지면 상호작용의 안전성과 효율성에 직접적인 영향을 미칩니다. 기계적 유연성과 모터 질량 분포와 같은 핵심 요소는 병렬 메커니즘 아키텍처의 채택을 촉진합니다. 그러나 최적 구성의 선택은 액추에이터 가용성과 작업 요구 사항에 따라 달라집니다.

### 방법론
- 병렬 발목 관절 메커니즘의 설계 및 평가를 위한 통합 방법론을 제안합니다.
- 다목적 최적화를 통해 메커니즘 기하 파라미터를 종합하여 다양한 설계 대안을 생성합니다.
- 스칼라 비용 함수를 사용하여 핵심 성능 지표를 집계하고 아키텍처 간 비교를 가능하게 합니다.

### 아키텍처 분석
- 두 가지 대표적 아키텍처에 초점: Spherical-Prismatic-Universal (SPU) 및 Revolute-Spherical-Universal (RSU).
- 두 아키텍처 모두에 대해 운동학을 해석합니다.
- RSU 아키텍처의 경우 파라미터화 방법을 도입하여 작업 공간 실현 가능성을 보장하고 최적화 프로세스를 가속화합니다.

### 실험 검증
- 기존 휴머노이드 로봇 발목 관절을 재설계함으로써 이 방법의 유효성을 검증합니다.
- 최적화된 RSU 아키텍처는 원래 직렬 설계보다 지속적으로 우수한 성능을 보이며, 비용 함수가 최대 41% 감소합니다.
- 일반적인 엔지니어링 설계의 RSU와 비교하여, 최적화된 RSU는 비용 함수를 추가로 14% 감소시킵니다.

### 결론
본 논문에서 제안한 통합 방법론은 병렬 발목 관절 설계를 위한 체계적 프레임워크를 제공하며, 최적화된 RSU 아키텍처는 전통적 설계보다 성능이 현저히 우수하여 다목적 최적화와 스칼라 비용 함수의 아키텍처 간 비교에서의 유효성을 검증합니다.
