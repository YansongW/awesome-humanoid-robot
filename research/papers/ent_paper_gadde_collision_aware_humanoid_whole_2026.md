---
$id: ent_paper_gadde_collision_aware_humanoid_whole_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Collision-Aware Humanoid Whole-Body Control under Imperfect Tracking Targets
  zh: Collision-Aware Humanoid Whole-Body Control under Imperfect Tracking Targets
  ko: Collision-Aware Humanoid Whole-Body Control under Imperfect Tracking Targets
summary:
  en: Humanoid robots often execute motion commands through whole-body controllers (WBCs) that track targets while maintaining
    balance and stability. However, most WBCs are blind to scene geometry, which can lead to collisions from imperfect target
    motions that are geometrically unsafe due to perception, planning, or teleoperation errors. We propose RECAL, a Robot--Environment
    Cross-Attention Layer ...
  zh: RECAL 是一种机器人—环境交叉注意力层（Robot–Environment Cross-Attention Layer），由 Mohitvishnu S. Gadde、Ashish Malik、Pranay Dugar、Aayam
    Kumar Shrestha 与 Alan Fern 提出，用于包裹原本对场景几何无感知的全身控制器（WBC）。它利用外部场景几何信息，在目标跟踪与碰撞避免之间进行权衡，支持浮动基座与末端执行器指令的碰撞感知跟踪，并已在仿真与真实 Digit
    V3 人形机器人上验证。
  ko: Humanoid robots often execute motion commands through whole-body controllers (WBCs) that track targets while maintaining
    balance and stability. However, most WBCs are blind to scene geometry, which can lead to collisions from imperfect target
    motions that are geometrically unsafe due to perception, planning, or teleoperation errors. We propose RECAL, a Robot--Environment
    Cross-Attention Layer ...
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
- humanoid_whole_body_control
- collision_avoidance
- cross_attention
- point_cloud
- floating_base_control
- sim_to_real
- end
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-09-21'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-09-21). Bibliographic metadata from arXiv API (2609.16405);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: arXiv:2609.16405 Collision-Aware Humanoid Whole-Body Control under Imperfect Tracking Targets
  url: https://arxiv.org/abs/2609.16405
  date: '2026-09-14'
  accessed_at: '2026-09-21'
---

## 概述

人形机器人通常通过全身控制器（WBC）跟踪运动指令并维持平衡，但多数 WBC 对场景几何不敏感，当目标运动因感知、规划或遥操作误差而几何不安全时容易发生碰撞。为此作者提出 RECAL，一个机器人—环境交叉注意力层，可包裹在无几何感知能力的 WBC 外层，借助外部场景几何在跟踪目标与避免碰撞之间做权衡。RECAL 将机器人、所持物体与环境统一表示为点云，通过机器人/物体点与环境点之间的交叉注意力生成几何感知的控制特征，从而支持浮动基座与末端执行器指令的碰撞感知跟踪，并可为手持物体提供避障。在仿真中，相较于其他几何感知 WBC 架构，RECAL 在冻结手臂与自适应手臂行走、物体搬运以及站立操作等场景下提升了避障能力，同时保持目标跟踪性能；作者还在真实 Digit V3 人形机器人上演示了该控制器。

## 核心内容

### 问题背景
人形机器人一般依靠全身控制器（WBC）执行运动指令，在跟踪目标的同时保持平衡与稳定。然而大多数 WBC 对场景几何是"盲"的：当目标运动因感知、规划或遥操作误差而变得几何不安全时，就可能引发碰撞。

### 方法
作者提出 **RECAL**（Robot–Environment Cross-Attention Layer），一个机器人—环境交叉注意力层，用于包裹原本不感知几何的 WBC，借助外部场景几何在目标跟踪与碰撞避免之间进行权衡。其要点包括：
- 支持对浮动基座指令与末端执行器指令的碰撞感知跟踪；
- 可为机器人所持物体提供碰撞避免；
- 将机器人、所持物体与环境统一表示为点云；
- 通过机器人/物体点与环境点之间的交叉注意力，生成几何感知的控制特征。

### 实验设置与关键结果
- 在仿真中，与其它几何感知 WBC 架构相比，RECAL 在以下场景中提升了碰撞避免能力，同时保持目标跟踪性能：
  - 冻结手臂（frozen-arm）行走；
  - 自适应手臂（adaptive-arm）行走；
  - 物体搬运；
  - 站立操作（standing-manipulation）。
- 作者进一步在真实 **Digit V3** 人形机器人上演示了该控制器。

### 结论
RECAL 通过交叉注意力引入场景几何，使原本几何盲的 WBC 获得碰撞感知能力，在不牺牲目标跟踪性能的前提下改善避障，并具备从仿真迁移到真实人形机器人平台的可行性。

## Overview

Humanoid robots often execute motion commands through whole-body controllers (WBCs) that track targets while maintaining balance and stability. However, most WBCs are blind to scene geometry, which can lead to collisions from imperfect target motions that are geometrically unsafe due to perception, planning, or teleoperation errors. We propose RECAL, a Robot--Environment Cross-Attention Layer that wraps a blind WBC to trade off target tracking against collision avoidance using external scene geometry. RECAL supports collision-aware tracking of floating-base and end-effector commands, including collision avoidance for held objects. It represents the robot, held objects, and environment as point clouds, using cross-attention between robot/object points and the environment to produce geometry-aware control features. In simulation, RECAL improves collision avoidance while preserving target-tracking performance across frozen-arm and adaptive-arm locomotion, object-carrying, and standing-manipulation scenarios relative to alternative geometry-aware WBC architectures. We further demonstrate the controller on a real Digit V3 humanoid robot.

## 参考
- https://arxiv.org/abs/2609.16405
