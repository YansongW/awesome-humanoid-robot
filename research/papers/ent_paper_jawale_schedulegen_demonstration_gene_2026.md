---
$id: ent_paper_jawale_schedulegen_demonstration_gene_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ScheduleGen: Demonstration Generation via Skill Scheduling for Multi-Arm Imitation Learning'
  zh: 'ScheduleGen: Demonstration Generation via Skill Scheduling for Multi-Arm Imitation Learning'
  ko: 'ScheduleGen: Demonstration Generation via Skill Scheduling for Multi-Arm Imitation Learning'
summary:
  en: Multi-arm robot platforms, including bimanual and humanoid robots, have the capability to complete tasks with lower
    cycle times than single-arm systems, but they are more difficult to safely control due to the presence of multi-arm constraints.
    The paradigm of training generalist robot policies from massive datasets is a promising approach to address general-purpose
    multi-arm manipulation, but ...
  zh: ScheduleGen 是一种面向多臂机器人（含双臂与人形平台）的演示生成规划与调度算法，由 Neel Jawale、Stephan Pleines、Soha Pouya、Yuke Zhu、Ajay Mandlekar、Caelan
    Garrett 提出。它针对现有演示生成方法忽视多臂约束、易产生不安全或失败行为的问题，将规划与调度结合以合成新演示。在 28 个仿真任务变体上平均数据生成成功率达 79.6%，所训练策略平均成功率为 65.5%。
  ko: Multi-arm robot platforms, including bimanual and humanoid robots, have the capability to complete tasks with lower
    cycle times than single-arm systems, but they are more difficult to safely control due to the presence of multi-arm constraints.
    The paradigm of training generalist robot policies from massive datasets is a promising approach to address general-purpose
    multi-arm manipulation, but ...
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
- multi_arm_manipulation
- demonstration_generation
- imitation_learning
- task_and_motion_planning
- sim_to_real_transfer
- humanoid_robotics
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-11-02'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-11-02). Bibliographic metadata from arXiv API (2610.39429);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2610.39429 ScheduleGen: Demonstration Generation via Skill Scheduling for Multi-Arm Imitation Learning'
  url: https://arxiv.org/abs/2610.39429
  date: '2026-10-29'
  accessed_at: '2026-11-02'
- id: src_002
  type: website
  title: Project page
  url: https://schedulegen.github.io/
  accessed_at: '2026-11-02'
---

## 概述

多臂机器人平台相比单臂系统能缩短任务周期，但因多臂约束的存在而更难安全控制；从大规模数据训练通用策略是有前景的路线，但多臂演示数据的获取仍是瓶颈。自动演示生成可从少量源演示合成新数据以缓解这一负担，然而现有算法忽略多臂约束，往往导致不安全与失败的行为。为此，作者提出 ScheduleGen，一个集规划与调度于一体的多臂演示生成算法。该方法在 28 个仿真任务变体上评估，其中包括七个由外部作者编写的 RoboDojo 任务以及此前系统无法进入的设置，取得 79.6% 的平均数据生成成功率，并训练出平均成功率 65.5% 的策略。其策略优于基于当前最优数据生成基线训练的策略，并通过零样本 sim-to-real 与 real-to-sim-to-real 迁移在八个真实世界变体上达到 50-80% 的成功率。

## 核心内容

### 问题背景

多臂机器人平台（包括双臂与人形机器人）具备比单臂系统更短任务周期的潜力，但由于多臂约束的存在，安全控制难度更高。以海量数据训练通用机器人策略是应对通用多臂操作的有前景范式，但大规模多臂操作数据集的获取仍是瓶颈。自动演示生成能够从少量源演示合成新演示，从而减轻数据采集负担；然而现有算法忽略多臂约束，常引发不安全且失败的行为。

### 方法

作者提出 ScheduleGen，一种用于多臂演示生成的集成式规划与调度算法，其核心是在演示生成过程中显式考虑多臂约束，以避免上述不安全与失败行为。

### 实验设置

- 评估覆盖 28 个仿真任务变体。
- 其中包含七个由外部作者编写的 RoboDojo 任务，以及此前系统无法进入的设置。
- 真实世界评估包含八个变体，通过零样本 sim-to-real 与 real-to-sim-to-real 迁移进行。

### 关键结果

- 平均数据生成成功率为 79.6%。
- 所训练策略的平均成功率为 65.5%。
- ScheduleGen 训练的策略优于基于当前最优数据生成基线所训练的策略。
- 在八个真实世界变体上取得 50-80% 的成功率。

### 结论

ScheduleGen 通过将规划与调度结合并纳入多臂约束，提升了多臂演示生成的可靠性与下游策略性能，并在仿真与真实世界迁移设置中验证了有效性。

## Overview

Multi-arm robot platforms, including bimanual and humanoid robots, have the capability to complete tasks with lower cycle times than single-arm systems, but they are more difficult to safely control due to the presence of multi-arm constraints. The paradigm of training generalist robot policies from massive datasets is a promising approach to address general-purpose multi-arm manipulation, but the acquisition of large multi-arm manipulation datasets remains a bottleneck. Automated demonstration generation can alleviate this burden by synthesizing new demonstrations from a handful of source demonstrations, but existing algorithms ignore multi-arm constraints and as a result often induce unsafe and unsuccessful behaviors. We address this limitation by introducing ScheduleGen, an integrated planning & scheduling algorithm for multi-arm demonstration generation. We evaluate ScheduleGen on 28 simulation task variants, including seven externally authored RoboDojo tasks and settings inaccessible to prior systems; it achieves 79.6% mean data-generation success and trains policies with 65.5% mean success. ScheduleGen policies outperform those trained on a state-of-the-art data generation baseline, and achieve 50-80% success across eight real-world variants through zero-shot sim-to-real and real-to-sim-to-real transfer. Videos and more at: https://schedulegen.github.io/

## 参考
- https://arxiv.org/abs/2610.39429
- https://schedulegen.github.io/
