---
$id: ent_paper_liu_coevolve_self_evolving_code_po_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'CoEvolve: Self-Evolving Code Policies from Skills to Strategies for Humanoid Robots'
  zh: 'CoEvolve: Self-Evolving Code Policies from Skills to Strategies for Humanoid Robots'
  ko: 'CoEvolve: Self-Evolving Code Policies from Skills to Strategies for Humanoid Robots'
summary:
  en: Recent advances in Vision-Language-Action (VLA) models and World Action Models (WAMs) have expanded the manipulation
    and whole body capabilities of individual robots. Yet a single robot remains limited by its embodiment, and many real
    world tasks require capabilities that can only emerge through cooperation. Existing multi robot frameworks largely emphasize
    task decomposition, allocation, and ...
  zh: CoEvolve 是一个将多机器人团队协作表示为固定机器人运动技能之上可执行代码的框架，由 Zicheng Liu、Haochen Wu、Jiawei He、Suyun Zhao、Huan Yang、Cheng Chi、Hao Tang
    提出。其核心是 Verifier Guided Coordination Evolution 机制：由多模态基础模型通过运动基元、语义目标、临时机器人角色与有界执行参数实例化协作策略，物理验证评估每次执行的状态转移，被拒绝的行为会从已接受的检查点触发结构化协作修订，验证过的经验则被保留以指导后续决策。在
    15 次基础任务运行、三种多模态骨干模型家族的设置下，CoEvolve 完成 8 项任务，且每种骨干均取得端到端成功。
  ko: Recent advances in Vision-Language-Action (VLA) models and World Action Models (WAMs) have expanded the manipulation
    and whole body capabilities of individual robots. Yet a single robot remains limited by its embodiment, and many real
    world tasks require capabilities that can only emerge through cooperation. Existing multi robot frameworks largely emphasize
    task decomposition, allocation, and ...
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
- multi_robot_coordination
- humanoid_robots
- code_policies
- verifier_guided_evolution
- vision_language_action
- unitree_g1
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-10-19'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-10-19). Bibliographic metadata from arXiv API (2610.23288);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2610.23288 CoEvolve: Self-Evolving Code Policies from Skills to Strategies for Humanoid Robots'
  url: https://arxiv.org/abs/2610.23288
  date: '2026-10-16'
  accessed_at: '2026-10-19'
---

## 概述

尽管 Vision-Language-Action（VLA）模型与世界动作模型（WAMs）提升了单台机器人的操作与全身能力，但单个机器人仍受自身形态限制，许多真实任务需要依靠协作才能涌现出所需能力。现有多机器人框架多侧重任务分解、分配与重规划，对物理执行偏离预期行为时如何调整可执行协作的支持有限。CoEvolve 将团队协作表达为固定机器人运动技能之上的可执行代码，并引入 Verifier Guided Coordination Evolution，由多模态基础模型借助运动基元、语义目标、临时机器人角色和有界执行参数来实例化协作策略。系统对每次执行的状态转移进行物理验证，被拒绝的行为会从已接受的检查点触发结构化协作修订，验证过的经验被保留用于指导后续决策。实验使用两台仿真 Unitree G1 人形机器人在受限走廊中搬运自由支撑的刚性负载，在 15 次基础任务运行、三种多模态骨干家族下完成 8 项任务，每种骨干均实现端到端成功，并在另外两种走廊布局以及同骨干与跨骨干经验初始化后取得验证通过的放置，同时暴露出运动精度与接触稳定性方面的持续局限。

## 核心内容

### 问题背景

Vision-Language-Action（VLA）模型与世界动作模型（WAMs）的进展扩展了单台机器人的操作与全身能力，但单台机器人仍受其形态（embodiment）限制，许多真实世界任务所需的能力只能通过协作产生。现有多机器人框架主要强调任务分解、分配与重规划，而在物理执行偏离预期行为时对可执行协作的适配支持有限。

### 方法

CoEvolve 将团队协作表示为固定机器人运动技能之上的可执行代码，并提出 Verifier Guided Coordination Evolution：

- 多模态基础模型通过运动基元、语义目标、临时机器人角色与有界执行参数来实例化协作策略。
- 物理验证对每次执行的状态转移进行评估。
- 被拒绝的行为会从已接受的检查点触发结构化的协作修订。
- 验证过的经验被保留下来，用于指导后续决策。

### 实验设置

评估使用两台仿真 Unitree G1 人形机器人，在受限走廊中搬运自由支撑的刚性负载。基础任务运行共 15 次，覆盖三种多模态骨干模型家族。

### 关键结果

- 在 15 次基础任务运行中，CoEvolve 完成 8 项任务，且每种骨干均取得端到端成功。
- 额外评估在另外两种走廊布局上取得验证通过的放置。
- 在同骨干与跨骨干经验初始化之后，同样取得验证通过的放置。
- 评估同时暴露出在运动精度与接触稳定性方面持续存在的局限。

### 结论

结果支持将可执行协作作为在共享物理约束下适配长时程多机器人协作的实用接口。

## Overview

Recent advances in Vision-Language-Action (VLA) models and World Action Models (WAMs) have expanded the manipulation and whole body capabilities of individual robots. Yet a single robot remains limited by its embodiment, and many real world tasks require capabilities that can only emerge through cooperation. Existing multi robot frameworks largely emphasize task decomposition, allocation, and replanning, while providing limited support for adapting executable coordination when physical execution deviates from the intended behavior. We present CoEvolve, a framework that represents team coordination as executable code over fixed robot motor skills. CoEvolve introduces Verifier Guided Coordination Evolution, where a multimodal foundation model instantiates coordination strategies through motion primitives, semantic objectives, temporary robot roles, and bounded execution parameters. Physical verification evaluates each executed transition, rejected behaviors trigger structured coordination revision from an accepted checkpoint, and verified experience is retained to guide subsequent decisions. We evaluate CoEvolve with two simulated Unitree G1 humanoids transporting a freely supported rigid payload through constrained corridors. Across 15 base task runs with three multimodal backbone families, CoEvolve completes 8 tasks, with every backbone achieving end to end success. Additional evaluations yield verified placement on two additional corridor layouts and after both same-backbone and cross-backbone experience initialization, while exposing persistent limitations in motion precision and contact stability. These results support executable coordination as a practical interface for adapting long horizon multi robot collaboration under shared physical constraints.

## 参考
- https://arxiv.org/abs/2610.23288
