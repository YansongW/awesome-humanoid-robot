---
$id: ent_paper_ovinnikov_predictive_safety_curricula_fo_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Predictive Safety Curricula for Robust Legged Locomotion
  zh: Predictive Safety Curricula for Robust Legged Locomotion
  ko: Predictive Safety Curricula for Robust Legged Locomotion
summary:
  en: Rare but consequential failures can persist in learned locomotion policies for legged robots even when average task
    performance is high, in part because standard curricula primarily adapt task difficulty rather than the distribution of
    safety-critical experience. We introduce Predictive Safety Curricula (PSC), a framework for allocating locomotion training
    experience using learned predictions of ...
  zh: Predictive Safety Curricula (PSC) 是一个利用对未来安全代价的学习预测来分配足式机器人运动训练经验的框架，由 Ivan Ovinnikov、Pascal Sutter、Christian Gehring
    与 Jordis Herrmann 提出。PSC 从策略 rollout 中训练一个分布式安全 critic，并据此优先采样地形上下文与已遇到的随机事件，在不改动任务奖励与策略优化损失的前提下改变训练分布。在 ANYmal-D 硬件上，PSC
    相比 learning-progress curriculum 将小腿碰撞发生率降低 63%，并在每个随机种子下均有下降。
  ko: Rare but consequential failures can persist in learned locomotion policies for legged robots even when average task
    performance is high, in part because standard curricula primarily adapt task difficulty rather than the distribution of
    safety-critical experience. We introduce Predictive Safety Curricula (PSC), a framework for allocating locomotion training
    experience using learned predictions of ...
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
- legged_locomotion
- safety_curriculum
- distributional_critic
- sim_to_real
- terrain_awareness
- training_experience_allocation
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-10-05'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-10-05). Bibliographic metadata from arXiv API (2609.37070);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: arXiv:2609.37070 Predictive Safety Curricula for Robust Legged Locomotion
  url: https://arxiv.org/abs/2609.37070
  date: '2026-09-29'
  accessed_at: '2026-10-05'
---

## 概述

足式机器人学习到的运动策略即便平均任务表现很高，仍可能残留罕见但后果严重的失败，原因之一是常规课程主要调整任务难度，而非安全关键经验的分布。为此作者提出 Predictive Safety Curricula (PSC)，用对未来安全代价的学习预测来分配训练经验：从策略 rollout 中训练分布式安全 critic，再用其预测同时为地形上下文和此前遇到的随机事件排优先级。该课程只改变训练分布，任务奖励与策略优化损失保持不变。在受控崎岖地形运动与生产级运动系统中评估，PSC 相比标准地形递进、基于优势的回放和学习进度课程都提升了可靠性，在困难地形与观测退化条件下增益最大。该分配原则还迁移到两套生产运动栈：在 ANYmal-D 硬件上，跨三个匹配训练种子，PSC 相比 learning-progress curriculum 使小腿碰撞发生率降低 63%，且每个种子均有下降；在一套生产爬楼梯平台上，PSC 在评估的硬件试验中消除了观察到的小腿碰撞。

## 核心内容

### 问题背景
学习得到的足式机器人运动策略即使平均任务表现很高，仍会残留罕见但后果严重的失败。作者认为部分原因在于标准课程主要调整任务难度，而不是调整安全关键经验的分布，因此这些稀有失败模式得不到足够的训练覆盖。

### 方法
- 提出 Predictive Safety Curricula (PSC)，一个用未来安全代价的学习预测来分配运动训练经验的框架。
- PSC 从策略 rollout 中训练一个分布式安全 critic（distributional safety critic）。
- 利用该 critic 的预测，同时为地形上下文（terrain contexts）和此前遇到的随机事件（previously encountered randomized events）排定优先级。
- 由此得到的课程只修改训练分布，任务奖励与策略优化损失均保持不变。

### 实验设置与对比
- 评估场景包括受控的崎岖地形运动，以及生产级运动系统。
- 对比基线包括：标准地形递进（standard terrain progression）、基于优势的回放（advantage-based replay）、学习进度课程（learning-progress curriculum）。

### 关键结果
- PSC 相对上述基线提升了可靠性，在困难地形和观测退化（degraded observations）条件下增益最大。
- 同一分配原则迁移到两套生产运动栈。
- 在 ANYmal-D 硬件上，跨三个匹配训练种子，PSC 相比 learning-progress curriculum 将小腿碰撞（shank-collision）发生率降低 63%，且每个种子均有下降。
- 在一套生产爬楼梯平台上，PSC 在评估的硬件试验中消除了观察到的小腿碰撞。

### 结论
结果表明，对未来安全代价的学习预测可以作为有效信号，把训练经验分配到稀有失败模式上，从而提升运动可靠性。

## Overview

Rare but consequential failures can persist in learned locomotion policies for legged robots even when average task performance is high, in part because standard curricula primarily adapt task difficulty rather than the distribution of safety-critical experience. We introduce Predictive Safety Curricula (PSC), a framework for allocating locomotion training experience using learned predictions of future safety cost. PSC trains a distributional safety critic from policy rollouts and uses its predictions to prioritize both terrain contexts and previously encountered randomized events. The resulting curriculum modifies the training distribution while leaving the task reward and policy-optimization loss unchanged. We evaluate PSC in controlled rough-terrain locomotion and in production locomotion systems. PSC improves reliability relative to standard terrain progression, advantage-based replay, and learning-progress curricula, with the largest gains on difficult terrain and under degraded observations. The same allocation principle transfers to two production locomotion stacks. On ANYmal-D hardware, PSC reduces shank-collision incidence by $63\%$ relative to the learning-progress curriculum across three matched training seeds, with a reduction in every seed. On a production stair-climbing platform, PSC eliminates observed shank collisions in the evaluated hardware trials. These results show that learned predictions of future safety cost can provide an effective signal for allocating training experience toward rare failure modes and improving locomotion reliability.

## 参考
- https://arxiv.org/abs/2609.37070
