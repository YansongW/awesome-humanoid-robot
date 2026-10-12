---
$id: ent_paper_xu_pantact_teaching_whole_body_de_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'PanTact: Teaching Whole-Body Dexterity with a Wearable Contact Interface'
  zh: 'PanTact: Teaching Whole-Body Dexterity with a Wearable Contact Interface'
  ko: 'PanTact: Teaching Whole-Body Dexterity with a Wearable Contact Interface'
summary:
  en: Humanoid robots have many degrees of freedom and contact surfaces, yet most loco-manipulation research restricts manipulation
    to the hands and avoids other body contacts with the environment. To extend manipulation beyond the hands, we present
    PanTact, a system that learns humanoid whole-body dexterity, the capability to manipulate with any suitable body surface,
    directly from robot-free human ...
  zh: PanTact 是一套让人形机器人学习全身灵巧操作的系统，能够利用身体任意合适表面与环境接触完成任务，而不再局限于双手。该系统由 Xiaomeng Xu、Han Zhang、Shuran Song 等人提出，核心思路是把接触视为可跨本体迁移的操作信息，通过无机器人的可穿戴数据采集接口、预测全身接触目标的视觉运动策略以及接触感知的全身控制来实现。作者在
    Unitree G1 人形机器人上部署了该系统，且未加装额外的身体接触传感器。
  ko: Humanoid robots have many degrees of freedom and contact surfaces, yet most loco-manipulation research restricts manipulation
    to the hands and avoids other body contacts with the environment. To extend manipulation beyond the hands, we present
    PanTact, a system that learns humanoid whole-body dexterity, the capability to manipulate with any suitable body surface,
    directly from robot-free human ...
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
- humanoid_whole_body_manipulation
- contact_based_manipulation
- wearable_data_collection
- visuomotor_policy
- whole_body_control
- loco_manipulation
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-10-12'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-10-12). Bibliographic metadata from arXiv API (2610.12558);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2610.12558 PanTact: Teaching Whole-Body Dexterity with a Wearable Contact Interface'
  url: https://arxiv.org/abs/2610.12558
  date: '2026-10-08'
  accessed_at: '2026-10-12'
---

## 概述

现有人形机器人虽具备大量自由度和接触表面，但多数移动操作研究仍把操作限制在双手，回避身体其他部位与环境的接触。PanTact 提出以接触作为以操作为中心、可跨本体迁移的信息：接触的位置与时机规定了完成任务所需的交互，而机器人自行决定如何在自身物理约束下协调身体去实现这些交互。为达成这一目标，系统包含三部分：一套可穿戴、无需机器人的数据采集接口，在自我中心视觉与双手 UMI 夹爪之外增加全身模块化接触贴片以记录身体接触位置与状态；一个缓解自我中心观测差异并预测全身接触目标的视觉运动策略；以及若干接触感知的全身控制公式，用合适的机器人表面实现主动接触目标。作者在 Unitree G1 上部署该系统，展示了包含身体支撑、推动、扫掠与负载分担在内的全身灵巧能力。

## 核心内容

### 问题背景
人形机器人拥有众多自由度和接触表面，但大多数移动操作研究把操作局限在双手，并回避身体其他部位与环境的接触。要让人形机器人具备全身灵巧性，即用身体任意合适表面进行操作，面临的核心难题在于：如何获取并迁移这类全身接触技能。

### 核心思路
PanTact 的关键思想是把接触当作以操作为中心、可跨本体迁移的信息。接触的位置与时机界定了完成任务所需的交互，而机器人则在自身物理约束下自行决定如何协调身体来实现这些交互。

### 方法
PanTact 通过三个环节完成全身接触的采集、学习与执行：
- **可穿戴、无机器人的数据采集接口**：在自我中心视觉与双手 UMI 夹爪的基础上，增加全身模块化接触贴片，用于记录身体接触的位置与状态。
- **视觉运动策略**：缓解自我中心观测差异，并预测全身接触目标。
- **接触感知的全身控制公式**：利用合适的机器人表面实现主动接触目标。

### 实验设置
作者将 PanTact 部署在 Unitree G1 人形机器人上，且未使用额外的身体接触传感器。

### 关键结果
系统展示了全身灵巧能力，涵盖身体支撑、推动、扫掠与负载分担等任务。

### 结论
PanTact 表明，以接触为媒介可以从无机器人的人类演示中直接学习人形机器人的全身灵巧操作，并将操作能力从双手扩展到身体其他表面。项目网站为 https://pantact.github.io。

## Overview

Humanoid robots have many degrees of freedom and contact surfaces, yet most loco-manipulation research restricts manipulation to the hands and avoids other body contacts with the environment. To extend manipulation beyond the hands, we present PanTact, a system that learns humanoid whole-body dexterity, the capability to manipulate with any suitable body surface, directly from robot-free human demonstrations. Our key idea is to use contact as manipulation-centric information that transfers across embodiments. Contact locations and timing specify the interactions needed to accomplish a task, while the robot chooses how to coordinate its body to realize them within its own physical constraints. Specifically, PanTact captures, learns, and executes whole-body contact via: 1) a wearable, robot-free data collection interface that augments egocentric vision and bimanual UMI grippers with whole-body modular contact patches to record body contact locations and states; 2) a visuomotor policy that mitigates the egocentric observation gap and predicts whole-body contact goals; and 3) contact-aware whole-body control formulations that realize active contact goals using suitable robot surfaces. We deploy PanTact on a Unitree G1 humanoid without additional body contact sensors, demonstrating whole-body dexterity involving body support, pushing, sweeping, and load-sharing. Website: https://pantact.github.io

## 参考
- https://arxiv.org/abs/2610.12558
