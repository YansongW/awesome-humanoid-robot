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
  en: Proposes a unified methodology for designing and evaluating parallel ankle mechanisms
    for humanoid robots, using multi-objective optimization and a scalar cost function
    to compare SPU and RSU architectures, validated by redesigning an existing robot
    ankle.
  zh: 提出了一种用于设计和评估人形机器人并联踝关节机构的统一方法，通过多目标优化和标量成本函数比较SPU与RSU架构，并通过重新设计现有机器人踝关节进行验证。
  ko: 휴머노이드 로봇을 위한 병렬 발목 메커니즘의 설계 및 평가를 위한 통합 방법론을 제안하며, 다목적 최적화와 스칼라 비용 함수를 활용해 SPU
    및 RSU 아키텍처를 비교하고 기존 로봇 발목의 재설계를 통해 검증한다.
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
  reviewed_at: '2026-06-28'
  confidence: medium
  notes: AI-extracted from abstract and provided metadata; requires human review of
    the full paper before verification.
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

## Overview

The paper presents a unified methodology for designing and evaluating parallel ankle mechanisms for humanoid robots. It couples closed-form inverse kinematics with multi-objective NSGA-II optimization to synthesize mechanism geometry, then ranks candidate solutions with a scalar cost function that normalizes key performance metrics across architectures and actuators. The framework is demonstrated on two representative parallel ankle architectures—the Spherical-Prismatic-Universal (SPU) and the Revolute-Spherical-Universal (RSU)—and validated by redesigning the ankle of an existing humanoid robot.

For both architectures the authors derive the inverse kinematics, and for the RSU they introduce a parameterization that enforces workspace feasibility over the desired operational region. The cost function is applied after optimization to compare the resulting designs against a baseline serial ankle and against a conventionally engineered RSU, showing reductions in the aggregated cost of up to 41% and 14%, respectively.

## Key Contributions

- Unified methodology for the design and comparative evaluation of parallel ankle mechanisms
- Closed-form inverse kinematics for SPU and RSU ankle architectures
- Novel RSU parameterization that guarantees workspace feasibility over the desired operational region
- Scalar cost function aggregating architecture-agnostic performance metrics for cross-actuator comparison
- Validation by redesigning an existing humanoid robot ankle, demonstrating up to 41% cost reduction over a serial design and 14% over a conventional RSU

## Relevance to Humanoid Robotics

The ankle is one of the most mechanically stressed joints in a humanoid robot because it must transmit ground reaction forces while enabling stable locomotion over uneven terrain. The paper directly supports humanoid hardware development by providing a quantitative, actuator-aware framework for selecting and tuning parallel ankle architectures. By making architecture selection and mass-distribution decisions more systematic, the work can shorten design iterations and inform scalable production choices for humanoid locomotion platforms.
