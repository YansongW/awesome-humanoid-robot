---
$id: ent_paper_li_efficient_real_world_online_re_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Efficient Real-World Online Reinforcement Learning for Robot Manipulation via Centralized Training and Critic Decomposition
  zh: Efficient Real-World Online Reinforcement Learning for Robot Manipulation via Centralized Training and Critic Decomposition
  ko: Efficient Real-World Online Reinforcement Learning for Robot Manipulation via Centralized Training and Critic Decomposition
summary:
  en: Real-world online reinforcement learning (RL) provides a promising approach for training robotic manipulation policies
    directly in the physical world, avoiding the sim-to-real gap and enabling continuous policy refinement through human-in-the-loop
    interaction. Recent methods have demonstrated sample-efficient learning through human intervention but remain limited
    to small randomization ranges and ...
  zh: 本文提出一种结合集中训练与分散执行（CTDE）和混合奖励架构（HRA）的统一框架，用于提升真实世界在线强化学习在机器人操作任务中的样本效率与策略性能。该方法通过共享多头评论家网络，将评论家分解为任务头与抓取头，并在两个机械臂和模拟人形机器人上验证，在维度随机化范围比先前工作大5-25倍的条件下，显著提升了任务成功率。
  ko: Real-world online reinforcement learning (RL) provides a promising approach for training robotic manipulation policies
    directly in the physical world, avoiding the sim-to-real gap and enabling continuous policy refinement through human-in-the-loop
    interaction. Recent methods have demonstrated sample-efficient learning through human intervention but remain limited
    to small randomization ranges and ...
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
- real_world_rl
- robot_manipulation
- centralized_training
- critic_decomposition
- sample_efficiency
- human_in_the_loop
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-08-17'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-08-17). Bibliographic metadata from arXiv API (2608.09762);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: arXiv:2608.09762 Efficient Real-World Online Reinforcement Learning for Robot Manipulation via Centralized Training
    and Critic Decomposition
  url: https://arxiv.org/abs/2608.09762
  date: '2026-08-10'
  accessed_at: '2026-08-17'
---

## 概述

该框架由Changhao Li等研究者提出，旨在解决真实世界在线强化学习中多智能体并发训练导致的非平稳性问题，以及现有方法随机化范围受限的不足。通过集中训练多智能体共享一个多头评论家，并将评论家分解为对应稀疏任务奖励和基于势能的抓取奖励的两个头，同时显式考虑离散夹爪策略的分类动作分布，重新制定了评论家与智能体的优化目标。实验在网球和香蕉抓取放置、锅复位及模拟积木重定位任务上验证，相比最先进基线，成功率分别从60%提升至80%、60%提升至90%、25%提升至95%，并成功完成基线始终失败的任务。

## 核心内容

### 问题背景
真实世界在线强化学习为机器人操作策略提供了一种直接在物理环境中训练的方法，避免了仿真到现实的迁移差距，并支持通过人类参与交互进行持续策略优化。然而，现有方法虽通过人类干预实现了样本高效学习，但仅限于较小的随机化范围，且面临多智能体并发训练带来的非平稳性挑战。

### 方法
本文提出一个统一框架，结合集中训练与分散执行（CTDE）和混合奖励架构（HRA）。具体而言：
- 多个智能体共享一个集中式多头评论家网络。
- 评论家被分解为任务头与抓取头，分别对应稀疏任务奖励和基于势能的抓取奖励。
- 重新制定评论家与智能体的优化目标，以利用分解后的Q值，并显式考虑离散夹爪策略的分类动作分布。

### 实验设置
- 在两个真实机械臂和一个模拟人形机器人上验证。
- 任务包括网球和香蕉的抓取放置、锅复位以及模拟积木重定位。
- 采用维度级域随机化，随机化范围约为先前工作的5-25倍。

### 关键结果
- 与最先进基线相比，网球抓取放置任务成功率从60%提升至80%。
- 香蕉抓取放置任务成功率从60%提升至90%。
- 模拟积木重定位任务成功率从25%提升至95%。
- 成功完成了一个基线始终失败的任务。

### 结论
实验结果表明，所提出的框架显著提升了样本效率和策略性能，为真实世界在线强化学习在机器人操作中的应用提供了更稳健和高效的解决方案。

## Overview

Real-world online reinforcement learning (RL) provides a promising approach for training robotic manipulation policies directly in the physical world, avoiding the sim-to-real gap and enabling continuous policy refinement through human-in-the-loop interaction. Recent methods have demonstrated sample-efficient learning through human intervention but remain limited to small randomization ranges and encounter challenges with the non-stationarity induced by concurrently training multiple agents. To address these limitations, we introduce a unified framework that combines centralized training with decentralized execution (CTDE) and a Hybrid Reward Architecture (HRA). This enables multiple actors to share a centralized multi-head critic. The critic is decomposed into task and grasp heads, corresponding to the sparse task reward and a potential-based grasping reward, respectively. We accordingly reformulate the critic and actor objectives to exploit the decomposed Q-values while explicitly accounting for the categorical action distribution of the discrete gripper policy. Experimental results demonstrate that the proposed framework substantially improves both sample efficiency and policy performance. We validate our approach on two robotic arms and a simulated humanoid robot across tennis ball and banana pick-and-place, pot reset, and simulated block relocation tasks under dimension-wise domain randomization, approximately 5-25x larger than those considered in prior work. Compared with a state-of-the-art baseline, our method improves the success rate from 60% to 80% on tennis ball pick-and-place, from 60% to 90% on banana pick-and-place, and from 25% to 95% on simulated block relocation, while also successfully accomplishing a task where the baseline consistently fails. Videos and more details are available at our project website: https://hil-harc.github.io/.

## 参考
- https://arxiv.org/abs/2608.09762
