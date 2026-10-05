---
$id: ent_paper_mousa_promo_preference_conditioned_m_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'PROMO: Preference-conditioned Multi-Objective Reinforcement Learning for Quadrupedal Robots'
  zh: 'PROMO: Preference-conditioned Multi-Objective Reinforcement Learning for Quadrupedal Robots'
  ko: 'PROMO: Preference-conditioned Multi-Objective Reinforcement Learning for Quadrupedal Robots'
summary:
  en: Quadrupedal locomotion requires balancing conflicting objectives such as command tracking, stability, and energy efficiency,
    yet conventional reinforcement learning (RL) hardcodes these priorities into a fixed scalar reward at training time. We
    present PROMO (Preference-Conditioned Multi-Objective Reinforcement Learning), a semantic multi-objective approach that
    makes this trade-off an explicit ...
  zh: PROMO（Preference-Conditioned Multi-Objective Reinforcement Learning）是一种语义多目标强化学习方法，由 Amr Mousa、Rifny Rachman、Neil Karavis、Michele
    Caprio 与 Richard Allmendinger 提出，将四足机器人运动中的目标权衡作为运行时输入交给单一策略。它把部署方的偏好与具体机体的运动先验分离，使操作者意图不再被硬编码进固定标量奖励。在仿真中采样 100 个偏好时，67
    个行为处于精确 Pareto 非支配状态，偏好与目标平均相关性达 0.843，并零样本迁移到 Unitree Go2。
  ko: Quadrupedal locomotion requires balancing conflicting objectives such as command tracking, stability, and energy efficiency,
    yet conventional reinforcement learning (RL) hardcodes these priorities into a fixed scalar reward at training time. We
    present PROMO (Preference-Conditioned Multi-Objective Reinforcement Learning), a semantic multi-objective approach that
    makes this trade-off an explicit ...
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
- quadrupedal_locomotion
- multi_objective_reinforcement_learning
- preference_conditioning
- pareto_front
- sim_to_real_transfer
- unitree_go2
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-10-05'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-10-05). Bibliographic metadata from arXiv API (2610.01260);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2610.01260 PROMO: Preference-conditioned Multi-Objective Reinforcement Learning for Quadrupedal Robots'
  url: https://arxiv.org/abs/2610.01260
  date: '2026-10-01'
  accessed_at: '2026-10-05'
- id: src_002
  type: website
  title: Project page
  url: https://amrmousa.com/promo/
  accessed_at: '2026-10-05'
---

## 概述

四足机器人运动需要同时兼顾指令跟踪、稳定性与能效等相互冲突的目标，而传统强化学习在训练阶段就把这些优先级固化进一个标量奖励中。PROMO 提出语义多目标方法，把这种权衡变成单一运动策略的显式运行时输入：策略以部署方偏好为条件，同时保持与机体相关的运动先验固定，从而将操作者意图与生成可行步态所需的奖励塑形项分离开来。与固定目标控制器、多目标基线以及独立训练的专业化策略相比，PROMO 用单一可部署策略实现了目标专门化与鲁棒性。仿真中采样 100 个偏好时，有 67 个行为在精确 Pareto 支配下非支配，偏好与目标的平均相关性为 0.843，说明其具备较广的 Pareto 覆盖与可预测的偏好响应。同一策略零样本迁移到 Unitree Go2，仅改变偏好即可相对均衡偏好将比能耗最多降低 30.4%、位置误差降低 38.7%、机体姿态峰值偏差降低 59.0%。

## 核心内容

### 问题背景
四足运动控制本质上是一个多目标问题：指令跟踪、稳定性与能效之间存在冲突。常规强化学习做法是在训练时把这些优先级写死为一个固定标量奖励，导致部署阶段无法按需调整权衡，也难以适应不同操作者意图。

### 方法
- PROMO 是一种语义多目标强化学习方法，将目标权衡作为显式的运行时输入提供给单一运动策略。
- 策略以部署方偏好为条件，同时保持与具体机体相关的运动先验固定。
- 这一设计把操作者意图与生成可行步态所必需的奖励塑形项分离开来，使偏好成为可调接口而非训练期常量。

### 实验设置与关键结果
- 在仿真中采样 100 个偏好，其中 67 个行为在精确 Pareto 支配下为非支配，偏好与目标的平均相关性为 0.843，表明 Pareto 覆盖较广且偏好响应可预测。
- 与固定目标控制器、多目标基线以及独立训练的专业化策略相比，PROMO 以单一可部署策略实现了目标专门化与鲁棒性。
- 同一策略零样本迁移到 Unitree Go2：仅改变偏好，即可相对均衡偏好将比能耗最多降低 30.4%、位置误差降低 38.7%、机体姿态峰值偏差降低 59.0%。

### 结论
结果表明，偏好条件化的多目标强化学习可作为自适应腿足运动的实用运行时接口，其作用不再局限于离线构建 Pareto 集。开源代码与视频见 https://armousa.com/promo/。

## Overview

Quadrupedal locomotion requires balancing conflicting objectives such as command tracking, stability, and energy efficiency, yet conventional reinforcement learning (RL) hardcodes these priorities into a fixed scalar reward at training time. We present PROMO (Preference-Conditioned Multi-Objective Reinforcement Learning), a semantic multi-objective approach that makes this trade-off an explicit runtime input to a single locomotion policy. PROMO conditions the policy on deployment facing preferences while keeping embodiment-specific locomotion priors fixed, thereby separating operator intent from reward shaping terms required for viable gait generation. Compared with fixed-objective controllers, multi-objective baselines, and independently trained specialists, PROMO achieves objective specialization and robustness from a single deployable policy. Across 100 sampled preferences in simulation, 67 behaviors are non-dominated under exact Pareto dominance, with a mean preference-objective correlation of 0.843, demonstrating broad Pareto coverage and predictable preference response. The same policy transfers zero-shot to a Unitree Go2, where preference changes alone reduce specific energy by up to 30.4%, position error by 38.7%, and peak body-attitude deviation by 59.0% relative to the balanced preference. These results establish preference-conditioned multi-objective RL as a practical runtime interface for adaptive legged locomotion, extending its role beyond offline Pareto-set construction. Open-source code and videos are available at https://amrmousa.com/promo/.

## 参考
- https://arxiv.org/abs/2610.01260
- https://amrmousa.com/promo/
