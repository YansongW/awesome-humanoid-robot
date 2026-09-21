---
$id: ent_paper_keshavarz_adaptive_mhe_a_sampling_based_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Adaptive-MHE : A Sampling-Based Adaptive MPC for Legged Loco-Manipulation via Moving Horizon Estimation'
  zh: 'Adaptive-MHE : A Sampling-Based Adaptive MPC for Legged Loco-Manipulation via Moving Horizon Estimation'
  ko: 'Adaptive-MHE : A Sampling-Based Adaptive MPC for Legged Loco-Manipulation via Moving Horizon Estimation'
summary:
  en: Legged robots have demonstrated a remarkable ability to traverse various terrains, yet generating effective loco-manipulation
    behaviors remains challenging. A key difficulty is that object and terrain parameters are typically unknown to the robot,
    and mismatches between these parameters and their simulated counterparts introduce a sim-to-real gap that degrades control
    performance. Classical ...
  zh: Adaptive-MHE 是一个面向腿足机器人 loco-manipulation 的在线采样式系统辨识框架，由 Hossein Keshavarz、Alejandro Ramirez-Serrano 与 Majid Khadiv
    提出。它基于 moving horizon estimation（MHE）在线估计物体与地形的物理参数（如质量、摩擦），并将估计结果与采样式模型预测控制器耦合，从而在变化且不确定的环境中实现自适应 loco-manipulation。在仿真与硬件实验中，该框架持续优于基线方法，并达到与已知真实参数控制器相当的性能。
  ko: Legged robots have demonstrated a remarkable ability to traverse various terrains, yet generating effective loco-manipulation
    behaviors remains challenging. A key difficulty is that object and terrain parameters are typically unknown to the robot,
    and mismatches between these parameters and their simulated counterparts introduce a sim-to-real gap that degrades control
    performance. Classical ...
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
- legged_loco_manipulation
- moving_horizon_estimation
- sampling_based_mpc
- system_identification
- sim_to_real
- adaptive_control
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-09-21'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-09-21). Bibliographic metadata from arXiv API (2609.17832);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2609.17832 Adaptive-MHE : A Sampling-Based Adaptive MPC for Legged Loco-Manipulation via Moving Horizon Estimation'
  url: https://arxiv.org/abs/2609.17832
  date: '2026-09-15'
  accessed_at: '2026-09-21'
---

## 概述

腿足机器人虽能穿越多种地形，但生成有效的 loco-manipulation 行为仍很困难，核心难点在于物体与地形参数对机器人未知，这些参数与仿真设定之间的不匹配会造成 sim-to-real gap，削弱控制性能。经典系统辨识（Sys-ID）方法通常假设动力学可微，而这一假设对接触丰富的腿足系统并不成立。采样式 Sys-ID 通过大规模并行 rollout 直接匹配仿真与记录的状态轨迹，绕开了可微性限制，但现有方法多为离线应用，无法随环境条件变化而调整。为此作者提出 Adaptive-MHE，一个基于 moving horizon estimation（MHE）的在线采样式 Sys-ID 框架，用于估计环境中物体与地形的物理参数（如质量、摩擦），并将其与采样式模型预测控制器耦合，实现变化与不确定环境下的自适应 loco-manipulation。仿真与硬件实验表明，该框架持续优于基线，并达到与可访问真实参数控制器相当的性能。

## 核心内容

### 问题背景
腿足机器人已展现出穿越多种地形的能力，但生成有效的 loco-manipulation 行为依然具有挑战性。一个关键困难在于，物体与地形参数对机器人而言通常是未知的，而这些参数与其仿真对应值之间的不匹配会引入 sim-to-real gap，进而降低控制性能。

经典系统辨识（Sys-ID）方法往往假设动力学可微，但这一假设对接触丰富的腿足系统并不成立。采样式 Sys-ID 通过大规模并行 rollout 直接匹配仿真与记录的状态轨迹，从而规避了可微性限制；然而现有方法通常以离线方式应用，无法随环境条件变化而自适应调整。

### 方法
作者提出 Adaptive-MHE，一个在线采样式 Sys-ID 框架：

- 基于 moving horizon estimation（MHE）构建；
- 在线估计环境中物体与地形的物理参数，例如质量与摩擦；
- 将该参数估计与采样式模型预测控制器相耦合；
- 由此支持在变化且不确定的环境中进行自适应 loco-manipulation。

### 实验与结果
在仿真与硬件实验中，该框架：

- 持续优于基线方法；
- 性能与可访问 ground-truth 参数的控制器相当。

### 结论
Adaptive-MHE 通过将基于 MHE 的在线采样式系统辨识与采样式模型预测控制相结合，解决了未知物体与地形参数带来的 sim-to-real gap 问题，并在仿真与硬件上验证了其自适应 loco-manipulation 的有效性。

## Overview

Legged robots have demonstrated a remarkable ability to traverse various terrains, yet generating effective loco-manipulation behaviors remains challenging. A key difficulty is that object and terrain parameters are typically unknown to the robot, and mismatches between these parameters and their simulated counterparts introduce a sim-to-real gap that degrades control performance. Classical system identification (Sys-ID) methods often assume differentiable dynamics, an assumption that does not hold for contact-rich legged systems. Sampling-based Sys-ID avoids this restriction by directly matching simulated and recorded state trajectories through massively parallel rollouts, but existing approaches are typically applied offline and do not adapt as environmental conditions change. We present Adaptive-MHE an online sampling-based Sys-ID framework, based on moving horizon estimation (MHE), that estimates the physical parameters of objects and terrain in the environment (e.g., mass, friction) and couples this estimate with a sampling-based model predictive controller, enabling adaptive loco-manipulation in changing and uncertain environments. In simulation and hardware experiments, our framework consistently outperforms baselines and matches the performance of a controller with access to ground-truth parameters.

## 参考
- https://arxiv.org/abs/2609.17832
