---
$id: ent_method_model_predictive_control
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: method
names:
  en: Model Predictive Control (MPC)
  zh: 模型预测控制（MPC）
  ko: 모델 예측 제어(MPC)
summary:
  en: An optimization-based control method that repeatedly solves a finite-horizon optimal control problem using a predictive
    model and applies only the first control action.
  zh: 基于预测模型反复求解有限时域最优控制问题并仅执行首步控制量的优化控制方法。
  ko: 예측 모델을 사용하여 유한 수평 최적 제어 문제를 반복적으로 풀고 첫 번째 제어 입력만 적용하는 최적화 기반 제어 방법.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
theoretical_depth:
- method
tags:
- control
- optimization
- locomotion
- gait
- whole_body_control
- realtime
- wiki_gap
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
  confidence: high
  notes: Body populated from Wiki chapter section by scripts/fill_gap_bodies_from_wiki.py; pending human review and translation
    to en/ko. Body backfilled from entity metadata by scripts/backfill_critical_entities.py.
sources:
- id: src_borrelli_bemporad_morari_2017
  type: other
  title: F. Borrelli, A. Bemporad, and M. Morari, Predictive Control for Linear and Hybrid Systems, Cambridge, 2017
  url: https://doi.org/10.1017/9781139061799
  date: '2017-01-01'
  accessed_at: '2026-07-09'
- id: src_kuindersma_et_al_2016
  type: paper
  title: S. Kuindersma et al., Optimization-based Locomotion Planning, Estimation, and Control Design for Atlas, Autonomous
    Robots, 2016
  url: https://doi.org/10.1007/s10514-016-9572-3
  date: '2016-08-01'
  accessed_at: '2026-07-09'
related_entities:
- id: ent_formalism_euler_lagrange_equations
  relationship: is_based_on
  description:
    en: MPC for humanoids commonly uses floating-base dynamics derived from Euler-Lagrange or Newton-Euler equations as the
      prediction model.
    zh: 人形机器人的 MPC 通常以欧拉-拉格朗日或牛顿-欧拉导出的浮动基动力学作为预测模型。
- id: ent_qp_standard_form
  relationship: solves
  description:
    en: Each MPC iteration solves a quadratic program (QP) when the dynamics and constraints are linearized.
    zh: 当动态与约束被线性化时，每次 MPC 迭代求解一个二次规划（QP）。
- id: ent_foundation_convex_optimization
  relationship: requires
  description:
    en: Stability and tractability of MPC rely on convex optimization theory and efficient QP solvers.
    zh: MPC 的稳定性与可解性依赖于凸优化理论与高效 QP 求解器。
---
## 概述
基于预测模型反复求解有限时域最优控制问题并仅执行首步控制量的优化控制方法。

## 核心内容
### 模型预测控制（MPC）的定义与定位
模型预测控制（MPC）属于 **method** 类型。 所属领域包括：07_ai_models_algorithms。 价值链层级：intelligence。 基于预测模型反复求解有限时域最优控制问题并仅执行首步控制量的优化控制方法。 英文名称为 *Model Predictive Control (MPC)*。 韩文名称为 *모델 예측 제어(MPC)*。

### 模型预测控制（MPC）的数学与原理基础
模型预测控制（MPC）建立在相关数学理论与物理规律之上。理解其前提假设、约束条件与推导过程，是正确应用该方法的前提。
具体而言，需要关注其输入空间、输出空间、目标函数以及收敛性或稳定性保证。
在人形机器人这一高维、欠驱动、强耦合系统中，模型预测控制（MPC）通常需要在实时性、精度与鲁棒性之间取得平衡。

### 算法步骤与实现要点
在实际实现模型预测控制（MPC）时，需要明确初始化条件、迭代规则、停止准则以及参数调优策略。
合理选择数值方法、线性代数求解器与并行计算策略，能够显著提升计算效率与稳定性。
同时，应充分考虑模型误差、传感器噪声与执行器饱和等工程约束，确保算法在真实平台上可靠运行。

### 典型应用与局限性
模型预测控制（MPC）可应用于人形机器人的运动规划、控制优化、状态估计与学习算法等多个环节。
然而，其计算复杂度、对模型精度的依赖以及在线适应能力仍是实际部署中需要重点解决的问题。

### 相关标签
- control
- optimization
- locomotion
- gait
- whole_body_control
- realtime
- wiki_gap

### 在人形机器人系统中的作用
作为人形机器人产业链中的关键method之一，模型预测控制（MPC）在系统设计、性能优化和产业化应用中扮演着重要角色。它与感知、决策、执行、能源、结构与验证等多个子系统相互耦合，共同决定了整机性能。相关研究与应用正在持续推进，以进一步提升其在实际场景中的可靠性、效率和经济性。

## 参考
- [F. Borrelli, A. Bemporad, and M. Morari, Predictive Control for Linear and Hybrid Systems, Cambridge, 2017](https://doi.org/10.1017/9781139061799)
- [S. Kuindersma et al., Optimization-based Locomotion Planning, Estimation, and Control Design for Atlas, Autonomous Robots, 2016](https://doi.org/10.1007/s10514-016-9572-3)

