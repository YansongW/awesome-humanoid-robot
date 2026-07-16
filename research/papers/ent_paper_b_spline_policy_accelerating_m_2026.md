---
$id: ent_paper_b_spline_policy_accelerating_m_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'B-spline Policy: Accelerating Manipulation Policies via B-spline Action Representations'
  zh: 'B-spline Policy: Accelerating Manipulation Policies via B-spline Action Representations'
  ko: 'B-spline Policy: Accelerating Manipulation Policies via B-spline Action Representations'
summary:
  en: 'arXiv:2607.09648v1 Announce Type: new Abstract: In this work, we present B-spline Policy (BSP), an action representation
    designed for accelerating robot manipulation policies. Rather than predicting discrete-time action chunks, BSP parameterizes
    actions as continuous B-spline curves defined by a set of knots and control points. This representation yields smooth,
    time-continuous trajectories that can be temporally scaled and executed by low-level controllers at higher frequencies
    and speeds. We show that B-spline-parameterized actions can be seamlessly integrated into standard policy learning pipelines
    by directly predicting B-spline parameters. Experiments on simulated and real-world tasks demonstrate that BSP significantly
    reduces task completion time, achieving substantial improvements over baseline methods while maintaining strong success
    rates. More results: https://b-spline-policy.github.io'
  zh: 'arXiv:2607.09648v1 Announce Type: new Abstract: In this work, we present B-spline Policy (BSP), an action representation
    designed for accelerating robot manipulation policies. Rather than predicting discrete-time action chunks, BSP parameterizes
    actions as continuous B-spline curves defined by a set of knots and control points. This representation yields smooth,
    time-continuous trajectories that can be temporally scaled and executed by low-level controllers at higher frequencies
    and speeds. We show that B-spline-parameterized actions can be seamlessly integrated into standard policy learning pipelines
    by directly predicting B-spline parameters. Experiments on simulated and real-world tasks demonstrate that BSP significantly
    reduces task completion time, achieving substantial improvements over baseline methods while maintaining strong success
    rates. More results: https://b-spline-policy.github.io'
  ko: 'arXiv:2607.09648v1 Announce Type: new Abstract: In this work, we present B-spline Policy (BSP), an action representation
    designed for accelerating robot manipulation policies. Rather than predicting discrete-time action chunks, BSP parameterizes
    actions as continuous B-spline curves defined by a set of knots and control points. This representation yields smooth,
    time-continuous trajectories that can be temporally scaled and executed by low-level controllers at higher frequencies
    and speeds. We show that B-spline-parameterized actions can be seamlessly integrated into standard policy learning pipelines
    by directly predicting B-spline parameters. Experiments on simulated and real-world tasks demonstrate that BSP significantly
    reduces task completion time, achieving substantial improvements over baseline methods while maintaining strong success
    rates. More results: https://b-spline-policy.github.io'
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
- robotics
- b_spline_policy
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.09648v1.
sources:
- id: src_001
  type: paper
  title: 'B-spline Policy: Accelerating Manipulation Policies via B-spline Action Representations (arXiv)'
  url: https://arxiv.org/abs/2607.09648
  date: '2026'
  accessed_at: '2026-07-14'
---
## 概述
In this work, we present B-spline Policy (BSP), an action representation designed for accelerating robot manipulation policies. Rather than predicting discrete-time action chunks, BSP parameterizes actions as continuous B-spline curves defined by a set of knots and control points. This representation yields smooth, time-continuous trajectories that can be temporally scaled and executed by low-level controllers at higher frequencies and speeds. We show that B-spline-parameterized actions can be seamlessly integrated into standard policy learning pipelines by directly predicting B-spline parameters. Experiments on simulated and real-world tasks demonstrate that BSP significantly reduces task completion time, achieving substantial improvements over baseline methods while maintaining strong success rates. More results: https://b-spline-policy.github.io

