---
$id: ent_paper_yu_mate_multi_agent_virtual_teleo_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'MATE: Multi-Agent Virtual Teleoperation Platform for Humanoid Collaboration Data Collection'
  zh: 'MATE: Multi-Agent Virtual Teleoperation Platform for Humanoid Collaboration Data Collection'
  ko: 'MATE: Multi-Agent Virtual Teleoperation Platform for Humanoid Collaboration Data Collection'
summary:
  en: Humanoid robots require diverse embodied experiences to acquire complex loco-manipulation and collaborative skills.
    However, existing humanoid data pipelines primarily focus on individual agents, while physical multi-robot collaboration
    remains difficult to scale due to costly hardware, dedicated spaces, and repeated resets. In this work, we introduce MATE,
    a Multi-Agent virtual TEleoperation ...
  zh: MATE 是一个面向人形机器人协作数据采集的多智能体虚拟遥操作平台，由 Yichuan Yu、Youzhuo Wang、Yiming Ren、Di Feng 等作者提出，允许多名异地操作者同时在共享物理环境中控制全身人形机器人。该工作构建了包含
    24.1 小时协调行为、2,500 个联合 episode 与五类长时程任务的多机协作数据集，并提出 EAIS 执行对齐交互采样策略以提升示范学习效果。实验表明该平台可高效采集数据、支持策略学习，并实现从虚拟示范到物理人形机器人的零样本迁移。
  ko: Humanoid robots require diverse embodied experiences to acquire complex loco-manipulation and collaborative skills.
    However, existing humanoid data pipelines primarily focus on individual agents, while physical multi-robot collaboration
    remains difficult to scale due to costly hardware, dedicated spaces, and repeated resets. In this work, we introduce MATE,
    a Multi-Agent virtual TEleoperation ...
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
- humanoid_collaboration
- teleoperation
- multi_agent_systems
- data_collection
- imitation_learning
- sim_to_real_transfer
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-09-28'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-09-28). Bibliographic metadata from arXiv API (2609.26520);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2609.26520 MATE: Multi-Agent Virtual Teleoperation Platform for Humanoid Collaboration Data Collection'
  url: https://arxiv.org/abs/2609.26520
  date: '2026-09-22'
  accessed_at: '2026-09-28'
---

## 概述

人形机器人要掌握复杂的移动操作与协作技能，需要多样化的具身经验，但现有数据管线多面向单智能体，物理多机协作又受硬件成本、专用场地与反复重置的限制而难以规模化。为此，作者提出 MATE，一个多智能体虚拟遥操作平台，让分布在不同地点的多名操作者同时操控共享物理环境中的全身人形机器人，在无需多台实体机器人与同地操作的前提下保留人形机器人、物体与环境之间物理耦合的交互。基于 MATE，作者构建了多机协作数据集，覆盖物体交接、接力配送、环境交互与协同搬运等五类长时程任务，共 2,500 个联合 episode、24.1 小时协调行为。为更好地从这些富含交互的示范中学习，作者提出 EAIS 执行对齐交互采样策略，在执行对齐的前缀内计算采样信号，优先关注推进任务与交互关键的行为。作者用代表性模仿学习与视觉-语言-动作策略在多种协作任务上评估 MATE，结果显示数据采集高效、策略学习有效，并能从虚拟示范零样本迁移到物理人形机器人，无需真实世界微调。

## 核心内容

### 问题背景
人形机器人获取复杂移动操作与协作技能依赖多样化的具身经验。现有的人形机器人数据管线主要面向单个智能体，而物理层面的多机器人协作因硬件昂贵、需要专用空间以及反复重置而难以规模化。

### 方法
作者提出 MATE，一个多智能体虚拟遥操作（Multi-Agent virtual TEleoperation）平台，用于人形机器人协作数据采集。其核心特点是：
- 支持多名地理上分布的操作者同时控制共享物理环境中的全身人形机器人；
- 无需多台物理机器人，也无需操作者同地作业；
- 同时保留人形机器人、物体与环境之间物理耦合的交互。

在数据利用方面，作者提出 EAIS（Execution-Aligned Interaction Sampling）策略，在执行对齐的前缀内计算采样信号，并优先考虑推进任务进展与交互关键的行为，以改善对富含交互示范的学习。

### 实验设置
- 数据：基于 MATE 构建的多人形机器人协作数据集，包含 2,500 个联合 episode、24.1 小时的协调行为，覆盖五类长时程任务，包括物体交接（object handover）、接力配送（relay delivery）、环境交互（environment interaction）与协同搬运（cooperative transport）。
- 策略：使用代表性的模仿学习与视觉-语言-动作（vision-language-action）策略，在多种协作任务上进行评估。

### 关键结果
实验表明：
- 数据采集高效；
- 策略学习有效；
- 可实现从虚拟示范到物理人形机器人的零样本迁移，且无需真实世界微调。

### 结论
MATE 通过虚拟多智能体遥操作绕开了物理多机协作在硬件、场地与重置上的瓶颈，同时保留物理耦合交互，为多机协作数据采集与策略学习提供了可行路径，并展现出向真实人形机器人零样本迁移的能力。项目主页：https://yerik-yu.github.io/MATE/

## Overview

Humanoid robots require diverse embodied experiences to acquire complex loco-manipulation and collaborative skills. However, existing humanoid data pipelines primarily focus on individual agents, while physical multi-robot collaboration remains difficult to scale due to costly hardware, dedicated spaces, and repeated resets. In this work, we introduce MATE, a Multi-Agent virtual TEleoperation platform for humanoid collaboration data collection that enables multiple geographically distributed operators to simultaneously control whole-body humanoids in a shared physics-based environment. MATE removes the need for multiple physical robots and co-located operation while preserving physically coupled interactions among humanoids, objects, and environments. Using MATE, we construct a multi-humanoid collaboration dataset comprising 24.1 hours of coordinated behavior across 2,500 joint episodes and five long-horizon tasks, including object handover, relay delivery, environment interaction, and cooperative transport. To improve learning from these interaction-rich demonstrations, we introduce EAIS, an Execution-Aligned Interaction Sampling strategy that computes sampling signals within an execution-aligned prefix and prioritizes task-progressing and interaction-critical behaviors. We evaluate MATE with representative imitation learning and vision-language-action policies across diverse collaboration tasks. Experiments demonstrate efficient data collection, effective policy learning, and zero-shot transfer from virtual demonstrations to a physical humanoid without real-world fine-tuning. Project page: https://yerik-yu.github.io/MATE/

## 参考
- https://arxiv.org/abs/2609.26520
