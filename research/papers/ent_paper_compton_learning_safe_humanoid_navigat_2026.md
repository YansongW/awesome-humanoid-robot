---
$id: ent_paper_compton_learning_safe_humanoid_navigat_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning Safe Humanoid Navigation from Reduced Order Models
  zh: Learning Safe Humanoid Navigation from Reduced Order Models
  ko: Learning Safe Humanoid Navigation from Reduced Order Models
summary:
  en: Research in humanoid robotics has achieved rapid progress in locomotion, and recent results have pushed the boundary
    on autonomous navigation. We demonstrate that a standard single-stage RL navigation pipeline struggles to scale to multi-level
    and multi-story terrain, limited by the difficulty of complex humanoid terrain interactions such as stairs. To overcome
    this challenge, we decompose the ...
  zh: 该工作提出 RoM-Nav，一种面向人形机器人导航的两阶段强化学习流程：先在降阶动力学模型上利用完整 3D LiDAR 观测训练导航策略，再以此知识启动全阶人形动力学策略，并冻结底层运动策略。作者来自 William D. Compton、Zachary
    Olkin、Ryan Bena、Aaron D. Ames 团队，在 Unitree G1 上实现了无地图多层导航，垂直位移超过 10m、路径长度超过 100m，并引入 Poisson 安全滤波器在分布外障碍下恢复安全性且不降低导航成功率。
  ko: Research in humanoid robotics has achieved rapid progress in locomotion, and recent results have pushed the boundary
    on autonomous navigation. We demonstrate that a standard single-stage RL navigation pipeline struggles to scale to multi-level
    and multi-story terrain, limited by the difficulty of complex humanoid terrain interactions such as stairs. To overcome
    this challenge, we decompose the ...
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
- reinforcement_learning
- reduced_order_model
- safety_filter
- lidar
- unitree_g1
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-09-21'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-09-21). Bibliographic metadata from arXiv API (2609.19272);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: arXiv:2609.19272 Learning Safe Humanoid Navigation from Reduced Order Models
  url: https://arxiv.org/abs/2609.19272
  date: '2026-09-16'
  accessed_at: '2026-09-21'
---

## 概述

该研究针对人形机器人自主导航中单阶段强化学习流程难以扩展到多层、多楼层地形的问题，指出楼梯等复杂地形交互是主要瓶颈。作者将导航问题拆解为两部分：首先在降阶动力学上训练策略，但保留完整 3D LiDAR 观测，使其能够应对复杂多层地形；随后用这一导航知识启动全阶人形动力学策略，并在回路中冻结运动策略。此外，作者对导航策略输出施加 Poisson 安全滤波器，在遇到分布外障碍时恢复安全性，同时不牺牲导航成功率。最终得到的 RoM-Nav 策略在 Unitree G1 上完成无地图多楼层导航，试验覆盖超过 10m 的垂直位移与超过 100m 的路径长度。

## 核心内容

### 问题背景
人形机器人运动控制进展迅速，自主导航也取得突破，但标准单阶段强化学习导航流程难以扩展到多层、多楼层地形。作者指出，瓶颈在于楼梯等复杂人形地形交互的难度。

### 方法
作者将导航问题分解为两个阶段：
- 第一阶段：在降阶动力学（reduced order dynamics）上训练策略，但使用完整的 3D LiDAR 观测，以应对复杂多层地形。
- 第二阶段：利用第一阶段的导航知识启动全阶人形动力学（full-order humanoid dynamics）策略，回路中保持运动策略冻结。
- 安全机制：对导航策略输出施加 Poisson 安全滤波器，在分布外障碍存在时恢复安全性，且不降低导航成功率。

### 实验设置与关键结果
- 在 Unitree G1 上验证最终得到的 RoM-Nav 策略。
- 实现无地图（mapless）多楼层导航。
- 试验覆盖超过 10m 的垂直位移与超过 100m 的路径长度。
- 项目主页含视频：https://wdc3iii.github.io/rom-nav/

### 结论
通过降阶模型预训练加全阶策略启动的两阶段分解，并配合 Poisson 安全滤波器，RoM-Nav 使单阶段流程难以处理的多层、多楼层人形导航成为可能，同时兼顾安全性与导航成功率。

## Overview

Research in humanoid robotics has achieved rapid progress in locomotion, and recent results have pushed the boundary on autonomous navigation. We demonstrate that a standard single-stage RL navigation pipeline struggles to scale to multi-level and multi-story terrain, limited by the difficulty of complex humanoid terrain interactions such as stairs. To overcome this challenge, we decompose the navigation problem into two pieces. First, we train a policy operating on the reduced order dynamics but with full 3D LiDAR observations to navigate complex, multi-story terrain. We then utilize this navigation knowledge to kickstart a policy operating on the full-order humanoid dynamics, with a frozen locomotion policy in the loop. Additionally, we demonstrate that applying a Poisson safety filter to the navigation policy output recovers safety in the presence of out-of-distribution obstacles, without dropping navigation success rate. We demonstrate the resulting RoM-Nav policy on a Unitree G1, accomplishing mapless multi-floor navigation covering trials with over 10m of vertical displacement and over 100m of path length. Project page with videos https://wdc3iii.github.io/rom-nav/ .

## 参考
- https://arxiv.org/abs/2609.19272
