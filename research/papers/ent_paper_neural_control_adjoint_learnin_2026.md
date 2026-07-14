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
  en: "arXiv:2605.03288v2 Announce Type: replace \nAbstract: Many physical AI tasks require sequential implicit computation:\
    \ at each step, boundary controls are applied, and the resulting configuration is obtained by solving an equilibrium problem.\
    \ This setting arises naturally in deformable object manipulation, where even bending a deformable linear object (DLO)\
    \ to a target shape can be nonlinear and multistable: identical boundary conditions may produce different configurations\
    \ depending on actuation history. Unlike explicit transition models, the control-to-configuration relation is implicit\
    \ and history-dependent, making long-horizon learning and control brittle; backpropagating through iterative solves is\
    \ also memory- and compute-intensive. We propose Neural Control, a boundary-control framework that propagates gradients\
    \ through branch-dependent sequences of equilibrium solves rather than a single fixed point. Neural Control computes trajectory-dependent\
    \ proxy gradients by differentiating equilibrium conditions with an adjoint formulation, avoiding solver unrolling while\
    \ keeping forward rollouts on converged equilibria. Combined with receding-horizon continuation, Neural Control re-anchors\
    \ optimization to realized equilibria and mitigates basin switching. We validate Neural Control on simulated and real\
    \ DLO manipulation, compare against SPSA and iCEM, and demonstrate applicability to a learned DEQ-style implicit equilibrium\
    \ model."
  zh: "arXiv:2605.03288v2 Announce Type: replace \nAbstract: Many physical AI tasks require sequential implicit computation:\
    \ at each step, boundary controls are applied, and the resulting configuration is obtained by solving an equilibrium problem.\
    \ This setting arises naturally in deformable object manipulation, where even bending a deformable linear object (DLO)\
    \ to a target shape can be nonlinear and multistable: identical boundary conditions may produce different configurations\
    \ depending on actuation history. Unlike explicit transition models, the control-to-configuration relation is implicit\
    \ and history-dependent, making long-horizon learning and control brittle; backpropagating through iterative solves is\
    \ also memory- and compute-intensive. We propose Neural Control, a boundary-control framework that propagates gradients\
    \ through branch-dependent sequences of equilibrium solves rather than a single fixed point. Neural Control computes trajectory-dependent\
    \ proxy gradients by differentiating equilibrium conditions with an adjoint formulation, avoiding solver unrolling while\
    \ keeping forward rollouts on converged equilibria. Combined with receding-horizon continuation, Neural Control re-anchors\
    \ optimization to realized equilibria and mitigates basin switching. We validate Neural Control on simulated and real\
    \ DLO manipulation, compare against SPSA and iCEM, and demonstrate applicability to a learned DEQ-style implicit equilibrium\
    \ model."
  ko: "arXiv:2605.03288v2 Announce Type: replace \nAbstract: Many physical AI tasks require sequential implicit computation:\
    \ at each step, boundary controls are applied, and the resulting configuration is obtained by solving an equilibrium problem.\
    \ This setting arises naturally in deformable object manipulation, where even bending a deformable linear object (DLO)\
    \ to a target shape can be nonlinear and multistable: identical boundary conditions may produce different configurations\
    \ depending on actuation history. Unlike explicit transition models, the control-to-configuration relation is implicit\
    \ and history-dependent, making long-horizon learning and control brittle; backpropagating through iterative solves is\
    \ also memory- and compute-intensive. We propose Neural Control, a boundary-control framework that propagates gradients\
    \ through branch-dependent sequences of equilibrium solves rather than a single fixed point. Neural Control computes trajectory-dependent\
    \ proxy gradients by differentiating equilibrium conditions with an adjoint formulation, avoiding solver unrolling while\
    \ keeping forward rollouts on converged equilibria. Combined with receding-horizon continuation, Neural Control re-anchors\
    \ optimization to realized equilibria and mitigates basin switching. We validate Neural Control on simulated and real\
    \ DLO manipulation, compare against SPSA and iCEM, and demonstrate applicability to a learned DEQ-style implicit equilibrium\
    \ model."
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

