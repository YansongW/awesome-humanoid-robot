---
$id: ent_paper_lu_pgx_physically_grounded_execut_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'PGX: Physically Grounded Execution for Long-Horizon Humanoid Loco-Manipulation'
  zh: 'PGX: Physically Grounded Execution for Long-Horizon Humanoid Loco-Manipulation'
  ko: 'PGX: Physically Grounded Execution for Long-Horizon Humanoid Loco-Manipulation'
summary:
  en: Robotic vision-language-action (VLA) models can execute diverse individual manipulation skills, yet they still struggle
    with long-horizon loco-manipulation tasks, where temporal structure, skills, and precision are tightly coupled within
    a monolithic model. We propose Physically Grounded Execution (PGX), a framework that offloads temporal and precision control
    to two classical training-free ...
  zh: PGX（Physically Grounded Execution）是一个面向长时程人形机器人移动操作（loco-manipulation）的框架，由 Kai Lu、Chenyang Ma、Ioannis Havoutis 提出。该框架将时间与精度控制卸载给两个无需训练的经典组件，使
    VLA 模型只需专注于各阶段的技能动态。在三个仿真任务与一个使用 Unitree G1 人形机器人的真实任务上，PGX 提升了阶段推进与任务成功率。
  ko: Robotic vision-language-action (VLA) models can execute diverse individual manipulation skills, yet they still struggle
    with long-horizon loco-manipulation tasks, where temporal structure, skills, and precision are tightly coupled within
    a monolithic model. We propose Physically Grounded Execution (PGX), a framework that offloads temporal and precision control
    to two classical training-free ...
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
- vision_language_action
- long_horizon_tasks
- state_machine
- world_coordinate_locking
- unitree_g1
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-11-23'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-11-23). Bibliographic metadata from arXiv API (2611.26596);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2611.26596 PGX: Physically Grounded Execution for Long-Horizon Humanoid Loco-Manipulation'
  url: https://arxiv.org/abs/2611.26596
  date: '2026-11-19'
  accessed_at: '2026-11-23'
---

## 概述

机器人视觉-语言-动作（VLA）模型虽能执行多种单项操作技能，但在长时程移动操作任务中仍显吃力，因为时间结构、技能与精度被紧耦合在单一模型内。PGX 将长时程移动操作分解为三层：基于谓词的状态机负责把控任务推进，用物理谓词门控阶段转换、触发恢复并协调导航与等待；VLA 技能仅在主动操作阶段内运行，专注于任务相关动作；世界坐标锁定（WCL）通过基站保持、物体相对定位与世界锚定接触目标维持空间一致性。作者在三个仿真任务和一个基于 Unitree G1 的真实任务上开展了实验，结果显示阶段推进与任务成功率均有改善。

## 核心内容

### 问题背景

机器人视觉-语言-动作（VLA）模型能够执行多样化的单项操作技能，但在长时程移动操作（loco-manipulation）任务中仍面临困难。这类任务中，时间结构、技能与精度被紧密耦合在一个单体模型内，难以兼顾。

### 方法

PGX（Physically Grounded Execution）将时间与精度控制卸载给两个经典的、无需训练的组件，使 VLA 得以专注于阶段特定的技能动态。框架分为三层：

- **基于谓词的状态机**：负责把控任务推进，利用物理谓词门控阶段转换、触发恢复，并协调导航与等待。共享的谓词语义将离线示教分割、在线执行与分阶段评估连接起来。
- **VLA 技能**：在主动操作阶段内运行，采用扁平或分阶段训练的模型，专注于与任务相关的动作。
- **世界坐标锁定（WCL）**：通过基站保持、物体相对定位与世界锚定接触目标，维持空间一致性。

### 实验设置

作者在三个仿真任务以及一个使用 Unitree G1 人形机器人的真实世界任务上开展了长时程移动操作实验。

### 关键结果

实验显示，PGX 在阶段推进与任务成功率方面均取得提升。

### 结论

通过将时间与精度控制从 VLA 中解耦，PGX 为长时程人形机器人移动操作提供了一种有效的执行框架。项目页面：https://kl-research.github.io/pgx

## Overview

Robotic vision-language-action (VLA) models can execute diverse individual manipulation skills, yet they still struggle with long-horizon loco-manipulation tasks, where temporal structure, skills, and precision are tightly coupled within a monolithic model. We propose Physically Grounded Execution (PGX), a framework that offloads temporal and precision control to two classical training-free components, allowing the VLA to focus on stage-specific skill dynamics. PGX decomposes long-horizon loco-manipulation into three layers: (i) a predicate-based state machine governs task progression, using physical predicates to gate phase transitions, trigger recovery, and coordinate navigation and waiting. Shared predicate semantics connect offline demonstration segmentation, online execution, and stage-wise evaluation; (ii) VLA skills operate within active manipulation phases, with flat or stage-trained models concentrating on task-relevant actions; and (iii) world-coordinate locking (WCL) maintains spatial consistency through base station keeping, object-relative positioning, and world-anchored contact targets. We demonstrate the effectiveness of PGX with extensive experiments conducted on three simulated tasks and one real-world task using a Unitree G1 humanoid robot for long-horizon loco-manipulation, showing improvements in stage progression and task success rates. Project page is available at: https://kl-research.github.io/pgx

## 参考
- https://arxiv.org/abs/2611.26596
