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
  reviewed_at: '2026-07-09'
  confidence: high
  notes: Curated names and summary from data/gap-entity-polish.yaml; placeholder body rewritten. Pending domain-expert final
    review.
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

# Model Predictive Control / 模型预测控制 / 모델 예측 제어

## 抽象

> **生活实例**：下棋时不仅看当前一步，而是预想未来几步并选最好的一步走。MPC 就是机器人在每个控制周期里“预想”未来运动并优化。
>
> **自然语言逻辑**：利用系统模型预测未来一段时间内的状态轨迹，以目标函数（如跟踪误差、能耗）最小化为目标，求解未来一段控制序列；只实施第一个控制量，下一时刻重新求解。

## 形式化骨架

在每个采样时刻 $t$，求解：

$$\min_{\mathbf{u}_{0:N-1}} \quad \sum_{k=0}^{N-1} \ell(\mathbf{x}_k, \mathbf{u}_k) + V_f(\mathbf{x}_N)$$

$$\text{s.t.} \quad \mathbf{x}_{k+1} = f(\mathbf{x}_k, \mathbf{u}_k), \quad \mathbf{x}_0 = \hat{\mathbf{x}}(t),$$

$$\mathbf{x}_k \in \mathcal{X}, \quad \mathbf{u}_k \in \mathcal{U},$$

其中 $N$ 为预测时域，$\ell$ 为阶段代价，$V_f$ 为终端代价。实施 $\mathbf{u}_0^*$ 后滚动时域。

## 与人形机器人的关系

- 步态优化：选择接触序列与质心/动量轨迹。
- 实时求解：依赖高效 QP 求解器（如 OSQP、qpOASES）。
- 鲁棒性：常结合扰动观测器或 tube-MPC 处理模型误差。

## 与其他知识点的关系

- `based_on` → [ent_formalism_euler_lagrange_equations]
- `solves` → [ent_qp_standard_form]
- `requires` → [ent_foundation_convex_optimization]
- `implemented_on` → 人形机器人整机 / 步态控制
