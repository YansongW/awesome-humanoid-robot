---
$id: ent_paper_nguyen_networked_humanoid_intelligenc_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Networked Humanoid Intelligence: Communication, Coordination, Collaboration, and Social Interaction'
  zh: 'Networked Humanoid Intelligence: Communication, Coordination, Collaboration, and Social Interaction'
  ko: 'Networked Humanoid Intelligence: Communication, Coordination, Collaboration, and Social Interaction'
summary:
  en: Humanoid robots are moving from laboratory platforms toward connected fleets that share workspaces, infrastructure,
    tasks, and knowledge with other robots and humans. As deployments grow, the operation and improvement of each humanoid
    depend on information exchanged across the network. However, existing research has largely studied humanoids as individual
    systems. This survey examines networked ...
  zh: 本文是一篇综述，将人形机器人视为联网群体而非孤立系统，围绕通信、协调、协作与人类社交智能四项信息交换功能构建网络化人形智能的研究框架。作者来自相关高校团队（Loc X. Nguyen、Huy Q. Le、Ji Su Yoon、Nguyen
    H. Tran、Eui-Nam Huh、Choong Seon Hong），通过统一工厂场景串联四项功能，并按六个维度梳理文献，同时区分实体与仿真人形机器人结果和其他平台或无实体智能体结果。文章还整理了硬件、数据集与基准，区分本地风险与联网引入的风险，并提出控制感知网络、紧凑体中心消息、物理约束下的协调、网络与具身感知的知识共享、群体级社交一致性和可问责人类监督等开放问题。
  ko: Humanoid robots are moving from laboratory platforms toward connected fleets that share workspaces, infrastructure,
    tasks, and knowledge with other robots and humans. As deployments grow, the operation and improvement of each humanoid
    depend on information exchanged across the network. However, existing research has largely studied humanoids as individual
    systems. This survey examines networked ...
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
- networked_humanoid
- humanoid_robotics
- robot_coordination
- human_robot_interaction
- survey
- embodied_ai
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-11-02'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-11-02). Bibliographic metadata from arXiv API (2610.34740);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2610.34740 Networked Humanoid Intelligence: Communication, Coordination, Collaboration, and Social Interaction'
  url: https://arxiv.org/abs/2610.34740
  date: '2026-10-26'
  accessed_at: '2026-11-02'
---

## 概述

随着人形机器人从实验室平台走向共享工作空间、基础设施、任务与知识的联网群体，其运行与改进越来越依赖网络间交换的信息，但既有研究多将人形机器人作为个体系统考察。本文以通信、协调、协作以及与人交互的社交智能四项信息交换功能为线索，系统审视网络化人形智能，先建立网络化人形系统的基础，明确每项功能所回答的问题，并用一个共同的工厂场景将它们联系起来。文献梳理沿交互架构、交换信息、物理耦合、运行时间尺度、系统规模和具身形态六个维度展开，并刻意将实体与仿真人形机器人的结果同其他机器人平台或无实体智能体的结果分开，因为后者无法充分体现平衡、全身运动、接触与物理交互等人形特有约束。文章还考察硬件、数据集与基准，区分本地处理的风险与联网带来的新风险，如信息过期或不安全知识传播，最后指出控制感知网络、紧凑的体中心消息、物理落地的协调、网络与具身感知的知识共享、群体级社交一致性以及可问责的人类监督等开放问题。

## 核心内容

### 问题背景
人形机器人正从实验室平台转向联网群体，与其他机器人及人类共享工作空间、基础设施、任务和知识。部署规模扩大后，单台人形机器人的运行与持续改进都依赖于网络中交换的信息。然而现有研究大多把人形机器人当作独立系统来分析，缺乏对网络化人形智能的整体审视。本文以综述形式填补这一空白，围绕信息交换的四项功能组织讨论：通信、协调、协作，以及涉及人类交互的社交智能。

### 方法
- 首先建立网络化人形系统的基础，界定每项功能所对应的核心问题，并通过一个共同的工厂场景把四项功能串联起来，说明它们在同一部署情境下如何相互关联。
- 沿六个维度梳理文献：交互架构、交换信息、物理耦合、运行时间尺度、系统规模、具身形态。
- 在证据筛选上，将实体人形机器人与仿真人形机器人得到的结果，同基于其他机器人平台或无实体智能体的结果区分开来，原因是后者无法完整反映人形特有的平衡、全身运动、接触和物理交互约束。
- 考察支撑网络化人形智能的硬件、数据集与基准。
- 对风险进行分类：区分可在本地处理的风险与由联网引入的风险，后者包括信息过期和不安全知识的传播。

### 关键结果与结论
本文为综述性工作，未报告具体实验数值。其主要产出是上述四功能框架、六维文献分类体系、实体与仿真人形机器人同其他平台证据的区分原则，以及硬件、数据集和基准的梳理。文章进一步指出若干开放问题：
- 控制感知的网络设计；
- 紧凑的体中心消息表示；
- 物理落地的协调方法；
- 网络与具身感知的知识共享；
- 群体级社交一致性；
- 可问责的人类监督。

## Overview

Humanoid robots are moving from laboratory platforms toward connected fleets that share workspaces, infrastructure, tasks, and knowledge with other robots and humans. As deployments grow, the operation and improvement of each humanoid depend on information exchanged across the network. However, existing research has largely studied humanoids as individual systems. This survey examines networked humanoid intelligence through four functions of information exchange: communication, coordination, collaboration, and social intelligence with human interaction. We first establish the foundations of networked humanoid systems, define the question addressed by each function, and connect them through a common factory scenario. We review the literature along six dimensions: interaction architecture, exchanged information, physical coupling, operating timescale, system scale, and embodiment. We separate results obtained with physical and simulated humanoids from those based on other robotic platforms or disembodied agents, because the latter do not fully capture humanoid-specific constraints such as balance, whole-body motion, contact, and physical interaction. We examine hardware, datasets, and benchmarks, and distinguish risks handled locally from those networking introduces, such as stale information or unsafe knowledge propagation. Finally, we identify open problems in control-aware networking, compact body-centric messages, physically grounded coordination, network- and embodiment-aware knowledge sharing, fleet-level social consistency, and accountable human oversight.

## 参考
- https://arxiv.org/abs/2610.34740
