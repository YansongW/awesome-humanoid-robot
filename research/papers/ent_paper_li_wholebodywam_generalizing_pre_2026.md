---
$id: ent_paper_li_wholebodywam_generalizing_pre_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'WholeBodyWAM: Generalizing Pre-trained World-Action Priors to Humanoid Loco-Manipulation via WBC-Grounded Coordination'
  zh: 'WholeBodyWAM: Generalizing Pre-trained World-Action Priors to Humanoid Loco-Manipulation via WBC-Grounded Coordination'
  ko: 'WholeBodyWAM: Generalizing Pre-trained World-Action Priors to Humanoid Loco-Manipulation via WBC-Grounded Coordination'
summary:
  en: World Action Models (WAMs) offer a promising approach to general-purpose robot manipulation by jointly modeling visual
    dynamics and actions. However, most WAM studies focus on tabletop or arm-centric manipulation, while humanoid loco-manipulation
    remains less explored. To address this gap, we introduce WholeBodyWAM, which jointly predicts future visual dynamics,
    manipulation actions, and ...
  zh: WholeBodyWAM 是一种面向人形机器人全身移动操作（loco-manipulation）的世界动作模型，由 Zhuo Li、Yiming Yao、Jim Tan、Mengjie Jing、Zhipeng Dong、Fei Chen
    提出。它联合预测未来视觉动态、操作动作与全身控制意图，在保留预训练世界动作先验的同时，将异构全身控制器（WBC）语义进行接地并协调全身行为。实验显示其仿真任务总体成功率达 91.9%，真实世界分布外任务进度提升 0.23，跨 WBC 的成功率方差降低
    70%。
  ko: World Action Models (WAMs) offer a promising approach to general-purpose robot manipulation by jointly modeling visual
    dynamics and actions. However, most WAM studies focus on tabletop or arm-centric manipulation, while humanoid loco-manipulation
    remains less explored. To address this gap, we introduce WholeBodyWAM, which jointly predicts future visual dynamics,
    manipulation actions, and ...
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
- world_action_model
- whole_body_control
- wbc_grounding
- visual_dynamics_prediction
- out_of_distribution_generalization
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-09-21'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-09-21). Bibliographic metadata from arXiv API (2609.16644);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2609.16644 WholeBodyWAM: Generalizing Pre-trained World-Action Priors to Humanoid Loco-Manipulation via WBC-Grounded
    Coordination'
  url: https://arxiv.org/abs/2609.16644
  date: '2026-09-15'
  accessed_at: '2026-09-21'
---

## 概述

现有世界动作模型（WAM）多聚焦于桌面或手臂为中心的操取任务，人形机器人的全身移动操作仍少有探索。WholeBodyWAM 针对这一空白，将未来视觉动态、操作动作与全身控制意图纳入统一预测框架，用于可泛化的人形 loco-manipulation。其核心思路不是从零重新学习全身行为，而是在保留预训练世界动作先验的基础上，对异构全身控制器（WBC）的语义进行结构化接地，并协调全身行为。实验结果表明，该方法在仿真中取得 91.9% 的总体任务成功率，在真实世界分布外任务上进度提升 0.23，并使不同 WBC 之间的成功率方差降低 70%。作者认为，这为通过结构化 WBC 接地与协调来扩展预训练世界动作先验、进而实现可扩展的人形全身智能提供了一条路径。

## 核心内容

### 问题背景
世界动作模型（World Action Models, WAMs）通过联合建模视觉动态与动作，为通用机器人操取提供了有前景的途径。然而，多数 WAM 研究集中在桌面或手臂为中心的操取场景，人形机器人的全身移动操作（loco-manipulation）仍较少被探索。这一空白意味着预训练的世界动作先验尚未被有效迁移到需要全身协调的人形任务中。

### 方法
作者提出 WholeBodyWAM，其特点在于：
- 联合预测未来视觉动态、操作动作以及全身控制意图，面向可泛化的人形 loco-manipulation；
- 在保留预训练世界动作先验的同时，对异构全身控制器（WBC）的语义进行接地（grounding）；
- 协调全身行为，而非从零重新学习全身行为。

### 实验与关键结果
- 仿真任务总体成功率达到 91.9%；
- 真实世界分布外（out-of-distribution）任务进度相对各自基线提升 0.23；
- 跨不同 WBC 的成功率方差相对各自基线降低 70%。

### 结论
结果表明，通过结构化的 WBC 接地与协调来扩展预训练世界动作先验，而非重新学习全身行为，是通向可扩展人形全身智能的一条可行路径。项目主页为 https://wholebodywam.github.io/。

## Overview

World Action Models (WAMs) offer a promising approach to general-purpose robot manipulation by jointly modeling visual dynamics and actions. However, most WAM studies focus on tabletop or arm-centric manipulation, while humanoid loco-manipulation remains less explored. To address this gap, we introduce WholeBodyWAM, which jointly predicts future visual dynamics, manipulation actions, and whole-body control intents for generalizable humanoid loco-manipulation. It preserves pre-trained world-action priors while grounding heterogeneous whole-body controller (WBC) semantics and coordinating whole-body behavior. Extensive experiments show that WholeBodyWAM achieves an overall simulation task success rate of 91.9%, with a 0.23 improvement in real-world out-of-distribution task progress and a 70% reduction in success-rate variance across WBCs relative to the respective baselines. These results suggest a path toward scalable humanoid whole-body intelligence by extending pre-trained world-action priors through structured WBC grounding and coordination, rather than relearning whole-body behavior from scratch. Project page: https://wholebodywam.github.io/.

## 参考
- https://arxiv.org/abs/2609.16644
