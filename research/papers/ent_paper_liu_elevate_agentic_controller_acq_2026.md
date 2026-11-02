---
$id: ent_paper_liu_elevate_agentic_controller_acq_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ELEVATE: Agentic Controller Acquisition from Task Failure for Quadrupedal Manipulation'
  zh: 'ELEVATE: Agentic Controller Acquisition from Task Failure for Quadrupedal Manipulation'
  ko: 'ELEVATE: Agentic Controller Acquisition from Task Failure for Quadrupedal Manipulation'
summary:
  en: Quadrupedal manipulators can extend their workspace through whole-body interaction, but task-planning agents' capabilities
    remain limited by their available controllers. We present ELEVATE, a framework that uses persistent failures during task-program
    refinement to identify and acquire missing whole-body control capabilities. When these failures suggest a missing physical
    capability, a coding ...
  zh: ELEVATE 是一个让任务规划智能体在任务程序精炼过程中，通过持续失败来识别并自主获取缺失全身控制能力的框架。当失败被判定为缺少某种物理能力时，编码智能体会构建并迭代精炼强化学习问题，指定行为专属的奖励、课程与终止条件，验证通过的控制器被加入能力库并与已有控制器组合以重试任务。从单个预训练的
    loco-manipulation 控制器出发，ELEVATE 在七个仿真任务序列中自主获得墙面支撑抬升、支撑操作与墙面下降控制器，并在初始控制器工作空间之外的五个任务上取得 98.4%–100% 的平均成功率。
  ko: Quadrupedal manipulators can extend their workspace through whole-body interaction, but task-planning agents' capabilities
    remain limited by their available controllers. We present ELEVATE, a framework that uses persistent failures during task-program
    refinement to identify and acquire missing whole-body control capabilities. When these failures suggest a missing physical
    capability, a coding ...
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
- quadrupedal_manipulation
- whole_body_control
- reinforcement_learning
- agentic_controller_acquisition
- sim_to_real_transfer
- task_and_motion_planning
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-11-02'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-11-02). Bibliographic metadata from arXiv API (2610.38388);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2610.38388 ELEVATE: Agentic Controller Acquisition from Task Failure for Quadrupedal Manipulation'
  url: https://arxiv.org/abs/2610.38388
  date: '2026-10-28'
  accessed_at: '2026-11-02'
- id: src_002
  type: website
  title: Project page
  url: https://agentic-quad-elevate.github.io/public/
  accessed_at: '2026-11-02'
---

## 概述

四足操作机器人可通过全身交互扩展工作空间，但任务规划智能体的能力受限于其可用的控制器集合。ELEVATE 把任务程序精炼中的持续失败当作能力缺口的信号，由编码智能体据此自动构建并迭代精炼强化学习问题，生成行为专属的奖励、课程与终止条件，再把验证通过的控制器纳入能力库并与现有控制器组合重试任务。系统从单个预训练的 loco-manipulation 控制器起步，在七个仿真任务序列中自主获得墙面支撑抬升、支撑操作与墙面下降三类控制器，并在后续的到达与物体操作任务中复用。在初始控制器工作空间之外的五个任务上，ELEVATE 五次独立运行的平均成功率为 98.4%–100%，而使用固定控制器库的编码智能体基线无法完成这些任务。所合成的任务程序与获取的控制器还能零真机训练、零微调地迁移到实体四足操作机器人上，在货架取物中达到 18/20 成功、在地面到货架放置中达到 16/20 成功。

## 核心内容

### 问题背景
四足操作机器人依靠全身交互可以突破原有工作空间限制，但任务规划智能体的能力上限取决于其可调用的控制器库。当任务需要某种尚未具备的全身控制能力时，现有智能体往往只能失败，而无法自行补齐能力缺口。

### 方法
ELEVATE 的核心思路是把任务程序精炼过程中的**持续性失败**作为能力缺失的判据，并据此触发控制器获取流程：

- 当失败模式表明缺少某种物理能力时，由一个编码智能体构建强化学习问题，并迭代精炼该问题。
- 精炼内容包括指定行为专属的奖励函数、课程安排与终止条件。
- 通过验证的控制器被加入能力库，并与已有控制器组合，用于重试原任务。
- 整个流程从单个预训练的 loco-manipulation 控制器出发，逐步扩展能力集合。

### 实验设置
- 平台：仿真环境中的四足操作机器人，任务序列共七个仿真任务。
- 自主获取的能力：墙面支撑抬升（wall-supported elevation）、支撑操作（supported manipulation）、墙面下降（wall descent）。
- 复用场景：后续的到达（reaching）与物体操作（object-manipulation）任务。
- 对比基线：使用固定控制器库的编码智能体。
- 评估方式：在初始控制器工作空间之外的五个任务上，进行五次独立运行。
- 真机迁移：将合成的任务程序与获取的控制器部署到实体四足操作机器人，不进行真机训练或微调。

### 关键结果
- 在初始控制器工作空间之外的五个任务上，ELEVATE 五次独立运行的平均成功率达到 **98.4%–100%**。
- 使用固定控制器库的编码智能体基线无法完成这些任务。
- 真机迁移中，货架取物（rack retrieval）成功 **18/20**，地面到货架放置（floor-to-rack placement）成功 **16/20**，且未使用真机训练或微调。

### 结论
ELEVATE 表明，任务执行中的持续失败可以作为自主获取新全身控制能力的有效信号；由编码智能体自动构建并精炼的强化学习问题能够产出可复用、可组合且可迁移到真机的控制器，从而突破初始控制器库的工作空间限制。

## Overview

Quadrupedal manipulators can extend their workspace through whole-body interaction, but task-planning agents' capabilities remain limited by their available controllers. We present ELEVATE, a framework that uses persistent failures during task-program refinement to identify and acquire missing whole-body control capabilities. When these failures suggest a missing physical capability, a coding agent formulates and iteratively refines a reinforcement-learning problem, specifying behavior-specific rewards, curricula, and termination conditions. Validated controllers are added to the capability library and composed with existing controllers to retry the task. Starting from a single pretrained loco-manipulation controller, ELEVATE autonomously acquires controllers for wall-supported elevation, supported manipulation, and wall descent across a sequence of seven simulation tasks. These controllers are reused in subsequent reaching and object-manipulation tasks. On the five tasks beyond the initial controller's workspace, ELEVATE achieves mean success rates of 98.4%-100% across five independent runs, while coding-agent baselines with a fixed controller library fail to complete these tasks. The synthesized task programs, together with the acquired controllers, also transfer to a physical quadrupedal manipulator without real-robot training or fine-tuning, achieving 18/20 successes in rack retrieval and 16/20 in floor-to-rack placement. Videos and demonstrations are available at https://agentic-quad-elevate.github.io/public/.

## 参考
- https://arxiv.org/abs/2610.38388
- https://agentic-quad-elevate.github.io/public/
