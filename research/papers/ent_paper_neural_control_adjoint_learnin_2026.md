---
$id: ent_paper_neural_control_adjoint_learnin_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Neural Control: Adjoint Learning Through Equilibrium Constraints'
  zh: 'Neural Control: Adjoint Learning Through Equilibrium Constraints'
  ko: 'Neural Control: Adjoint Learning Through Equilibrium Constraints'
summary:
  en: 'arXiv:2605.03288v2 Announce Type: replace Abstract: Many physical AI tasks require sequential implicit computation:
    at each step, boundary controls are applied, and the resulting configuration is obtained by solving an equilibrium problem.
    This setting arises naturally in deformable object manipulation, where even bending a deformable linear object (DLO) to
    a target shape can be nonlinear and multistable: identical boundary conditions may produce different configurations depending
    on actuation history. Unlike explicit transition models, the control-to-configuration relation is implicit and history-dependent,
    making long-horizon learning and control brittle; backpropagating through iterative solves is also memory- and compute-intensive.
    We propose Neural Control, a boundary-control framework that propagates gradients through branch-dependent sequences of
    equilibrium solves rather than a single fixed point. Neural Control computes trajectory-dependent proxy gradients by differentiating
    equilibrium conditions with an adjoint formulation, avoiding solver unrolling while keeping forward rollouts on converged
    equilibria. Combined with receding-horizon continuation, Neural Control re-anchors optimization to realized equilibria
    and mitigates basin switching. We validate Neural Control on simulated and real DLO manipulation, compare against SPSA
    and iCEM, and demonstrate applicability to a learned DEQ-style implicit equilibrium model.'
  zh: 'arXiv:2605.03288v2 Announce Type: replace Abstract: Many physical AI tasks require sequential implicit computation:
    at each step, boundary controls are applied, and the resulting configuration is obtained by solving an equilibrium problem.
    This setting arises naturally in deformable object manipulation, where even bending a deformable linear object (DLO) to
    a target shape can be nonlinear and multistable: identical boundary conditions may produce different configurations depending
    on actuation history. Unlike explicit transition models, the control-to-configuration relation is implicit and history-dependent,
    making long-horizon learning and control brittle; backpropagating through iterative solves is also memory- and compute-intensive.
    We propose Neural Control, a boundary-control framework that propagates gradients through branch-dependent sequences of
    equilibrium solves rather than a single fixed point. Neural Control computes trajectory-dependent proxy gradients by differentiating
    equilibrium conditions with an adjoint formulation, avoiding solver unrolling while keeping forward rollouts on converged
    equilibria. Combined with receding-horizon continuation, Neural Control re-anchors optimization to realized equilibria
    and mitigates basin switching. We validate Neural Control on simulated and real DLO manipulation, compare against SPSA
    and iCEM, and demonstrate applicability to a learned DEQ-style implicit equilibrium model.'
  ko: 'arXiv:2605.03288v2 Announce Type: replace Abstract: Many physical AI tasks require sequential implicit computation:
    at each step, boundary controls are applied, and the resulting configuration is obtained by solving an equilibrium problem.
    This setting arises naturally in deformable object manipulation, where even bending a deformable linear object (DLO) to
    a target shape can be nonlinear and multistable: identical boundary conditions may produce different configurations depending
    on actuation history. Unlike explicit transition models, the control-to-configuration relation is implicit and history-dependent,
    making long-horizon learning and control brittle; backpropagating through iterative solves is also memory- and compute-intensive.
    We propose Neural Control, a boundary-control framework that propagates gradients through branch-dependent sequences of
    equilibrium solves rather than a single fixed point. Neural Control computes trajectory-dependent proxy gradients by differentiating
    equilibrium conditions with an adjoint formulation, avoiding solver unrolling while keeping forward rollouts on converged
    equilibria. Combined with receding-horizon continuation, Neural Control re-anchors optimization to realized equilibria
    and mitigates basin switching. We validate Neural Control on simulated and real DLO manipulation, compare against SPSA
    and iCEM, and demonstrate applicability to a learned DEQ-style implicit equilibrium model.'
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
- neural_control
- robotics
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2605.03288v2.
sources:
- id: src_001
  type: paper
  title: 'Neural Control: Adjoint Learning Through Equilibrium Constraints'
  url: https://arxiv.org/abs/2605.03288
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Many physical AI tasks require sequential implicit computation: at each step, boundary controls are applied, and the resulting configuration is obtained by solving an equilibrium problem. This setting arises naturally in deformable object manipulation, where even bending a deformable linear object (DLO) to a target shape can be nonlinear and multistable: identical boundary conditions may produce different configurations depending on actuation history. Unlike explicit transition models, the control-to-configuration relation is implicit and history-dependent, making long-horizon learning and control brittle; backpropagating through iterative solves is also memory- and compute-intensive. We propose Neural Control, a boundary-control framework that propagates gradients through branch-dependent sequences of equilibrium solves rather than a single fixed point. Neural Control computes trajectory-dependent proxy gradients by differentiating equilibrium conditions with an adjoint formulation, avoiding solver unrolling while keeping forward rollouts on converged equilibria. Combined with receding-horizon continuation, Neural Control re-anchors optimization to realized equilibria and mitigates basin switching. We validate Neural Control on simulated and real DLO manipulation, compare against SPSA and iCEM, and demonstrate applicability to a learned DEQ-style implicit equilibrium model.

