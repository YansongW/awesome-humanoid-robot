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
  zh: Neural Control 是一个针对物理AI中隐式、历史依赖的边界控制问题的框架，由研究团队提出。其核心贡献在于通过伴随公式对平衡条件进行微分，计算轨迹依赖的代理梯度，从而避免展开求解器，同时结合后退时域延续策略来缓解优化中的盆地切换问题。
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2605.03288v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (713 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'Neural Control: Adjoint Learning Through Equilibrium Constraints'
  url: https://arxiv.org/abs/2605.03288
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
在可变形物体操作等物理AI任务中，控制到构型的映射是隐式且依赖历史的，这导致长时域学习和控制变得脆弱，且通过迭代求解反向传播会消耗大量内存和计算资源。Neural Control 框架通过伴随公式对平衡条件进行微分，计算轨迹依赖的代理梯度，从而在不展开求解器的情况下，在收敛的平衡点上进行前向滚动。结合后退时域延续策略，该框架将优化重新锚定到已实现的平衡点，有效缓解了盆地切换问题。

## 核心内容
### 方法
- **问题设定**：针对物理AI中每一步施加边界控制后需通过求解平衡问题获得构型的场景，特别是可变形线性对象（DLO）操作中存在的非线性和多稳态特性。
- **核心挑战**：控制到构型的映射是隐式且依赖历史的，导致长时域学习脆弱；通过迭代求解反向传播需要大量内存和计算。
- **Neural Control 框架**：
  - 通过伴随公式对平衡条件进行微分，计算轨迹依赖的代理梯度，避免展开求解器。
  - 前向滚动在收敛的平衡点上进行，而非展开迭代过程。
  - 结合后退时域延续策略，将优化重新锚定到已实现的平衡点，缓解盆地切换问题。

### 实验设置
- **验证场景**：在仿真和真实DLO操作任务上进行验证。
- **对比方法**：与SPSA和iCEM进行对比。
- **扩展应用**：展示了在学习的DEQ风格隐式平衡模型上的适用性。

### 关键结果
- Neural Control 在仿真和真实DLO操作任务中均表现出有效性，优于对比方法。
- 通过避免求解器展开，显著降低了内存和计算开销。
- 后退时域延续策略有效缓解了优化中的盆地切换问题，提升了长时域控制的稳定性。

## Overview
Many physical AI tasks require sequential implicit computation: at each step, boundary controls are applied, and the resulting configuration is obtained by solving an equilibrium problem. This setting arises naturally in deformable object manipulation, where even bending a deformable linear object (DLO) to a target shape can be nonlinear and multistable: identical boundary conditions may produce different configurations depending on actuation history. Unlike explicit transition models, the control-to-configuration relation is implicit and history-dependent, making long-horizon learning and control brittle; backpropagating through iterative solves is also memory- and compute-intensive. We propose Neural Control, a boundary-control framework that propagates gradients through branch-dependent sequences of equilibrium solves rather than a single fixed point. Neural Control computes trajectory-dependent proxy gradients by differentiating equilibrium conditions with an adjoint formulation, avoiding solver unrolling while keeping forward rollouts on converged equilibria. Combined with receding-horizon continuation, Neural Control re-anchors optimization to realized equilibria and mitigates basin switching. We validate Neural Control on simulated and real DLO manipulation, compare against SPSA and iCEM, and demonstrate applicability to a learned DEQ-style implicit equilibrium model.

## 参考
- http://arxiv.org/abs/2605.03288v2

## 개요
변형 가능한 물체 조작과 같은 물리 AI 작업에서 제어에서 형상으로의 매핑은 암시적이고 이력에 의존적이어서, 장시간 영역 학습 및 제어가 취약해지고, 반복적 역전파를 통한 해석은 많은 메모리와 계산 자원을 소모합니다. Neural Control 프레임워크는 수반 공식을 통해 평형 조건을 미분하여 궤적 의존적 대리 기울기를 계산함으로써, 솔버를 전개하지 않고 수렴된 평형점에서 전방 롤아웃을 수행합니다. 후퇴 시간 영역 연속 전략을 결합하여 최적화를 구현된 평형점에 재정박함으로써, 분지 전환 문제를 효과적으로 완화합니다.

## 핵심 내용
### 방법
- **문제 설정**: 물리 AI에서 각 단계마다 경계 제어를 적용한 후 평형 문제를 풀어 형상을 얻는 시나리오를 대상으로 하며, 특히 변형 가능한 선형 물체(DLO) 조작에서 존재하는 비선형성 및 다중 안정성 특성을 다룹니다.
- **핵심 과제**: 제어에서 형상으로의 매핑이 암시적이고 이력에 의존적이어서 장시간 영역 학습이 취약하며, 반복적 역전파를 통한 해석은 많은 메모리와 계산을 필요로 합니다.
- **Neural Control 프레임워크**:
  - 수반 공식을 통해 평형 조건을 미분하여 궤적 의존적 대리 기울기를 계산하고, 솔버 전개를 피합니다.
  - 전방 롤아웃은 반복 과정을 전개하지 않고 수렴된 평형점에서 수행됩니다.
  - 후퇴 시간 영역 연속 전략을 결합하여 최적화를 구현된 평형점에 재정박함으로써 분지 전환 문제를 완화합니다.

### 실험 설정
- **검증 시나리오**: 시뮬레이션 및 실제 DLO 조작 작업에서 검증합니다.
- **비교 방법**: SPSA 및 iCEM과 비교합니다.
- **확장 응용**: 학습된 DEQ 스타일 암시적 평형 모델에서의 적용 가능성을 보여줍니다.

### 주요 결과
- Neural Control은 시뮬레이션 및 실제 DLO 조작 작업에서 모두 효과적임을 보여주며, 비교 방법보다 우수합니다.
- 솔버 전개를 피함으로써 메모리 및 계산 오버헤드를 크게 줄입니다.
- 후퇴 시간 영역 연속 전략은 최적화에서 분지 전환 문제를 효과적으로 완화하여 장시간 영역 제어의 안정성을 향상시킵니다.
