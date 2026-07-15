---
$id: ent_paper_hu_active_uncertainty_reduction_f_2022
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Active Uncertainty Reduction for Human-Robot Interaction: An Implicit Dual Control Approach'
  zh: 人机交互中的主动不确定性降低：一种隐式双控制方法
  ko: '인간-로봇 상호작용을 위한 능동적 불확실성 감소: 암시적 이중 제어 접근법'
summary:
  en: Presents an implicit dual-control stochastic MPC algorithm that enables robots to actively reduce uncertainty about
    hidden human states during interactive motion planning via scenario-tree-based stochastic dynamic programming.
  zh: The ability to accurately predict human behavior is central to the safety and efficiency of robot autonomy in interactive
    settings. Unfortunately, robots often lack access to key information on which these predictions may hinge, such as people's
    goals, attention, and willingness to cooperate. Dual control theory addresses this challenge by treating unknown parameters
    of a predictive model as stochastic hidden states and inferring their values at runtime using information gathered during
    system operation. While able to optimally and automatically trade off exploration and exploitation, dual con
  ko: 시나리오 트리 기반 확률적 동적 프로그래밍을 통해 상호작용적 모션 계획 중 숨겨진 인간 상태에 대한 불확실성을 능동적으로 줄일 수 있는 암시적 이중 제어 확률적 MPC 알고리즘을 제시한다.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- dual_control
- stochastic_mpc
- implicit_dual_control
- human_robot_interaction
- intent_inference
- uncertainty_reduction
- interactive_motion_planning
- belief_space_planning
- scenario_tree
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2202.07720v2.
sources:
- id: src_001
  type: paper
  title: 'Active Uncertainty Reduction for Human-Robot Interaction: An Implicit Dual Control Approach'
  url: https://arxiv.org/abs/2202.07720
  date: '2022'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## 概述
The ability to accurately predict human behavior is central to the safety and efficiency of robot autonomy in interactive settings. Unfortunately, robots often lack access to key information on which these predictions may hinge, such as people's goals, attention, and willingness to cooperate. Dual control theory addresses this challenge by treating unknown parameters of a predictive model as stochastic hidden states and inferring their values at runtime using information gathered during system operation. While able to optimally and automatically trade off exploration and exploitation, dual control is computationally intractable for general interactive motion planning, mainly due to the fundamental coupling between robot trajectory optimization and human intent inference. In this paper, we present a novel algorithmic approach to enable active uncertainty reduction for interactive motion planning based on the implicit dual control paradigm. Our approach relies on sampling-based approximation of stochastic dynamic programming, leading to a model predictive control problem that can be readily solved by real-time gradient-based optimization methods. The resulting policy is shown to preserve the dual control effect for a broad class of predictive human models with both continuous and categorical uncertainty. The efficacy of our approach is demonstrated with simulated driving examples.

## 核心内容
The ability to accurately predict human behavior is central to the safety and efficiency of robot autonomy in interactive settings. Unfortunately, robots often lack access to key information on which these predictions may hinge, such as people's goals, attention, and willingness to cooperate. Dual control theory addresses this challenge by treating unknown parameters of a predictive model as stochastic hidden states and inferring their values at runtime using information gathered during system operation. While able to optimally and automatically trade off exploration and exploitation, dual control is computationally intractable for general interactive motion planning, mainly due to the fundamental coupling between robot trajectory optimization and human intent inference. In this paper, we present a novel algorithmic approach to enable active uncertainty reduction for interactive motion planning based on the implicit dual control paradigm. Our approach relies on sampling-based approximation of stochastic dynamic programming, leading to a model predictive control problem that can be readily solved by real-time gradient-based optimization methods. The resulting policy is shown to preserve the dual control effect for a broad class of predictive human models with both continuous and categorical uncertainty. The efficacy of our approach is demonstrated with simulated driving examples.

## 参考
- http://arxiv.org/abs/2202.07720v2


