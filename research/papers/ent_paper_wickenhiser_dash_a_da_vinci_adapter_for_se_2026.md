---
$id: ent_paper_wickenhiser_dash_a_da_vinci_adapter_for_se_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'DASH: A da Vinci Adapter for Serial-link and Humanoid Robots as an Accessible Platform for Surgical Robotics Research'
  zh: 'DASH: A da Vinci Adapter for Serial-link and Humanoid Robots as an Accessible Platform for Surgical Robotics Research'
  ko: 'DASH: A da Vinci Adapter for Serial-link and Humanoid Robots as an Accessible Platform for Surgical Robotics Research'
summary:
  en: Robotic minimally invasive surgery offers well-documented clinical benefits, but the cost and infrastructure requirements
    of purpose-built platforms limit access in rural and lower-resourced facilities. Recent work has teleoperated general-purpose
    robots for laparoscopic tasks and in vivo procedures, but relied on handheld instruments coupled through passive linkages
    rather than native robotic ...
  zh: DASH 是一种 da Vinci 器械适配器，可将 da Vinci Classic 与 Xi 手术器械安装到通用串行链机器人及人形机器人平台上，由 Sara Wickenhiser、Junrong Zhou、Zekai Liang、Lizzie
    Peiros 与 Michael C. Yip 提出。该适配器无需改动器械本身，可兼容多种负载能力的机器人平台，并通过无线方式识别插入的器械以加载对应的运动学与耦合矩阵。遥操作实验验证了 DASH 的有效性及其为手术机器人研究提供可及平台的价值。
  ko: Robotic minimally invasive surgery offers well-documented clinical benefits, but the cost and infrastructure requirements
    of purpose-built platforms limit access in rural and lower-resourced facilities. Recent work has teleoperated general-purpose
    robots for laparoscopic tasks and in vivo procedures, but relied on handheld instruments coupled through passive linkages
    rather than native robotic ...
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
- surgical_robotics
- da_vinci_instruments
- robot_adapter
- teleoperation
- humanoid_robots
- minimally_invasive_surgery
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-10-12'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-10-12). Bibliographic metadata from arXiv API (2610.05792);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2610.05792 DASH: A da Vinci Adapter for Serial-link and Humanoid Robots as an Accessible Platform for Surgical
    Robotics Research'
  url: https://arxiv.org/abs/2610.05792
  date: '2026-10-05'
  accessed_at: '2026-10-12'
---

## 概述

机器人微创手术具有明确的临床收益，但专用平台的高成本与基础设施要求限制了其在农村和资源匮乏场景中的可及性。已有工作尝试用通用机器人遥操作完成腹腔镜任务与活体操作，但依赖手持器械通过被动连杆耦合，而非机器人原生驱动。DASH 转而将 da Vinci Classic 与 Xi 器械适配到可融入临床工作流的通用机器人上，包含两类适配器，且无需对器械本身做任何修改。每个适配器可适配多种负载能力的机器人平台，能够接合器械的原生锁扣，并无线识别所插入的器械，从而加载器械专属的运动学与耦合矩阵。遥操作实验表明 DASH 有效，并有助于让更多研究者获得手术机器人平台的研究入口。

## 核心内容

### 问题背景
机器人微创手术的临床优势已有充分记录，但专用平台在成本与基础设施上的门槛，使农村及资源较少的手术机构难以获得相关能力。近期研究已尝试用通用机器人遥操作完成腹腔镜任务乃至活体操作，但这些方案依赖手持器械并通过被动连杆耦合，未使用机器人原生的驱动方式。

### 方法
作者提出 DASH（da Vinci Adapter for Serial-link and Humanoid），即面向串行链与人形平台的 da Vinci 适配器，将 da Vinci Classic 与 Xi 器械适配到可整合进临床工作流的通用机器人上。其设计要点包括：
- 包含两类适配器，且无需对器械本身进行任何修改；
- 每个适配器可兼容多种负载能力的机器人平台；
- 能够接合器械的原生锁扣；
- 可无线识别插入的器械，据此加载器械专属的运动学与耦合矩阵。

### 实验与结果
通过遥操作实验验证了 DASH 的有效性，并展示了其在让研究者更便捷地使用手术机器人平台方面的价值。摘要未给出具体任务数量、精度指标或对比基线等定量结果。

### 结论
DASH 以不改动器械的方式，把 da Vinci 器械接入通用串行链与人形机器人平台，为手术机器人研究提供了一种更易获得的平台路径。

## Overview

Robotic minimally invasive surgery offers well-documented clinical benefits, but the cost and infrastructure requirements of purpose-built platforms limit access in rural and lower-resourced facilities. Recent work has teleoperated general-purpose robots for laparoscopic tasks and in vivo procedures, but relied on handheld instruments coupled through passive linkages rather than native robotic actuation. Instead, we adapt da Vinci Classic and Xi instruments onto general-purpose robots that can integrate in clinical workflows. We present DASH, a da Vinci Adapter for Serial-link and Humanoid platforms, consisting of two types of adapters that require no modification to the instruments themselves. Each adapter is compatible with many robotic platform load capacities, engages the instrument's native latch, and wirelessly identifies inserted tools to load instrument-specific kinematics and coupling matrices. Teleoperated experiments demonstrate the efficacy of DASH and its benefits for enabling research access to surgical robotic platforms.

## 参考
- https://arxiv.org/abs/2610.05792
