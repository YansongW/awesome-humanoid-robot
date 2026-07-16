---
$id: ent_paper_dexterous_safe_control_for_hum_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Dexterous Safe Control for Humanoids in Cluttered Environments via Projected Safe Set Algorithm
  zh: Dexterous Safe Control for Humanoids in Cluttered Environments via Projected Safe Set Algorithm
  ko: Dexterous Safe Control for Humanoids in Cluttered Environments via Projected Safe Set Algorithm
summary:
  en: Dexterous Safe Control for Humanoids in Cluttered Environments via Projected Safe Set Algorithm is a 2025 work on manipulation
    for humanoid robots.
  zh: Dexterous Safe Control for Humanoids in Cluttered Environments via Projected Safe Set Algorithm is a 2025 work on manipulation
    for humanoid robots.
  ko: Dexterous Safe Control for Humanoids in Cluttered Environments via Projected Safe Set Algorithm is a 2025 work on manipulation
    for humanoid robots.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- dexterous_safe_control_for_hum
- humanoid
- manipulation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2502.02858v1.
sources:
- id: src_001
  type: paper
  title: Dexterous Safe Control for Humanoids in Cluttered Environments via Projected Safe Set Algorithm (arXiv)
  url: https://arxiv.org/abs/2502.02858
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
It is critical to ensure safety for humanoid robots in real-world applications without compromising performance. In this paper, we consider the problem of dexterous safety, featuring limb-level geometry constraints for avoiding both external and self-collisions in cluttered environments. Compared to safety with simplified bounding geometries in sprase environments, dexterous safety produces numerous constraints which often lead to infeasible constraint sets when solving for safe robot control. To address this issue, we propose Projected Safe Set Algorithm (p-SSA), an extension of classical safe control algorithms to multi-constraint cases. p-SSA relaxes conflicting constraints in a principled manner, minimizing safety violations to guarantee feasible robot control. We verify our approach in simulation and on a real Unitree G1 humanoid robot performing complex collision avoidance tasks. Results show that p-SSA enables the humanoid to operate robustly in challenging situations with minimal safety violations and directly generalizes to various tasks with zero parameter tuning.

## 核心内容
It is critical to ensure safety for humanoid robots in real-world applications without compromising performance. In this paper, we consider the problem of dexterous safety, featuring limb-level geometry constraints for avoiding both external and self-collisions in cluttered environments. Compared to safety with simplified bounding geometries in sprase environments, dexterous safety produces numerous constraints which often lead to infeasible constraint sets when solving for safe robot control. To address this issue, we propose Projected Safe Set Algorithm (p-SSA), an extension of classical safe control algorithms to multi-constraint cases. p-SSA relaxes conflicting constraints in a principled manner, minimizing safety violations to guarantee feasible robot control. We verify our approach in simulation and on a real Unitree G1 humanoid robot performing complex collision avoidance tasks. Results show that p-SSA enables the humanoid to operate robustly in challenging situations with minimal safety violations and directly generalizes to various tasks with zero parameter tuning.

## 参考
- http://arxiv.org/abs/2502.02858v1

## Overview
It is critical to ensure safety for humanoid robots in real-world applications without compromising performance. In this paper, we consider the problem of dexterous safety, featuring limb-level geometry constraints for avoiding both external and self-collisions in cluttered environments. Compared to safety with simplified bounding geometries in sparse environments, dexterous safety produces numerous constraints which often lead to infeasible constraint sets when solving for safe robot control. To address this issue, we propose Projected Safe Set Algorithm (p-SSA), an extension of classical safe control algorithms to multi-constraint cases. p-SSA relaxes conflicting constraints in a principled manner, minimizing safety violations to guarantee feasible robot control. We verify our approach in simulation and on a real Unitree G1 humanoid robot performing complex collision avoidance tasks. Results show that p-SSA enables the humanoid to operate robustly in challenging situations with minimal safety violations and directly generalizes to various tasks with zero parameter tuning.

