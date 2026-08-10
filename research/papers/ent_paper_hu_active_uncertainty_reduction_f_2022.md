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
  zh: 本文提出一种隐式双重控制随机MPC算法，使机器人能在交互运动规划中主动降低对人类隐藏状态的不确定性。该方法基于场景树随机动态规划的采样近似，可实时求解，并保留双重控制效应。模拟驾驶实验验证了其有效性。
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2202.07720v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (868 chars, DeepSeek).'
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
机器人准确预测人类行为对交互安全与效率至关重要，但常缺乏目标、注意力等关键信息。双重控制理论将预测模型未知参数视为随机隐藏状态，在运行时通过信息收集进行推断，能最优权衡探索与利用。然而，由于机器人轨迹优化与人类意图推断的耦合，通用交互运动规划中双重控制计算困难。本文提出基于隐式双重控制范式的算法，通过随机动态规划的采样近似，将问题转化为可实时梯度优化的MPC问题，适用于连续与分类不确定性的人类模型。

## 核心内容
### 方法架构
- 采用隐式双重控制（implicit dual control）范式，将人类隐藏状态（如目标、注意力）建模为随机变量，在运动规划中同时考虑轨迹优化与不确定性降低。
- 基于场景树（scenario tree）的随机动态规划（stochastic dynamic programming）进行采样近似，将原耦合问题转化为可求解的MPC形式。

### 算法实现
- 通过实时梯度优化方法（gradient-based optimization）求解MPC问题，避免传统双重控制的高计算复杂度。
- 支持连续与分类不确定性（continuous and categorical uncertainty）的预测人类模型，保留双重控制效应（dual control effect）。

### 实验设置
- 在模拟驾驶场景（simulated driving examples）中验证，机器人需推断人类驾驶员的目标与意图。
- 对比基线方法，评估主动不确定性降低对交互安全与效率的影响。

### 关键结果
- 算法能自动权衡探索（exploration）与利用（exploitation），在不确定性较高时主动收集信息，降低预测误差。
- 与被动方法相比，显著提升交互轨迹的平滑性与安全性，尤其在人类行为不可预测的场景中。

### 结论
- 隐式双重控制为交互运动规划提供了一种计算可行的主动不确定性降低方案，适用于实时机器人系统。
- 未来可扩展至更复杂的人类模型与多机器人交互场景。

## Overview
The ability to accurately predict human behavior is central to the safety and efficiency of robot autonomy in interactive settings. Unfortunately, robots often lack access to key information on which these predictions may hinge, such as people's goals, attention, and willingness to cooperate. Dual control theory addresses this challenge by treating unknown parameters of a predictive model as stochastic hidden states and inferring their values at runtime using information gathered during system operation. While able to optimally and automatically trade off exploration and exploitation, dual control is computationally intractable for general interactive motion planning, mainly due to the fundamental coupling between robot trajectory optimization and human intent inference. In this paper, we present a novel algorithmic approach to enable active uncertainty reduction for interactive motion planning based on the implicit dual control paradigm. Our approach relies on sampling-based approximation of stochastic dynamic programming, leading to a model predictive control problem that can be readily solved by real-time gradient-based optimization methods. The resulting policy is shown to preserve the dual control effect for a broad class of predictive human models with both continuous and categorical uncertainty. The efficacy of our approach is demonstrated with simulated driving examples.

## 参考
- http://arxiv.org/abs/2202.07720v2

## 개요
로봇이 인간의 행동을 정확히 예측하는 것은 상호작용의 안전성과 효율성에 매우 중요하지만, 목표나 주의력과 같은 핵심 정보가 부족한 경우가 많습니다. 이중 제어 이론은 예측 모델의 알려지지 않은 매개변수를 무작위 숨은 상태로 간주하고, 실행 중 정보 수집을 통해 이를 추론하며, 탐험과 활용을 최적으로 균형 잡을 수 있습니다. 그러나 로봇 궤적 최적화와 인간 의도 추론의 결합으로 인해, 일반적인 상호작용 운동 계획에서 이중 제어는 계산적으로 어렵습니다. 본 논문은 암시적 이중 제어 패러다임에 기반한 알고리즘을 제안하며, 확률적 동적 계획의 샘플 근사를 통해 문제를 실시간 경사 기반 최적화가 가능한 MPC 문제로 변환하고, 연속 및 범주형 불확실성을 가진 인간 모델에 적용할 수 있습니다.

## 핵심 내용
### 방법 아키텍처
- 암시적 이중 제어 패러다임을 채택하여 인간의 숨은 상태(예: 목표, 주의력)를 확률 변수로 모델링하고, 운동 계획에서 궤적 최적화와 불확실성 감소를 동시에 고려합니다.
- 시나리오 트리 기반의 확률적 동적 계획을 샘플 근사하여, 원래의 결합 문제를 해결 가능한 MPC 형태로 변환합니다.

### 알고리즘 구현
- 실시간 경사 기반 최적화 방법을 통해 MPC 문제를 해결하여, 전통적인 이중 제어의 높은 계산 복잡도를 피합니다.
- 연속 및 범주형 불확실성을 가진 예측 인간 모델을 지원하며, 이중 제어 효과를 유지합니다.

### 실험 설정
- 시뮬레이션된 운전 시나리오에서 검증하며, 로봇이 인간 운전자의 목표와 의도를 추론해야 합니다.
- 기준 방법과 비교하여, 능동적 불확실성 감소가 상호작용 안전성과 효율성에 미치는 영향을 평가합니다.

### 주요 결과
- 알고리즘은 탐험과 활용을 자동으로 균형 잡아, 불확실성이 높을 때 능동적으로 정보를 수집하여 예측 오류를 줄입니다.
- 수동적 방법과 비교하여, 특히 인간 행동이 예측 불가능한 시나리오에서 상호작용 궤적의 매끄러움과 안전성을 크게 향상시킵니다.

### 결론
- 암시적 이중 제어는 상호작용 운동 계획에 계산적으로 실현 가능한 능동적 불확실성 감소 방안을 제공하며, 실시간 로봇 시스템에 적합합니다.
- 향후 더 복잡한 인간 모델과 다중 로봇 상호작용 시나리오로 확장할 수 있습니다.
