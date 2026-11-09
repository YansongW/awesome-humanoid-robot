---
$id: ent_paper_wu_sugarv2_learning_diverse_visua_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'SUGARv2: Learning Diverse Visual Humanoid Loco-Manipulation Skills from Synthesized Interaction References'
  zh: 'SUGARv2: Learning Diverse Visual Humanoid Loco-Manipulation Skills from Synthesized Interaction References'
  ko: 'SUGARv2: Learning Diverse Visual Humanoid Loco-Manipulation Skills from Synthesized Interaction References'
summary:
  en: Scaling up visual humanoid loco-manipulation skill acquisition requires reducing the human effort needed as tasks and
    spatial configurations expand, particularly in demonstration collection and task-specific training design. We present
    SUGARv2, a unified framework for learning diverse visual humanoid loco-manipulation skills through interaction reference
    synthesis and a shared training pipeline. ...
  zh: SUGARv2 是一个统一框架，用于学习多样化的视觉人形机器人移动操作技能，由 Tianshu Wu、Tianxiang Gui、Yue Chen、Tingxu Liu、Ziye Peng、Guangjie Yang、Xiangqi
    Kong、Ye Shi 等人提出。其核心思路是通过复用任务模板合成机器人与物体的协调运动参考，并以基于参考的模仿作为跨任务的统一学习目标，先训练特权教师策略，再经教师蒸馏与强化学习得到视觉策略。在五项人形机器人移动操作任务上，该框架在仿真中取得
    91.0% 的平均成功率，并在真实人形机器人上完成了全身操作的 sim-to-real 迁移。
  ko: Scaling up visual humanoid loco-manipulation skill acquisition requires reducing the human effort needed as tasks and
    spatial configurations expand, particularly in demonstration collection and task-specific training design. We present
    SUGARv2, a unified framework for learning diverse visual humanoid loco-manipulation skills through interaction reference
    synthesis and a shared training pipeline. ...
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
- visual_policy_learning
- sim_to_real_transfer
- teacher_student_distillation
- interaction_reference_synthesis
- imitation_learning
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-11-09'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-11-09). Bibliographic metadata from arXiv API (2611.09266);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2611.09266 SUGARv2: Learning Diverse Visual Humanoid Loco-Manipulation Skills from Synthesized Interaction
    References'
  url: https://arxiv.org/abs/2611.09266
  date: '2026-11-06'
  accessed_at: '2026-11-09'
- id: src_002
  type: website
  title: Project page
  url: https://tianshuwu.github.io/sugarv2-humanoid/
  accessed_at: '2026-11-09'
---

## 概述

SUGARv2 面向视觉人形机器人移动操作技能的规模化获取问题，旨在降低示范采集与任务专属训练设计所需的人力成本。为低成本获得多样化参考，该方法将可复用的任务模板适配到不同空间配置，从而合成协调的机器人运动与物体运动。学习目标上，它以基于参考的模仿作为各任务共用的目标，减少任务专属奖励设计。训练流程先获得执行这些参考的特权教师策略，再通过教师蒸馏与强化学习训练视觉策略，并借助多样物体实例与视觉域随机化提升视觉泛化与 sim-to-real 迁移能力。在五项任务上，仿真平均成功率为 91.0%，真实人形机器人部署进一步验证了全身操作的迁移效果。

## 核心内容

### 问题背景

扩展视觉人形机器人移动操作技能时，随着任务数量与空间配置的增加，人力投入会显著上升，尤其体现在示范采集和任务专属训练设计两个方面。SUGARv2 针对这两处瓶颈提出统一框架，目标是以较低成本获得多样化交互参考，并用共享训练流程覆盖多种任务。

### 方法

- **交互参考合成**：将可复用的任务模板适配到不同空间配置，合成协调的机器人运动与物体运动，从而以较低成本获得多样化参考。
- **统一学习目标**：以基于参考的模仿作为跨任务的共同学习目标，减少任务专属的奖励设计。
- **训练流程**：先训练特权教师策略来执行这些参考；再通过教师蒸馏与强化学习训练视觉策略，视觉策略沿用相同的基于参考的模仿奖励。
- **泛化与迁移支持**：训练中使用多样物体实例与视觉域随机化，以支持视觉泛化与 sim-to-real 迁移。

### 实验设置与关键结果

- 在五项人形机器人移动操作任务上进行评估。
- 仿真中平均成功率达到 91.0%。
- 在真实人形机器人上部署，进一步展示了全身操作的成功 sim-to-real 迁移。

### 结论

结果表明，该框架在学习多样化视觉人形机器人移动操作技能方面具有潜力，其参考合成与共享训练流程能够同时缓解示范采集与任务专属训练设计的人力负担。

## Overview

Scaling up visual humanoid loco-manipulation skill acquisition requires reducing the human effort needed as tasks and spatial configurations expand, particularly in demonstration collection and task-specific training design. We present SUGARv2, a unified framework for learning diverse visual humanoid loco-manipulation skills through interaction reference synthesis and a shared training pipeline. To obtain diverse references at low cost, we adapt reusable task templates to different spatial configurations, synthesizing coordinated robot and object motions. To reduce task-specific reward design and training effort, we use reference-based imitation as a common learning objective across tasks. We first train privileged teachers to execute these references, then train visual policies through teacher distillation and reinforcement learning with the same reference-based mimic rewards, using diverse object instances and visual domain randomization to support visual generalization and sim-to-real transfer. Across five humanoid loco-manipulation tasks, SUGARv2 achieves a mean success rate of 91.0% in simulation. Deployment on a real humanoid robot further demonstrates successful sim-to-real transfer for whole-body manipulation. These results demonstrate the framework's potential for learning diverse visual humanoid loco-manipulation skills.

## 参考
- https://arxiv.org/abs/2611.09266
- https://tianshuwu.github.io/sugarv2-humanoid/
