---
$id: ent_paper_learning_differentiable_reacha_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning Differentiable Reachability Maps for Optimization-based Humanoid Motion Generation
  zh: Learning Differentiable Reachability Maps for Optimization-based Humanoid Motion Generation
  ko: Learning Differentiable Reachability Maps for Optimization-based Humanoid Motion Generation
summary:
  en: Learning Differentiable Reachability Maps for Optimization-based Humanoid Motion Generation is a 2025 work on loco-manipulation
    and whole-body-control for humanoid robots.
  zh: Learning Differentiable Reachability Maps for Optimization-based Humanoid Motion Generation is a 2025 work on loco-manipulation
    and whole-body-control for humanoid robots.
  ko: Learning Differentiable Reachability Maps for Optimization-based Humanoid Motion Generation is a 2025 work on loco-manipulation
    and whole-body-control for humanoid robots.
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
- learning_differentiable_reacha
- loco_manipulation
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2508.11275v1.
sources:
- id: src_001
  type: paper
  title: Learning Differentiable Reachability Maps for Optimization-based Humanoid Motion Generation (arXiv)
  url: https://arxiv.org/abs/2508.11275
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
To reduce the computational cost of humanoid motion generation, we introduce a new approach to representing robot kinematic reachability: the differentiable reachability map. This map is a scalar-valued function defined in the task space that takes positive values only in regions reachable by the robot's end-effector. A key feature of this representation is that it is continuous and differentiable with respect to task-space coordinates, enabling its direct use as constraints in continuous optimization for humanoid motion planning. We describe a method to learn such differentiable reachability maps from a set of end-effector poses generated using a robot's kinematic model, using either a neural network or a support vector machine as the learning model. By incorporating the learned reachability map as a constraint, we formulate humanoid motion generation as a continuous optimization problem. We demonstrate that the proposed approach efficiently solves various motion planning problems, including footstep planning, multi-contact motion planning, and loco-manipulation planning for humanoid robots.

## 核心内容
To reduce the computational cost of humanoid motion generation, we introduce a new approach to representing robot kinematic reachability: the differentiable reachability map. This map is a scalar-valued function defined in the task space that takes positive values only in regions reachable by the robot's end-effector. A key feature of this representation is that it is continuous and differentiable with respect to task-space coordinates, enabling its direct use as constraints in continuous optimization for humanoid motion planning. We describe a method to learn such differentiable reachability maps from a set of end-effector poses generated using a robot's kinematic model, using either a neural network or a support vector machine as the learning model. By incorporating the learned reachability map as a constraint, we formulate humanoid motion generation as a continuous optimization problem. We demonstrate that the proposed approach efficiently solves various motion planning problems, including footstep planning, multi-contact motion planning, and loco-manipulation planning for humanoid robots.

## 参考
- http://arxiv.org/abs/2508.11275v1

## Overview
To reduce the computational cost of humanoid motion generation, we introduce a new approach to representing robot kinematic reachability: the differentiable reachability map. This map is a scalar-valued function defined in the task space that takes positive values only in regions reachable by the robot's end-effector. A key feature of this representation is that it is continuous and differentiable with respect to task-space coordinates, enabling its direct use as constraints in continuous optimization for humanoid motion planning. We describe a method to learn such differentiable reachability maps from a set of end-effector poses generated using a robot's kinematic model, using either a neural network or a support vector machine as the learning model. By incorporating the learned reachability map as a constraint, we formulate humanoid motion generation as a continuous optimization problem. We demonstrate that the proposed approach efficiently solves various motion planning problems, including footstep planning, multi-contact motion planning, and loco-manipulation planning for humanoid robots.

## Content
To reduce the computational cost of humanoid motion generation, we introduce a new approach to representing robot kinematic reachability: the differentiable reachability map. This map is a scalar-valued function defined in the task space that takes positive values only in regions reachable by the robot's end-effector. A key feature of this representation is that it is continuous and differentiable with respect to task-space coordinates, enabling its direct use as constraints in continuous optimization for humanoid motion planning. We describe a method to learn such differentiable reachability maps from a set of end-effector poses generated using a robot's kinematic model, using either a neural network or a support vector machine as the learning model. By incorporating the learned reachability map as a constraint, we formulate humanoid motion generation as a continuous optimization problem. We demonstrate that the proposed approach efficiently solves various motion planning problems, including footstep planning, multi-contact motion planning, and loco-manipulation planning for humanoid robots.

## 개요
휴머노이드 동작 생성의 계산 비용을 줄이기 위해, 우리는 로봇의 운동학적 도달 가능성을 표현하는 새로운 접근 방식인 미분 가능 도달 가능성 맵(differentiable reachability map)을 소개합니다. 이 맵은 작업 공간(task space)에서 정의된 스칼라 값 함수로, 로봇의 엔드 이펙터가 도달할 수 있는 영역에서만 양의 값을 가집니다. 이 표현의 핵심 특징은 작업 공간 좌표에 대해 연속적이고 미분 가능하여, 휴머노이드 동작 계획을 위한 연속 최적화에서 제약 조건으로 직접 사용할 수 있다는 점입니다. 우리는 로봇의 운동학적 모델을 사용하여 생성된 엔드 이펙터 자세 집합으로부터 이러한 미분 가능 도달 가능성 맵을 학습하는 방법을 설명하며, 학습 모델로는 신경망 또는 서포트 벡터 머신을 사용합니다. 학습된 도달 가능성 맵을 제약 조건으로 통합함으로써, 휴머노이드 동작 생성을 연속 최적화 문제로 정식화합니다. 우리는 제안된 접근 방식이 보행 계획(footstep planning), 다중 접촉 동작 계획(multi-contact motion planning), 그리고 휴머노이드 로봇의 이동-조작 계획(loco-manipulation planning)을 포함한 다양한 동작 계획 문제를 효율적으로 해결함을 입증합니다.

## 핵심 내용
휴머노이드 동작 생성의 계산 비용을 줄이기 위해, 우리는 로봇의 운동학적 도달 가능성을 표현하는 새로운 접근 방식인 미분 가능 도달 가능성 맵(differentiable reachability map)을 소개합니다. 이 맵은 작업 공간(task space)에서 정의된 스칼라 값 함수로, 로봇의 엔드 이펙터가 도달할 수 있는 영역에서만 양의 값을 가집니다. 이 표현의 핵심 특징은 작업 공간 좌표에 대해 연속적이고 미분 가능하여, 휴머노이드 동작 계획을 위한 연속 최적화에서 제약 조건으로 직접 사용할 수 있다는 점입니다. 우리는 로봇의 운동학적 모델을 사용하여 생성된 엔드 이펙터 자세 집합으로부터 이러한 미분 가능 도달 가능성 맵을 학습하는 방법을 설명하며, 학습 모델로는 신경망 또는 서포트 벡터 머신을 사용합니다. 학습된 도달 가능성 맵을 제약 조건으로 통합함으로써, 휴머노이드 동작 생성을 연속 최적화 문제로 정식화합니다. 우리는 제안된 접근 방식이 보행 계획(footstep planning), 다중 접촉 동작 계획(multi-contact motion planning), 그리고 휴머노이드 로봇의 이동-조작 계획(loco-manipulation planning)을 포함한 다양한 동작 계획 문제를 효율적으로 해결함을 입증합니다.
