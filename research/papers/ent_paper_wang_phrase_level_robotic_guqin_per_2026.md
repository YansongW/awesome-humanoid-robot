---
$id: ent_paper_wang_phrase_level_robotic_guqin_per_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Phrase-Level Robotic Guqin Performance: Bimanual Motion Planning and Audio-Tactile Interaction Monitoring'
  zh: 'Phrase-Level Robotic Guqin Performance: Bimanual Motion Planning and Audio-Tactile Interaction Monitoring'
  ko: 'Phrase-Level Robotic Guqin Performance: Bimanual Motion Planning and Audio-Tactile Interaction Monitoring'
summary:
  en: Recent advances in humanoid robotics and embodied intelligence have enabled robots to perform increasingly complex manipulation
    tasks. However, musical instrument performance remains a formidable benchmark, demanding not only collision-free trajectory
    execution but also precise contact timing, asymmetric bimanual coordination, and target acoustic outcomes on physical
    instruments. The guqin, a ...
  zh: 本文提出一套面向古琴乐句级自主演奏的异构双臂机器人系统，作者为 Zhen Wang、Zhiheng Chen、Tianyuan Bao、Tianwei Zhang。研究将古琴演奏建模为离散—连续混合执行问题，并构建分层规划框架以协调指法分配、构型连续性、避障与双手接触时序。在包含
    25 个演奏事件的乐句上，系统在实体古琴上完成散音与七徽泛音序列，重复试验中事件正确率分别达到 93.6% 与 96.8%。
  ko: Recent advances in humanoid robotics and embodied intelligence have enabled robots to perform increasingly complex manipulation
    tasks. However, musical instrument performance remains a formidable benchmark, demanding not only collision-free trajectory
    execution but also precise contact timing, asymmetric bimanual coordination, and target acoustic outcomes on physical
    instruments. The guqin, a ...
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
- bimanual_manipulation
- motion_planning
- musical_instrument_performance
- tactile_sensing
- auditory_feedback
- humanoid_robotics
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-09-28'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-09-28). Bibliographic metadata from arXiv API (2609.24133);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2609.24133 Phrase-Level Robotic Guqin Performance: Bimanual Motion Planning and Audio-Tactile Interaction
    Monitoring'
  url: https://arxiv.org/abs/2609.24133
  date: '2026-09-21'
  accessed_at: '2026-09-28'
---

## 概述

乐器演奏被视为机器人操作领域的高难度基准，古琴作为七弦无品弹拨乐器，其毫米级弦距、右手瞬时拨弦与左手持续泛音按触对操作精度与双手协调提出了特殊要求。本文搭建了一套物理异构双臂机器人系统，用于乐句级别的古琴自主演奏，并将演奏任务形式化为离散—连续混合执行问题。所提出的分层规划框架统一处理工作手指分配、构型连续性、避障以及连续音乐事件之间紧凑的双手接触时序安排。系统还融合了视觉引导的乐器定位、基于触觉的泛音接触监测，以及由听觉反馈驱动的拨弦参数标定。在实体古琴上针对一个含 25 个事件的乐句开展实验，系统能够稳定执行散音与七徽泛音的协调序列，重复试验中两类事件正确率分别为 93.6% 和 96.8%。

## 核心内容

### 问题背景
人形机器人与具身智能的进展使机器人能够完成日益复杂的操作任务，但乐器演奏仍是极具挑战性的基准：它不仅要求无碰撞的轨迹执行，还要求精确的接触时刻、非对称的双手协调，以及在真实乐器上达成目标声学效果。古琴是七弦无品弹拨乐器，其毫米级弦距、右手瞬时拨弦动作与左手持续泛音按触，构成了独特的操作难题。

### 方法
- 将古琴演奏形式化为离散—连续混合执行问题。
- 提出分层规划框架，在连续音乐事件之间统一协调：工作手指分配、构型连续性、避障，以及紧凑的双手接触时序安排。
- 系统集成三项感知与标定能力：视觉引导的乐器定位、基于触觉的泛音接触监测、由听觉反馈驱动的拨弦参数标定。
- 硬件平台为物理异构双臂机器人系统。

### 实验设置
在实体古琴上对一个包含 25 个事件的乐句进行真实世界实验，演奏内容涉及散音与七徽泛音序列的协调执行，并通过重复试验评估事件正确率。

### 关键结果
- 散音事件正确率：93.6%。
- 七徽泛音事件正确率：96.8%。
- 系统能够可靠执行协调的散音与七徽泛音序列。

### 结论
该工作表明，通过分层规划与视觉、触觉、听觉多模态反馈的结合，异构双臂机器人系统可在物理古琴上实现乐句级别的自主演奏，为乐器演奏这一高难度操作基准提供了可行路径。

## Overview

Recent advances in humanoid robotics and embodied intelligence have enabled robots to perform increasingly complex manipulation tasks. However, musical instrument performance remains a formidable benchmark, demanding not only collision-free trajectory execution but also precise contact timing, asymmetric bimanual coordination, and target acoustic outcomes on physical instruments. The guqin, a seven-string fretless zither, presents unique manipulation challenges due to its millimetric string spacing, transient right-hand plucking, and sustained left-hand harmonic contacts. In this work, we present a physical heterogeneous dual-arm robotic system for phrase-level autonomous guqin performance. We formulate guqin playing as a hybrid discrete--continuous execution problem and develop a hierarchical planning framework that coordinates working finger assignment, configuration continuity, obstacle avoidance, and tight bimanual contact schedules across consecutive musical events. The system integrates vision-guided instrument localization, tactile-based harmonic contact monitoring, and auditory feedback-informed plucking parameter calibration. Real-world experiments on a 25-event phrase demonstrate that the system reliably executes coordinated open-string and seventh-hui harmonic sequences on a physical guqin, achieving 93.6% and 96.8% event correctness across repeated trials.

## 参考
- https://arxiv.org/abs/2609.24133
