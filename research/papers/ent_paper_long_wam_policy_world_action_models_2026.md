---
$id: ent_paper_long_wam_policy_world_action_models_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'WAM-Policy: World Action Models with On-Policy Distillation for Quadrupedal Loco-Manipulation'
  zh: 'WAM-Policy: World Action Models with On-Policy Distillation for Quadrupedal Loco-Manipulation'
  ko: 'WAM-Policy: World Action Models with On-Policy Distillation for Quadrupedal Loco-Manipulation'
summary:
  en: Arm-free quadrupeds can perform loco-manipulation, walking on three legs while manipulating with a front leg, yet no
    existing policy for it follows language instructions. World action models (WAMs) have emerged as effective language-conditioned
    manipulation policies, but are pretrained for robot arms and sample slowly. WAM-Policy turns one WAM into a quadrupedal
    loco-manipulation policy via two ...
  zh: WAM-Policy 由 Junlin Long、Xu Deng、Yiran Wang、Yue Yang、Yang Zhao、Zeyu Zhang 提出，旨在将面向机械臂的世界动作模型（WAM）转化为四足机器人无臂移动操作策略，并使其能够遵循语言指令。方法分两阶段：先通过跨形态策略适配与加速，将机械臂中心的
    WAM 迁移至四足平台，并用同策略自蒸馏（OPSD）蒸馏出仅需一个视频步与两个动作步的学生策略；再通过强化学习调优教师，并用多教师同策略蒸馏（M-OPD）将多个慢速专家合并为少步学生。在 QLM-Bench 的十个仿真任务上，迁移策略达到
    77.0%，OPSD 学生保持 76.7% 且采样快 14 倍，经任务特定 RL 与 M-OPD 提升至 85.0%，并在真实 Unitree Go2 Air 上部署了 OPSD 学生。
  ko: Arm-free quadrupeds can perform loco-manipulation, walking on three legs while manipulating with a front leg, yet no
    existing policy for it follows language instructions. World action models (WAMs) have emerged as effective language-conditioned
    manipulation policies, but are pretrained for robot arms and sample slowly. WAM-Policy turns one WAM into a quadrupedal
    loco-manipulation policy via two ...
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
- quadrupedal_loco_manipulation
- world_action_models
- on_policy_distillation
- language_conditioned_policy
- cross_morphology_transfer
- reinforcement_learning
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-11-23'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-11-23). Bibliographic metadata from arXiv API (2611.24011);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2611.24011 WAM-Policy: World Action Models with On-Policy Distillation for Quadrupedal Loco-Manipulation'
  url: https://arxiv.org/abs/2611.24011
  date: '2026-11-18'
  accessed_at: '2026-11-23'
- id: src_002
  type: website
  title: Project page
  url: https://github.com/AIGeeksGroup/WAM-Policy,
  accessed_at: '2026-11-23'
- id: src_003
  type: website
  title: Project page
  url: https://aigeeksgroup.github.io/WAM-Policy/
  accessed_at: '2026-11-23'
---

## 概述

现有无臂四足机器人可以三条腿行走、用前腿操作，但尚无策略能遵循语言指令完成此类移动操作。世界动作模型（WAM）已成为有效的语言条件操作策略，却面向机械臂预训练且采样缓慢。WAM-Policy 通过两阶段把单个 WAM 转为四足移动操作策略：第一阶段进行跨形态策略适配与加速，将机械臂中心的 WAM 适配到四足平台，并以同策略自蒸馏（OPSD）把迁移后的策略蒸馏为仅需一个视频步和两个动作步的学生；第二阶段进行任务特定改进与合并，用强化学习调优教师，再以多教师同策略蒸馏（M-OPD）把慢速专家合并为一个少步学生。在 QLM-Bench 的十个仿真任务（含 1,000 条无需遥操作合成的演示）上，迁移策略达 77.0%，OPSD 学生保持 76.7% 且采样快 14 倍，任务特定 RL 与 M-OPD 进一步提升至 85.0%。作者还将 OPSD 学生部署在真实 Unitree Go2 Air 上，以较低推理成本获得更强的四足策略。

## 核心内容

### 问题背景
无臂四足机器人能够以三条腿行走、用一条前腿执行操作，即四足移动操作（loco-manipulation），但现有策略均不支持语言指令。世界动作模型（WAM）在语言条件操作上表现有效，然而其预训练面向机械臂，且推理采样速度慢，难以直接用于四足平台。

### 方法
WAM-Policy 将单个 WAM 转化为四足移动操作策略，分为两个阶段：

- **第一阶段：跨形态策略适配与加速（Cross-Morphology Policy Adaptation and Acceleration）**
  - 将面向机械臂的 WAM 适配到四足机器人形态。
  - 采用同策略自蒸馏（on-policy self-distillation, OPSD），把迁移后的策略蒸馏为学生策略，使其推理仅需一个视频步和两个动作步。
  - 该学生策略受限于教师策略，而教师仅通过模仿演示学习。

- **第二阶段：任务特定改进与合并（Task-Specific Improvement and Merging）**
  - 使用强化学习（RL）对教师策略进行任务特定调优。
  - 通过多教师同策略蒸馏（multi-teacher on-policy distillation, M-OPD）将多个慢速专家合并为一个少步学生策略。

### 实验设置
- 在 QLM-Bench 上进行评估，包含十个仿真任务，共 1,000 条演示，演示数据无需遥操作即可合成。
- 将 OPSD 学生策略部署到真实 Unitree Go2 Air 机器人上。

### 关键结果
- 迁移后的策略在 QLM-Bench 上达到 77.0% 的成功率。
- OPSD 学生策略保持 76.7% 的成功率，同时采样速度提升 14 倍。
- 经任务特定 RL 与 M-OPD 后，性能提升至 85.0%。

### 结论
WAM-Policy 以较低的推理成本获得了更强的四足机器人策略，并验证了从机械臂 WAM 到四足移动操作策略的跨形态迁移与蒸馏路径的可行性。

## Overview

Arm-free quadrupeds can perform loco-manipulation, walking on three legs while manipulating with a front leg, yet no existing policy for it follows language instructions. World action models (WAMs) have emerged as effective language-conditioned manipulation policies, but are pretrained for robot arms and sample slowly. WAM-Policy turns one WAM into a quadrupedal loco-manipulation policy via two stages. The first, Cross-Morphology Policy Adaptation and Acceleration, adapts the arm-centric WAM to quadrupeds and distills the transferred policy into a student with one video and two action steps by on-policy self-distillation (OPSD). This student, however, is bounded by its teacher, which only imitates demonstrations. The second stage, Task-Specific Improvement and Merging, therefore tunes the teacher by reinforcement learning (RL) and merges the slow specialists into one few-step student by multi-teacher on-policy distillation (M-OPD). On QLM-Bench, ten simulated tasks with 1,000 demonstrations synthesized without teleoperation, the transferred policy reaches 77.0%, and the OPSD student keeps 76.7% while sampling 14 times faster. Task-specific RL and M-OPD lift it to 85.0%. We also deploy the OPSD student on a real Unitree Go2 Air. WAM-Policy thus achieves a stronger quadrupedal policy at a fraction of the inference cost.

## 参考
- https://arxiv.org/abs/2611.24011
- https://github.com/AIGeeksGroup/WAM-Policy,
- https://aigeeksgroup.github.io/WAM-Policy/
