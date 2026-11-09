---
$id: ent_paper_bohlinger_stride_learning_humanoid_locom_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'STRIDE: Learning Humanoid Locomotion in Minutes with Acceleration-Based Rewards'
  zh: 'STRIDE: Learning Humanoid Locomotion in Minutes with Acceleration-Based Rewards'
  ko: 'STRIDE: Learning Humanoid Locomotion in Minutes with Acceleration-Based Rewards'
summary:
  en: Learning locomotion directly on a humanoid robot is a promising direction to avoid the sim-to-real gap. However, locomotion
    rewards in Reinforcement Learning (RL) typically track the base velocity, which cannot be measured onboard without an
    external motion capture system or well-calibrated state estimator. This is why we introduce \method{}, which learns humanoid
    locomotion from minutes of ...
  zh: STRIDE 是一种直接在真实人形机器人上学习运动策略的方法，由 Nico Bohlinger 与 Jan Peters 提出。其核心是用仅依赖机载 IMU 的加速度指令跟踪奖励替代传统的基座速度跟踪奖励，并结合 off-policy
    算法 XQC、高增益关节位置控制与左右对称增强，在仿真中让 Unitree G1 与 Booster T1 在 14 分钟样本内学会行走。
  ko: Learning locomotion directly on a humanoid robot is a promising direction to avoid the sim-to-real gap. However, locomotion
    rewards in Reinforcement Learning (RL) typically track the base velocity, which cannot be measured onboard without an
    external motion capture system or well-calibrated state estimator. This is why we introduce \method{}, which learns humanoid
    locomotion from minutes of ...
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
- reinforcement_learning
- imu_reward
- off_policy_rl
- symmetry_augmentation
- sim_to_real
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-11-09'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-11-09). Bibliographic metadata from arXiv API (2611.08857);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2611.08857 STRIDE: Learning Humanoid Locomotion in Minutes with Acceleration-Based Rewards'
  url: https://arxiv.org/abs/2611.08857
  date: '2026-11-06'
  accessed_at: '2026-11-09'
---

## 概述

直接在真实人形机器人上学习运动可规避仿真到现实的差距，但强化学习常用的基座速度奖励难以在机上无外部动捕或良好状态估计器时获得。STRIDE 因此改为奖励机器人跟随给定的加速度指令曲线，该奖励只需机载 IMU 即可计算。为高效利用这一奖励，方法采用 off-policy 算法 XQC，并配合关节位置控制器的高增益设置与左右对称数据增强。在仿真中，STRIDE 在 Unitree G1 和 Booster T1 上于 14 分钟样本内学会行走；相比缺少这两个组件的设置，训练中跌倒次数减少 81%，而后者需要超过一小时才能学会。

## 核心内容

### 问题背景
直接在真实人形机器人上学习运动是避免 sim-to-real 差距的有前景方向。然而强化学习中的运动奖励通常跟踪基座速度，而该量在没有外部动捕系统或良好标定的状态估计器时无法机载测量，这限制了真机直接学习的可行性。

### 方法
- **奖励设计**：STRIDE 不跟踪基座速度，而是奖励机器人跟随指令的加速度曲线，该奖励仅需机载 Inertial Measurement Unit (IMU)。
- **学习算法**：采用 off-policy 强化学习算法 XQC，以从该奖励中高效学习。
- **关键组件**：将关节位置控制器的高增益设置与左右对称增强结合使用。

### 实验设置
实验在仿真中进行，平台为 Unitree G1 与 Booster T1 两款人形机器人。

### 关键结果
- STRIDE 在 14 分钟样本内学会行走。
- 与不使用高增益设置和左右对称增强这两个组件的学习相比，训练期间跌倒次数减少 81%。
- 缺少这两个组件时，机器人需要超过一小时才能学会。

### 结论
仅依赖机载 IMU 的加速度指令奖励，配合 XQC、高增益关节位置控制与左右对称增强，可在数分钟级样本内实现人形机器人行走学习，并显著降低训练中的跌倒。

## Overview

Learning locomotion directly on a humanoid robot is a promising direction to avoid the sim-to-real gap. However, locomotion rewards in Reinforcement Learning (RL) typically track the base velocity, which cannot be measured onboard without an external motion capture system or well-calibrated state estimator. This is why we introduce \method{}, which learns humanoid locomotion from minutes of samples with a reward that only requires the onboard Inertial Measurement Unit (IMU). Instead of tracking the base velocity, STRIDE rewards the robot for following a commanded acceleration profile. To learn efficiently from this reward, we use the off-policy RL algorithm XQC and combine a high gain setting for the joint position controllers with left-right symmetry augmentation. In simulation, STRIDE learns to walk on the Unitree G1 and Booster T1 humanoids within 14 minutes of samples. Compared to learning without these two components, it reduces the falls during training by 81%, while without them the robot learns only in over an hour.

## 参考
- https://arxiv.org/abs/2611.08857
