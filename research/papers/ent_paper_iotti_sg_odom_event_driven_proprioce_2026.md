---
$id: ent_paper_iotti_sg_odom_event_driven_proprioce_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'SG-ODOM: Event-Driven Proprioceptive State Estimation with Stability-Gated Contact Updates for Legged Robots'
  zh: 'SG-ODOM: Event-Driven Proprioceptive State Estimation with Stability-Gated Contact Updates for Legged Robots'
  ko: 'SG-ODOM: Event-Driven Proprioceptive State Estimation with Stability-Gated Contact Updates for Legged Robots'
summary:
  en: Reliable proprioceptive state estimation for legged robots fuses inertial sensing with kinematic sensing from leg encoders.
    The latter assumes a foot is stationary during the stance phase; however, physical foot touchdown does not necessarily
    provide a stationary reference for odometry, particularly during impact and load transfer. Repeatedly applying kinematic
    corrections throughout the same ...
  zh: SG-ODOM 是一个面向腿足机器人的本体感知里程计框架，由 Francesco Iotti、Chiyun Noh、Franco Angelini、Manolo Garabini、Ayoung Kim、Maurice Fallon
    与 Frank Dellaert 提出。其核心是用稳定性门控的接触选择来调度运动学更新：足端物理触地后需达到足够稳定的支撑条件才被接受用于状态估计，并由超时更新限制纯 IMU 递推的最长持续时间。在四足与人形平台的多个序列上，该方法精度与代表性先进估计器相当或更优，在
    GrandTour 数据集的室外序列上相对位姿误差（RPE）最多降低 25%。
  ko: Reliable proprioceptive state estimation for legged robots fuses inertial sensing with kinematic sensing from leg encoders.
    The latter assumes a foot is stationary during the stance phase; however, physical foot touchdown does not necessarily
    provide a stationary reference for odometry, particularly during impact and load transfer. Repeatedly applying kinematic
    corrections throughout the same ...
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
- proprioceptive_odometry
- state_estimation
- legged_robots
- contact_scheduling
- humanoid_robots
- relative_pose_error
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-11-23'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-11-23). Bibliographic metadata from arXiv API (2611.20710);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2611.20710 SG-ODOM: Event-Driven Proprioceptive State Estimation with Stability-Gated Contact Updates for
    Legged Robots'
  url: https://arxiv.org/abs/2611.20710
  date: '2026-11-16'
  accessed_at: '2026-11-23'
---

## 概述

腿足机器人的可靠本体感知状态估计通常融合惯性传感与来自腿部编码器的运动学信息，后者依赖支撑相内足端静止的假设。但物理触地并不必然提供稳定的里程计参考，尤其在冲击与载荷转移阶段，而在同一接触相内反复施加运动学修正会引入冗余或不可靠的信息。SG-ODOM 因此引入稳定性门控的接触选择机制来调度运动学更新：足端触地后，只有达到足够稳定支撑条件时该接触才被接受用于状态估计，由此产生的已验证触地事件触发一次估计器修正；同时以超时更新限定无中断 IMU 递推的最长时长。作者在四足与人形等多种腿足平台上，将该框架与代表性先进本体感知估计器进行对比评估。在评估序列中，SG-ODOM 的估计精度具有竞争力或更优，在 GrandTour 数据集的室外序列上相较基线估计器将相对位姿误差（RPE）最多降低 25%。

## 核心内容

### 问题背景

腿足机器人的本体感知状态估计一般融合两类信息：惯性传感，以及由腿部编码器提供的运动学信息。运动学信息的使用前提是支撑相内足端保持静止，从而可作为里程计的静止参考。然而，物理触地并不一定意味着足端已能提供稳定的里程计参考，在冲击与载荷转移阶段尤其如此。若在同一接触相内反复施加运动学修正，会引入冗余或不可靠的信息，影响估计质量。

### 方法

SG-ODOM 是一个本体感知里程计框架，其关键设计是以稳定性门控的接触选择来调度运动学更新：

- **稳定性门控**：足端发生物理触地后，并不立即用于状态估计；只有当足端达到足够稳定的支撑条件时，稳定性门控才接受该接触。
- **事件驱动修正**：被接受的接触形成一个“已验证触地事件”，该事件触发一次估计器修正，而非在整段接触相内持续修正。
- **超时更新**：在缺乏有效触地事件时，通过超时更新限定无中断 IMU 递推的最大持续时间，避免长时间纯惯性递推带来的漂移。

### 实验设置

作者在多种腿足平台上进行评估，涵盖四足机器人与人形机器人，并与代表性的先进本体感知状态估计器进行对比。评估使用 GrandTour 数据集中的室外序列等序列。

### 关键结果

在所评估的序列上，SG-ODOM 展现出具有竞争力或更优的估计精度；在 GrandTour 数据集的室外序列上，相较基线估计器，其相对位姿误差（RPE）最多降低 25%。

### 结论

通过稳定性门控的接触选择与事件驱动的修正调度，SG-ODOM 避免了在单一接触相内重复施加不可靠运动学修正的问题，并在四足与人形平台上取得有竞争力或更优的本体感知状态估计精度。源码与视频已公开。

## Overview

Reliable proprioceptive state estimation for legged robots fuses inertial sensing with kinematic sensing from leg encoders. The latter assumes a foot is stationary during the stance phase; however, physical foot touchdown does not necessarily provide a stationary reference for odometry, particularly during impact and load transfer. Repeatedly applying kinematic corrections throughout the same contact phase can introduce redundant or unreliable information. We present SG-ODOM, a proprioceptive odometry framework that uses stability-gated contact selection to schedule kinematic updates. Following physical touchdown, a stability gate accepts the contact for state estimation only after the foot reaches a sufficiently stable support condition. The resulting validated touchdown event triggers an estimator correction, while additional timeout updates bound the maximum duration of uninterrupted IMU propagation. The framework is evaluated on multiple legged platforms, both quadrupedal and humanoid robots, against representative state-of-the-art proprioceptive estimators. Across the evaluated sequences, SG-ODOM demonstrates competitive or superior estimation accuracy, reducing Relative Pose Error (RPE) by up to 25% compared to the baseline estimator on outdoor sequences from the GrandTour dataset. Source code: https://github.com/ori-drs/SG-ODOM. Video: https://youtu.be/-583_RyuhqQ

## 参考
- https://arxiv.org/abs/2611.20710
