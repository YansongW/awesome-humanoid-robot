---
$id: ent_paper_liu_perception_and_action_system_f_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Perception-and-action system for humanoid robot task execution in construction
  zh: Perception-and-action system for humanoid robot task execution in construction
  ko: Perception-and-action system for humanoid robot task execution in construction
summary:
  en: Humanoid robots, with their human-like shape and multi-tasking capabilities, are well-aligned with human-dominated workplaces,
    like those in civil and construction engineering, where they could collaborate with human workers or autonomously perform
    physically demanding and hazardous tasks. Despite this promise, limited research has explored how to endow these robots
    with the practical ...
  zh: 本研究提出了一种用于人形机器人在建筑环境中执行任务的感知-动作系统，由Yanxi Liu和Yizhi Liu开发。该系统包含两个深度网络：Humanoid-PoseNet将人体姿态转换为机器人可行姿态，Humanoid-ActionNet学习可执行动作，实验显示机器人可靠执行八种建筑相关动作，平均运动跟踪误差为82.45毫米MPJPE。
  ko: Humanoid robots, with their human-like shape and multi-tasking capabilities, are well-aligned with human-dominated workplaces,
    like those in civil and construction engineering, where they could collaborate with human workers or autonomously perform
    physically demanding and hazardous tasks. Despite this promise, limited research has explored how to endow these robots
    with the practical ...
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
- humanoid_robot
- construction_task
- perception_action_system
- pose_estimation
- imitation_learning
- motion_tracking
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-08-04'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-08-04). Bibliographic metadata from arXiv API (2608.01600);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: arXiv:2608.01600 Perception-and-action system for humanoid robot task execution in construction
  url: https://arxiv.org/abs/2608.01600
  date: '2026-08-03'
  accessed_at: '2026-08-04'
---

## 概述

该研究针对人形机器人在建筑领域应用不足的问题，设计了一个从工人演示中学习和执行建筑任务的感知-动作系统。系统通过Humanoid-PoseNet提取并转换人体姿态，再由Humanoid-ActionNet生成机器人动作，实验验证了其在八种建筑动作上的执行能力，平均误差为82.45毫米MPJPE，为建筑场景中的人形协作机器人部署提供了初步探索。

## 核心内容

### 问题背景
人形机器人因其类人形态和多任务能力，适合在建筑和土木工程等人类主导的工作场所中协作或执行危险任务。然而，现有研究较少关注赋予这些机器人实际执行建筑任务的能力，本研究旨在填补这一空白。

### 方法
提出的感知-动作系统包含两个深度网络：
- **Humanoid-PoseNet**：从工人演示中提取人体姿态，并将其转换为机械上可行的人形机器人姿态。
- **Humanoid-ActionNet**：基于转换后的姿态，学习机器人可执行的动作。

该系统通过端到端的学习流程，使机器人能够从演示中获取任务技能。

### 实验设置与结果
实验评估了人形机器人在建筑相关任务中的执行性能。结果显示，机器人可靠地执行了八种建筑相关动作，平均运动跟踪误差为82.45毫米MPJPE（平均每关节位置误差）。该误差指标衡量了机器人动作与演示动作之间的对齐精度。

### 结论
本研究为建筑环境中部署人形协作机器人迈出了早期一步，验证了基于演示学习的感知-动作系统的可行性，但未涉及实际施工现场的复杂环境或长期稳定性测试。

## Overview

Humanoid robots, with their human-like shape and multi-tasking capabilities, are well-aligned with human-dominated workplaces, like those in civil and construction engineering, where they could collaborate with human workers or autonomously perform physically demanding and hazardous tasks. Despite this promise, limited research has explored how to endow these robots with the practical capabilities needed to perform construction tasks. To this end, this study proposes a novel perception-and-action system that enables humanoid robots to learn and perform construction tasks from worker demonstrations. This system contains two deep networks: Humanoid-PoseNet, which extracts human postures and translates them into mechanically feasible poses for a humanoid robot; and Humanoid-ActionNet, which learns robot-executable actions based on these translated poses. Experimental results demonstrate that the humanoid robot reliably executed eight construction-related actions, achieving an average motion-tracking error of 82.45 mm MPJPE (Mean Per Joint Position Error). This work provides an early step toward deploying humanoid collaborators in construction.

## 参考
- https://arxiv.org/abs/2608.01600
