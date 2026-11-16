---
$id: ent_paper_cai_ila_a_transferable_interface_l_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ILA: A Transferable Interface-Level Adapter for Compliant Humanoid Motion Tracking'
  zh: 'ILA: A Transferable Interface-Level Adapter for Compliant Humanoid Motion Tracking'
  ko: 'ILA: A Transferable Interface-Level Adapter for Compliant Humanoid Motion Tracking'
summary:
  en: Humanoid motion tracking is fundamental to reproducing human motions on humanoid robots and serves as an important tool
    for teleoperation and motion data collection. However, directly tracking reference motions can be unsafe in constrained
    environments or during physical human--robot interaction, motivating the need for compliant motion tracking. We present
    ILA, an Interface-Level Adapter for ...
  zh: ILA 是一种用于实现柔顺人形机器人运动跟踪的接口级适配器，由 ZhuoChang Cai、Zihao Yan、Jinxuan Zhu、Yanjie Li 与 Hao Xiong 提出。它无需专用交互传感器，通过从机器人的观测历史中调整运动参考，使机器人能够响应物理引导，同时保留预训练运动跟踪器的原有能力。ILA
    完全在仿真中训练，可直接插入不同的预训练跟踪器而无需重新训练，在三个跟踪器上将引导目标误差降低 63.6–75.4%。
  ko: Humanoid motion tracking is fundamental to reproducing human motions on humanoid robots and serves as an important tool
    for teleoperation and motion data collection. However, directly tracking reference motions can be unsafe in constrained
    environments or during physical human--robot interaction, motivating the need for compliant motion tracking. We present
    ILA, an Interface-Level Adapter for ...
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
- humanoid_motion_tracking
- compliant_control
- interface_adapter
- physical_human_robot_interaction
- sensor_free
- motion_retargeting
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-11-16'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-11-16). Bibliographic metadata from arXiv API (2611.14985);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2611.14985 ILA: A Transferable Interface-Level Adapter for Compliant Humanoid Motion Tracking'
  url: https://arxiv.org/abs/2611.14985
  date: '2026-11-11'
  accessed_at: '2026-11-16'
---

## 概述

人形机器人运动跟踪是复现人类动作、支撑遥操作与运动数据采集的基础能力，但在受限环境或人机物理交互中直接跟踪参考运动可能不安全，因此需要柔顺的运动跟踪。作者提出 ILA，一种接口级适配器，它不依赖专用交互传感器，而是根据机器人的观测历史对运动参考进行修正，使机器人能够响应人类的物理引导，同时保持预训练跟踪器的原有性能。作为接口级模块，ILA 可直接接入不同的预训练运动跟踪器，适配器与跟踪策略均无需重新训练。ILA 完全在仿真中训练，用于预测物理交互引起的参考修正。作者用三个运动跟踪器进行评估，相比原始策略将引导目标误差降低了 63.6–75.4%，匹配的仿真研究与硬件实验进一步表明其在提升人类引导响应性的同时保持了标称运动跟踪性能。

## 核心内容

### 问题背景

人形机器人运动跟踪用于在机器人上复现人类动作，是遥操作与运动数据采集的重要工具。然而，在受限环境中或人机物理交互过程中，直接跟踪参考运动可能不安全，这促使研究者关注柔顺运动跟踪。现有预训练运动跟踪器通常不具备柔顺响应能力，而引入专用交互传感器又会增加硬件负担。

### 方法

- 提出 ILA（Interface-Level Adapter），一种接口级适配器，用于实现柔顺的人形机器人运动跟踪，且不需要专用交互传感器。
- ILA 从机器人的观测历史中调整运动参考，使机器人能够响应物理引导，同时保留预训练运动跟踪器的能力。
- 作为接口级模块，ILA 可直接插入不同的预训练运动跟踪器，适配器与跟踪策略均无需重新训练。
- ILA 完全在仿真中训练，学习预测由物理交互引起的参考修正。

### 实验设置

作者使用三个不同的人形机器人运动跟踪器对 ILA 进行评估，并开展了匹配的仿真研究与硬件实验。

### 关键结果

- 与各跟踪器的原始策略相比，ILA 将引导目标误差降低了 63.6–75.4%。
- 匹配的仿真研究与硬件实验表明，ILA 在提升机器人对人类引导响应性的同时，保持了标称运动跟踪性能。

### 结论

结果表明，柔顺引导可以作为预训练人形机器人运动跟踪器的一种可复用、无传感器的扩展方式。

## Overview

Humanoid motion tracking is fundamental to reproducing human motions on humanoid robots and serves as an important tool for teleoperation and motion data collection. However, directly tracking reference motions can be unsafe in constrained environments or during physical human--robot interaction, motivating the need for compliant motion tracking. We present ILA, an Interface-Level Adapter for compliant humanoid motion tracking without dedicated interaction sensors. ILA adapts motion references from the robot's observation history, allowing the robot to respond to physical guidance while preserving the capabilities of a pretrained motion tracker. As an interface-level module, ILA can be directly plugged into different pretrained motion trackers without retraining either the adapter or the tracking policies. ILA is trained entirely in simulation to predict reference corrections induced by physical interaction. We evaluate ILA with three humanoid motion trackers and achieve a 63.6--75.4% reduction in guidance-target error compared with their original policies. Matched simulation studies and hardware experiments further show that ILA improves responsiveness to human guidance while preserving nominal motion-tracking performance. These results demonstrate compliant guidance as a reusable, sensor-free extension to pretrained humanoid motion trackers.

## 参考
- https://arxiv.org/abs/2611.14985