## Content
It is critical to ensure safety for humanoid robots in real-world applications without compromising performance. In this paper, we consider the problem of dexterous safety, featuring limb-level geometry constraints for avoiding both external and self-collisions in cluttered environments. Compared to safety with simplified bounding geometries in sparse environments, dexterous safety produces numerous constraints which often lead to infeasible constraint sets when solving for safe robot control. To address this issue, we propose Projected Safe Set Algorithm (p-SSA), an extension of classical safe control algorithms to multi-constraint cases. p-SSA relaxes conflicting constraints in a principled manner, minimizing safety violations to guarantee feasible robot control. We verify our approach in simulation and on a real Unitree G1 humanoid robot performing complex collision avoidance tasks. Results show that p-SSA enables the humanoid to operate robustly in challenging situations with minimal safety violations and directly generalizes to various tasks with zero parameter tuning.

## 개요
휴머노이드 로봇이 실제 환경에서 성능 저하 없이 안전을 보장하는 것은 매우 중요합니다. 본 논문에서는 혼잡한 환경에서 외부 충돌 및 자체 충돌을 모두 회피하기 위한 팔다리 수준의 기하학적 제약 조건을 특징으로 하는 정밀 안전 문제를 다룹니다. 희소 환경에서 단순화된 경계 기하학을 사용한 안전과 비교할 때, 정밀 안전은 수많은 제약 조건을 생성하며, 이는 종종 안전한 로봇 제어를 해결할 때 실행 불가능한 제약 조건 집합으로 이어집니다. 이 문제를 해결하기 위해, 우리는 고전적인 안전 제어 알고리즘을 다중 제약 조건 사례로 확장한 Projected Safe Set Algorithm (p-SSA)을 제안합니다. p-SSA는 원칙적인 방식으로 충돌하는 제약 조건을 완화하여 안전 위반을 최소화하고 실행 가능한 로봇 제어를 보장합니다. 우리는 시뮬레이션과 실제 Unitree G1 휴머노이드 로봇이 복잡한 충돌 회피 작업을 수행하는 환경에서 접근 방식을 검증합니다. 결과는 p-SSA가 휴머노이드가 최소한의 안전 위반으로 어려운 상황에서 강건하게 작동할 수 있게 하며, 매개변수 조정 없이 다양한 작업에 직접 일반화됨을 보여줍니다.

## 핵심 내용
휴머노이드 로봇이 실제 환경에서 성능 저하 없이 안전을 보장하는 것은 매우 중요합니다. 본 논문에서는 혼잡한 환경에서 외부 충돌 및 자체 충돌을 모두 회피하기 위한 팔다리 수준의 기하학적 제약 조건을 특징으로 하는 정밀 안전 문제를 다룹니다. 희소 환경에서 단순화된 경계 기하학을 사용한 안전과 비교할 때, 정밀 안전은 수많은 제약 조건을 생성하며, 이는 종종 안전한 로봇 제어를 해결할 때 실행 불가능한 제약 조건 집합으로 이어집니다. 이 문제를 해결하기 위해, 우리는 고전적인 안전 제어 알고리즘을 다중 제약 조건 사례로 확장한 Projected Safe Set Algorithm (p-SSA)을 제안합니다. p-SSA는 원칙적인 방식으로 충돌하는 제약 조건을 완화하여 안전 위반을 최소화하고 실행 가능한 로봇 제어를 보장합니다. 우리는 시뮬레이션과 실제 Unitree G1 휴머노이드 로봇이 복잡한 충돌 회피 작업을 수행하는 환경에서 접근 방식을 검증합니다. 결과는 p-SSA가 휴머노이드가 최소한의 안전 위반으로 어려운 상황에서 강건하게 작동할 수 있게 하며, 매개변수 조정 없이 다양한 작업에 직접 일반화됨을 보여줍니다.
