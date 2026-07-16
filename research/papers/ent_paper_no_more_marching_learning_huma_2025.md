---
$id: ent_paper_no_more_marching_learning_huma_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'No More Marching: Learning Humanoid Locomotion for Short-Range SE(2) Targets'
  zh: 'No More Marching: Learning Humanoid Locomotion for Short-Range SE(2) Targets'
  ko: 'No More Marching: Learning Humanoid Locomotion for Short-Range SE(2) Targets'
summary:
  en: 'No More Marching: Learning Humanoid Locomotion for Short-Range SE(2) Targets is a 2025 work on locomotion for humanoid
    robots.'
  zh: 'No More Marching: Learning Humanoid Locomotion for Short-Range SE(2) Targets is a 2025 work on locomotion for humanoid
    robots.'
  ko: 'No More Marching: Learning Humanoid Locomotion for Short-Range SE(2) Targets is a 2025 work on locomotion for humanoid
    robots.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- locomotion
- no_more_marching
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2508.14098v2.
sources:
- id: src_001
  type: paper
  title: 'No More Marching: Learning Humanoid Locomotion for Short-Range SE(2) Targets (arXiv)'
  url: https://arxiv.org/abs/2508.14098
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Humanoids operating in real-world workspaces must frequently execute task-driven, short-range movements to SE(2) target poses. To be practical, these transitions must be fast, robust, and energy efficient. While learning-based locomotion has made significant progress, most existing methods optimize for velocity-tracking rather than direct pose reaching, resulting in inefficient, marching-style behavior when applied to short-range tasks. In this work, we develop a reinforcement learning approach that directly optimizes humanoid locomotion for SE(2) targets. Central to this approach is a new constellation-based reward function that encourages natural and efficient target-oriented movement. To evaluate performance, we introduce a benchmarking framework that measures energy consumption, time-to-target, and footstep count on a distribution of SE(2) goals. Our results show that the proposed approach consistently outperforms standard methods and enables successful transfer from simulation to hardware, highlighting the importance of targeted reward design for practical short-range humanoid locomotion.

## 核心内容
Humanoids operating in real-world workspaces must frequently execute task-driven, short-range movements to SE(2) target poses. To be practical, these transitions must be fast, robust, and energy efficient. While learning-based locomotion has made significant progress, most existing methods optimize for velocity-tracking rather than direct pose reaching, resulting in inefficient, marching-style behavior when applied to short-range tasks. In this work, we develop a reinforcement learning approach that directly optimizes humanoid locomotion for SE(2) targets. Central to this approach is a new constellation-based reward function that encourages natural and efficient target-oriented movement. To evaluate performance, we introduce a benchmarking framework that measures energy consumption, time-to-target, and footstep count on a distribution of SE(2) goals. Our results show that the proposed approach consistently outperforms standard methods and enables successful transfer from simulation to hardware, highlighting the importance of targeted reward design for practical short-range humanoid locomotion.

## 参考
- http://arxiv.org/abs/2508.14098v2

## Overview
Humanoids operating in real-world workspaces must frequently execute task-driven, short-range movements to SE(2) target poses. To be practical, these transitions must be fast, robust, and energy efficient. While learning-based locomotion has made significant progress, most existing methods optimize for velocity-tracking rather than direct pose reaching, resulting in inefficient, marching-style behavior when applied to short-range tasks. In this work, we develop a reinforcement learning approach that directly optimizes humanoid locomotion for SE(2) targets. Central to this approach is a new constellation-based reward function that encourages natural and efficient target-oriented movement. To evaluate performance, we introduce a benchmarking framework that measures energy consumption, time-to-target, and footstep count on a distribution of SE(2) goals. Our results show that the proposed approach consistently outperforms standard methods and enables successful transfer from simulation to hardware, highlighting the importance of targeted reward design for practical short-range humanoid locomotion.

## Content
Humanoids operating in real-world workspaces must frequently execute task-driven, short-range movements to SE(2) target poses. To be practical, these transitions must be fast, robust, and energy efficient. While learning-based locomotion has made significant progress, most existing methods optimize for velocity-tracking rather than direct pose reaching, resulting in inefficient, marching-style behavior when applied to short-range tasks. In this work, we develop a reinforcement learning approach that directly optimizes humanoid locomotion for SE(2) targets. Central to this approach is a new constellation-based reward function that encourages natural and efficient target-oriented movement. To evaluate performance, we introduce a benchmarking framework that measures energy consumption, time-to-target, and footstep count on a distribution of SE(2) goals. Our results show that the proposed approach consistently outperforms standard methods and enables successful transfer from simulation to hardware, highlighting the importance of targeted reward design for practical short-range humanoid locomotion.

## 개요
실제 작업 공간에서 작동하는 휴머노이드는 SE(2) 목표 자세로 작업 기반의 단거리 이동을 자주 수행해야 합니다. 실용적이기 위해서는 이러한 전환이 빠르고, 견고하며, 에너지 효율적이어야 합니다. 학습 기반 보행 기술은 상당한 진전을 이루었지만, 대부분의 기존 방법은 직접적인 자세 도달보다는 속도 추적에 최적화되어 있어 단거리 작업에 적용할 때 비효율적인 행진식 행동을 초래합니다. 본 연구에서는 휴머노이드 보행을 SE(2) 목표에 직접 최적화하는 강화 학습 접근법을 개발합니다. 이 접근법의 핵심은 자연스럽고 효율적인 목표 지향적 움직임을 장려하는 새로운 별자리 기반 보상 함수입니다. 성능을 평가하기 위해 SE(2) 목표 분포에 대한 에너지 소비, 목표 도달 시간, 보폭 수를 측정하는 벤치마킹 프레임워크를 도입합니다. 결과는 제안된 접근법이 표준 방법보다 일관되게 우수하며 시뮬레이션에서 하드웨어로의 성공적인 전환을 가능하게 함을 보여주며, 실용적인 단거리 휴머노이드 보행을 위한 목표 지향적 보상 설계의 중요성을 강조합니다.

## 핵심 내용
실제 작업 공간에서 작동하는 휴머노이드는 SE(2) 목표 자세로 작업 기반의 단거리 이동을 자주 수행해야 합니다. 실용적이기 위해서는 이러한 전환이 빠르고, 견고하며, 에너지 효율적이어야 합니다. 학습 기반 보행 기술은 상당한 진전을 이루었지만, 대부분의 기존 방법은 직접적인 자세 도달보다는 속도 추적에 최적화되어 있어 단거리 작업에 적용할 때 비효율적인 행진식 행동을 초래합니다. 본 연구에서는 휴머노이드 보행을 SE(2) 목표에 직접 최적화하는 강화 학습 접근법을 개발합니다. 이 접근법의 핵심은 자연스럽고 효율적인 목표 지향적 움직임을 장려하는 새로운 별자리 기반 보상 함수입니다. 성능을 평가하기 위해 SE(2) 목표 분포에 대한 에너지 소비, 목표 도달 시간, 보폭 수를 측정하는 벤치마킹 프레임워크를 도입합니다. 결과는 제안된 접근법이 표준 방법보다 일관되게 우수하며 시뮬레이션에서 하드웨어로의 성공적인 전환을 가능하게 함을 보여주며, 실용적인 단거리 휴머노이드 보행을 위한 목표 지향적 보상 설계의 중요성을 강조합니다.
