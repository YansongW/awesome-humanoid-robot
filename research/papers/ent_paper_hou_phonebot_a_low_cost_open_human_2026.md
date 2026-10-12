---
$id: ent_paper_hou_phonebot_a_low_cost_open_human_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'PhoneBot: A Low-Cost Open Humanoid Robot Platform Reusing Smartphones'
  zh: 'PhoneBot: A Low-Cost Open Humanoid Robot Platform Reusing Smartphones'
  ko: 'PhoneBot: A Low-Cost Open Humanoid Robot Platform Reusing Smartphones'
summary:
  en: The adoption of humanoid robots in education and research remains limited by high hardware costs, complex sensing systems,
    and substantial computational requirements. This paper presents PhoneBot, a low-cost, open-source humanoid robot platform
    that repurposes commodity smartphones as its primary sensing and computing unit. By using a smartphone's integrated inertial
    measurement unit (IMU), ...
  zh: PhoneBot 是一个低成本、开源的人形机器人平台，由 Ruochen Hou、Quanyou Wang、Daniel Koh 和 Dennis W. Hong 提出，其核心思路是把消费级智能手机复用为机器人的主要感知与计算单元。该平台采用模块化下半身结构，由
    13 个低成本执行器驱动，躯干搭载智能手机以支持感知、控制计算与用户交互，并实现了稳定行走、视觉跟随、对话交互、拍摄和移动远程临场等功能。
  ko: The adoption of humanoid robots in education and research remains limited by high hardware costs, complex sensing systems,
    and substantial computational requirements. This paper presents PhoneBot, a low-cost, open-source humanoid robot platform
    that repurposes commodity smartphones as its primary sensing and computing unit. By using a smartphone's integrated inertial
    measurement unit (IMU), ...
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
- humanoid_robot
- low_cost_platform
- open_source
- smartphone_reuse
- mobile_telepresence
- vision_based_following
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-10-12'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-10-12). Bibliographic metadata from arXiv API (2610.08737);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2610.08737 PhoneBot: A Low-Cost Open Humanoid Robot Platform Reusing Smartphones'
  url: https://arxiv.org/abs/2610.08737
  date: '2026-10-06'
  accessed_at: '2026-10-12'
---

## 概述

PhoneBot 针对人形机器人在教育与研究中因硬件成本高、感知系统复杂、算力需求大而难以普及的问题，提出了一种低成本、开源的人形机器人平台。它把普通智能手机作为核心的感知与计算单元，利用手机内置的 IMU、摄像头、无线连接和板载处理能力，从而降低硬件成本并简化系统架构。机器人本体由模块化下半身结构与躯干上的智能手机组成，下半身由 13 个低成本执行器驱动。作者介绍了其机械设计、软件架构与实时通信框架，用以支撑稳定行走以及基于视觉的人形跟随、对话交互、拍摄和移动远程临场等能力。实验评估表明该平台能够可靠行走、进行感知驱动的交互，并可直接使用市售消费级智能手机完成部署，其硬件与软件设计完全开源。

## 核心内容

### 问题背景
人形机器人在教育和研究领域的普及受到多重限制：硬件成本高昂、感知系统复杂，以及对算力的较高要求。PhoneBot 试图通过复用消费级智能手机来缓解这些问题。

### 方法
- 核心思路：将普通智能手机作为机器人的主要感知与计算单元。
- 感知与计算来源：利用智能手机集成的 IMU、摄像头、无线连接以及板载处理能力。
- 结构设计：采用模块化下半身结构，由 13 个低成本执行器驱动；躯干安装智能手机，用于支持感知、控制计算和用户交互。
- 系统组成：论文描述了支撑稳定行走的机械设计、软件架构与实时通信框架。

### 功能与能力
平台支持稳定行走，并具备以下能力：
- 基于视觉的人形跟随
- 对话交互
- 拍摄
- 移动远程临场

### 实验与结果
实验评估显示，PhoneBot 能够实现可靠行走与感知驱动的交互，并且可以直接使用市售消费级智能手机完成部署。

### 结论
PhoneBot 的硬件与软件设计完全开源，为教育、研究和快速原型开发提供了一个低成本、可复现的平台。更多细节见 https://phonebot.dev。

## Overview

The adoption of humanoid robots in education and research remains limited by high hardware costs, complex sensing systems, and substantial computational requirements. This paper presents PhoneBot, a low-cost, open-source humanoid robot platform that repurposes commodity smartphones as its primary sensing and computing unit. By using a smartphone's integrated inertial measurement unit (IMU), camera, wireless connectivity, and onboard processing capabilities, PhoneBot reduces hardware costs and simplifies the system architecture. The robot combines a modular lower-body structure driven by 13 low-cost actuators with a torso-mounted smartphone that supports perception, control computation, and user interaction. We describe the mechanical design, software architecture, and real-time communication framework that support stable locomotion and capabilities including vision-based human following, conversational interaction, filming, and mobile telepresence. Experimental evaluations demonstrate reliable walking, perception-driven interaction, and straightforward deployment using off-the-shelf consumer smartphones. With fully open-source hardware and software designs, PhoneBot provides an affordable, reproducible platform for education, research, and rapid prototyping. More details are available at https://phonebot.dev.

## 参考
- https://arxiv.org/abs/2610.08737
