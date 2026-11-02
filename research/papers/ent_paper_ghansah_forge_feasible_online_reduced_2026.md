---
$id: ent_paper_ghansah_forge_feasible_online_reduced_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'FORGE: Feasible Online Reduced-Order Reference Generation and Whole-Body Execution for Agile Humanoid Locomotion'
  zh: 'FORGE: Feasible Online Reduced-Order Reference Generation and Whole-Body Execution for Agile Humanoid Locomotion'
  ko: 'FORGE: Feasible Online Reduced-Order Reference Generation and Whole-Body Execution for Agile Humanoid Locomotion'
summary:
  en: This paper presents a two-stage learning framework for versatile and agile humanoid locomotion that couples online reduced-order
    model (ROM) reference generation with whole-body tracking control. In the first stage, we train a command-conditioned
    whole-body reference generator using single rigid body dynamics combined with full humanoid kinematics. In the second
    stage, the frozen ROM policy is ...
  zh: 本文提出 FORGE，一个两阶段学习框架，将在线降阶模型（ROM）参考生成与全身跟踪控制相结合，用于实现多样且敏捷的人形机器人运动。第一阶段的参考生成器基于单刚体动力学与完整人形运动学训练，第二阶段冻结该 ROM 策略并在线生成参考，用于训练全身跟踪策略。作者在
    Unitree G1 人形机器人上验证了该方法，实现了 -2.0 m/s 至 2.8 m/s 的纵向速度、±1.0 m/s 的横向速度、±3.0 rad/s 的角速度、单腿跳跃以及指令间的连续切换。
  ko: This paper presents a two-stage learning framework for versatile and agile humanoid locomotion that couples online reduced-order
    model (ROM) reference generation with whole-body tracking control. In the first stage, we train a command-conditioned
    whole-body reference generator using single rigid body dynamics combined with full humanoid kinematics. In the second
    stage, the frozen ROM policy is ...
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
- reduced_order_model
- whole_body_control
- reference_generation
- reinforcement_learning
- unitree_g1
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-11-02'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-11-02). Bibliographic metadata from arXiv API (2610.37974);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2610.37974 FORGE: Feasible Online Reduced-Order Reference Generation and Whole-Body Execution for Agile Humanoid
    Locomotion'
  url: https://arxiv.org/abs/2610.37974
  date: '2026-10-27'
  accessed_at: '2026-11-02'
---

## 概述

FORGE 面向人形机器人敏捷运动的参考生成与执行问题，采用两阶段学习框架。第一阶段在降阶模型空间中训练一个以指令为条件的全身参考生成器，该生成器结合单刚体动力学与完整人形运动学，从而保证参考在运动学与动力学上的一致性。第二阶段冻结该 ROM 策略并在线展开，为全阶动力学模型上的全身跟踪策略生成训练参考。由于参考生成在简化的 ROM 空间中进行，单一统一框架即可覆盖较宽的指令空间与多种运动策略。作者在 Unitree G1 上展示了统一的参考策略与全身跟踪策略，覆盖大范围速度指令、单腿跳跃与连续指令切换。

## 核心内容

### 问题背景
人形机器人要在较宽指令范围内实现敏捷运动，需要同时解决参考轨迹的可行性与全身执行的跟踪精度问题。直接在完整动力学上学习策略难以覆盖大范围指令与多种运动模式，而简化模型虽易于生成参考，却需保证其与完整人形运动学、动力学一致。

### 方法
作者提出两阶段学习框架 FORGE：

- **第一阶段**：训练一个以指令为条件的全身参考生成器，使用单刚体动力学结合完整人形运动学，在降阶模型（ROM）空间中学习运动学-动力学一致的参考。
- **第二阶段**：冻结第一阶段得到的 ROM 策略，将其在线展开以生成参考，用于在全阶动力学模型上训练全身跟踪策略。

该设计使得在简化 ROM 空间中即可生成覆盖广泛指令空间与多种运动策略的参考，并由单一统一框架完成。

### 实验设置
方法在 Unitree G1 人形机器人上进行验证，使用一个统一的参考策略与一个全身跟踪策略。

### 关键结果
实验实现了：

- 纵向速度 -2.0 m/s 至 2.8 m/s；
- 横向速度最高 ±1.0 m/s；
- 角速度最高 ±3.0 rad/s；
- 单腿跳跃；
- 指令间的连续切换。

上述能力均由同一个参考策略与同一个全身跟踪策略完成。

### 结论
将在线降阶模型参考生成与全身跟踪控制耦合的两阶段框架，能够在统一策略下实现人形机器人较宽指令范围的敏捷运动与多策略切换。

## Overview

This paper presents a two-stage learning framework for versatile and agile humanoid locomotion that couples online reduced-order model (ROM) reference generation with whole-body tracking control. In the first stage, we train a command-conditioned whole-body reference generator using single rigid body dynamics combined with full humanoid kinematics. In the second stage, the frozen ROM policy is rolled out online to generate references for training a whole-body tracking policy on the full-order dynamics model. Learning a kino-dynamically consistent reference generator in the simplified ROM space enables us to generate references over a broad command space and over multiple locomotion strategies using a single unified framework. We demonstrate the approach on a Unitree G1 humanoid robot, achieving longitudinal velocities from -2.0 m/s to 2.8 m/s, lateral velocities up to +-1.0 m/s, angular velocities up to +-3.0 rad/s, one-legged hopping, and continuous transitions across the commands, all using one unified reference policy and one whole-body tracking policy.

## 参考
- https://arxiv.org/abs/2610.37974
