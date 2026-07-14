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
  en: An optimization-based control method that repeatedly solves a finite-horizon
    optimal control problem using a predictive model and applies only the first control
    action.
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
  notes: Body populated from Wiki chapter section by scripts/fill_gap_bodies_from_wiki.py;
    pending human review and translation to en/ko.
sources:
- id: src_borrelli_bemporad_morari_2017
  type: other
  title: F. Borrelli, A. Bemporad, and M. Morari, Predictive Control for Linear and
    Hybrid Systems, Cambridge, 2017
  url: https://doi.org/10.1017/9781139061799
  date: '2017-01-01'
  accessed_at: '2026-07-09'
- id: src_kuindersma_et_al_2016
  type: paper
  title: S. Kuindersma et al., Optimization-based Locomotion Planning, Estimation,
    and Control Design for Atlas, Autonomous Robots, 2016
  url: https://doi.org/10.1007/s10514-016-9572-3
  date: '2016-08-01'
  accessed_at: '2026-07-09'
related_entities:
- id: ent_formalism_euler_lagrange_equations
  relationship: is_based_on
  description:
    en: MPC for humanoids commonly uses floating-base dynamics derived from Euler-Lagrange
      or Newton-Euler equations as the prediction model.
    zh: 人形机器人的 MPC 通常以欧拉-拉格朗日或牛顿-欧拉导出的浮动基动力学作为预测模型。
- id: ent_qp_standard_form
  relationship: solves
  description:
    en: Each MPC iteration solves a quadratic program (QP) when the dynamics and constraints
      are linearized.
    zh: 当动态与约束被线性化时，每次 MPC 迭代求解一个二次规划（QP）。
- id: ent_foundation_convex_optimization
  relationship: requires
  description:
    en: Stability and tractability of MPC rely on convex optimization theory and efficient
      QP solvers.
    zh: MPC 的稳定性与可解性依赖于凸优化理论与高效 QP 求解器。
---

## 概述
基于预测模型反复求解有限时域最优控制问题并仅执行首步控制量的优化控制方法。

## Overview
An optimization-based control method that repeatedly solves a finite-horizon optimal control problem using a predictive model and applies only the first control action.

## 개요
An optimization-based control method that repeatedly solves a finite-horizon optimal control problem using a predictive model and applies only the first control action.
