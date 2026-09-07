---
$id: ent_paper_calvert_a_system_for_fast_resilient_an_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: A System for Fast, Resilient, and Adaptable Loco-Manipulation Behaviors on Humanoid Robots
  zh: A System for Fast, Resilient, and Adaptable Loco-Manipulation Behaviors on Humanoid Robots
  ko: A System for Fast, Resilient, and Adaptable Loco-Manipulation Behaviors on Humanoid Robots
summary:
  en: There is tremendous value in humanoid robots taking on physically demanding, hazardous, and repetitive work in spaces
    built for humans. However, a useful robot for these spaces must coordinate locomotion, whole-body motion, perception,
    contact, and operator supervision. We present a robot-local, runtime-editable behavior authoring and runtime system that
    addresses these challenges. We argue that ...
  zh: 本文提出了一套面向人形机器人的本地化、运行时可编辑的行为编写与运行系统，旨在实现快速、鲁棒且适应性强的移动操作（loco-manipulation）行为。该系统由加州大学伯克利分校等机构的研究者开发，结合了以对象为中心的Affordance
    Templates、树状行为结构及运行时可编辑感知，并在Unitree H1-2和Alex机器人上完成了六种任务变体的演示验证。
  ko: There is tremendous value in humanoid robots taking on physically demanding, hazardous, and repetitive work in spaces
    built for humans. However, a useful robot for these spaces must coordinate locomotion, whole-body motion, perception,
    contact, and operator supervision. We present a robot-local, runtime-editable behavior authoring and runtime system that
    addresses these challenges. We argue that ...
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
- loco_manipulation
- behavior_authoring
- runtime_editable
- affordance_templates
- whole_body_control
- humanoid_robots
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-09-07'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-09-07). Bibliographic metadata from arXiv API (2609.01518);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: arXiv:2609.01518 A System for Fast, Resilient, and Adaptable Loco-Manipulation Behaviors on Humanoid Robots
  url: https://arxiv.org/abs/2609.01518
  date: '2026-09-01'
  accessed_at: '2026-09-07'
- id: src_002
  type: website
  title: Project page
  url: https://www.youtube.com/playlist?list=PLJK5CTyotYqsfgfnXb-09YNFeBose6uEY
  accessed_at: '2026-09-07'
---

## 概述

该系统通过将行为架构作为能力、速度和可靠性的主要推动力，解决了人形机器人在人类环境中协调运动、全身控制、感知与操作监督的挑战。其核心创新在于运行时可编辑性，允许操作员在机器人运行过程中快速创建、调整和组合行为，而无需停机重编译。系统采用对象为中心的Affordance Templates提供组织逻辑，并通过行为场景和原始场景动作实现动态感知更新。实验结果表明，该系统在推门穿越和颜色分拣任务中表现出色，且行为创建时间从数小时缩短至分钟级，与最新学习方法的性能相当。

## 核心内容

### 问题背景
人形机器人在人类建造的空间中执行体力要求高、危险且重复的任务具有巨大价值，但实现这一目标需要机器人协调多种能力，包括移动、全身运动、感知、接触管理和操作员监督。现有系统往往在行为架构上缺乏灵活性，难以快速适应新任务或环境变化。

### 方法
本文提出的行为架构包含三个关键组件：
- **对象为中心的Affordance Templates**：提供以任务对象为核心的行为组织逻辑，使机器人能够理解环境中物体的可操作属性。
- **树状行为结构**：为复杂行为提供层次化组织和执行逻辑，支持行为的模块化组合与扩展。
- **运行时可编辑感知**：通过行为场景和原始场景动作，使感知系统能够在运行过程中动态更新，适应环境变化。

操作员界面与机器人保持持续同步，支持运行时的行为编写、监控和修复。动作原语通过全身控制器执行，该控制器支持并发身体运动和行走，确保移动与操作的无缝集成。

### 实验设置与结果
系统在Unitree H1-2和Alex两款人形机器人上进行了验证，覆盖六种任务变体。关键实验结果包括：
- **推门穿越任务**：在34秒内完成，展示了系统在动态环境中的移动操作协调能力。
- **颜色分拣任务**：在人为干扰条件下，45秒内完成六个球的按颜色分拣，验证了系统的鲁棒性。
- **行为编写效率**：计时编写会话显示，从零开始创建新的移动操作行为以及改编现有行为均可在数小时内完成，体现了运行时编辑性的优势。

### 结论
与文献中的最新学习方法相比，本系统在性能上具有竞争力。研究结果表明，行为架构本身可以成为提升机器人能力、速度和可靠性的关键因素，而运行时可编辑性则为快速行为创建和适应提供了有效途径。该系统为人形机器人在真实人类环境中部署提供了实用的技术方案。

## Overview

There is tremendous value in humanoid robots taking on physically demanding, hazardous, and repetitive work in spaces built for humans. However, a useful robot for these spaces must coordinate locomotion, whole-body motion, perception, contact, and operator supervision. We present a robot-local, runtime-editable behavior authoring and runtime system that addresses these challenges. We argue that behavior architecture can be a primary enabler of capability, speed, and reliability, and that runtime editability enables fast behavior creation, adaptation, extension, and combination. Our behavior architecture combines object-centric Affordance Templates, a tree structure that provides organization and logic, and runtime-editable perception through a behavior scene and primitive scene actions. Our operator interface remains continuously synchronized to the robot for runtime authoring, monitoring, and repair. Action primitives execute through a whole-body controller that supports concurrent body motions and walking. Demonstrations of our system cover six task variants on Unitree H1-2 and Alex. We execute a push door traversal in 34 seconds and sort six balls by color in 45 seconds under human disturbance. Timed authoring sessions show scratch creation of new loco-manipulation behaviors and adaptation of existing ones in hours. Comparison against the literature finds our approach to be competitive with recent learned systems.

## 参考
- https://arxiv.org/abs/2609.01518
- https://www.youtube.com/playlist?list=PLJK5CTyotYqsfgfnXb-09YNFeBose6uEY
