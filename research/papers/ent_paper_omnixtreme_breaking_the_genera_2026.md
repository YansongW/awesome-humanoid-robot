---
$id: ent_paper_omnixtreme_breaking_the_genera_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'OmniXtreme: Breaking the Generality Barrier in High-Dynamic Humanoid Control'
  zh: 高动态动作会撞上硬件边界
  ko: 'OmniXtreme: Breaking the Generality Barrier in High-Dynamic Humanoid Control'
summary:
  en: 'OmniXtreme: Breaking the Generality Barrier in High-Dynamic Humanoid Control is a knowledge node related to paper in
    the humanoid robot value chain.'
  zh: 'High-fidelity motion tracking serves as the ultimate litmus test for generalizable, human-level motor skills. However,
    current policies often hit a "generality barrier": as motion libraries scale in diversity, tracking fidelity inevitably
    collapses - especially for real-world deployment of high-dynamic motions. We identify this failure as the result of two
    compounding factors: the learning bottleneck in scaling multi-motion optimization and the physical executability constraints
    that arise in real-world actuation. To overcome these challenges, we introduce OmniXtreme, a scalable framework that decouples
    general motor skill learning from sim-to-real physical skill refinement. Our approach uses a flow-matching policy with
    high-capacity architectures to scale representation capacity without i'
  ko: 'OmniXtreme: Breaking the Generality Barrier in High-Dynamic Humanoid Control is a knowledge node related to paper in
    the humanoid robot value chain.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- behavioral_foundation_model
- imitation_learning
- motion_tracker
- motion_tracking
- physics_based_control
- whole_body_control
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.23843v1.
sources:
- id: src_001
  type: paper
  title: 'OmniXtreme: Breaking the Generality Barrier in High-Dynamic Humanoid Control (arXiv)'
  url: https://arxiv.org/abs/2602.23843
  date: '2026'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 高动态动作会撞上硬件边界 project page
  url: https://extreme-humanoid.github.io/
  date: '2026'
  accessed_at: '2026-07-01'
theoretical_depth:
- system
---
## 概述
High-fidelity motion tracking serves as the ultimate litmus test for generalizable, human-level motor skills. However, current policies often hit a "generality barrier": as motion libraries scale in diversity, tracking fidelity inevitably collapses - especially for real-world deployment of high-dynamic motions. We identify this failure as the result of two compounding factors: the learning bottleneck in scaling multi-motion optimization and the physical executability constraints that arise in real-world actuation. To overcome these challenges, we introduce OmniXtreme, a scalable framework that decouples general motor skill learning from sim-to-real physical skill refinement. Our approach uses a flow-matching policy with high-capacity architectures to scale representation capacity without interference-intensive multi-motion RL optimization, followed by an actuation-aware refinement phase that ensures robust performance on physical hardware. Extensive experiments demonstrate that OmniXtreme maintains high-fidelity tracking across diverse, high-difficulty datasets. On real robots, the unified policy successfully executes multiple extreme motions, effectively breaking the long-standing fidelity-scalability trade-off in high-dynamic humanoid control.

## 核心内容
High-fidelity motion tracking serves as the ultimate litmus test for generalizable, human-level motor skills. However, current policies often hit a "generality barrier": as motion libraries scale in diversity, tracking fidelity inevitably collapses - especially for real-world deployment of high-dynamic motions. We identify this failure as the result of two compounding factors: the learning bottleneck in scaling multi-motion optimization and the physical executability constraints that arise in real-world actuation. To overcome these challenges, we introduce OmniXtreme, a scalable framework that decouples general motor skill learning from sim-to-real physical skill refinement. Our approach uses a flow-matching policy with high-capacity architectures to scale representation capacity without interference-intensive multi-motion RL optimization, followed by an actuation-aware refinement phase that ensures robust performance on physical hardware. Extensive experiments demonstrate that OmniXtreme maintains high-fidelity tracking across diverse, high-difficulty datasets. On real robots, the unified policy successfully executes multiple extreme motions, effectively breaking the long-standing fidelity-scalability trade-off in high-dynamic humanoid control.

## 参考
- http://arxiv.org/abs/2602.23843v1

## Overview
High-fidelity motion tracking serves as the ultimate litmus test for generalizable, human-level motor skills. However, current policies often hit a "generality barrier": as motion libraries scale in diversity, tracking fidelity inevitably collapses - especially for real-world deployment of high-dynamic motions. We identify this failure as the result of two compounding factors: the learning bottleneck in scaling multi-motion optimization and the physical executability constraints that arise in real-world actuation. To overcome these challenges, we introduce OmniXtreme, a scalable framework that decouples general motor skill learning from sim-to-real physical skill refinement. Our approach uses a flow-matching policy with high-capacity architectures to scale representation capacity without interference-intensive multi-motion RL optimization, followed by an actuation-aware refinement phase that ensures robust performance on physical hardware. Extensive experiments demonstrate that OmniXtreme maintains high-fidelity tracking across diverse, high-difficulty datasets. On real robots, the unified policy successfully executes multiple extreme motions, effectively breaking the long-standing fidelity-scalability trade-off in high-dynamic humanoid control.

