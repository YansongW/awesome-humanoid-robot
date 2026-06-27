---
$id: ent_paper_hu_active_uncertainty_reduction_f_2022
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Active Uncertainty Reduction for Human-Robot Interaction: An Implicit Dual
    Control Approach'
  zh: 人机交互中的主动不确定性降低：一种隐式双控制方法
  ko: '인간-로봇 상호작용을 위한 능동적 불확실성 감소: 암시적 이중 제어 접근법'
summary:
  en: Presents an implicit dual-control stochastic MPC algorithm that enables robots
    to actively reduce uncertainty about hidden human states during interactive motion
    planning via scenario-tree-based stochastic dynamic programming.
  zh: 提出了一种隐式双控制随机模型预测控制算法，使机器人能够通过基于场景树的随机动态规划，在交互式运动规划中主动降低对人类隐状态的感知不确定性。
  ko: 시나리오 트리 기반 확률적 동적 프로그래밍을 통해 상호작용적 모션 계획 중 숨겨진 인간 상태에 대한 불확실성을 능동적으로 줄일 수 있는
    암시적 이중 제어 확률적 MPC 알고리즘을 제시한다.
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
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from provided metadata and abstract; requires human review against
    the full arXiv text before verification.
sources:
- id: src_001
  type: paper
  title: 'Active Uncertainty Reduction for Human-Robot Interaction: An Implicit Dual
    Control Approach'
  url: https://arxiv.org/abs/2202.07720
  date: '2022'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## Overview

This paper addresses the challenge of safe and efficient robot autonomy in interactive settings where the robot must predict human behavior without directly observing key latent variables such as goals, attention, and cooperativeness. The authors formulate human-in-the-loop planning as a stochastic optimal control problem with hidden human states, and propose an implicit dual-control stochastic MPC (ID-SMPC) algorithm that preserves the dual control effect without relying on heuristic probing terms.

The core technical approach combines sampling-based approximation of stochastic dynamic programming with a scenario-tree formulation, yielding a nonlinear MPC problem solvable by standard gradient-based optimization methods in real time. The algorithm supports both continuous parametric uncertainty and categorical mode uncertainty in predictive human models, and is evaluated in simulated driving scenarios where it demonstrates improved safety and liveness compared to explicit dual and non-dual baselines.

## Key Contributions

- Formulates a broad class of human-in-the-loop planning problems as stochastic optimal control with hidden human states.
- Develops an implicit dual stochastic MPC (ID-SMPC) algorithm that preserves the dual control effect without heuristic probing terms.
- Supports both continuous parametric and categorical mode uncertainty in predictive human models.
- Reformulates the Bellman recursion into a scenario-tree MPC problem solvable by standard nonlinear optimization solvers.
- Demonstrates improved safety and liveness over explicit dual and non-dual baselines in simulated driving scenarios.

## Relevance to Humanoid Robotics

The framework is directly relevant to humanoid robots deployed in shared human environments, where safe motion planning depends on real-time inference of human intent, attention, and cooperation. By enabling active uncertainty reduction through planned exploration, the method supports robust decision-making for humanoids in crowded or collaborative settings.
