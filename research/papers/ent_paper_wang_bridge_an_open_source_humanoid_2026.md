---
$id: ent_paper_wang_bridge_an_open_source_humanoid_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'BRIDGE: An Open-Source Humanoid Platform via Morphology-Control Co-Design for Physical AI'
  zh: 'BRIDGE: An Open-Source Humanoid Platform via Morphology-Control Co-Design for Physical AI'
  ko: 'BRIDGE: An Open-Source Humanoid Platform via Morphology-Control Co-Design for Physical AI'
summary:
  en: Developing humanoid robots capable of leveraging human behavioral data is essential for general-purpose embodiment,
    yet conventional development remains bottlenecked by a decoupled paradigm that isolates hardware design from whole-body
    control. This approach leads to suboptimal systems that compromise human-like fluidity and agility. To bridge this gap,
    we introduce a data-driven ...
  zh: BRIDGE 是一个通过形态-控制协同设计框架开发的开源人形机器人平台，由 Jianren Wang 等人提出，旨在利用人类行为数据实现通用具身智能。该框架引入新指标联合优化运动学重定向保真度和动态跟踪性能，最终实现 88cm 高的
    Bridge 平台，在运动保真度和动态性能上超越基线人形机器人（Bumi、K1 和 Toddlerbot）。
  ko: Developing humanoid robots capable of leveraging human behavioral data is essential for general-purpose embodiment,
    yet conventional development remains bottlenecked by a decoupled paradigm that isolates hardware design from whole-body
    control. This approach leads to suboptimal systems that compromise human-like fluidity and agility. To bridge this gap,
    we introduce a data-driven ...
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
- morphology_control_co_design
- whole_body_control
- open_source_platform
- motion_fidelity
- dynamic_maneuvers
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-09-07'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-09-07). Bibliographic metadata from arXiv API (2609.03497);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2609.03497 BRIDGE: An Open-Source Humanoid Platform via Morphology-Control Co-Design for Physical AI'
  url: https://arxiv.org/abs/2609.03497
  date: '2026-09-03'
  accessed_at: '2026-09-07'
---

## 概述

传统人形机器人开发将硬件设计与全身控制分离，导致系统无法实现类人的流畅性和敏捷性。为此，作者提出数据驱动的形态-控制协同设计框架，通过新指标量化形态保真度，该指标同时考虑运动学重定向到人类运动的保真度和动态跟踪性能。框架在多个指标上达到最先进水平，并实现为开源平台 Bridge，附带控制策略，展示出在基础运动、鲁棒平衡和高动态操作上的卓越性能。

## 核心内容

### 问题背景
人形机器人要通用化，需利用人类行为数据，但传统开发采用硬件设计与全身控制解耦的范式，导致系统次优，缺乏类人流畅性和敏捷性。这种分离限制了机器人适应复杂动态任务的能力。

### 方法
- 提出数据驱动的形态-控制协同设计框架，联合优化人形形态以实现类人运动。
- 引入新指标，该指标联合考虑两个关键方面：
  - 运动学重定向保真度：衡量机器人运动与人类运动的重定向匹配程度。
  - 动态跟踪性能：评估机器人执行动态动作时的跟踪精度。
- 框架通过协同设计，使形态和控制策略相互适配，提升整体性能。

### 实验设置与结果
- 与基线人形机器人（Bumi、K1 和 Toddlerbot）进行比较，评估所有指标。
- 框架在所有指标上均达到最先进（SOTA）性能，优于基线系统。
- 最终实现为 Bridge 平台，高 88cm，开源发布，并附带控制策略。
- 实验表明，Bridge 能高保真地捕捉人类运动数据，在基础运动、鲁棒平衡和高动态操作中表现出色。

### 结论
Bridge 展示了形态-控制协同设计的有效性，为通用人形机器人提供开源平台，支持人类行为数据利用，推动物理 AI 发展。视频和开源材料可在项目网站获取。

## Overview

Developing humanoid robots capable of leveraging human behavioral data is essential for general-purpose embodiment, yet conventional development remains bottlenecked by a decoupled paradigm that isolates hardware design from whole-body control. This approach leads to suboptimal systems that compromise human-like fluidity and agility. To bridge this gap, we introduce a data-driven morphology-control co-design framework that optimizes humanoid morphology for human-like movement. To quantify morphological fidelity, we also introduce a novel metric that jointly considers kinematic retargeting fidelity to human motion and dynamic tracking performance. Our framework achieves state-of-the-art (SOTA) performance across all metrics compared to baseline humanoids (Bumi, K1, and Toddlerbot). Finally, we realize this design in Bridge, an open-source, 88cm-tall humanoid platform released alongside its control policy. We demonstrate that Bridge captures human motion data with superior fidelity, exhibiting exceptional performance across foundational locomotion, robust balance, and highly dynamic maneuvers. Videos and open-source materials: https://sites.google.com/view/bridgerobot.

## 参考
- https://arxiv.org/abs/2609.03497
