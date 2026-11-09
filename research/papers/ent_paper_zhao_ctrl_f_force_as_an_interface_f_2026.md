---
$id: ent_paper_zhao_ctrl_f_force_as_an_interface_f_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Ctrl-F: Force as an Interface for Humanoid Loco-Manipulation'
  zh: 'Ctrl-F: Force as an Interface for Humanoid Loco-Manipulation'
  ko: 'Ctrl-F: Force as an Interface for Humanoid Loco-Manipulation'
summary:
  en: 'Humanoid motion tracking has scaled to general policies that reproduce diverse human motion, but the resulting behavior
    is in free-space: the tracker knows where the body should be, not how it should interact with the environment. Other work
    makes the object part of the objective, yet abstracts that interaction to contact or geometry, which leaves the demanding
    cases under-explored. We argue that ...'
  zh: Ctrl-F 是一个分层运动-力控制框架，由 Mengjie Zhao、Yuxin Chen、Yiyang Shao、Chuye Hong、Jiakang Chen、Koushil Sreenath、Masayoshi Tomizuka
    提出，在运动跟踪基础上引入显式力指令——即在每个指定接触部位（如手或脚）施加的三维力。该框架由统一的运动-力控制器与高层力规划器组成，前者在跟踪参考运动的同时向世界施加指令力，后者依据物体状态与本体感知在线生成力指令。在仿真与硬件实验中，Ctrl-F
    完成了需要大且持续交互力的移动操作任务，并能在负载变化时在线调整指令，而无力感知的跟踪器无法做到这一点。
  ko: 'Humanoid motion tracking has scaled to general policies that reproduce diverse human motion, but the resulting behavior
    is in free-space: the tracker knows where the body should be, not how it should interact with the environment. Other work
    makes the object part of the objective, yet abstracts that interaction to contact or geometry, which leaves the demanding
    cases under-explored. We argue that ...'
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
- humanoid_loco_manipulation
- force_control
- motion_tracking
- hierarchical_control
- force_planner
- contact_interaction
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-11-09'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-11-09). Bibliographic metadata from arXiv API (2611.05507);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2611.05507 Ctrl-F: Force as an Interface for Humanoid Loco-Manipulation'
  url: https://arxiv.org/abs/2611.05507
  date: '2026-11-03'
  accessed_at: '2026-11-09'
- id: src_002
  type: website
  title: Project page
  url: https://forcectrl.github.io/
  accessed_at: '2026-11-09'
---

## 概述

现有的人形机器人运动跟踪已能通过通用策略复现多样的人类动作，但行为局限于自由空间：跟踪器只知道身体该在哪里，并不知道该如何与环境交互。另一些工作把物体纳入目标，却将交互抽象为接触或几何，使高难度情形缺乏探索。作者认为力是连接运动模仿与物体交互的自然指令通道，它不仅能指定在哪里接触，还能指定用多大的力。为此提出 Ctrl-F 分层运动-力框架，为运动跟踪增加显式力指令，即在每个指定接触身体部位施加三维力。该框架包含统一的运动-力控制器与高层力规划器两部分，前者跟踪参考运动并向世界施加指令力，后者基于物体状态与本体感知在线发布力指令。仿真与硬件结果表明，Ctrl-F 能完成需要大且持续交互力的移动操作，并随负载变化在线调整指令，这是无力感知的跟踪器所无法达到的。

## 核心内容

### 问题背景

人形机器人运动跟踪已扩展到可复现多样人类动作的通用策略，但这类行为发生在自由空间中：跟踪器知道身体应在何处，却不知道应如何与环境交互。已有工作将物体纳入优化目标，但把交互抽象为接触或几何，导致对交互力要求苛刻的场景研究不足。作者主张，力是运动模仿与物体交互之间的自然指令通道，它既指定接触位置，也指定接触力度。

### 方法

Ctrl-F 是一个分层运动-力框架，在运动跟踪之上增加显式力指令，即在每个指定接触身体部位（如手或脚）给出一个三维力。框架包含两个层级：

- **统一运动-力控制器**：在跟踪参考运动的同时，将指令力施加到世界中。
- **高层力规划器**：根据物体状态与本体感知观测，在线生成力指令。

### 实验设置与关键结果

作者在仿真与硬件上进行了验证。Ctrl-F 能够完成需要大且持续交互力的移动操作任务，并能在负载变化时在线调整力指令，这些均超出无力感知跟踪器的能力范围。

在硬件上，Ctrl-F 展示了基于手的拖动、推动与举升，以及基于脚的踢击；在推动与踢击任务中成功操作了重达 20kg 的箱子，而无力感知基线在这些任务中失败。此外，Ctrl-F 还能在任务中途引入额外负载时进行在线适应。

### 结论

将力作为运动跟踪与物体交互之间的显式指令接口，可使 humanoid 完成高交互力的 loco-manipulation 任务，并具备对负载变化的在线适应能力。

## Overview

Humanoid motion tracking has scaled to general policies that reproduce diverse human motion, but the resulting behavior is in free-space: the tracker knows where the body should be, not how it should interact with the environment. Other work makes the object part of the objective, yet abstracts that interaction to contact or geometry, which leaves the demanding cases under-explored. We argue that force is a natural command channel between motion imitation and object interaction, one that specifies not just where to make contact but how hard. We present Ctrl-F, a hierarchical motion-force framework that augments motion tracking with an explicit force command, a 3-D force at each designated contact body such as a hand or a foot. The hierarchical framework comprises: (1) A unified motion-force controller tracks the reference motion while applying the commanded force to the world. (2) A high-level force planner that issues a force command online based on object state and proprioception observations. In simulation and on hardware, Ctrl-F completes loco-manipulation that demands large, sustained interaction force and adjusts its command online as the load changes, both out of reach of a force-blind tracker. On hardware, Ctrl-F demonstrates hand-based dragging, pushing, and lifting, as well as foot-based kicking, successfully manipulating boxes weighing up to 20kg in pushing and kicking tasks where the force-blind baseline fails, while adapting online to additional loads introduced mid-task.

## 参考
- https://arxiv.org/abs/2611.05507
- https://forcectrl.github.io/
