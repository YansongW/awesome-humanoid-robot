---
$id: ent_paper_zhang_humanoid_horizon_extending_tas_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Humanoid Horizon: Extending Task Horizon in Whole-Body Loco-Manipulation via Parallel Training, Dynamic Starting, and
    Reward Gating'
  zh: 'Humanoid Horizon: Extending Task Horizon in Whole-Body Loco-Manipulation via Parallel Training, Dynamic Starting, and
    Reward Gating'
  ko: 'Humanoid Horizon: Extending Task Horizon in Whole-Body Loco-Manipulation via Parallel Training, Dynamic Starting, and
    Reward Gating'
summary:
  en: Cluttered indoor environments, where large and heavy objects are scattered across diverse surfaces, require humanoid
    robots to sequentially navigate, grasp, transport, and accurately place each item at its target location within a single
    uninterrupted episode. This long-horizon, whole-body loco-manipulation task remains a significant challenge for current
    methods. Previous approaches often suffer ...
  zh: Humanoid Horizon 是一个面向人形机器人长时程全身移动操作（loco-manipulation）的统一策略框架，由 Haozhuo Zhang、Qiang Zhang、Jian Tang、Mingzhe Ni、Michele
    Caprio、Angelo Cangelosi、Wei Pan 提出。它通过并行训练策略、动态起始机制与奖励门控三项机制，缓解易得奖励偏置与灾难性遗忘问题。在 LHM-Humanoid 基准（350 个训练场景、66 个留出场景）的双物体任务上，各阶段成功率超过
    80%。
  ko: Cluttered indoor environments, where large and heavy objects are scattered across diverse surfaces, require humanoid
    robots to sequentially navigate, grasp, transport, and accurately place each item at its target location within a single
    uninterrupted episode. This long-horizon, whole-body loco-manipulation task remains a significant challenge for current
    methods. Previous approaches often suffer ...
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
- long_horizon_tasks
- whole_body_control
- parallel_training
- reward_shaping
- catastrophic_forgetting
- tags
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-10-12'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-10-12). Bibliographic metadata from arXiv API (2610.08320);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2610.08320 Humanoid Horizon: Extending Task Horizon in Whole-Body Loco-Manipulation via Parallel Training,
    Dynamic Starting, and Reward Gating'
  url: https://arxiv.org/abs/2610.08320
  date: '2026-10-06'
  accessed_at: '2026-10-12'
- id: src_002
  type: website
  title: Project page
  url: https://haozhuo-zhang.github.io/Humanoid-Horizon-project-page/
  accessed_at: '2026-10-12'
---

## 概述

该工作针对杂乱室内环境中人形机器人需在单个不间断回合内依次完成导航、抓取、搬运与精确放置的长时程全身移动操作任务。作者指出以往方法存在两大问题：一是易得奖励偏置，训练过度偏重早期搬运阶段而忽视后期阶段；二是灾难性遗忘，聚焦后期阶段会导致早期阶段性能下降。为此提出 Humanoid Horizon 统一策略框架，包含并行训练策略、动态起始机制与奖励门控三项相互关联的机制。并行训练策略将 N 个场景组织为 S 条由共享策略驱动的并发阶段流，使所有搬运阶段持续获得梯度更新；动态起始机制用上游 rollout 的终止状态更新各环境初始状态；奖励门控在前一物体位移超过阈值时将后续回合奖励置零。在 LHM-Humanoid 基准上，双物体任务各阶段成功率超过 80%，且随物体数量增加性能下降较为平缓。

## 核心内容

### 问题背景
在杂乱的室内环境中，大型且沉重的物体散布于不同表面，人形机器人需要在单个不间断回合内依次完成导航、抓取、搬运，并将每件物品准确放置到目标位置。这类长时程、全身性的移动操作任务对现有方法仍是重大挑战。已有方法主要面临两个问题：

- **易得奖励偏置**：训练过度强调早期搬运阶段，牺牲了后期阶段的表现。
- **灾难性遗忘**：当训练聚焦于后期阶段时，早期阶段的能力会出现退化。

### 方法
作者提出 **Humanoid Horizon**，一个统一的策略框架，通过三项相互关联的机制应对上述限制：

- **Parallel Training Strategy（并行训练策略）**：将 $N$ 个场景组织为 $S$ 条并发的阶段流，由共享策略统一驱动，确保所有搬运阶段都能获得持续的梯度更新，从而消除顺序优化的瓶颈。
- **Dynamic Starting Mechanism（动态起始机制）**：使用上游 rollout 的终止状态来更新每个环境的初始状态，逐步扩大状态转移的覆盖范围，并增强阶段边界处的鲁棒性。
- **Reward Gating（奖励门控）**：在后期阶段流中，当紧邻的前一个物体被移动超出设定阈值时，将本回合剩余部分的奖励置零，使共享策略学会不去扰动刚刚放置好的物体，从而在整个回合中保持此前的放置结果。

### 实验设置与关键结果
- 评测基准为 **LHM-Humanoid**，包含 350 个训练场景与 66 个留出场景。
- 在双物体任务上，上述策略组合使各阶段成功率超过 **80%**。
- 当依次搬运的物体数量超过两个时，成功率随任务时程增长而下降，但相比所有基线方法出现的急剧下降，本方法的性能退化更为平缓。

### 结论
Humanoid Horizon 通过并行训练、动态起始与奖励门控的协同设计，在长时程全身移动操作任务中同时缓解了易得奖励偏置与灾难性遗忘，在双物体设定下取得各阶段超过 80% 的成功率，并在更长时程下展现出相对基线更为平缓的性能退化。

## Overview

Cluttered indoor environments, where large and heavy objects are scattered across diverse surfaces, require humanoid robots to sequentially navigate, grasp, transport, and accurately place each item at its target location within a single uninterrupted episode. This long-horizon, whole-body loco-manipulation task remains a significant challenge for current methods. Previous approaches often suffer from two main issues: easy-reward bias, where training overemphasizes early transport stages at the expense of later ones, and catastrophic forgetting, where focusing on later stages leads to a decline in earlier-stage performance. In this work, we introduce Humanoid Horizon, a unified policy framework designed to overcome these limitations through three interrelated mechanisms. The Parallel Training Strategy organizes $N$ scenes into $S$ concurrent stage streams governed by a shared policy, ensuring all transport stages receive continuous gradient updates and removing the bottleneck of sequential optimization. The Dynamic Starting Mechanism updates each environment's initial state with terminal states from upstream rollouts, gradually broadening transition coverage and enhancing robustness at stage boundaries. Reward Gating sets the reward to zero for the rest of the episode in later-stage streams when the immediately preceding object is displaced beyond a set threshold, so the shared policy learns not to disturb a just-placed object and earlier placements are preserved throughout the episode. Collectively, these strategies achieve per-stage success rates exceeding 80\% on the two-object LHM-Humanoid benchmark (350 training scenes, 66 held-out scenes). As the number of sequentially transported objects grows beyond two, success declines with the horizon, but the degradation is graceful relative to the sharp drop seen in all baselines.

## 参考
- https://arxiv.org/abs/2610.08320
- https://haozhuo-zhang.github.io/Humanoid-Horizon-project-page/
