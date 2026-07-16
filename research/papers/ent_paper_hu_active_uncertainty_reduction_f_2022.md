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

## Overview
The ability to accurately predict human behavior is central to the safety and efficiency of robot autonomy in interactive settings. Unfortunately, robots often lack access to key information on which these predictions may hinge, such as people's goals, attention, and willingness to cooperate. Dual control theory addresses this challenge by treating unknown parameters of a predictive model as stochastic hidden states and inferring their values at runtime using information gathered during system operation. While able to optimally and automatically trade off exploration and exploitation, dual control is computationally intractable for general interactive motion planning, mainly due to the fundamental coupling between robot trajectory optimization and human intent inference. In this paper, we present a novel algorithmic approach to enable active uncertainty reduction for interactive motion planning based on the implicit dual control paradigm. Our approach relies on sampling-based approximation of stochastic dynamic programming, leading to a model predictive control problem that can be readily solved by real-time gradient-based optimization methods. The resulting policy is shown to preserve the dual control effect for a broad class of predictive human models with both continuous and categorical uncertainty. The efficacy of our approach is demonstrated with simulated driving examples.

## Content
The ability to accurately predict human behavior is central to the safety and efficiency of robot autonomy in interactive settings. Unfortunately, robots often lack access to key information on which these predictions may hinge, such as people's goals, attention, and willingness to cooperate. Dual control theory addresses this challenge by treating unknown parameters of a predictive model as stochastic hidden states and inferring their values at runtime using information gathered during system operation. While able to optimally and automatically trade off exploration and exploitation, dual control is computationally intractable for general interactive motion planning, mainly due to the fundamental coupling between robot trajectory optimization and human intent inference. In this paper, we present a novel algorithmic approach to enable active uncertainty reduction for interactive motion planning based on the implicit dual control paradigm. Our approach relies on sampling-based approximation of stochastic dynamic programming, leading to a model predictive control problem that can be readily solved by real-time gradient-based optimization methods. The resulting policy is shown to preserve the dual control effect for a broad class of predictive human models with both continuous and categorical uncertainty. The efficacy of our approach is demonstrated with simulated driving examples.

## 개요
상호작용 환경에서 인간 행동을 정확히 예측하는 능력은 로봇 자율성의 안전성과 효율성에 핵심적입니다. 불행히도 로봇은 종종 인간의 목표, 주의, 협력 의지와 같이 예측의 근간이 되는 핵심 정보에 접근하지 못합니다. 이중 제어 이론은 예측 모델의 알려지지 않은 매개변수를 확률적 은닉 상태로 취급하고, 시스템 작동 중 수집된 정보를 활용하여 실행 시간에 그 값을 추론함으로써 이 문제를 해결합니다. 탐험과 활용을 최적으로 자동으로 절충할 수 있지만, 이중 제어는 일반적인 상호작용 운동 계획에서 계산적으로 다루기 어렵습니다. 이는 주로 로봇 궤적 최적화와 인간 의도 추론 간의 근본적인 결합 때문입니다. 본 논문에서는 암시적 이중 제어 패러다임을 기반으로 상호작용 운동 계획을 위한 능동적 불확실성 감소를 가능하게 하는 새로운 알고리즘 접근법을 제시합니다. 우리의 접근법은 확률적 동적 프로그래밍의 샘플링 기반 근사에 의존하며, 이는 실시간 그래디언트 기반 최적화 방법으로 쉽게 해결할 수 있는 모델 예측 제어 문제로 이어집니다. 결과 정책은 연속적 및 범주적 불확실성을 모두 가진 광범위한 예측 인간 모델에 대해 이중 제어 효과를 유지하는 것으로 나타났습니다. 우리 접근법의 효용성은 시뮬레이션된 운전 예제를 통해 입증됩니다.

## 핵심 내용
상호작용 환경에서 인간 행동을 정확히 예측하는 능력은 로봇 자율성의 안전성과 효율성에 핵심적입니다. 불행히도 로봇은 종종 인간의 목표, 주의, 협력 의지와 같이 예측의 근간이 되는 핵심 정보에 접근하지 못합니다. 이중 제어 이론은 예측 모델의 알려지지 않은 매개변수를 확률적 은닉 상태로 취급하고, 시스템 작동 중 수집된 정보를 활용하여 실행 시간에 그 값을 추론함으로써 이 문제를 해결합니다. 탐험과 활용을 최적으로 자동으로 절충할 수 있지만, 이중 제어는 일반적인 상호작용 운동 계획에서 계산적으로 다루기 어렵습니다. 이는 주로 로봇 궤적 최적화와 인간 의도 추론 간의 근본적인 결합 때문입니다. 본 논문에서는 암시적 이중 제어 패러다임을 기반으로 상호작용 운동 계획을 위한 능동적 불확실성 감소를 가능하게 하는 새로운 알고리즘 접근법을 제시합니다. 우리의 접근법은 확률적 동적 프로그래밍의 샘플링 기반 근사에 의존하며, 이는 실시간 그래디언트 기반 최적화 방법으로 쉽게 해결할 수 있는 모델 예측 제어 문제로 이어집니다. 결과 정책은 연속적 및 범주적 불확실성을 모두 가진 광범위한 예측 인간 모델에 대해 이중 제어 효과를 유지하는 것으로 나타났습니다. 우리 접근법의 효용성은 시뮬레이션된 운전 예제를 통해 입증됩니다.
