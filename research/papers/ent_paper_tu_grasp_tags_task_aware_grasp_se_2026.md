---
$id: ent_paper_tu_grasp_tags_task_aware_grasp_se_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Grasp-TAGS: Task-Aware Grasp Selection via Critic Distillation for Prehensile Loco-Manipulation'
  zh: 'Grasp-TAGS: Task-Aware Grasp Selection via Critic Distillation for Prehensile Loco-Manipulation'
  ko: 'Grasp-TAGS: Task-Aware Grasp Selection via Critic Distillation for Prehensile Loco-Manipulation'
summary:
  en: Loco-manipulation, which requires mobile manipulators to coordinate locomotion and manipulation over long horizons,
    is a key capability for large-object rearrangement in applications such as service robotics and warehouse automation.
    Despite recent progress, reliably executing these tasks remains challenging because performance depends on complex robot-object
    and object-environment interaction ...
  zh: Grasp-TAGS 是一个面向目标条件大物体重排的任务感知抓取选择框架，由 Xun Tu、Minghao Zou 与 Karthik Desingh 提出。该方法在多种初始抓取配置上训练统一的 PPO 强化学习策略，并将学习到的
    critic 蒸馏为轻量级抓取效用网络，仅凭候选抓取配置与目标信息即可对抓取排序。推理时在接触物体之前就选出预测下游效用最高的抓取，平均成功率达 89.84%，比最佳单抓取策略的 79.87% 提升 9.97 个百分点。
  ko: Loco-manipulation, which requires mobile manipulators to coordinate locomotion and manipulation over long horizons,
    is a key capability for large-object rearrangement in applications such as service robotics and warehouse automation.
    Despite recent progress, reliably executing these tasks remains challenging because performance depends on complex robot-object
    and object-environment interaction ...
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
- loco_manipulation
- grasp_selection
- critic_distillation
- reinforcement_learning
- object_rearrangement
- ppo
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-11-09'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-11-09). Bibliographic metadata from arXiv API (2611.09864);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2611.09864 Grasp-TAGS: Task-Aware Grasp Selection via Critic Distillation for Prehensile Loco-Manipulation'
  url: https://arxiv.org/abs/2611.09864
  date: '2026-11-06'
  accessed_at: '2026-11-09'
---

## 概述

该工作聚焦移动操作机器人在长时程内协调移动与操作以完成大物体重排的问题，指出性能受制于复杂的机器人—物体与物体—环境交互动力学。现有基于模型的方法依赖精确动力学模型，而基于学习的方法虽降低了这一要求，却通常假定固定或预定义的初始抓取；然而几何上同样稳定的不同抓取会带来显著不同的下游操作表现。为此作者提出 Grasp-TAGS：在多种初始抓取配置上训练统一的 PPO 策略，并把学到的 critic 蒸馏成轻量级抓取效用网络，使其仅利用候选抓取配置与目标信息对抓取排序。推理阶段在发生接触之前即选择预测下游效用最高的抓取，交由下游策略完成任务。实验显示其重排成功率优于固定单抓取策略与随机抓取选择，并在所有评估物体上降低了最终朝向误差。

## 核心内容

### 问题背景

移动操作（loco-manipulation）要求移动机械臂在长时程中协调移动与操作，是服务机器人与仓储自动化中大物体重排的关键能力。此类任务的可靠执行仍然困难，原因在于性能取决于复杂的机器人—物体以及物体—环境交互动力学。已有方法分为两类：基于模型的方法往往需要精确的动力学模型；基于学习的方法降低了对模型的要求，但通常假定固定或预定义的初始抓取。作者指出，几何上稳定的不同抓取可能导致下游操作性能出现显著差异，因此初始抓取的选择本身值得作为决策问题来处理。

### 方法

- **统一策略训练**：在多种初始抓取配置上训练一个统一的、基于 PPO 的强化学习策略，使策略具备在多样抓取条件下完成任务的能力。
- **critic 蒸馏**：将上述策略学习到的 critic 蒸馏为一个轻量级抓取效用网络（grasp utility network）。
- **抓取排序与选择**：该效用网络仅使用候选抓取配置与目标信息，即可对候选抓取进行排序；推理时在尚未接触物体之前，就选择预测下游效用最高的抓取，再交由下游策略完成任务。
- **框架定位**：Grasp-TAGS 是一个面向目标条件大物体重排的任务感知抓取选择框架。

### 实验设置

实验在目标条件的大物体重排任务上评估，对比对象包括固定单抓取策略与随机抓取选择；评估指标为任务成功率与最终朝向误差，覆盖多个评估物体。

### 关键结果

- Grasp-TAGS 的平均成功率达到 **89.84%**，而表现最好的单抓取策略为 **79.87%**，提升 **9.97 个百分点**。
- 相比固定单抓取策略与随机抓取选择，Grasp-TAGS 均提升了重排成功率。
- 在所有评估物体上，Grasp-TAGS 都降低了最终朝向误差。

### 结论

结果表明，在接触之前基于学习到的下游效用进行任务感知的抓取选择，能够有效改善长时程大物体重排的成功率与最终朝向精度，且无需依赖精确动力学模型或预定义初始抓取。更多定性结果见补充网页：https://rpm-lab-umn.github.io/Grasp-TAGS-web-page/

## Overview

Loco-manipulation, which requires mobile manipulators to coordinate locomotion and manipulation over long horizons, is a key capability for large-object rearrangement in applications such as service robotics and warehouse automation. Despite recent progress, reliably executing these tasks remains challenging because performance depends on complex robot-object and object-environment interaction dynamics. Existing approaches address this challenge either through model-based methods, which often require accurate dynamics models, or through learning-based methods, which reduce this requirement but typically assume a fixed or predefined initial grasp. However, different geometrically stable grasps can lead to substantially different downstream manipulation performance. Therefore, we propose Grasp-TAGS, a task-aware grasp selection framework for goal-conditioned large-object rearrangement. We train a unified PPO-based reinforcement learning policy across multiple initial grasp configurations and distill the learned critic into a lightweight grasp utility network that ranks candidate grasps using only the candidate grasp configuration and goal information. At inference time, we select the grasp with the highest predicted downstream utility for the downstream policy to complete the task, before even making a contact. Experiments demonstrate that Grasp-TAGS improves rearrangement success over both fixed single-grasp policies and random grasp selection, achieving an average success rate of 89.84% compared with 79.87% for the best-performing single-grasp policies, an improvement of 9.97 percentage points. Grasp-TAGS also reduces final orientation errors across all evaluated objects. For more qualitative results, refer to the supplementary webpage: https://rpm-lab-umn.github.io/Grasp-TAGS-web-page/

## 参考
- https://arxiv.org/abs/2611.09864
