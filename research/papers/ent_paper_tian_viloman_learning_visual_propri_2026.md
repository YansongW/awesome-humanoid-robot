---
$id: ent_paper_tian_viloman_learning_visual_propri_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ViLoMan: Learning Visual-Proprioceptive Whole-Body Loco-Manipulation Skills for Humanoid Robots'
  zh: 'ViLoMan: Learning Visual-Proprioceptive Whole-Body Loco-Manipulation Skills for Humanoid Robots'
  ko: 'ViLoMan: Learning Visual-Proprioceptive Whole-Body Loco-Manipulation Skills for Humanoid Robots'
summary:
  en: Humanoid loco-manipulation requires adaptive whole-body coordination to seamlessly integrate locomotion and physical
    interaction. Despite recent advances, learning autonomous loco-manipulation remains challenging due to the scarcity of
    diverse, physically executable robot-object interaction data and the difficulty of learning unified whole-body control
    directly from onboard observations. We ...
  zh: ViLoMan 是一个面向人形机器人自主 loco-manipulation 的可扩展框架，由 Zejie Tian、Ruibing Hou、Bingpeng Ma、Börje F. Karlsson、Shiguang Shan 提出。该方法先将人类-物体交互的部分运动学演示转化为完整且物理可执行的机器人轨迹，再通过
    teacher-student 蒸馏学习统一策略，把以自我为中心的深度观测与本体感知直接映射为关节级全身动作。部署时策略无需参考运动或中间指令，在仿真与真实世界的关门任务中，单一策略即可让 Unitree G1 仅凭机载深度感知与本体感知完成任务。
  ko: Humanoid loco-manipulation requires adaptive whole-body coordination to seamlessly integrate locomotion and physical
    interaction. Despite recent advances, learning autonomous loco-manipulation remains challenging due to the scarcity of
    diverse, physically executable robot-object interaction data and the difficulty of learning unified whole-body control
    directly from onboard observations. We ...
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
- whole_body_control
- teacher_student_distillation
- sim_to_real_transfer
- visual_proprioceptive_policy
- door_closing
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-09-21'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-09-21). Bibliographic metadata from arXiv API (2609.19340);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2609.19340 ViLoMan: Learning Visual-Proprioceptive Whole-Body Loco-Manipulation Skills for Humanoid Robots'
  url: https://arxiv.org/abs/2609.19340
  date: '2026-09-16'
  accessed_at: '2026-09-21'
- id: src_002
  type: website
  title: Project page
  url: https://viloman-anonymous.pages.dev/
  accessed_at: '2026-09-21'
---

## 概述

人形机器人的 loco-manipulation 需要全身协调，将移动与物理交互融为一体，但多样且物理可执行的机器人-物体交互数据稀缺，且难以直接从机载观测学习统一的全身控制。ViLoMan 针对这一难题提出可扩展框架：它先把人类-物体交互的部分运动学演示转换为完整、物理可执行的机器人轨迹，再借助 teacher-student 蒸馏框架，从这些轨迹中学习统一策略，将以自我为中心的深度观测与本体感知测量直接映射到关节级全身动作。部署阶段，该策略不需要参考运动，也不需要中间命令。作者在仿真与真实世界中，针对多种门配置与机器人初始条件评估了关门任务，结果显示单一策略即可让 Unitree G1 仅依靠机载深度感知与本体感知完成整个任务，并在任务变化下保持稳健泛化，同时有效实现从仿真到现实的迁移。

## 核心内容

### 问题背景
人形机器人的 loco-manipulation 要求全身自适应协调，把移动与物理交互无缝结合。尽管已有进展，自主 loco-manipulation 的学习仍面临两大障碍：一是缺乏多样且物理可执行的机器人-物体交互数据；二是难以直接从机载观测中学习统一的全身控制。

### 方法
ViLoMan 是一个可扩展的自主人形 loco-manipulation 框架，包含两个关键环节：
- 数据转化：将人类-物体交互的部分运动学演示，转化为完整、物理可执行的机器人轨迹。
- 策略学习：在这些轨迹之上采用 teacher-student 蒸馏框架，学习一个统一策略，将以自我为中心的深度观测与本体感知测量直接映射为关节级全身动作。
- 部署特性：策略在部署时既不需要参考运动，也不需要中间命令。

### 实验设置
作者在关门任务上评估 ViLoMan，覆盖仿真与真实世界中的多种门配置以及不同的机器人初始条件。

### 关键结果
- 单一策略即可让 Unitree G1 人形机器人仅使用机载深度感知与本体感知完成完整任务。
- 策略在任务变化下表现出稳健的泛化能力。
- 策略能够有效地从仿真迁移到现实。

### 结论
ViLoMan 通过将部分人类演示转化为物理可执行的机器人轨迹，并结合 teacher-student 蒸馏学习统一的视觉-本体感知全身策略，使人形机器人无需参考运动或中间命令即可自主完成 loco-manipulation 任务，并在仿真与真实环境中验证了泛化性与 sim-to-real 迁移效果。项目页面为 viloman-anonymous.pages.dev。

## Overview

Humanoid loco-manipulation requires adaptive whole-body coordination to seamlessly integrate locomotion and physical interaction. Despite recent advances, learning autonomous loco-manipulation remains challenging due to the scarcity of diverse, physically executable robot-object interaction data and the difficulty of learning unified whole-body control directly from onboard observations. We present ViLoMan, a scalable framework for autonomous humanoid loco-manipulation. ViLoMan first transforms partial kinematic demonstrations of human-object interactions into complete, physically executable robot trajectories. It then leverages these trajectories within a teacher-student distillation framework to learn a unified policy that maps egocentric depth observations and proprioceptive measurements directly to joint-level whole-body actions. During deployment, the policy requires neither reference motions nor intermediate commands. We evaluate ViLoMan on door-closing tasks across diverse door configurations and robot initial conditions in both simulation and the real world. Experimental results demonstrate that a single policy enables a Unitree G1 humanoid to complete the full task using only onboard depth sensing and proprioception, while generalizing robustly across task variations and transferring effectively from simulation to reality. Project page: viloman-anonymous.pages.dev.

## 参考
- https://arxiv.org/abs/2609.19340
- https://viloman-anonymous.pages.dev/
