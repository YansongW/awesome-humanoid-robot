---
$id: ent_paper_qu_ressafe_learning_safety_filter_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ResSafe: Learning Safety Filtering with Residual Reinforcement Learning for Humanoids'
  zh: 'ResSafe: Learning Safety Filtering with Residual Reinforcement Learning for Humanoids'
  ko: 'ResSafe: Learning Safety Filtering with Residual Reinforcement Learning for Humanoids'
summary:
  en: Safe control of humanoid robots remains challenging due to their high-dimensional dynamics, contact-rich interactions,
    and sensitivity to disturbances. Although reinforcement learning has enabled effective locomotion and motion tracking,
    learned policies can still generate unsafe actions that lead to instability or falls. In this work, we propose residual
    reinforcement learning as an implicit ...
  zh: ResSafe 提出将残差强化学习用作人形机器人控制中的隐式安全过滤机制，由 Gechen Qu、Tong Zhang、Bike Zhang、Yen-Jen Wang、Koushil Sreenath、Claire Tomlin、Jason
    Jangho Choi 合作完成。该方法将任务性能与安全性解耦：标称策略只负责任务性能，残差策略专门学习安全修正，从而获得更优的性能—安全 Pareto 权衡，并避免在单一策略训练中反复调参多个相互竞争的奖励项。
  ko: Safe control of humanoid robots remains challenging due to their high-dimensional dynamics, contact-rich interactions,
    and sensitivity to disturbances. Although reinforcement learning has enabled effective locomotion and motion tracking,
    learned policies can still generate unsafe actions that lead to instability or falls. In this work, we propose residual
    reinforcement learning as an implicit ...
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
- humanoid_control
- residual_reinforcement_learning
- safety_filtering
- safe_control
- locomotion
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-09-21'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-09-21). Bibliographic metadata from arXiv API (2609.15988);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2609.15988 ResSafe: Learning Safety Filtering with Residual Reinforcement Learning for Humanoids'
  url: https://arxiv.org/abs/2609.15988
  date: '2026-09-14'
  accessed_at: '2026-09-21'
---

## 概述

人形机器人的安全控制因其高维动力学、富接触交互以及对扰动敏感而颇具挑战。尽管强化学习已能实现有效的行走与动作跟踪，但学到的策略仍可能输出导致失稳或跌倒的不安全动作。ResSafe 的做法是不再让单一标称策略同时兼顾性能、安全与鲁棒性，而是把二者解耦：标称策略专注于任务性能，残差策略学习安全修正。作者指出，这种解耦带来了更好的性能—安全 Pareto 权衡，也免去了在单策略训练中仔细调节多个相互竞争奖励项的负担，并表明残差策略可以充当一种隐式安全过滤器。

## 核心内容

### 问题背景
人形机器人的安全控制面临高维动力学、富接触交互以及对扰动敏感等困难。强化学习虽然已能支撑有效的行走与动作跟踪，但所学策略仍可能产生不安全动作，进而引发失稳或跌倒。

### 方法
- 提出将残差强化学习作为人形机器人安全控制的隐式安全过滤机制。
- 核心思路是性能与安全的解耦：不再依赖单一标称策略同时平衡性能、安全与鲁棒性。
- 标称策略只关注任务性能，残差策略则学习安全修正。
- 作者指出，这种解耦带来更好的性能—安全 Pareto 权衡，并避免了在单一策略训练中仔细调节多个相互竞争奖励项的需要。
- 作者表明残差策略可以充当隐式安全过滤器。

### 实验设置与关键结果
摘要未提供具体实验平台、基准、数据集或定量结果。

### 结论
通过将任务性能与安全修正分离到标称策略与残差策略中，ResSafe 为安全人形控制提供了一种隐式安全过滤思路，并改善了性能与安全之间的权衡。

## Overview

Safe control of humanoid robots remains challenging due to their high-dimensional dynamics, contact-rich interactions, and sensitivity to disturbances. Although reinforcement learning has enabled effective locomotion and motion tracking, learned policies can still generate unsafe actions that lead to instability or falls. In this work, we propose residual reinforcement learning as an implicit safety-filtering mechanism for safe humanoid control. Instead of relying on a single nominal policy to simultaneously balance performance, safety, and robustness, we decouple performance and safety. The nominal policy focuses solely on task performance, while a residual policy learns safety corrections. This decoupling leads to a better performance--safety Pareto trade-off and avoids the need for careful tuning of multiple competing reward terms within a single policy training. We show that the residual policy can act as an implicit safety filter.

## 参考
- https://arxiv.org/abs/2609.15988
