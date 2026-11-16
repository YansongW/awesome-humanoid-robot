---
$id: ent_paper_wang_react_reflection_consistent_mo_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ReACT: Reflection-Consistent Modulation and Cross-Load Consistency for Humanoid Velocity Tracking Under Asymmetric
    Loads'
  zh: 'ReACT: Reflection-Consistent Modulation and Cross-Load Consistency for Humanoid Velocity Tracking Under Asymmetric
    Loads'
  ko: 'ReACT: Reflection-Consistent Modulation and Cross-Load Consistency for Humanoid Velocity Tracking Under Asymmetric
    Loads'
summary:
  en: In recent years, humanoid loco-manipulation has progressed to whole-body grasping, lifting, and transport. A basic requirement
    underlying these tasks is carrying the object to its destination, which depends on the locomotion controller accurately
    executing velocity commands from the navigation policy. However, carrying an object in one hand introduces a persistent
    asymmetric upper-body load that ...
  zh: ReACT 是一个面向人形机器人单侧负重场景的速度跟踪框架，由 Xianghui Wang、Aoran Fu、Liyou Luo、Shanze Wang、Xiaoyu Shen、Dan Zhang、Wei Zhang 提出。其核心是反射一致性扰动调制与跨负载跟踪一致性训练两项机制，在
    Unitree G1 上验证了非对称负载下的速度跟踪改进与方向偏差降低。
  ko: In recent years, humanoid loco-manipulation has progressed to whole-body grasping, lifting, and transport. A basic requirement
    underlying these tasks is carrying the object to its destination, which depends on the locomotion controller accurately
    executing velocity commands from the navigation policy. However, carrying an object in one hand introduces a persistent
    asymmetric upper-body load that ...
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
- humanoid_locomotion
- velocity_tracking
- asymmetric_load
- disturbance_modulation
- cross_load_consistency
- loco_manipulation
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-11-16'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-11-16). Bibliographic metadata from arXiv API (2611.13929);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2611.13929 ReACT: Reflection-Consistent Modulation and Cross-Load Consistency for Humanoid Velocity Tracking
    Under Asymmetric Loads'
  url: https://arxiv.org/abs/2611.13929
  date: '2026-11-10'
  accessed_at: '2026-11-16'
---

## 概述

人形机器人搬运物体时，单手负重会带来持续的上体非对称负载，使运动控制器执行导航速度指令的精度下降，累积的跟踪偏差会转化为位置与朝向漂移，增加碰撞与导航失败风险。为此，作者提出 ReACT 框架，利用估计的力/力矩（wrench）调制 actor 特征以补偿负载，并保持反射观测下的动作对应关系，即反射一致性扰动调制。同时，跨负载跟踪一致性训练在相同速度指令下对比负载与空载条件，促使两种工况下的速度跟踪表现趋于一致。在 Unitree G1 人形机器人上的仿真实验显示速度跟踪改善、方向偏差减小；真实实验中，在固定无地图导航策略与单侧手部负载下，全部 40 次导航试验均实现无碰撞到达目标。

## 核心内容

### 问题背景

人形机器人 loco-manipulation 已发展到全身抓取、举升与搬运阶段，而这类任务的基本要求是把物体运送到目的地，这依赖运动控制器准确执行来自导航策略的速度指令。然而单手携带物体会引入持续的上体非对称负载，导致速度跟踪性能退化。持续的跟踪偏差会累积为位置与朝向偏差，从而提高碰撞与导航失败的风险。

### 方法

ReACT 框架包含两个关键组成部分：

- **反射一致性扰动调制（Reflection-consistent disturbance modulation）**：使用估计的 wrench 对 actor 特征进行调制以实现负载补偿，同时在反射观测下保持动作对应关系。
- **跨负载跟踪一致性训练（Cross-load tracking consistency training）**：在相同速度指令下比较负载与空载条件，促使不同负载工况下的速度跟踪保持一致。

### 实验设置

- 仿真实验平台为 Unitree G1 人形机器人，测试在不同非对称负载下的表现。
- 真实世界实验采用固定的无地图（mapless）导航策略，在单侧手部负载条件下进行导航测试。

### 关键结果

- 仿真实验显示，在不同非对称负载下速度跟踪得到改善，方向偏差有所减小。
- 真实实验中，全部 40 次测试的导航试验均实现无碰撞到达目标。

### 结论

ReACT 通过反射一致性扰动调制与跨负载跟踪一致性训练，缓解了单侧上体非对称负载造成的速度跟踪退化，并在仿真与真实机器人导航试验中验证了其有效性。

## Overview

In recent years, humanoid loco-manipulation has progressed to whole-body grasping, lifting, and transport. A basic requirement underlying these tasks is carrying the object to its destination, which depends on the locomotion controller accurately executing velocity commands from the navigation policy. However, carrying an object in one hand introduces a persistent asymmetric upper-body load that can degrade velocity tracking. Persistent tracking biases can accumulate into position and heading deviations, increasing the risk of collisions and navigation failure. To address this problem, we present ReACT, a framework for accurate velocity tracking under asymmetric upper-body loads. Reflection-consistent disturbance modulation uses the estimated wrench to modulate actor features for load compensation while preserving action correspondence under reflected observations. Cross-load tracking consistency training compares loaded and unloaded conditions under the same velocity commands to promote consistent velocity tracking across loading conditions. Simulation experiments on a Unitree G1 humanoid robot show improved velocity tracking and reduced directional bias under varying asymmetric loads. Real-world experiments demonstrate collision-free goal reaching in all 40 tested navigation trials under unilateral hand loads with a fixed mapless navigation policy.

## 参考
- https://arxiv.org/abs/2611.13929