## 核心内容
Many physical AI tasks require sequential implicit computation: at each step, boundary controls are applied, and the resulting configuration is obtained by solving an equilibrium problem. This setting arises naturally in deformable object manipulation, where even bending a deformable linear object (DLO) to a target shape can be nonlinear and multistable: identical boundary conditions may produce different configurations depending on actuation history. Unlike explicit transition models, the control-to-configuration relation is implicit and history-dependent, making long-horizon learning and control brittle; backpropagating through iterative solves is also memory- and compute-intensive. We propose Neural Control, a boundary-control framework that propagates gradients through branch-dependent sequences of equilibrium solves rather than a single fixed point. Neural Control computes trajectory-dependent proxy gradients by differentiating equilibrium conditions with an adjoint formulation, avoiding solver unrolling while keeping forward rollouts on converged equilibria. Combined with receding-horizon continuation, Neural Control re-anchors optimization to realized equilibria and mitigates basin switching. We validate Neural Control on simulated and real DLO manipulation, compare against SPSA and iCEM, and demonstrate applicability to a learned DEQ-style implicit equilibrium model.

## 参考
- http://arxiv.org/abs/2605.03288v2

## Overview
Many physical AI tasks require sequential implicit computation: at each step, boundary controls are applied, and the resulting configuration is obtained by solving an equilibrium problem. This setting arises naturally in deformable object manipulation, where even bending a deformable linear object (DLO) to a target shape can be nonlinear and multistable: identical boundary conditions may produce different configurations depending on actuation history. Unlike explicit transition models, the control-to-configuration relation is implicit and history-dependent, making long-horizon learning and control brittle; backpropagating through iterative solves is also memory- and compute-intensive. We propose Neural Control, a boundary-control framework that propagates gradients through branch-dependent sequences of equilibrium solves rather than a single fixed point. Neural Control computes trajectory-dependent proxy gradients by differentiating equilibrium conditions with an adjoint formulation, avoiding solver unrolling while keeping forward rollouts on converged equilibria. Combined with receding-horizon continuation, Neural Control re-anchors optimization to realized equilibria and mitigates basin switching. We validate Neural Control on simulated and real DLO manipulation, compare against SPSA and iCEM, and demonstrate applicability to a learned DEQ-style implicit equilibrium model.

