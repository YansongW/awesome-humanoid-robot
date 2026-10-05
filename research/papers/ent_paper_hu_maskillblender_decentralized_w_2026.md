---
$id: ent_paper_hu_maskillblender_decentralized_w_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'MASkillBlender: Decentralized Whole-Body Coordination for Multi-Humanoid Loco-Manipulation via Skill Blending'
  zh: 'MASkillBlender: Decentralized Whole-Body Coordination for Multi-Humanoid Loco-Manipulation via Skill Blending'
  ko: 'MASkillBlender: Decentralized Whole-Body Coordination for Multi-Humanoid Loco-Manipulation via Skill Blending'
summary:
  en: Coordinated multi-humanoid loco-manipulation is promising yet challenging due to high-dimensional whole-body control,
    decentralized decision making, and scalability. While recent reinforcement learning methods have improved single-humanoid
    whole-body control, extending them to the multi-humanoid setting remains nontrivial and often requires substantial reward
    engineering or task-specific design. ...
  zh: MASkillBlender 是一个面向多台人形机器人的通用多智能体强化学习框架，由 Yifan Hu、Luhang Hong、Mingkang Long、Danning Wang、Chengfeng Jia、Rong Su、Junjie
    Fu、Guanghui Wen 提出，用于实现去中心化的全身 loco-manipulation 协调。其核心思路是在可复用的预训练单机人形技能之上学习一个共享的去中心化高层策略，仅依赖任务级奖励即可产生协调行为，无需任务特定的运动参考。作者还引入基于置换的数据增强策略，并在同质
    Markov 博弈框架下从理论上证明置换样本保持原样本的策略梯度方向。
  ko: Coordinated multi-humanoid loco-manipulation is promising yet challenging due to high-dimensional whole-body control,
    decentralized decision making, and scalability. While recent reinforcement learning methods have improved single-humanoid
    whole-body control, extending them to the multi-humanoid setting remains nontrivial and often requires substantial reward
    engineering or task-specific design. ...
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
- multi_humanoid_coordination
- whole_body_control
- loco_manipulation
- multi_agent_reinforcement_learning
- decentralized_policy
- skill_blending
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-10-05'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-10-05). Bibliographic metadata from arXiv API (2610.01102);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2610.01102 MASkillBlender: Decentralized Whole-Body Coordination for Multi-Humanoid Loco-Manipulation via
    Skill Blending'
  url: https://arxiv.org/abs/2610.01102
  date: '2026-10-01'
  accessed_at: '2026-10-05'
---

## 概述

多台人形机器人协同完成移动与操作任务具有广阔前景，但受制于高维全身控制、去中心化决策与可扩展性等难题。已有的强化学习方法虽提升了单台人形机器人的全身控制能力，但推广到多机场景并不简单，往往需要大量奖励工程或针对具体任务的设计。MASkillBlender 提出一种通用多智能体强化学习框架，通过在可复用的预训练单机人形技能之上学习共享的去中心化高层策略，仅用任务级奖励即可实现协调行为，且不依赖任务特定的运动参考。为提升学习效率，作者针对同质多机系统设计了基于置换的数据增强策略，并从理论上说明在同质 Markov 博弈建模下，置换后的样本仍保持原样本的策略梯度方向。该框架在两种人形本体、多个多机协调任务上进行了评估，仿真结果显示其能稳定取得良好的任务表现，并在不同任务与人形本体间实现协调行为。

## 核心内容

### 问题背景

多台人形机器人协同的 loco-manipulation（移动-操作）任务兼具应用价值与挑战性，主要难点在于：

- 高维全身控制；
- 去中心化决策；
- 可扩展性。

近期强化学习方法已改善单台人形机器人的全身控制，但将其扩展到多机设定并不容易，通常需要大量奖励工程或任务特定设计。

### 方法

作者提出 MASkillBlender，一个通用的多智能体强化学习框架，用于实现去中心化的多机人形全身协调。其关键设计包括：

- 在可复用的预训练单机人形技能之上，学习一个共享的去中心化高层策略；
- 仅使用任务级奖励即可产生协调行为，无需任务特定的运动参考；
- 针对同质多机系统引入基于置换（permutation-based）的数据增强策略以提升学习效率；
- 在同质 Markov 博弈（homogeneous Markov game）建模下，从理论上证明置换后的样本保持原样本的策略梯度方向。

### 实验设置

- 在两种人形本体（two humanoid embodiments）上，针对多个多机协调任务进行评估；
- 评估基于仿真结果。

### 关键结果

- 所提框架在不同任务与人形本体上均能持续取得较强的任务表现；
- 能够实现跨任务、跨人形本体的协调行为。

### 结论

MASkillBlender 通过复用预训练单机技能并学习共享去中心化高层策略，为多机人形全身协调提供了一种通用方案，减少了对任务特定运动参考与复杂奖励工程的依赖，并借助置换数据增强提升了同质多机系统的学习效率。

## Overview

Coordinated multi-humanoid loco-manipulation is promising yet challenging due to high-dimensional whole-body control, decentralized decision making, and scalability. While recent reinforcement learning methods have improved single-humanoid whole-body control, extending them to the multi-humanoid setting remains nontrivial and often requires substantial reward engineering or task-specific design. We propose MASkillBlender, a general multi-agent reinforcement learning framework to achieve decentralized multi-humanoid whole-body coordination. By learning a shared decentralized high-level policy over reusable pre-trained single-humanoid skills, MASkillBlender enables coordinated behaviors using only task-level rewards, without requiring task-specific motion references. To improve learning efficiency, we further introduce a permutation-based data augmentation strategy for homogeneous multi-humanoid systems, and theoretically show that the permuted samples preserve the policy-gradient direction of the original samples under the homogeneous Markov game formulation. We evaluate MASkillBlender on multiple multi-humanoid coordination tasks across two humanoid embodiments. Simulation results demonstrate that the proposed framework consistently achieves strong task performance and enables coordinated behaviors across different tasks and humanoid embodiments.

## 参考
- https://arxiv.org/abs/2610.01102
