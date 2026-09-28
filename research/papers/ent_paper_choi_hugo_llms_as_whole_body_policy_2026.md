---
$id: ent_paper_choi_hugo_llms_as_whole_body_policy_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'HuGo: LLMs as Whole-Body Policy Code Designers for Humanoid Loco-Manipulation'
  zh: 'HuGo: LLMs as Whole-Body Policy Code Designers for Humanoid Loco-Manipulation'
  ko: 'HuGo: LLMs as Whole-Body Policy Code Designers for Humanoid Loco-Manipulation'
summary:
  en: For humanoids to be useful in everyday environments, they must perform a wide range of tasks that couple locomotion
    and manipulation. Existing approaches commonly acquire a loco-manipulation policy through reward engineering or demonstrations
    followed by task-specific training, making it costly to scale to new tasks. In this work, we propose a hierarchical approach
    to humanoid loco-manipulation ...
  zh: HuGo（Humanoid policy code Generation）是一种面向人形机器人全身 loco-manipulation 的分层方法，由 Seoyeon Choi、Shizhao Ye、Nicholas Bui、Aayushi
    Shrivastava、Kanghyun Ryu、Dhruva Tirumala、Markus Wulfmeier、Negar Mehr 提出。它利用 LLM 根据任务描述在冻结的低层全身策略之上生成可执行的闭环高层策略代码，并通过 rollout
    中的数值轨迹与选定视频帧进行迭代精化，从而免去逐任务的奖励设计与示教采集。在五个仿真任务、两种低层策略下，HuGo 显著优于高层强化学习基线，并接近基于示教基线的表现，还实现了仿真策略到硬件的零样本迁移。
  ko: For humanoids to be useful in everyday environments, they must perform a wide range of tasks that couple locomotion
    and manipulation. Existing approaches commonly acquire a loco-manipulation policy through reward engineering or demonstrations
    followed by task-specific training, making it costly to scale to new tasks. In this work, we propose a hierarchical approach
    to humanoid loco-manipulation ...
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
- llm_policy_generation
- hierarchical_control
- whole_body_policy
- sim_to_real_transfer
- code_refinement
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-09-28'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-09-28). Bibliographic metadata from arXiv API (2609.30594);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2609.30594 HuGo: LLMs as Whole-Body Policy Code Designers for Humanoid Loco-Manipulation'
  url: https://arxiv.org/abs/2609.30594
  date: '2026-09-24'
  accessed_at: '2026-09-28'
---

## 概述

人形机器人要在日常环境中发挥作用，就必须完成大量将移动与操作耦合在一起的任务，而现有方法通常依赖奖励工程或示教数据，再针对每个任务单独训练策略，扩展到新任务的代价很高。为此，作者提出分层式的 HuGo 方法：在冻结的低层全身策略之上，由 LLM 依据任务描述生成可执行的闭环高层策略代码，把任务逻辑写成程序。给定任务、观测与指令规范后，HuGo 利用 rollout 产生的数值轨迹和挑选的视频帧构造反馈，对代码进行有针对性的更新与精化。在五个仿真任务和两种低层策略上，该方法大幅超过高层强化学习基线，并接近基于示教的基线，且无需任务专属奖励设计或示教采集。作者还展示了仿真生成策略到硬件的零样本迁移，并表明将同一精化回路用于真实世界 rollout 可进一步提升迁移表现，而无需专家示教或策略重训练。

## 核心内容

### 问题背景
人形机器人要在日常环境中真正有用，需要执行大量同时耦合移动（locomotion）与操作（manipulation）的任务。现有做法通常通过奖励工程或示教来获得 loco-manipulation 策略，并随后进行任务专属训练，这使得向新任务扩展的成本很高。本文的目标是消除这种逐任务的需求。

### 方法
- 提出分层式人形 loco-manipulation 方法 **HuGo**（Humanoid policy code Generation）。
- 底层是一个**冻结的低层全身策略**，不参与训练更新。
- 高层由 **LLM** 负责：根据任务描述生成可执行、闭环的高层策略代码。
- 输入规范包括任务、观测与指令（command）规格，LLM 据此在代码中构建任务逻辑。
- 精化环节：HuGo 利用 rollout 得到的数值轨迹以及选定的视频帧生成反馈，并据此对代码做有针对性的更新。

### 实验设置
- 在**五个仿真任务**上进行评估。
- 使用**两种不同的低层策略**。
- 对比对象包括：高层强化学习基线、基于示教的基线。
- 全程不使用任务专属的奖励设计，也不进行示教采集。

### 关键结果
- 在五个仿真任务、两种低层策略下，HuGo **显著优于高层强化学习基线**。
- HuGo 的性能**接近基于示教的基线**。
- 上述表现是在没有任务专属奖励设计与示教采集的前提下取得的。
- 进一步展示了仿真生成策略到硬件的**零样本迁移**。
- 将同一精化回路应用于真实世界 rollout，可进一步提升迁移表现，且**无需专家示教，也无需策略重训练**。

### 结论
HuGo 表明，借助 LLM 生成并精化高层策略代码，可以在冻结低层全身策略的基础上完成人形 loco-manipulation，避免逐任务的奖励工程与示教采集，并具备向真实硬件迁移的潜力。项目网站为 https://iconlab.negarmehr.com/HuGo/。

## Overview

For humanoids to be useful in everyday environments, they must perform a wide range of tasks that couple locomotion and manipulation. Existing approaches commonly acquire a loco-manipulation policy through reward engineering or demonstrations followed by task-specific training, making it costly to scale to new tasks. In this work, we propose a hierarchical approach to humanoid loco-manipulation that eliminates these per-task requirements. HuGo, Humanoid policy code Generation, uses a Large Language Model (LLM) to generate executable, closed-loop high-level policy code from a task description on top of a frozen low-level whole-body policy. Given the task, observation, and command specifications, the LLM constructs the task logic in code. HuGo then refines the policy from its rollouts using numerical trajectories and selected video frames to produce feedback and targeted code updates. Across five simulation tasks, using two different low-level policies, HuGo substantially outperforms a high-level reinforcement learning baseline and approaches the performance of a demonstration-based baseline. We achieve this level of performance without task-specific reward design or demonstration collection. We further demonstrate zero-shot transfer of simulation-generated policies to hardware and show that applying the same refinement loop to real-world rollouts can further improve transfer performance without expert demonstrations or policy retraining. Project website is https://iconlab.negarmehr.com/HuGo/

## 参考
- https://arxiv.org/abs/2609.30594
