---
$id: ent_paper_kumbhar_lidar_based_humanoid_navigatio_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: LiDAR-based Humanoid Navigation in Dynamic, Non-Convex Environments via Spatio-Temporal Safe Corridors
  zh: LiDAR-based Humanoid Navigation in Dynamic, Non-Convex Environments via Spatio-Temporal Safe Corridors
  ko: LiDAR-based Humanoid Navigation in Dynamic, Non-Convex Environments via Spatio-Temporal Safe Corridors
summary:
  en: Navigating humanoid robots through dynamic, non-convex environments requires tightly coupling onboard perception with
    footstep planning and dynamic locomotion control. Existing methods frequently discard complex free space through simplified
    convex obstacle bounds and fail to account for real-time dynamic occupancy predictions. This paper presents a real-time
    framework for humanoid navigation ...
  zh: 该论文提出一种面向人形机器人实时导航的框架，直接从基于 LiDAR 的粒子表示构建时空安全走廊，并与基于 Linear Inverted Pendulum (LIP) 的规划及 Whole Body Control (WBC) 耦合，从而在动态非凸环境中实现导航。作者为
    Shubham S. Kumbhar 与 Panagiotis Artemiadis。在 Digit 人形机器人的仿真中，该框架在 24×24 m² 场地内绕行并进入移动非凸障碍的成功率达到 96%。
  ko: Navigating humanoid robots through dynamic, non-convex environments requires tightly coupling onboard perception with
    footstep planning and dynamic locomotion control. Existing methods frequently discard complex free space through simplified
    convex obstacle bounds and fail to account for real-time dynamic occupancy predictions. This paper presents a real-time
    framework for humanoid navigation ...
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
- humanoid_navigation
- lidar_perception
- safe_corridors
- footstep_planning
- whole_body_control
- dynamic_environments
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-10-19'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-10-19). Bibliographic metadata from arXiv API (2610.17232);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: arXiv:2610.17232 LiDAR-based Humanoid Navigation in Dynamic, Non-Convex Environments via Spatio-Temporal Safe Corridors
  url: https://arxiv.org/abs/2610.17232
  date: '2026-10-12'
  accessed_at: '2026-10-19'
---

## 概述

该工作针对人形机器人在动态、非凸环境中导航时感知与步态规划、动态运动控制需紧密耦合的难题展开。现有方法常以简化的凸障碍边界丢弃复杂自由空间，且未考虑实时动态占据预测。作者提出实时框架，直接从 LiDAR 粒子表示构造时空安全走廊，避免限制性几何假设，并将其与基于 Linear Inverted Pendulum (LIP) 的规划及 Whole Body Control (WBC) 结合。仿真在 Digit 人形机器人上进行，在 24×24 m² 场地内绕行并进入移动非凸障碍的成功率为 96%。消融实验表明，所提出的迭代多面体生成在狭窄走廊中显著优于单次迭代基线，评估还显示其对杂乱、传感器噪声、控制延迟与力扰动具有鲁棒性。

## 核心内容

### 问题背景
人形机器人在动态、非凸环境中导航，需要将机载感知与落脚点规划、动态运动控制紧密耦合。现有方法往往通过简化的凸障碍边界丢弃复杂自由空间，并且未能考虑实时的动态占据预测，因而难以应对移动的非凸结构。

### 方法
- 从基于 LiDAR 的粒子表示直接构建时空安全走廊（spatio-temporal safe corridors），不依赖限制性的几何假设。
- 将安全走廊与基于 Linear Inverted Pendulum (LIP) 的规划以及 Whole Body Control (WBC) 相耦合，形成实时导航框架。
- 采用迭代多面体生成方式构造走廊。

### 实验设置
- 在 Digit 人形机器人上进行仿真。
- 场景为 24×24 m² 场地，包含移动的非凸障碍，机器人需绕行并在其内部导航。
- 开展消融实验，比较迭代多面体生成与单次迭代基线。
- 评估对杂乱、传感器噪声、控制延迟与力扰动的鲁棒性。

### 关键结果
- 在 24×24 m² 场地内绕行并进入移动非凸障碍的成功率为 96%。
- 消融实验确认，所提出的迭代多面体生成在狭窄走廊中显著优于单次迭代基线。
- 评估显示框架对杂乱、传感器噪声、控制延迟与力扰动具有鲁棒性。

### 结论
该框架能够在不引入限制性几何假设的前提下，实现动态非凸环境中的人形机器人实时导航，并在仿真中表现出较高的成功率与鲁棒性。

## Overview

Navigating humanoid robots through dynamic, non-convex environments requires tightly coupling onboard perception with footstep planning and dynamic locomotion control. Existing methods frequently discard complex free space through simplified convex obstacle bounds and fail to account for real-time dynamic occupancy predictions. This paper presents a real-time framework for humanoid navigation that directly constructs spatio-temporal safe corridors from LiDAR-based particle representations and couples them with Linear Inverted Pendulum (LIP)-based planning and Whole Body Control (WBC) to enable navigation around and within moving non-convex structures without restrictive geometric assumptions. Simulations on the Digit humanoid yield a 96% success rate in navigating around and inside moving non-convex obstacles in a 24 by 24 m^2 arena. Ablation studies confirm that the proposed iterative polytope generation significantly outperforms single-iteration baselines in narrow corridors, while evaluations demonstrate robustness to clutter, sensor noise, control delays, and force perturbations.

## 参考
- https://arxiv.org/abs/2610.17232
