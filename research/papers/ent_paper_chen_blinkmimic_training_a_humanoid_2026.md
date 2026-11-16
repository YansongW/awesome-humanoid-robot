---
$id: ent_paper_chen_blinkmimic_training_a_humanoid_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'BlinkMimic: Training a Humanoid Motion Tracker in Minutes on a Single GPU'
  zh: 'BlinkMimic: Training a Humanoid Motion Tracker in Minutes on a Single GPU'
  ko: 'BlinkMimic: Training a Humanoid Motion Tracker in Minutes on a Single GPU'
summary:
  en: Whole-body motion tracking lets a humanoid robot follow reference motions, but training a tracking policy for a library
    of motions has usually taken hours of GPU time. SuperMimic showed that the policy can instead be trained by backpropagating
    through a world model learned from parallel simulation, and InstantTrack added Muon updates, a residual policy around
    the reference and an averaged ...
  zh: BlinkMimic 是一种用于人形机器人全身运动跟踪策略的训练方案，由 Fuyi Chen 提出，建立在 SuperMimic 与 InstantTrack 之上。在仿真 Unitree G1 上，它用单张 RTX 4090 在
    3.4 分钟内为全部 40 个 LAFAN1 动作片段训练出单一策略，判定标准为连续三个检查点的归一化回报不低于 0.82 且无失败片段（三个随机种子取平均）。其新增组件包括随训练进程下降的步长、由部署条件下策略失败触发的重置，以及整个迭代过程的
    GPU 图捕获。
  ko: Whole-body motion tracking lets a humanoid robot follow reference motions, but training a tracking policy for a library
    of motions has usually taken hours of GPU time. SuperMimic showed that the policy can instead be trained by backpropagating
    through a world model learned from parallel simulation, and InstantTrack added Muon updates, a residual policy around
    the reference and an averaged ...
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
- humanoid_motion_tracking
- whole_body_control
- world_model
- training_efficiency
- unitree_g1
- lafan1
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-11-16'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-11-16). Bibliographic metadata from arXiv API (2611.16422);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2611.16422 BlinkMimic: Training a Humanoid Motion Tracker in Minutes on a Single GPU'
  url: https://arxiv.org/abs/2611.16422
  date: '2026-11-12'
  accessed_at: '2026-11-16'
- id: src_002
  type: website
  title: Project page
  url: https://github.com/fuyichen0725/blinkmimic
  accessed_at: '2026-11-16'
---

## 概述

全身运动跟踪使人形机器人能够跟随参考动作，但为动作库训练跟踪策略通常需要数小时 GPU 时间。SuperMimic 提出通过对从并行仿真中学得的世界模型进行反向传播来训练策略，InstantTrack 则加入 Muon 更新、围绕参考动作的残差策略以及平均化的部署策略。BlinkMimic 在两者基础上进一步加速这一训练流程，并在仿真 Unitree G1 上验证：单张 RTX 4090 上 3.4 分钟即可为全部 40 个 LAFAN1 片段训练出单一策略。作者将训练时间拆解为单次迭代开销、拟合动作所需迭代数与消除最后失败所需迭代数三项，并把继承与新增组件分别归入其中。通过每个组件三个随机种子的留一消融，作者分析了各组件影响哪一时间项，并结合梯度、更新规则与失败案例的进一步测量解释其作用。

## 核心内容

### 问题背景

全身运动跟踪让仿真人形机器人跟随参考动作，但为整个动作库训练跟踪策略通常要消耗数小时 GPU 时间。此前工作 SuperMimic 表明，可以改为对从并行仿真中学得的世界模型做反向传播来训练策略；InstantTrack 进一步引入 Muon 更新、围绕参考动作的残差策略以及平均化的部署策略。BlinkMimic 在二者基础上提出一套更快的训练配方。

### 方法

作者将训练时间分解为三个部分，并把继承组件与新增组件分别归入其中：

- 单次迭代的开销；
- 拟合动作所需的迭代数；
- 消除最后失败所需的迭代数。

新增组件包括：

- 一种随训练进展而下降的步长；
- 由部署条件下部署策略的失败所触发的重置；
- 对整个迭代过程进行 GPU 图捕获。

### 实验设置

- 平台：仿真 Unitree G1。
- 动作库：全部 40 个 LAFAN1 片段，训练单一策略。
- 硬件：单张 RTX 4090。
- 成功判据：连续三个检查点达到不低于 0.82 的归一化回报，且无失败片段。
- 统计方式：三个随机种子取平均。
- 消融：对每个组件做留一消融，每个配置三个随机种子。

### 关键结果

- 在上述设置下，BlinkMimic 用 3.4 分钟完成全部 40 个 LAFAN1 片段的单一策略训练。
- 留一消融显示每个组件分别影响上述三个时间项中的哪一项。
- 作者进一步测量梯度、更新规则与失败案例，用以解释这些效应。

### 结论

BlinkMimic 通过针对训练时间各构成项的组件设计，显著缩短了人形机器人全身运动跟踪策略的训练时间。代码与逐种子结果已公开于 https://github.com/fuyichen0725/blinkmimic。

## Overview

Whole-body motion tracking lets a humanoid robot follow reference motions, but training a tracking policy for a library of motions has usually taken hours of GPU time. SuperMimic showed that the policy can instead be trained by backpropagating through a world model learned from parallel simulation, and InstantTrack added Muon updates, a residual policy around the reference and an averaged deployed policy. We build on both and present BlinkMimic, a recipe that makes this training faster. On a simulated Unitree G1, BlinkMimic trains one policy for all 40 LAFAN1 clips in 3.4 minutes on a single RTX 4090, measured until three consecutive checkpoints reach a normalized return of at least 0.82 with no failed clip (mean of three seeds). We split training time into the cost of an iteration, the iterations needed to fit the motions, and the iterations needed to remove the last failures, and assign each component, inherited or new, to one of these terms. The new components are a step size that decreases once training has progressed, resets directed by failures of the deployed policy under deployment conditions, and GPU graph capture of the whole iteration. A leave-one-out ablation with three seeds per component shows which term each component affects, and further measurements of the gradient, the update rule and the failure cases explain these effects. Code and per-seed results are available at https://github.com/fuyichen0725/blinkmimic.

## 参考
- https://arxiv.org/abs/2611.16422
- https://github.com/fuyichen0725/blinkmimic
