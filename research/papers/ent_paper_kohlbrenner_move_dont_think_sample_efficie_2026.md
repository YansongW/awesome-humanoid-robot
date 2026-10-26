---
$id: ent_paper_kohlbrenner_move_dont_think_sample_efficie_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Move, don''t think: sample-efficient collision avoidance with lossy proximity sensors'
  zh: 'Move, don''t think: sample-efficient collision avoidance with lossy proximity sensors'
  ko: 'Move, don''t think: sample-efficient collision avoidance with lossy proximity sensors'
summary:
  en: Data-driven robots must learn to avoid collisions with as few demonstrations as possible to avoid collecting large datasets
    of destructive collision examples. We explore whole-body proximity sensors as inductive biases for learning reflexive
    collision-dodging behavior and find that lossy sensors with low resolution were stronger biases than high-resolution coverage.
    We also found that, perhaps ...
  zh: 该研究探索将全身接近传感器作为归纳偏置，用于学习反射式避碰行为，并在强化学习环境中比较了八种候选表征。作者在刻意受限的样本与计算预算下，端到端训练了超过 200 台人形机器人玩简化版躲避球。核心发现是低分辨率的有损传感器比高分辨率全覆盖是更强的归纳偏置，而预测接触发生的时间与位置反而降低了学习样本效率。
  ko: Data-driven robots must learn to avoid collisions with as few demonstrations as possible to avoid collecting large datasets
    of destructive collision examples. We explore whole-body proximity sensors as inductive biases for learning reflexive
    collision-dodging behavior and find that lossy sensors with low resolution were stronger biases than high-resolution coverage.
    We also found that, perhaps ...
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
- collision_avoidance
- proximity_sensors
- sample_efficiency
- humanoid_robots
- reinforcement_learning
- inductive_bias
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-10-26'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-10-26). Bibliographic metadata from arXiv API (2610.31891);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2610.31891 Move, don''t think: sample-efficient collision avoidance with lossy proximity sensors'
  url: https://arxiv.org/abs/2610.31891
  date: '2026-10-22'
  accessed_at: '2026-10-26'
---

## 概述

数据驱动的机器人需要以尽可能少的示范学会避碰，以避免采集大量具有破坏性的碰撞样本。作者将全身接近传感器视为学习反射式躲避行为的归纳偏置，并在强化学习环境中系统考察了八种候选表征，涵盖隐空间压缩、未来接触预测、有损腐蚀与特权状态估计。实验在刻意受限的样本与计算预算下，端到端训练超过 200 台人形机器人玩简化版躲避球。结果显示，低分辨率的有损传感器比高分辨率全覆盖提供更强的归纳偏置；而预测接触发生的时间与位置这一看似合理的做法，反而削弱了样本效率。

## 核心内容

### 问题背景
数据驱动机器人方法通常依赖大量示范来学习避碰，但碰撞样本本身具有破坏性，采集成本高。作者希望以尽可能少的示范让机器人学会反射式躲避行为，并考察何种感知表征能作为有效的归纳偏置。

### 方法
- 以全身接近传感器作为学习反射式避碰行为的归纳偏置来源。
- 在强化学习环境中考察八种候选表征，包括隐空间压缩、未来接触预测、有损腐蚀以及特权状态估计。
- 采用端到端训练方式，任务为简化版躲避球。

### 实验设置
- 训练对象为超过 200 台人形机器人。
- 训练在刻意受限的样本与计算预算下进行，以突出样本效率的差异。

### 关键结果
- 低分辨率的有损传感器比高分辨率全覆盖构成更强的归纳偏置。
- 与直觉相反，预测接触在机器人身体上发生的时间与位置，反而降低了学习样本效率。

### 结论
在样本与计算受限的条件下，简单且有损的接近感知表征比高分辨率覆盖或显式的接触预测更有利于样本高效地学习反射式避碰行为。

## Overview

Data-driven robots must learn to avoid collisions with as few demonstrations as possible to avoid collecting large datasets of destructive collision examples. We explore whole-body proximity sensors as inductive biases for learning reflexive collision-dodging behavior and find that lossy sensors with low resolution were stronger biases than high-resolution coverage. We also found that, perhaps unintuitively, anticipating when and where contact happens on the body of a robot reduced its learning sample efficiency. We investigated eight candidate representations in a reinforcement learning environment, which included latent compression, future contact anticipation, lossy corruption, and privileged state estimation. The candidate representations were tested by training over 200 humanoid robots to play a simplified version of dodgeball end-to-end under an intentionally constrained sample and compute budget.

## 参考
- https://arxiv.org/abs/2610.31891