## Content
Many physical AI tasks require sequential implicit computation: at each step, boundary controls are applied, and the resulting configuration is obtained by solving an equilibrium problem. This setting arises naturally in deformable object manipulation, where even bending a deformable linear object (DLO) to a target shape can be nonlinear and multistable: identical boundary conditions may produce different configurations depending on actuation history. Unlike explicit transition models, the control-to-configuration relation is implicit and history-dependent, making long-horizon learning and control brittle; backpropagating through iterative solves is also memory- and compute-intensive. We propose Neural Control, a boundary-control framework that propagates gradients through branch-dependent sequences of equilibrium solves rather than a single fixed point. Neural Control computes trajectory-dependent proxy gradients by differentiating equilibrium conditions with an adjoint formulation, avoiding solver unrolling while keeping forward rollouts on converged equilibria. Combined with receding-horizon continuation, Neural Control re-anchors optimization to realized equilibria and mitigates basin switching. We validate Neural Control on simulated and real DLO manipulation, compare against SPSA and iCEM, and demonstrate applicability to a learned DEQ-style implicit equilibrium model.

## 개요
많은 물리적 AI 작업은 순차적인 암시적 계산을 필요로 합니다. 각 단계에서 경계 제어가 적용되고, 결과 구성은 평형 문제를 해결하여 얻어집니다. 이러한 설정은 변형 가능한 물체 조작에서 자연스럽게 발생하며, 변형 가능한 선형 물체(DLO)를 목표 형상으로 구부리는 것조차 비선형적이고 다중 안정적일 수 있습니다. 동일한 경계 조건이라도 작동 이력에 따라 다른 구성을 생성할 수 있습니다. 명시적 전이 모델과 달리, 제어-구성 관계는 암시적이고 이력에 의존적이어서 장기 학습 및 제어를 취약하게 만듭니다. 또한 반복적 해법을 통한 역전파는 메모리와 계산 집약적입니다. 우리는 단일 고정점 대신 분기 의존적 평형 해법 시퀀스를 통해 그래디언트를 전파하는 경계 제어 프레임워크인 Neural Control을 제안합니다. Neural Control은 인접 공식화를 통해 평형 조건을 미분하여 궤적 의존적 대리 그래디언트를 계산하며, 솔버 언롤링을 피하면서 수렴된 평형 상태에서의 순방향 롤아웃을 유지합니다. 후퇴 수평 연속법과 결합하여 Neural Control은 최적화를 실현된 평형 상태에 재고정하고 분지 전환을 완화합니다. 우리는 시뮬레이션 및 실제 DLO 조작에서 Neural Control을 검증하고, SPSA 및 iCEM과 비교하며, 학습된 DEQ 스타일 암시적 평형 모델에 대한 적용 가능성을 입증합니다.

## 핵심 내용
많은 물리적 AI 작업은 순차적인 암시적 계산을 필요로 합니다. 각 단계에서 경계 제어가 적용되고, 결과 구성은 평형 문제를 해결하여 얻어집니다. 이러한 설정은 변형 가능한 물체 조작에서 자연스럽게 발생하며, 변형 가능한 선형 물체(DLO)를 목표 형상으로 구부리는 것조차 비선형적이고 다중 안정적일 수 있습니다. 동일한 경계 조건이라도 작동 이력에 따라 다른 구성을 생성할 수 있습니다. 명시적 전이 모델과 달리, 제어-구성 관계는 암시적이고 이력에 의존적이어서 장기 학습 및 제어를 취약하게 만듭니다. 또한 반복적 해법을 통한 역전파는 메모리와 계산 집약적입니다. 우리는 단일 고정점 대신 분기 의존적 평형 해법 시퀀스를 통해 그래디언트를 전파하는 경계 제어 프레임워크인 Neural Control을 제안합니다. Neural Control은 인접 공식화를 통해 평형 조건을 미분하여 궤적 의존적 대리 그래디언트를 계산하며, 솔버 언롤링을 피하면서 수렴된 평형 상태에서의 순방향 롤아웃을 유지합니다. 후퇴 수평 연속법과 결합하여 Neural Control은 최적화를 실현된 평형 상태에 재고정하고 분지 전환을 완화합니다. 우리는 시뮬레이션 및 실제 DLO 조작에서 Neural Control을 검증하고, SPSA 및 iCEM과 비교하며, 학습된 DEQ 스타일 암시적 평형 모델에 대한 적용 가능성을 입증합니다.
