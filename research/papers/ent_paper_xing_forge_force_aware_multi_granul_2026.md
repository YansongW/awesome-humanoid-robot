---
$id: ent_paper_xing_forge_force_aware_multi_granul_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'FORGE: Force-Aware Multi-Granularity Control for Efficient Humanoid Loco-Manipulation'
  zh: 'FORGE: Force-Aware Multi-Granularity Control for Efficient Humanoid Loco-Manipulation'
  ko: 'FORGE: Force-Aware Multi-Granularity Control for Efficient Humanoid Loco-Manipulation'
summary:
  en: 'Humanoid loco-manipulation requires coordinated locomotion, balance regulation, and manipulation under frequent contacts,
    making teleoperated demonstration collection difficult: a practical controller must simultaneously provide precision,
    stability, and contact awareness. We propose FORGE, a force-aware multi-granularity control system with a coarse-to-fine
    command space spanning velocity ...'
  zh: FORGE 是一种面向人形机器人移动操作（loco-manipulation）的力感知多粒度控制系统，由 Liangjun Xing、Ke Fan、Kailin Li 等研究者提出。该系统采用从粗到细的命令空间，涵盖速度导航、平面足部落点、腕部位姿跟踪与可选的力条件输入，训练时无需全身人体运动轨迹或关节角参考。其核心贡献在于结合动量观测器与学习式修正实现持续接触下的力感知，并在部署阶段仅凭本体感知与重建的低层手臂
    PD 力矩估计腕部等效交互力，无需腕部力/力矩传感器。
  ko: 'Humanoid loco-manipulation requires coordinated locomotion, balance regulation, and manipulation under frequent contacts,
    making teleoperated demonstration collection difficult: a practical controller must simultaneously provide precision,
    stability, and contact awareness. We propose FORGE, a force-aware multi-granularity control system with a coarse-to-fine
    command space spanning velocity ...'
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
- humanoid_loco_manipulation
- force_aware_control
- multi_granularity_control
- momentum_observer
- teleoperation
- whole_body_control
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-11-16'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-11-16). Bibliographic metadata from arXiv API (2611.17142);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2611.17142 FORGE: Force-Aware Multi-Granularity Control for Efficient Humanoid Loco-Manipulation'
  url: https://arxiv.org/abs/2611.17142
  date: '2026-11-12'
  accessed_at: '2026-11-16'
---

## 概述

人形机器人移动操作需要在频繁接触条件下协调行走、平衡调节与操作，遥操作示教采集因此十分困难，控制器必须同时兼顾精度、稳定性与接触感知。FORGE 通过构建从速度导航、平面足部落点到腕部位姿跟踪、再到可选力条件输入的多粒度命令空间，实现了粗到细的统一控制。策略训练不依赖全身人体运动轨迹或关节角参考，部署时仅需相对骨盆的稀疏双侧腕部位姿、粗粒度运动命令以及可选的期望腕部负载输入。为应对持续接触，系统将动量观测器与经仿真器接触力监督训练的学习式修正相结合，并利用本体感知与重建的低层手臂 PD 力矩估计低频腕部等效交互力。此外，冻结的运动先验与非对称残差动作共同稳定了操作引发的全身修正。

## 核心内容

### 问题背景

人形机器人移动操作要求同时协调行走、平衡调节与操作，且过程中伴随频繁接触。这使得遥操作示教数据采集困难：实用控制器必须同时具备精度、稳定性与接触感知能力。现有方法往往依赖全身人体运动轨迹或关节角参考，部署时也常需腕部力/力矩传感器，限制了实用性。

### 方法

FORGE 提出力感知的多粒度控制框架，其命令空间由粗到细依次为：

- 速度导航命令
- 平面足部落点
- 腕部位姿跟踪
- 可选的力条件输入

策略训练阶段不需要全身人体运动轨迹，也不需要关节角参考。部署阶段仅消费三类输入：相对骨盆的稀疏双侧腕部位姿、粗粒度运动命令，以及可选的期望腕部负载。

针对持续接触场景，FORGE 将动量观测器与学习式修正相结合，后者在训练中接受仿真器接触力监督。部署时，系统从本体感知与重建的低层手臂 PD 力矩中估计低频的腕部等效交互力，无需腕部力/力矩传感器。一个准静态虚拟目标回路利用该估计值与可选的期望施加力输入来调整腕部目标。为稳定操作引发的全身修正，系统采用冻结的运动先验与非对称残差动作。

### 实验设置

实验评估涵盖以下方面：

- 统一控制的稳定性
- 任务空间跟踪
- 准静态腕部等效力估计
- 与刚性箱体持续接触时的挤压力
- 下游扩散策略在不同负载条件下执行蹲起搬运（squat-and-lift）任务

### 结论

FORGE 在不依赖全身运动轨迹、关节角参考与腕部力/力矩传感器的前提下，实现了力感知的多粒度人形移动操作控制，并通过上述多维度实验验证了统一控制稳定性、跟踪性能、力估计能力与下游任务执行效果。项目网站为 https://bb0928.github.io/forge/。

## Overview

Humanoid loco-manipulation requires coordinated locomotion, balance regulation, and manipulation under frequent contacts, making teleoperated demonstration collection difficult: a practical controller must simultaneously provide precision, stability, and contact awareness. We propose FORGE, a force-aware multi-granularity control system with a coarse-to-fine command space spanning velocity navigation, planar foot placement, wrist-pose tracking, and optional force-conditioning inputs. Policy training requires no full-body human motion trajectories or joint-angle references; deployment consumes only sparse bilateral wrist poses relative to the pelvis, coarse motion commands, and optional desired wrist-load inputs. For sustained contact, FORGE combines a momentum observer with a learned correction trained using simulator contact-force supervision. At deployment, it estimates low-frequency, wrist-equivalent interaction forces from proprioception and reconstructed low-level arm PD torques, without wrist force/torque sensors. A quasi-static virtual-target loop uses this estimate and an optional desired applied-force input to adapt the wrist target. A frozen locomotion prior and asymmetric residual actions stabilize manipulation-induced whole-body corrections. Experiments evaluate unified-control stability, task-space tracking, quasi-static wrist-equivalent force estimation, squeezing forces during sustained contact with a rigid box, and downstream diffusion-policy execution of a squat-and-lift task across payload conditions. Website: https://bb0928.github.io/forge/.

## 参考
- https://arxiv.org/abs/2611.17142