## Content
High-fidelity motion tracking serves as the ultimate litmus test for generalizable, human-level motor skills. However, current policies often hit a "generality barrier": as motion libraries scale in diversity, tracking fidelity inevitably collapses - especially for real-world deployment of high-dynamic motions. We identify this failure as the result of two compounding factors: the learning bottleneck in scaling multi-motion optimization and the physical executability constraints that arise in real-world actuation. To overcome these challenges, we introduce OmniXtreme, a scalable framework that decouples general motor skill learning from sim-to-real physical skill refinement. Our approach uses a flow-matching policy with high-capacity architectures to scale representation capacity without interference-intensive multi-motion RL optimization, followed by an actuation-aware refinement phase that ensures robust performance on physical hardware. Extensive experiments demonstrate that OmniXtreme maintains high-fidelity tracking across diverse, high-difficulty datasets. On real robots, the unified policy successfully executes multiple extreme motions, effectively breaking the long-standing fidelity-scalability trade-off in high-dynamic humanoid control.

## 개요
고충실도 모션 트래킹은 일반화 가능한 인간 수준의 운동 기술을 평가하는 궁극적인 시금석입니다. 그러나 현재의 정책은 종종 "일반성 장벽"에 부딪힙니다. 모션 라이브러리의 다양성이 확장됨에 따라 트래킹 충실도는 필연적으로 붕괴되며, 특히 고역학적 동작의 실제 환경 배포에서 두드러집니다. 우리는 이러한 실패를 두 가지 복합 요인의 결과로 식별합니다: 다중 모션 최적화 확장에서의 학습 병목 현상과 실제 구동에서 발생하는 물리적 실행 가능성 제약입니다. 이러한 문제를 극복하기 위해, 우리는 일반 운동 기술 학습을 시뮬레이션-실제 물리적 기술 개선과 분리하는 확장 가능한 프레임워크인 OmniXtreme을 소개합니다. 우리의 접근 방식은 간섭이 심한 다중 모션 강화 학습 최적화 없이 표현 용량을 확장하기 위해 고용량 아키텍처를 갖춘 흐름 매칭 정책을 사용하며, 이후 물리적 하드웨어에서 강력한 성능을 보장하는 구동 인식 개선 단계를 따릅니다. 광범위한 실험을 통해 OmniXtreme이 다양하고 난이도가 높은 데이터셋에서 고충실도 트래킹을 유지함을 입증합니다. 실제 로봇에서 통합 정책은 여러 극한 동작을 성공적으로 실행하여 고역학적 휴머노이드 제어에서 오랜 기간 지속된 충실도-확장성 트레이드오프를 효과적으로 깨뜨립니다.

## 핵심 내용
고충실도 모션 트래킹은 일반화 가능한 인간 수준의 운동 기술을 평가하는 궁극적인 시금석입니다. 그러나 현재의 정책은 종종 "일반성 장벽"에 부딪힙니다. 모션 라이브러리의 다양성이 확장됨에 따라 트래킹 충실도는 필연적으로 붕괴되며, 특히 고역학적 동작의 실제 환경 배포에서 두드러집니다. 우리는 이러한 실패를 두 가지 복합 요인의 결과로 식별합니다: 다중 모션 최적화 확장에서의 학습 병목 현상과 실제 구동에서 발생하는 물리적 실행 가능성 제약입니다. 이러한 문제를 극복하기 위해, 우리는 일반 운동 기술 학습을 시뮬레이션-실제 물리적 기술 개선과 분리하는 확장 가능한 프레임워크인 OmniXtreme을 소개합니다. 우리의 접근 방식은 간섭이 심한 다중 모션 강화 학습 최적화 없이 표현 용량을 확장하기 위해 고용량 아키텍처를 갖춘 흐름 매칭 정책을 사용하며, 이후 물리적 하드웨어에서 강력한 성능을 보장하는 구동 인식 개선 단계를 따릅니다. 광범위한 실험을 통해 OmniXtreme이 다양하고 난이도가 높은 데이터셋에서 고충실도 트래킹을 유지함을 입증합니다. 실제 로봇에서 통합 정책은 여러 극한 동작을 성공적으로 실행하여 고역학적 휴머노이드 제어에서 오랜 기간 지속된 충실도-확장성 트레이드오프를 효과적으로 깨뜨립니다.
