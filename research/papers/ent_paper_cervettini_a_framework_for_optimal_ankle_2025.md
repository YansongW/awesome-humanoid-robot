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
  zh: 提出了一种用于设计和评估人形机器人并联踝关节机构的统一方法，通过多目标优化和标量成本函数比较SPU与RSU架构，并通过重新设计现有机器人踝关节进行验证。
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

