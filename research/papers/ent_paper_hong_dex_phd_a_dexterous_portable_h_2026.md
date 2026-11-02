---
$id: ent_paper_hong_dex_phd_a_dexterous_portable_h_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'DEX-PHD: A Dexterous Portable Handheld Device for Multimodal Data Collection'
  zh: 'DEX-PHD: A Dexterous Portable Handheld Device for Multimodal Data Collection'
  ko: 'DEX-PHD: A Dexterous Portable Handheld Device for Multimodal Data Collection'
summary:
  en: Existing manipulation data collection methods typically offer either accurate robot-state acquisition through kinematic-chain-based
    teleoperation or convenient, portable operation through vision-based approaches. We present DEX-PHD, a portable handheld
    device that combines these advantages for dexterous manipulation by integrating a dexterous robot hand, continuous per-finger
    control, and ...
  zh: DEX-PHD 是一款便携式手持设备，用于采集灵巧操作的多模态数据。作者为 Jooyoung Hong、Noboru Myers、Obin Kwon、Yixian Yang 与 Joohyung Kim。该设备将灵巧机器人手、逐指连续控制与多模态记录集成于一体，可采集本体感知信息、指尖接触数据与腕部相机视频，操作者通过关节级映射直接控制机器人手，且无缆设计支持在多种环境中采集数据。
  ko: Existing manipulation data collection methods typically offer either accurate robot-state acquisition through kinematic-chain-based
    teleoperation or convenient, portable operation through vision-based approaches. We present DEX-PHD, a portable handheld
    device that combines these advantages for dexterous manipulation by integrating a dexterous robot hand, continuous per-finger
    control, and ...
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
- dexterous_manipulation
- data_collection
- handheld_device
- multimodal_sensing
- humanoid_robot
- open_loop_replay
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-11-02'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-11-02). Bibliographic metadata from arXiv API (2610.35462);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2610.35462 DEX-PHD: A Dexterous Portable Handheld Device for Multimodal Data Collection'
  url: https://arxiv.org/abs/2610.35462
  date: '2026-10-26'
  accessed_at: '2026-11-02'
---

## 概述

现有操作数据采集方法通常只能二选一：基于运动链的遥操作能获得准确的机器人状态，而基于视觉的方法则便于携带、操作方便。DEX-PHD 试图把这两类优势结合起来，它是一台便携式手持设备，集成了灵巧机器人手、逐指连续控制和多模态记录能力。系统在操作者通过关节级映射直接控制机器人手的同时，记录本体感知信息、指尖接触数据和腕部相机视频，无缆设计使其能够在多种环境中使用。作者在需要多指协同的富接触任务上演示了该设备，并将采集到的示范通过开环回放在实体人形机器人上部署，结果显示开环回放保留了手指运动的主要时间模式以及与任务相关的接触。据此，DEX-PHD 为便携式、多模态的灵巧操作数据采集提供了一个实用平台。

## 核心内容

### 问题背景

灵巧操作的数据采集长期面临取舍：基于运动链的遥操作能够获得准确的机器人状态，但设备通常不便携；基于视觉的方法操作方便、便于携带，却难以直接获得精确的机器人状态。DEX-PHD 的目标是在同一套便携设备中兼顾二者。

### 方法

DEX-PHD 是一台便携式手持设备，核心设计包括三部分：

- 集成灵巧机器人手，操作者通过关节级映射直接控制机器人手，实现逐指连续控制；
- 多模态记录，同步采集本体感知信息、指尖接触数据与腕部相机视频；
- 无缆（untethered）设计，使数据采集可以跨多种环境进行。

### 实验设置

作者在需要多指协同操作的富接触任务上对 DEX-PHD 进行了演示，并将采集到的示范以开环回放方式部署到实体人形机器人上。

### 关键结果

开环回放的结果表明，手指运动的主要时间模式以及任务相关的接触得以保留。

### 结论

DEX-PHD 为便携式、多模态的灵巧操作数据采集提供了一个实用平台。

## Overview

Existing manipulation data collection methods typically offer either accurate robot-state acquisition through kinematic-chain-based teleoperation or convenient, portable operation through vision-based approaches. We present DEX-PHD, a portable handheld device that combines these advantages for dexterous manipulation by integrating a dexterous robot hand, continuous per-finger control, and multimodal logging. The system records proprioceptive information, fingertip contact data, and wrist-camera video, while the operator directly controls the robot hand through joint-level mapping. Its untethered design enables data collection across diverse environments. We demonstrate DEX-PHD on contact-rich tasks requiring coordinated multi-finger manipulation and deploy the collected demonstrations through open-loop replay on a physical humanoid robot. The results show that open-loop replay preserves the main temporal patterns of finger motion and task-relevant contact. Therefore, DEX-PHD provides a practical platform for portable, multimodal dexterous manipulation data collection.

## 参考
- https://arxiv.org/abs/2610.35462
