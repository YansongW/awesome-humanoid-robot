---
$id: ent_paper_mahmud_contact_as_a_decision_variable_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Contact as a Decision Variable: Capability-Tradeoff Contact Selection for Legged Loco-Manipulation'
  zh: 'Contact as a Decision Variable: Capability-Tradeoff Contact Selection for Legged Loco-Manipulation'
  ko: 'Contact as a Decision Variable: Capability-Tradeoff Contact Selection for Legged Loco-Manipulation'
summary:
  en: 'In this paper, we study the joint selection of an environmental support contact and a whole-body configuration for
    a prescribed loco-manipulation task. A contact may provide greater physical support while restricting the motion required
    for the task. We formulate this problem through three capability measures: residual wrench, end-effector reach, and base
    mobility available after satisfying the ...'
  zh: 本文研究在给定 loco-manipulation 任务下，如何联合选择环境支撑接触点与全身构型。作者提出 Capability-Tradeoff Contact Selection（CTCS），通过残差力旋量、末端执行器可达范围与基座机动性三项能力度量，在接触获取成本之间进行权衡。在
    Unitree Go2 四足机器人搭配 AgileX NERO 机械臂的仿真与硬件实验中，CTCS 在 392 种任务条件下优于仅地面支撑与固定接触方案，并相较逐一遍历精确评估取得约 3 倍加速。
  ko: 'In this paper, we study the joint selection of an environmental support contact and a whole-body configuration for
    a prescribed loco-manipulation task. A contact may provide greater physical support while restricting the motion required
    for the task. We formulate this problem through three capability measures: residual wrench, end-effector reach, and base
    mobility available after satisfying the ...'
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
- contact_selection
- whole_body_control
- legged_robots
- capability_tradeoff
- sensitivity_analysis
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-09-28'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-09-28). Bibliographic metadata from arXiv API (2609.30140);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2609.30140 Contact as a Decision Variable: Capability-Tradeoff Contact Selection for Legged Loco-Manipulation'
  url: https://arxiv.org/abs/2609.30140
  date: '2026-09-24'
  accessed_at: '2026-09-28'
---

## 概述

该工作将接触视为决策变量，而非预先固定的约束，用于腿足式 loco-manipulation 任务中的支撑接触与全身构型联合选择。作者用残差力旋量、末端执行器可达范围与基座机动性三项能力度量刻画某个接触在满足任务需求后所保留的能力，并将其与接触获取成本相权衡。由于对每个候选接触逐一评估这些能力需要反复求解全身优化，计算代价高昂，作者提出 CTCS：先筛选接触与任务可行性，再在同一支撑面内对相似候选分组，借助局部敏感性分析由精确锚点评估预测其能力，并通过选择性精确评估校验预测，最终对候选排序并对入围者做精确评估以完成选择。实验在 Unitree Go2 四足机器人加装 AgileX NERO 机械臂上进行，覆盖 392 种任务条件与九个可用支撑面。结果显示 CTCS 能选出对任务具有有利能力权衡的支撑面，优于仅地面支撑与固定接触方案，并在接近逐一遍历精确评估所得平均目标值的同时实现约 3 倍加速。

## 核心内容

### 问题背景
在腿足式 loco-manipulation 任务中，机器人需要同时决定用哪个环境表面作为支撑接触，以及采取何种全身构型。接触选择存在内在矛盾：某个接触可能提供更强的物理支撑，却限制了完成任务所需的运动范围。作者将这一问题形式化为接触与全身构型的联合选择问题。

### 能力度量与目标
作者用三项能力度量刻画候选接触在满足任务要求之后所保留的能力：
- 残差力旋量（residual wrench）
- 末端执行器可达范围（end-effector reach）
- 基座机动性（base mobility）

这些能力与接触获取成本（contact acquisition cost）相互权衡。对每个候选接触评估上述能力，需要反复进行全身优化，计算开销很大。

### 方法：CTCS
为降低计算成本，作者提出 Capability-Tradeoff Contact Selection（CTCS），其流程包括：
- 对候选接触与任务可行性进行筛选；
- 在每个支撑面内部将相似候选分组；
- 利用局部敏感性分析，由精确锚点评估预测各组候选的能力；
- 通过选择性精确评估对预测结果进行校验；
- 按能力对候选排序，并对入围短名单做精确评估以完成最终选择。

### 实验设置
评估在仿真与硬件实验中开展，平台为 Unitree Go2 四足机器人，搭载 AgileX NERO 机械臂。实验覆盖 392 种任务条件，可用支撑面共九个。

### 关键结果
- CTCS 优于仅地面支撑（ground-only）与固定接触（fixed-contact）支撑方案，因为它能够选出为任务提供有利能力权衡的支撑面。
- 与对每个候选逐一精确评估相比，CTCS 取得约 3 倍加速，同时其结果的平均目标值与逐一精确评估所得十分接近。

### 结论
将接触作为决策变量、并以能力权衡为依据进行选择，可让腿足式 loco-manipulation 系统在支撑性与任务所需运动自由度之间取得更优平衡；CTCS 通过分组预测与选择性精确评估，在保持接近精确评估效果的同时显著降低计算成本。

## Overview

In this paper, we study the joint selection of an environmental support contact and a whole-body configuration for a prescribed loco-manipulation task. A contact may provide greater physical support while restricting the motion required for the task. We formulate this problem through three capability measures: residual wrench, end-effector reach, and base mobility available after satisfying the task requirements, and we balance them against contact acquisition cost. Evaluating these capabilities for every candidate requires repeated whole-body optimizations. To reduce this computational cost, we propose Capability-Tradeoff Contact Selection (CTCS). CTCS screens candidates for contact and task feasibility, groups similar candidates within each surface, and predicts their capabilities from exact anchor evaluations using local sensitivity analysis. It checks these predictions through selective exact evaluations, ranks candidates by capability, and evaluates a shortlist exactly for final selection. We evaluate CTCS in simulations and hardware experiments using a Unitree Go2 quadruped with an AgileX NERO arm across $392$ task conditions with nine available support surfaces. Results show that CTCS outperforms ground-only and fixed-contact support, as it can select support surfaces that provide favorable capability trade-offs for the task. Compared with evaluating every candidate exactly, CTCS achieves approximately $3\times$ speedup while closely matching the resulting mean objective value.

## 参考
- https://arxiv.org/abs/2609.30140
