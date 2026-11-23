---
$id: ent_paper_soenessardien_reference_free_humanoid_skateb_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Reference-Free Humanoid Skateboarding via Termination-Shaped Reinforcement Learning
  zh: Reference-Free Humanoid Skateboarding via Termination-Shaped Reinforcement Learning
  ko: Reference-Free Humanoid Skateboarding via Termination-Shaped Reinforcement Learning
summary:
  en: Humanoid locomotion research has advanced rapidly on walking and running, but \emph {object-mediated} locomotion, in
    which a robot must coordinate its body with a passive external object, remains difficult. One challenging task is skateboarding,
    which requires simultaneous interaction with the ground and a passive but movable platform to achieve forward motion.
    Current methods for tackling ...
  zh: 该论文提出一种无需参考数据的深度强化学习框架，使 K1 人形机器人能够学会滑板运动。方法将任务奖励与"利用阻断"终止条件相结合，通过多种约束（如脚离开板面、双脚同时站板、过度扭转、与板分离、板体运动不稳）在训练中动态调整出现频率，形成从站姿控制到持续人–板协同运动的隐式课程。作者为
    Ganeshvar Soenessardien、Michael Przystupa 与 Kevin Sebastian Luck。
  ko: Humanoid locomotion research has advanced rapidly on walking and running, but \emph {object-mediated} locomotion, in
    which a robot must coordinate its body with a passive external object, remains difficult. One challenging task is skateboarding,
    which requires simultaneous interaction with the ground and a passive but movable platform to achieve forward motion.
    Current methods for tackling ...
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
- humanoid_skateboarding
- reinforcement_learning
- termination_shaped_reward
- object_mediated_locomotion
- model_free_learning
- humanoid_robot
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-11-23'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-11-23). Bibliographic metadata from arXiv API (2611.26054);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: arXiv:2611.26054 Reference-Free Humanoid Skateboarding via Termination-Shaped Reinforcement Learning
  url: https://arxiv.org/abs/2611.26054
  date: '2026-11-19'
  accessed_at: '2026-11-23'
---

## 概述

人形机器人行走与奔跑研究进展迅速，但需要与被动外部物体协同的"物体中介"运动仍然困难，滑板即是典型任务：机器人须同时与地面和可移动的被动板体交互以获得前进动力。现有滑板方法依赖人类示范或需要系统辨识的解析转向模型。本文提出一种不依赖示范等先验数据的深度强化学习框架，采用无模型学习让 K1 人形机器人习得滑板技能。方法将任务奖励与利用阻断终止条件结合，引入脚离开板面、双脚站板、过度扭转、与板分离、板体运动不稳等多项行为约束，并利用这些约束在训练中变化的发生频率，形成从站姿控制到持续机器人–板体运动的隐式进阶。

## 核心内容

### 问题背景
人形机器人在行走与奔跑方面已取得快速进展，但"物体中介"运动——机器人需与被动外部物体协调身体——仍具挑战。滑板任务要求机器人同时与地面和一块被动但可移动的板体交互以产生前进运动。现有滑板方法要么依赖人类示范，要么使用需要系统辨识的解析转向模型。

### 方法
本文提出一种深度强化学习框架，不依赖示范等先验数据，采用无模型学习使 K1 人形机器人学会滑板。核心设计是将任务奖励与"利用阻断"（exploit-blocking）终止条件相结合，并引入多项约束来限制不良行为：
- 失去踩板脚（losing the planted board foot）
- 双脚同时站在板上
- 过度扭转
- 与板体分离
- 板体运动不稳定

这些约束在训练过程中的出现频率不断变化，从而产生一种隐式进阶：从站姿控制逐步过渡到持续的机器人–板体运动。

### 实验设置
摘要未提供具体实验设置细节（如仿真环境、训练时长、对比基线等）。

### 关键结果
摘要未给出定量结果；主要贡献为框架本身及上述约束机制带来的隐式课程效果。

### 结论
无需参考数据的强化学习框架可使 K1 人形机器人习得滑板运动，终止条件塑造的约束频率变化构成从站姿到持续运动的隐式进阶。

## Overview

Humanoid locomotion research has advanced rapidly on walking and running, but \emph {object-mediated} locomotion, in which a robot must coordinate its body with a passive external object, remains difficult. One challenging task is skateboarding, which requires simultaneous interaction with the ground and a passive but movable platform to achieve forward motion. Current methods for tackling skateboarding with humanoid robots either require human demonstrations or utilise analytic steering models that require system identification. In this paper, we introduce a deep reinforcement learning framework that does not rely on prior data such as demonstrations and enables robots such as the K1 humanoid to learn to skateboard using model-free learning. The method combines task rewards with exploit-blocking terminations. We introduce a number of constraints restricting behaviours such as losing the planted board foot, standing with both feet on the board, excessive twisting, separation from the board, and unstable board motion. Their changing prevalence during training produces an implicit progression from stance control towards sustained robot--board locomotion.

## 参考
- https://arxiv.org/abs/2611.26054
