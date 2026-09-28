---
$id: ent_paper_liu_opt2vla_force_aware_vision_lan_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Opt2VLA: Force-Aware Vision-Language-Action for Contact-Rich Humanoid Whole-Body Manipulation'
  zh: 'Opt2VLA: Force-Aware Vision-Language-Action for Contact-Rich Humanoid Whole-Body Manipulation'
  ko: 'Opt2VLA: Force-Aware Vision-Language-Action for Contact-Rich Humanoid Whole-Body Manipulation'
summary:
  en: Humanoid robots are expected to perform diverse human-level tasks in daily environments, many of which require precise
    regulation of interaction forces. While recent vision-language-action (VLA) models have shown promise for semantic planning
    and visuomotor control, existing humanoid systems primarily represent actions through geometric motion goals and rely
    on whole-body controllers focused on ...
  zh: Opt2VLA 是一个面向人形机器人全身操作、具备力感知能力的视觉-语言-动作（VLA）框架，由 Fukang Liu、Yipu Chen、Jaehwi Jang、Danfei Xu、Zsolt Kira、Ye Zhao 提出。其核心是在
    VLA 与控制器的接口处引入显式力指令，由单一多任务 VLA 策略同时预测几何运动目标与连续接触力参考值，并交由基于强化学习（RL）的任务专用全身控制器跟踪。训练数据通过带显式力参考的全身轨迹优化（TO）生成，以保证动力学可行且接触一致。
  ko: Humanoid robots are expected to perform diverse human-level tasks in daily environments, many of which require precise
    regulation of interaction forces. While recent vision-language-action (VLA) models have shown promise for semantic planning
    and visuomotor control, existing humanoid systems primarily represent actions through geometric motion goals and rely
    on whole-body controllers focused on ...
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
- vision_language_action
- humanoid_whole_body_manipulation
- contact_rich_tasks
- force_control
- trajectory_optimization
- reinforcement_learning
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-09-28'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-09-28). Bibliographic metadata from arXiv API (2609.23968);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2609.23968 Opt2VLA: Force-Aware Vision-Language-Action for Contact-Rich Humanoid Whole-Body Manipulation'
  url: https://arxiv.org/abs/2609.23968
  date: '2026-09-21'
  accessed_at: '2026-09-28'
---

## 概述

现有人形机器人 VLA 系统多以几何运动目标表示动作，依赖侧重运动跟踪的全身控制器，对交互力的显式推理与控制有限，这在接触丰富任务中尤为突出：几何上相似的动作可能因任务情境不同而需要不同的力区间，且接触发生后视觉观测可能变得不可靠。为此，作者提出 Opt2VLA，在 VLA 到控制器的接口上引入显式力指令，用单一多任务 VLA 策略联合预测几何运动目标与连续接触力参考，再由任务专用的 RL 全身控制器进行跟踪。为获得可扩展且具物理依据的监督信号，作者通过带显式力参考的全身轨迹优化生成动力学可行、接触一致的训练数据。在三个接触丰富的人形任务上，显式力条件化相比仅运动控制实现了更准确、更一致的力调节，而来自 TO 的物理接地力矩监督进一步提升了力跟踪精度与稳定性；闭环评估还在仿真与人形硬件上展示了语言条件化的力调制能力。

## 核心内容

### 问题背景
人形机器人被期望在日常环境中完成多样化的人类级别任务，其中许多任务需要精确调节交互力。近期 VLA 模型在语义规划与视觉运动控制上展现出潜力，但现有人形系统主要以几何运动目标表示动作，并依赖聚焦运动跟踪的全身控制器，对交互力的显式推理或控制较为有限。这一局限在接触丰富任务中尤为关键：几何上相似的运动可能因任务情境不同而需要不同的力区间，且接触之后视觉观测可能不再可靠。

### 方法
- 提出 Opt2VLA，一个力感知的 VLA 框架，在 VLA 与控制器的接口处引入显式力指令，用于人形机器人全身操作。
- 采用单一多任务 VLA 策略，联合预测几何运动目标与连续接触力参考值。
- 预测出的目标与力参考由任务专用的、基于强化学习（RL）的全身控制器进行跟踪。
- 为提供可扩展且具物理依据的监督，使用带显式力参考的全身轨迹优化（TO）生成动力学可行且接触一致的训练数据。

### 实验与结果
- 在三个接触丰富的人形机器人任务上进行评估。
- 显式力条件化相比仅运动控制，实现了更准确、更一致的力调节。
- 来自 TO 的物理接地力矩监督进一步提升了力跟踪精度与稳定性。
- 闭环评估在仿真与人形硬件上展示了 Opt2VLA 的语言条件化力调制能力。

### 结论
Opt2VLA 通过在 VLA 到控制器的接口引入显式力指令，并结合轨迹优化提供的物理接地监督，弥补了现有人形 VLA 系统在接触丰富任务中力推理与控制不足的问题，在仿真与硬件上验证了语言条件化力调制的可行性。

## Overview

Humanoid robots are expected to perform diverse human-level tasks in daily environments, many of which require precise regulation of interaction forces. While recent vision-language-action (VLA) models have shown promise for semantic planning and visuomotor control, existing humanoid systems primarily represent actions through geometric motion goals and rely on whole-body controllers focused on motion tracking, with limited explicit reasoning or control of interaction forces. This limitation is particularly relevant in contact-rich tasks, where geometrically similar motions may require different force regimes depending on the task context and where visual observations may become unreliable after contact. In this work, we present Opt2VLA, a force-aware VLA framework that introduces explicit force commands at the VLA-to-control interface for humanoid whole-body manipulation. A single multi-task VLA policy jointly predicts both geometric motion goals and continuous contact-force references, which are tracked by task-specific reinforcement learning (RL)-based whole-body controllers. To provide scalable and physically grounded supervision, we generate dynamically feasible and contact-consistent training data via whole-body trajectory optimization (TO) with explicit force references. We evaluate Opt2VLA on three contact-rich humanoid tasks and show that explicit force conditioning enables more accurate and consistent force regulation than motion-only control, while physically grounded torque supervision from TO further improves force tracking accuracy and stability. Closed-loop evaluations further demonstrate language-conditioned force modulation with Opt2VLA in simulation and on humanoid hardware.

## 参考
- https://arxiv.org/abs/2609.23968
