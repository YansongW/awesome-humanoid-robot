---
$id: ent_paper_zhang_can_i_join_you_extended_social_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Can I join you? Extended Social Force Based Model with Predictive Control and Barrier Functions for Humanoid Group Repositioning
    Amidst Obstacles
  zh: Can I join you? Extended Social Force Based Model with Predictive Control and Barrier Functions for Humanoid Group Repositioning
    Amidst Obstacles
  ko: Can I join you? Extended Social Force Based Model with Predictive Control and Barrier Functions for Humanoid Group Repositioning
    Amidst Obstacles
summary:
  en: As social and service robots increasingly share interaction spaces in public, they may form groups while coordinating
    tasks or interacting with humans. Initial group formation alone is insufficient in dynamic settings, because it can be
    disrupted when a person or another agent joins, leaves, or passes through the group. Although group dynamics and repositioning
    have been widely studied in swarm ...
  zh: 该论文提出一种面向人形机器人群体重新编队行为的新框架，将传统 Social Force 与 Model Predictive Control（MPC）和 Control Barrier Functions（CBF）相结合，以应对群体形成受到干扰时的安全与社交适宜性问题。作者为
    Chuxuan Zhang、Niloofar Jahanshahi、Yasaman Etesam、Mo Chen 与 Angelica Lim。核心贡献在于通过 MPC 进行前瞻规划、由 CBF 约束安全性，从而在复杂环境中生成更平滑、更安全的群体重定位行为，并通过仿真消融实验与在线用户研究进行验证。
  ko: As social and service robots increasingly share interaction spaces in public, they may form groups while coordinating
    tasks or interacting with humans. Initial group formation alone is insufficient in dynamic settings, because it can be
    disrupted when a person or another agent joins, leaves, or passes through the group. Although group dynamics and repositioning
    have been widely studied in swarm ...
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
- humanoid_robotics
- social_force_model
- model_predictive_control
- control_barrier_functions
- group_repositioning
- human_robot_interaction
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-11-16'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-11-16). Bibliographic metadata from arXiv API (2611.14853);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: arXiv:2611.14853 Can I join you? Extended Social Force Based Model with Predictive Control and Barrier Functions
    for Humanoid Group Repositioning Amidst Obstacles
  url: https://arxiv.org/abs/2611.14853
  date: '2026-11-11'
  accessed_at: '2026-11-16'
---

## 概述

论文关注人形机器人群体在公共交互空间中因成员加入、离开或穿行而导致的群体结构扰动问题，指出群体动力学与重定位在群体机器人和虚拟智能体领域已有较多研究，但针对人形机器人群体、且符合社交规范的重定位行为关注不足。现有基于社会力的方法虽为群体行为提供了基础，但障碍物处理能力有限，环境复杂度上升时可能产生不安全行为。为此，作者提出一种新框架：以 Model Predictive Control 引导传统 Social Force 进行前瞻规划，并用 Control Barrier Functions 对行为加以约束以提升安全性。该方法旨在在多种群体形成扰动下产生更安全且具社交意识的重定位行为，并通过仿真消融实验与在线用户研究进行评估，结果显示其在复杂环境中能生成更平滑、更安全的重定位行为，同时保持社交适宜性。

## 核心内容

### 问题背景
随着社交机器人与服务机器人越来越多地共享公共交互空间，它们可能在协调任务或与人交互时形成群体。仅完成初始群体形成在动态环境中并不充分，因为当有人或其他智能体加入、离开或穿行于群体时，群体结构会被打乱。群体动力学与重定位虽在群体机器人和虚拟智能体场景中被广泛研究，但人形机器人群体中符合社交规范的重定位行为受到的关注较少。现有基于社会力的方法为群体行为提供了有用基础，但其障碍物处理能力有限，随着环境复杂度增加可能产生不安全行为。

### 方法
作者提出一种新框架，对传统 Social Force 进行调制：
- 由 Model Predictive Control（MPC）引导，实现前瞻性规划；
- 由 Control Barrier Functions（CBF）施加约束，以提升机器人群体重定位行为的安全性。

该方法的目标是在多种群体形成扰动下，产生更安全且具社交意识的群体重定位行为。

### 实验设置
论文通过仿真中的消融实验（ablation study）与在线用户研究（online user study）对方法进行评估。

### 关键结果
结果表明，所提方法能够在复杂环境中产生更平滑、更安全的重定位行为，同时保持社交适宜性。

### 结论
该框架将 Social Force 与 MPC、CBF 结合，用于人形机器人群体在障碍物环境中的社交适宜重定位，并在仿真与用户研究中验证了其在安全性与平滑性方面的优势。

## Overview

As social and service robots increasingly share interaction spaces in public, they may form groups while coordinating tasks or interacting with humans. Initial group formation alone is insufficient in dynamic settings, because it can be disrupted when a person or another agent joins, leaves, or passes through the group. Although group dynamics and repositioning have been widely studied in swarm robotics and virtual-agent settings, little attention has been given to socially appropriate repositioning behaviors in groups of humanoid robots. Existing social-force-based approaches provide a useful foundation for group behavior, but they have limited obstacle handling, and can produce unsafe behavior as environmental complexity increases. We propose a novel framework that modulates traditional Social Force, guided by Model Predictive Control (MPC) to plan ahead, bounded by Control Barrier Functions (CBF) to increase safety for robot groups repositioning behaviors. This approach aims to produce safer and socially aware group repositioning behaviors under various group formation disturbance. We evaluate the method in simulation through an ablation study and an online user study. The results show that our proposed method can produce smoother and safer repositioning behaviors in complex environments while preserving social appropriateness.

## 参考
- https://arxiv.org/abs/2611.14853
