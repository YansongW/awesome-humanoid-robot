---
$id: ent_paper_wang_dr_mpc_fast_and_feasible_dynam_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'DR-MPC: Fast and Feasible Dynamics-Relaxed Model-Predictive Control for Legged Locomotion'
  zh: 'DR-MPC: Fast and Feasible Dynamics-Relaxed Model-Predictive Control for Legged Locomotion'
  ko: 'DR-MPC: Fast and Feasible Dynamics-Relaxed Model-Predictive Control for Legged Locomotion'
summary:
  en: This paper presents dynamics-relaxed model predictive control (DR-MPC), a novel MPC formulation for legged locomotion,
    and a tailored interior-point method (IPM) solver. The formulation combines online optimization feasibility by construction
    with a contact-aware input parameterization. DR-MPC moves the dynamics equality and affine input constraints into quadratic
    penalties and retains only ...
  zh: 本文提出 dynamics-relaxed model predictive control（DR-MPC），一种面向足式运动的 MPC 新形式，并配套设计了专用的内点法（IPM）求解器。该方法通过将动力学等式约束与仿射输入约束转化为二次惩罚项，仅保留非空的箱式约束，从而在构造上保证在线优化可行性，并引入接触感知的输入参数化。在相同
    DR-MPC 形式下，其实现相比 HPIPM 取得中位 16.0×、相比 OSQP 取得中位 4.4× 的端到端加速，并在 Unitree Go1 四足机器人上验证了中位 4.4 ms 的机载 MPC 端到端耗时。
  ko: This paper presents dynamics-relaxed model predictive control (DR-MPC), a novel MPC formulation for legged locomotion,
    and a tailored interior-point method (IPM) solver. The formulation combines online optimization feasibility by construction
    with a contact-aware input parameterization. DR-MPC moves the dynamics equality and affine input constraints into quadratic
    penalties and retains only ...
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
theoretical_depth:
- system
tags:
- model_predictive_control
- legged_locomotion
- interior_point_method
- quadratic_programming
- quadruped_robot
- real_time_control
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-09-21'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-09-21). Bibliographic metadata from arXiv API (2609.20035);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2609.20035 DR-MPC: Fast and Feasible Dynamics-Relaxed Model-Predictive Control for Legged Locomotion'
  url: https://arxiv.org/abs/2609.20035
  date: '2026-09-17'
  accessed_at: '2026-09-21'
---

## 概述

DR-MPC 是一种面向足式运动的模型预测控制新形式，由 Run Wang、Alapati Tuerxun、Shuo Liu、Wei Xiao、Ján Drgoňa、Yilin Mo、Liang Wu 提出，并配有专门设计的内点法求解器。其核心思路是把动力学等式约束和仿射输入约束移入二次惩罚项，只保留非空的箱式约束，使在线优化的可行性由构造保证，同时采用接触感知的输入参数化。由此得到的箱式约束二次规划具有块箭头型 Hessian，可通过 Schur 补消去状态与仿射输出方向；在摆动相力消元与接触对齐的 move blocking 之后，求解器只需对约简后的控制系统做分解。在相同 DR-MPC 形式下，该方法相比 HPIPM 与 OSQP 分别取得中位 16.0× 与 4.4× 的端到端 MPC 加速，仿真中运动性能相当，并在 Unitree Go1 四足机器人上实现中位 4.4 ms 的机载端到端耗时。

## 核心内容

### 问题背景
足式运动的模型预测控制通常需要在线求解带动力学等式约束与输入约束的优化问题，这类约束会显著增加求解负担，影响机载实时性。本文关注如何在保持运动性能的前提下，提升 MPC 的端到端求解速度与在线可行性。

### 方法
- 提出 dynamics-relaxed model predictive control（DR-MPC）形式：将动力学等式约束与仿射输入约束移入二次惩罚项，仅保留非空的箱式约束，使在线优化可行性由构造保证。
- 采用接触感知（contact-aware）的输入参数化。
- 所得问题为箱式约束二次规划（QP），其 Hessian 呈块箭头（block-arrow）结构，可借助 Schur 补消去状态方向与仿射输出方向。
- 配套设计专用内点法（IPM）求解器：在摆动相力消元（swing-force elimination）与接触对齐的 move blocking 之后，仅对约简后的控制系统进行分解。

### 实验设置与关键结果
- 在相同 DR-MPC 形式下的实现对比中，本方法端到端 MPC 速度中位数相比 HPIPM 提升 16.0×，相比 OSQP 提升 4.4×。
- 仿真中运动性能与对比方法相当。
- DR-MPC 的机载 MPC 端到端耗时中位数为 4.4 ms。
- 在 Unitree Go1 四足机器人上完成验证。

### 结论
DR-MPC 通过约束松弛与接触感知参数化，在保证在线可行性的同时显著降低求解开销，并在真实四足平台上实现了毫秒级的机载 MPC 端到端耗时。开源代码将在论文发表后提供。

## Overview

This paper presents dynamics-relaxed model predictive control (DR-MPC), a novel MPC formulation for legged locomotion, and a tailored interior-point method (IPM) solver. The formulation combines online optimization feasibility by construction with a contact-aware input parameterization. DR-MPC moves the dynamics equality and affine input constraints into quadratic penalties and retains only nonempty box constraints. The resulting box-constrained quadratic program (QP) has a block-arrow Hessian that enables the state and affine-output directions to be eliminated through a Schur complement. The solver factors only the reduced control system after swing-force elimination and contact-aligned move blocking. For the evaluated implementations using the same DR-MPC formulation, our method achieves median end-to-end MPC speedups of $16.0\times$ over HPIPM and $4.4\times$ over OSQP, with comparable locomotion performance in simulation. DR-MPC achieves a median onboard MPC end-to-end time of $4.4$ ms and is validated on a Unitree Go1 quadruped. Open-source code will be made available after publication.

## 参考
- https://arxiv.org/abs/2609.20035
