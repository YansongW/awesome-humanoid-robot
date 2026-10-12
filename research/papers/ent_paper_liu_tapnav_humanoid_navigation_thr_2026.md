---
$id: ent_paper_liu_tapnav_humanoid_navigation_thr_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'TAPNAV: Humanoid Navigation through Tactile Active Perception'
  zh: 'TAPNAV: Humanoid Navigation through Tactile Active Perception'
  ko: 'TAPNAV: Humanoid Navigation through Tactile Active Perception'
summary:
  en: Navigation in vision-denied environments is challenging for humanoid robots because proprioceptive odometry drifts and
    localization uncertainty accumulates rapidly. We present TAPNAV, a tactile active-perception framework that enables humanoid
    navigation toward a goal by actively probing surrounding structures without relying on vision. TAPNAV maintains a pose
    belief from odometry, IMU, and ...
  zh: TAPNAV 是一种面向人形机器人的触觉主动感知导航框架，由 Huaze Liu、Zhenyu Wu、Jaehwi Jang 等人提出，可在无视觉条件下通过主动触碰周围结构完成导航。该方法融合里程计、IMU 与触觉接触观测维护位姿信念，并将不确定性感知的全局路径规划与信息增益驱动的局部探测相结合。在仿真与
    Unitree G1 上的实验表明，其状态估计误差低于基线，任务完成率更高。
  ko: Navigation in vision-denied environments is challenging for humanoid robots because proprioceptive odometry drifts and
    localization uncertainty accumulates rapidly. We present TAPNAV, a tactile active-perception framework that enables humanoid
    navigation toward a goal by actively probing surrounding structures without relying on vision. TAPNAV maintains a pose
    belief from odometry, IMU, and ...
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
- tactile_active_perception
- uncertainty_aware_planning
- whole_body_control
- vision_denied_environments
- state_estimation
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-10-12'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-10-12). Bibliographic metadata from arXiv API (2610.10748);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2610.10748 TAPNAV: Humanoid Navigation through Tactile Active Perception'
  url: https://arxiv.org/abs/2610.10748
  date: '2026-10-07'
  accessed_at: '2026-10-12'
---

## 概述

在视觉受限环境中，人形机器人仅靠本体感受里程计会快速累积定位不确定性，导致导航失败。TAPNAV 通过主动探测周围结构来获取定位线索，不依赖视觉。它基于里程计、IMU 和触觉接触观测维护位姿信念，并让全局规划器搜索能够借助触觉修正机会、使预测定位不确定性保持有界的路线，同时由局部规划器选择期望信息增益最大的探测动作。全身控制器负责协调机器人的行走与末端接触，以执行导航和探测动作。作者在仿真和 Unitree G1 上针对不同户型与障碍物几何形状进行了评估，结果显示 TAPNAV 的状态估计误差更低、任务完成率更高。

## 核心内容

### 问题背景
在视觉被遮挡或不可用的环境中，人形机器人导航面临的核心困难是本体感受里程计会发生漂移，定位不确定性迅速累积，从而难以可靠地抵达目标点。

### 方法
TAPNAV 是一个触觉主动感知框架，其核心思路是不依赖视觉，而是通过主动探测周围结构来获取定位线索。系统包含以下组成部分：
- **位姿信念维护**：融合里程计、IMU 与触觉接触观测，持续估计机器人位姿。
- **全局规划器**：搜索能够将预测定位不确定性保持在一定范围内的路线，其方式是主动利用可进行触觉修正的机会。
- **局部规划器**：选择使期望信息增益最大的探测动作。
- **全身控制器**：协调人形机器人的行走运动与末端执行器接触，以执行规划出的导航与探测动作。

### 实验设置
作者在仿真环境以及 Unitree G1 人形机器人上进行了评估，测试场景涵盖不同的户型布局与障碍物几何形状。

### 关键结果
与基线方法相比，TAPNAV 取得了更低的状态估计误差和更高的任务完成率。

### 结论
实验结果表明，主动规划与环境的物理交互可以为定位提供线索，从而在无视觉条件下实现可靠的人形机器人导航。

## Overview

Navigation in vision-denied environments is challenging for humanoid robots because proprioceptive odometry drifts and localization uncertainty accumulates rapidly. We present TAPNAV, a tactile active-perception framework that enables humanoid navigation toward a goal by actively probing surrounding structures without relying on vision. TAPNAV maintains a pose belief from odometry, IMU, and tactile contact observations, and couples uncertainty-aware global route planning with information-gain-driven local probing. The global planner searches for routes that keep predicted localization uncertainty bounded by exploiting opportunities for tactile correction, while the local planner selects probe actions that maximize expected information gain. A whole-body controller coordinates the humanoid's locomotion and end-effector contact to execute the planned navigation and probe motions. We evaluate TAPNAV in simulation and on a Unitree G1 across different floor plans and obstacle geometries. TAPNAV achieves lower state estimation error and a higher task completion rate than baselines. These results demonstrate that actively planning physical interactions with the environment can provide localization cues for reliable humanoid navigation without vision.

## 参考
- https://arxiv.org/abs/2610.10748