## 核心内容
In this work, we present B-spline Policy (BSP), an action representation designed for accelerating robot manipulation policies. Rather than predicting discrete-time action chunks, BSP parameterizes actions as continuous B-spline curves defined by a set of knots and control points. This representation yields smooth, time-continuous trajectories that can be temporally scaled and executed by low-level controllers at higher frequencies and speeds. We show that B-spline-parameterized actions can be seamlessly integrated into standard policy learning pipelines by directly predicting B-spline parameters. Experiments on simulated and real-world tasks demonstrate that BSP significantly reduces task completion time, achieving substantial improvements over baseline methods while maintaining strong success rates. More results: https://b-spline-policy.github.io

## 参考
- http://arxiv.org/abs/2607.09648v1

## Overview
In this work, we present B-spline Policy (BSP), an action representation designed for accelerating robot manipulation policies. Rather than predicting discrete-time action chunks, BSP parameterizes actions as continuous B-spline curves defined by a set of knots and control points. This representation yields smooth, time-continuous trajectories that can be temporally scaled and executed by low-level controllers at higher frequencies and speeds. We show that B-spline-parameterized actions can be seamlessly integrated into standard policy learning pipelines by directly predicting B-spline parameters. Experiments on simulated and real-world tasks demonstrate that BSP significantly reduces task completion time, achieving substantial improvements over baseline methods while maintaining strong success rates. More results: https://b-spline-policy.github.io

## Content
In this work, we present B-spline Policy (BSP), an action representation designed for accelerating robot manipulation policies. Rather than predicting discrete-time action chunks, BSP parameterizes actions as continuous B-spline curves defined by a set of knots and control points. This representation yields smooth, time-continuous trajectories that can be temporally scaled and executed by low-level controllers at higher frequencies and speeds. We show that B-spline-parameterized actions can be seamlessly integrated into standard policy learning pipelines by directly predicting B-spline parameters. Experiments on simulated and real-world tasks demonstrate that BSP significantly reduces task completion time, achieving substantial improvements over baseline methods while maintaining strong success rates. More results: https://b-spline-policy.github.io

## 개요
본 연구에서는 로봇 조작 정책의 가속화를 위해 설계된 행동 표현인 B-스플라인 정책(BSP)을 제시합니다. BSP는 이산 시간 단위의 행동 청크를 예측하는 대신, 일련의 매듭점과 제어점으로 정의된 연속적인 B-스플라인 곡선으로 행동을 매개변수화합니다. 이 표현은 부드럽고 시간 연속적인 궤적을 생성하며, 이를 시간적으로 확장하여 저수준 제어기가 더 높은 주파수와 속도로 실행할 수 있습니다. B-스플라인으로 매개변수화된 행동은 B-스플라인 매개변수를 직접 예측함으로써 표준 정책 학습 파이프라인에 원활하게 통합될 수 있음을 보여줍니다. 시뮬레이션 및 실제 작업 실험을 통해 BSP가 작업 완료 시간을 크게 단축시키며, 강력한 성공률을 유지하면서 기준 방법 대비 상당한 개선을 달성함을 입증했습니다. 추가 결과: https://b-spline-policy.github.io

## 핵심 내용
본 연구에서는 로봇 조작 정책의 가속화를 위해 설계된 행동 표현인 B-스플라인 정책(BSP)을 제시합니다. BSP는 이산 시간 단위의 행동 청크를 예측하는 대신, 일련의 매듭점과 제어점으로 정의된 연속적인 B-스플라인 곡선으로 행동을 매개변수화합니다. 이 표현은 부드럽고 시간 연속적인 궤적을 생성하며, 이를 시간적으로 확장하여 저수준 제어기가 더 높은 주파수와 속도로 실행할 수 있습니다. B-스플라인으로 매개변수화된 행동은 B-스플라인 매개변수를 직접 예측함으로써 표준 정책 학습 파이프라인에 원활하게 통합될 수 있음을 보여줍니다. 시뮬레이션 및 실제 작업 실험을 통해 BSP가 작업 완료 시간을 크게 단축시키며, 강력한 성공률을 유지하면서 기준 방법 대비 상당한 개선을 달성함을 입증했습니다. 추가 결과: https://b-spline-policy.github.io
