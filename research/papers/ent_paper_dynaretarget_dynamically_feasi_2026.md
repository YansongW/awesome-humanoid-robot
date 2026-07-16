---
$id: ent_paper_dynaretarget_dynamically_feasi_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'DynaRetarget: Dynamically-Feasible Retargeting using Sampling-Based Trajectory Optimization'
  zh: 'DynaRetarget: Dynamically-Feasible Retargeting using Sampling-Based Trajectory Optimization'
  ko: 'DynaRetarget: Dynamically-Feasible Retargeting using Sampling-Based Trajectory Optimization'
summary:
  en: 'DynaRetarget: Dynamically-Feasible Retargeting using Sampling-Based Trajectory Optimization is a 2026 work on loco-manipulation
    and whole-body-control for humanoid robots.'
  zh: 'DynaRetarget: Dynamically-Feasible Retargeting using Sampling-Based Trajectory Optimization is a 2026 work on loco-manipulation
    and whole-body-control for humanoid robots.'
  ko: 'DynaRetarget: Dynamically-Feasible Retargeting using Sampling-Based Trajectory Optimization is a 2026 work on loco-manipulation
    and whole-body-control for humanoid robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- dynaretarget
- humanoid
- loco_manipulation
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.06827v3.
sources:
- id: src_001
  type: paper
  title: 'DynaRetarget: Dynamically-Feasible Retargeting using Sampling-Based Trajectory Optimization (arXiv)'
  url: https://arxiv.org/abs/2602.06827
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
In this paper, we introduce DynaRetarget, a complete pipeline for retargeting human motions to humanoid control policies. The core component of DynaRetarget is a novel Sampling-Based Trajectory Optimization (SBTO) framework that refines imperfect kinematic trajectories into dynamically feasible motions. SBTO incrementally advances the optimization horizon, enabling optimization over the entire trajectory for long-horizon tasks. We validate DynaRetarget by successfully retargeting hundreds of humanoid-object demonstrations and achieving higher success rates than the state of the art. The framework also generalizes across varying object properties, such as mass, size, and geometry, using the same tracking objective. This ability to robustly retarget diverse demonstrations opens the door to generating large-scale synthetic datasets of humanoid loco-manipulation trajectories, addressing a major bottleneck in real-world data collection.

## 核心内容
In this paper, we introduce DynaRetarget, a complete pipeline for retargeting human motions to humanoid control policies. The core component of DynaRetarget is a novel Sampling-Based Trajectory Optimization (SBTO) framework that refines imperfect kinematic trajectories into dynamically feasible motions. SBTO incrementally advances the optimization horizon, enabling optimization over the entire trajectory for long-horizon tasks. We validate DynaRetarget by successfully retargeting hundreds of humanoid-object demonstrations and achieving higher success rates than the state of the art. The framework also generalizes across varying object properties, such as mass, size, and geometry, using the same tracking objective. This ability to robustly retarget diverse demonstrations opens the door to generating large-scale synthetic datasets of humanoid loco-manipulation trajectories, addressing a major bottleneck in real-world data collection.

## 参考
- http://arxiv.org/abs/2602.06827v3

## Overview
In this paper, we introduce DynaRetarget, a complete pipeline for retargeting human motions to humanoid control policies. The core component of DynaRetarget is a novel Sampling-Based Trajectory Optimization (SBTO) framework that refines imperfect kinematic trajectories into dynamically feasible motions. SBTO incrementally advances the optimization horizon, enabling optimization over the entire trajectory for long-horizon tasks. We validate DynaRetarget by successfully retargeting hundreds of humanoid-object demonstrations and achieving higher success rates than the state of the art. The framework also generalizes across varying object properties, such as mass, size, and geometry, using the same tracking objective. This ability to robustly retarget diverse demonstrations opens the door to generating large-scale synthetic datasets of humanoid loco-manipulation trajectories, addressing a major bottleneck in real-world data collection.

## Content
In this paper, we introduce DynaRetarget, a complete pipeline for retargeting human motions to humanoid control policies. The core component of DynaRetarget is a novel Sampling-Based Trajectory Optimization (SBTO) framework that refines imperfect kinematic trajectories into dynamically feasible motions. SBTO incrementally advances the optimization horizon, enabling optimization over the entire trajectory for long-horizon tasks. We validate DynaRetarget by successfully retargeting hundreds of humanoid-object demonstrations and achieving higher success rates than the state of the art. The framework also generalizes across varying object properties, such as mass, size, and geometry, using the same tracking objective. This ability to robustly retarget diverse demonstrations opens the door to generating large-scale synthetic datasets of humanoid loco-manipulation trajectories, addressing a major bottleneck in real-world data collection.

## 개요
본 논문에서는 인간의 동작을 휴머노이드 제어 정책으로 리타겟팅하는 완전한 파이프라인인 DynaRetarget을 소개합니다. DynaRetarget의 핵심 구성 요소는 불완전한 운동학적 궤적을 동적으로 실행 가능한 동작으로 정제하는 새로운 샘플링 기반 궤적 최적화(SBTO) 프레임워크입니다. SBTO는 최적화 지평을 점진적으로 확장하여 장기 과제에 대해 전체 궤적에 걸친 최적화를 가능하게 합니다. 우리는 수백 개의 휴머노이드-객체 시연을 성공적으로 리타겟팅하고 최신 기술보다 높은 성공률을 달성함으로써 DynaRetarget을 검증합니다. 이 프레임워크는 또한 동일한 추적 목표를 사용하여 질량, 크기, 기하학과 같은 다양한 객체 속성에 걸쳐 일반화됩니다. 다양한 시연을 강건하게 리타겟팅하는 이러한 능력은 휴머노이드 이동-조작 궤적의 대규모 합성 데이터셋을 생성하는 길을 열어, 실제 데이터 수집의 주요 병목 현상을 해결합니다.

## 핵심 내용
본 논문에서는 인간의 동작을 휴머노이드 제어 정책으로 리타겟팅하는 완전한 파이프라인인 DynaRetarget을 소개합니다. DynaRetarget의 핵심 구성 요소는 불완전한 운동학적 궤적을 동적으로 실행 가능한 동작으로 정제하는 새로운 샘플링 기반 궤적 최적화(SBTO) 프레임워크입니다. SBTO는 최적화 지평을 점진적으로 확장하여 장기 과제에 대해 전체 궤적에 걸친 최적화를 가능하게 합니다. 우리는 수백 개의 휴머노이드-객체 시연을 성공적으로 리타겟팅하고 최신 기술보다 높은 성공률을 달성함으로써 DynaRetarget을 검증합니다. 이 프레임워크는 또한 동일한 추적 목표를 사용하여 질량, 크기, 기하학과 같은 다양한 객체 속성에 걸쳐 일반화됩니다. 다양한 시연을 강건하게 리타겟팅하는 이러한 능력은 휴머노이드 이동-조작 궤적의 대규모 합성 데이터셋을 생성하는 길을 열어, 실제 데이터 수집의 주요 병목 현상을 해결합니다.
