---
$id: ent_paper_liu_learning_slope_adaptive_whole_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning Slope-Adaptive Whole-Body Locomotion for Humanoid Robots in Roofing Construction
  zh: Learning Slope-Adaptive Whole-Body Locomotion for Humanoid Robots in Roofing Construction
  ko: Learning Slope-Adaptive Whole-Body Locomotion for Humanoid Robots in Roofing Construction
summary:
  en: Roofing requires workers to coordinate locomotion, balance, and work-related body motions on pitched surfaces, creating
    a challenging application for humanoid robots. Directly retargeted human demonstrations, however, may preserve motion
    appearance while placing the robot's feet or hands incorrectly relative to the roof. This study presents a task-semantic
    scene-grounded framework for learning ...
  zh: 该研究提出了一种面向任务语义、以场景为基准的框架，用于让 Unitree G1 人形机器人在屋面施工中学习适应坡度的全身运动。作者为 Songyang Liu 与 Shuai Li。核心做法是将人体演示重定向到机器人，并用度量屋面模型提供空间参考，通过轨迹级优化与执行感知强化学习，使机器人在动态跟踪误差下仍满足支撑、作业间隙与不穿透等约束。
  ko: Roofing requires workers to coordinate locomotion, balance, and work-related body motions on pitched surfaces, creating
    a challenging application for humanoid robots. Directly retargeted human demonstrations, however, may preserve motion
    appearance while placing the robot's feet or hands incorrectly relative to the roof. This study presents a task-semantic
    scene-grounded framework for learning ...
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
- whole_body_control
- motion_retargeting
- reinforcement_learning
- construction_robotics
- slope_adaptation
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-09-21'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-09-21). Bibliographic metadata from arXiv API (2609.20558);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: arXiv:2609.20558 Learning Slope-Adaptive Whole-Body Locomotion for Humanoid Robots in Roofing Construction
  url: https://arxiv.org/abs/2609.20558
  date: '2026-09-17'
  accessed_at: '2026-09-21'
---

## 概述

屋面作业要求工人在倾斜表面上同时协调行走、平衡与作业动作，这对人形机器人构成挑战。直接重定向的人体演示往往只保留动作外观，却让机器人的脚或手相对屋面的位置出现偏差。该研究构建了一个以任务语义和场景为基准的学习框架，在 Unitree G1 上学习屋面工风格的全身运动。人体演示由跟踪系统采集并重定向到机器人，同时用度量屋面模型补充跟踪系统无法提供的空间参考。轨迹级优化将推断出的支撑接触点与标注的作业关系锚定到屋面，执行感知强化学习则促使策略在动态跟踪误差下保持这些关系。实验涵盖多动作跟踪、屋面坡度覆盖矩阵、五路 nailgun 消融、hammering 与 lateral pushing 的跨任务实验，以及与纯强化学习和零样本遥操作的对比。

## 核心内容

### 问题背景
屋面施工要求工人在倾斜屋面上协调行走、平衡与作业相关的身体动作，是人形机器人应用的难点场景。直接重定向人体演示虽然能保留动作外观，却可能使机器人脚部或手部相对屋面的位置不正确，从而破坏支撑与作业关系。

### 方法
- 在 Unitree G1 上构建任务语义、场景为基准的框架，用于学习屋面工风格的全身运动。
- 使用跟踪系统采集人体演示并重定向到机器人。
- 引入度量屋面模型，提供跟踪系统缺失的空间参考。
- 采用轨迹级优化，将推断出的支撑接触点与标注的作业关系锚定到屋面。
- 使用执行感知强化学习，使策略在动态跟踪误差下仍保持上述关系。

### 实验设置
- 多动作跟踪研究。
- 屋面坡度覆盖矩阵。
- 五路 nailgun 消融实验。
- hammering 与 lateral pushing 的跨任务实验。
- 与纯强化学习及零样本遥操作的对比。

### 关键结果
- 方法在所有评估种子下均满足支撑、作业间隙与不穿透准则。
- 在 nailgun、hammering 与 pushing 三类任务中，作业间隙误差介于 0.256 至 0.531 cm，每类任务均取得 3/3 的成功评估。
- 物理实验复现了上坡行走、nailgun、hammering 与弯腰动作，平均基座坐标系运动误差低于 80 mm。

### 结论
研究结果表明，以场景为基准的人体运动学习可作为面向建筑应用的人形机器人运动基元的有前景基础。

## Overview

Roofing requires workers to coordinate locomotion, balance, and work-related body motions on pitched surfaces, creating a challenging application for humanoid robots. Directly retargeted human demonstrations, however, may preserve motion appearance while placing the robot's feet or hands incorrectly relative to the roof. This study presents a task-semantic scene-grounded framework for learning roofer-style whole-body motions on a Unitree G1. Human demonstrations are captured using a tracking system and retargeted to the robot, while a metric roof model supplies the spatial reference unavailable from the tracking system. A trajectory-level optimization grounds inferred support contacts and annotated work relations to the roof, and execution-aware reinforcement learning encourages the resulting policy to preserve these relations under dynamic tracking errors. The framework is evaluated through a multi-motion tracking study, a roof-pitch coverage matrix, a five-way nailgun ablation, cross-task experiments on hammering and lateral pushing, and comparisons with pure reinforcement learning and zero-shot teleoperation. Our method enables the robot to satisfy support, work-clearance, and nonpenetration criteria across all evaluated seeds. Across nailgun, hammering, and pushing, it achieves work-clearance errors between 0.256 and 0.531 cm and 3/3 successful evaluations per task. Physical experiments reproduce uphill walking, nailgun, hammering, and bending motions with mean base-frame motion errors below 80 mm. These findings establish scene-grounded human motion learning as a promising basis for construction-oriented humanoid motion primitives.

## 参考
- https://arxiv.org/abs/2609.20558
