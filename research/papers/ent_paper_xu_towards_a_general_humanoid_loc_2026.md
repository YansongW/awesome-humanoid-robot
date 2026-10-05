---
$id: ent_paper_xu_towards_a_general_humanoid_loc_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Towards a General Humanoid Loco-Manipulation Model via Egocentric Whole-Body Human Data Pretraining
  zh: Towards a General Humanoid Loco-Manipulation Model via Egocentric Whole-Body Human Data Pretraining
  ko: Towards a General Humanoid Loco-Manipulation Model via Egocentric Whole-Body Human Data Pretraining
summary:
  en: Humanoid whole-body manipulation has advanced rapidly, enabling policies to coordinate locomotion, posture, bimanual
    interaction, and dexterous hand movements. Meanwhile, egocentric human videos provide diverse examples of everyday interactions
    across objects and scenes, offering scalable supervision without robot operation. However, existing supervision from these
    videos provides limited ...
  zh: 该工作探索如何利用人类自身经验数据来支撑人形机器人全身移动操作（loco-manipulation）的可扩展学习。作者构建了 HumanVerse-500，一个通过轻量可穿戴系统采集、同步第一视角视频与身体及手部运动的 500 小时开放世界人类行为数据集，并基于此提出全身人形视觉-语言-动作策略
    $λ_0$。$λ_0$ 采用三阶段训练，在 SIMPLE 与 4 项真实世界移动操作任务上取得当前最优性能。
  ko: Humanoid whole-body manipulation has advanced rapidly, enabling policies to coordinate locomotion, posture, bimanual
    interaction, and dexterous hand movements. Meanwhile, egocentric human videos provide diverse examples of everyday interactions
    across objects and scenes, offering scalable supervision without robot operation. However, existing supervision from these
    videos provides limited ...
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
- egocentric_video
- whole_body_control
- human_data_pretraining
- wearable_motion_capture
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-10-05'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-10-05). Bibliographic metadata from arXiv API (2610.00438);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: arXiv:2610.00438 Towards a General Humanoid Loco-Manipulation Model via Egocentric Whole-Body Human Data Pretraining
  url: https://arxiv.org/abs/2610.00438
  date: '2026-09-30'
  accessed_at: '2026-10-05'
---

## 概述

人形机器人的全身操作已能协调移动、姿态、双臂交互与灵巧手动作，而第一视角人类视频提供了无需机器人操作即可获得的可扩展监督信号，但既有视频监督对全身运动及手-物交互协调的覆盖有限，人形遥操作采集此类监督又成本高昂、难以规模化。为此，作者提出 HumanVerse-500，用轻量可穿戴系统同步采集第一视角视频与身体、手部运动，覆盖开放环境中的多样人类移动操作行为，总时长 500 小时。在此基础上，作者构建了全身人形视觉-语言-动作策略 $λ_0$，通过三阶段训练逐步学习交互、协调身体与手部运动，并适配到下游任务与机器人本体。该策略在训练中学习共享表征空间以迁移人类经验，同时用领域特定接口处理人与机器人在状态和动作上的差异。在 SIMPLE 与 4 项真实世界移动操作任务上的评测显示其达到当前最优性能，作者还分析了其扩展行为、泛化能力与各训练阶段的贡献。

## 核心内容

### 问题背景
人形全身操作近年来进展迅速，策略已能协调移动、姿态、双臂交互与灵巧手动作。第一视角人类视频蕴含跨物体、跨场景的日常交互样例，可在无需机器人实际操作的前提下提供可扩展的监督。然而，现有来自这类视频的监督对全身运动以及手-物交互协调的覆盖不足；而通过人形遥操作获取同类监督则成本高、难以规模化。因此，作者研究人类经验如何支持人形移动操作的可扩展学习。

### 数据集：HumanVerse-500
- 规模：500 小时。
- 内容：开放世界环境中多样的人类移动操作行为。
- 采集方式：轻量可穿戴系统，同步第一视角视频与身体、手部运动。

### 方法：$λ_0$
作者提出 $λ_0$，一个全身人形视觉-语言-动作策略，采用三阶段训练：
1. 从多样的第一视角数据集中学习交互；
2. 使用 HumanVerse-500 协调身体与手部运动；
3. 将策略适配到下游任务与机器人本体。

在三阶段中，$λ_0$ 学习一个共享表征空间以实现人类经验迁移，同时以领域特定接口处理人类与机器人之间在状态和动作上的差异。

### 实验与结果
- 评测基准与任务：SIMPLE 以及 4 项真实世界移动操作任务。
- 结果：取得当前最优（state-of-the-art）性能。
- 进一步分析：扩展行为（scaling behavior）、泛化能力，以及各训练阶段的贡献，用以理解人类数据如何支持下游全身人形控制。

### 结论与开源
作者将公开代码、模型与数据，以支持后续研究。

## Overview

Humanoid whole-body manipulation has advanced rapidly, enabling policies to coordinate locomotion, posture, bimanual interaction, and dexterous hand movements. Meanwhile, egocentric human videos provide diverse examples of everyday interactions across objects and scenes, offering scalable supervision without robot operation. However, existing supervision from these videos provides limited coverage of whole-body movement and coordination with hand-object interaction, while obtaining such supervision through humanoid teleoperation is also costly and difficult to scale. We therefore explore how human experience can support scalable learning of humanoid loco-manipulation. To support this study, we introduce HumanVerse-500, a 500-hour dataset of diverse human loco-manipulation behaviors in open-world environments, collected with a lightweight wearable system that synchronizes egocentric video with body and hand motion. Building on this dataset, we develop $λ_0$, a whole-body humanoid vision-language-action policy, through three-stage training that first learns interaction from diverse egocentric datasets, then coordinates body and hand motion using HumanVerse-500, and finally adapts the policy to downstream tasks and robot embodiments. Across these stages, $λ_0$ learns a shared representation space for human experience transfer, while domain-specific interfaces handle differences between human and robot states and actions. We evaluate $λ_0$ on SIMPLE and 4 real-world loco-manipulation tasks, achieving state-of-the-art performance, and further analyze its scaling behavior, generalization, and training-stage contributions to understand how human data support downstream whole-body humanoid control. We will release our code, models, and data to support further research.

## 参考
- https://arxiv.org/abs/2610.00438
