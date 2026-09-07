---
$id: ent_paper_kim_establishing_a_dynamic_multimo_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Establishing a Dynamic Multimodal HRI Dataset for Engagement Analysis with a Humanoid Robot
  zh: Establishing a Dynamic Multimodal HRI Dataset for Engagement Analysis with a Humanoid Robot
  ko: Establishing a Dynamic Multimodal HRI Dataset for Engagement Analysis with a Humanoid Robot
summary:
  en: This paper presents an experimental design for constructing a multimodal dataset to analyze user engagement in human-robot
    interaction (HRI). Prior studies have mainly relied on observable behavioral cues, with limited frameworks integrating
    physiological signals. We therefore propose a structured data-collection protocol to build a multimodal dataset that includes
    wearable physiological signals, ...
  zh: 本文提出了一种构建多模态人机交互（HRI）数据集的实验设计，用于分析用户参与度。作者Buwan Kim和Wonse Jo提出了一种结构化数据采集协议，整合可穿戴生理信号、行为数据和自我报告测量，并在不同任务复杂度条件下进行实验。
  ko: This paper presents an experimental design for constructing a multimodal dataset to analyze user engagement in human-robot
    interaction (HRI). Prior studies have mainly relied on observable behavioral cues, with limited frameworks integrating
    physiological signals. We therefore propose a structured data-collection protocol to build a multimodal dataset that includes
    wearable physiological signals, ...
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
- human_robot_interaction
- multimodal_dataset
- engagement_analysis
- physiological_signals
- data_collection_protocol
- humanoid_robot
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-09-07'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-09-07). Bibliographic metadata from arXiv API (2609.03255);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: arXiv:2609.03255 Establishing a Dynamic Multimodal HRI Dataset for Engagement Analysis with a Humanoid Robot
  url: https://arxiv.org/abs/2609.03255
  date: '2026-09-03'
  accessed_at: '2026-09-07'
---

## 概述

该研究针对现有HRI参与度分析主要依赖可观察行为线索、缺乏生理信号整合框架的问题，提出了一种系统的数据采集方案。实验设计定义了不同任务复杂度水平，并同步采集穿戴式生理信号、行为数据和用户自我报告，以构建一个全面的多模态数据集。该协议旨在为后续参与度建模提供标准化数据基础。

## 核心内容

### 问题背景
在人机交互研究中，用户参与度是评估交互质量的关键指标。以往研究多依赖视频编码或问卷等可观察行为线索，但这些方法难以捕捉用户内在的生理状态变化，且缺乏统一的数据采集框架来整合多源信息。

### 方法
本文提出一个结构化数据采集协议，包含三个主要数据模态：
- **可穿戴生理信号**：通过穿戴设备记录用户生理反应（如心率、皮肤电导等），以反映交互过程中的内在状态。
- **行为数据**：记录用户与机器人交互时的动作、姿态或面部表情等可观察行为。
- **自我报告测量**：在实验后收集用户主观评价，用于标注参与度水平。

实验设计引入了**不同任务复杂度**条件，以系统性地考察任务难度对参与度的影响。该协议旨在确保数据采集的一致性和可重复性。

### 实验设置
论文重点在于实验设计而非具体实验结果，因此未提供详细实验参数或结果数据。其核心贡献在于提出一个可复用的数据采集框架，为未来研究建立标准化流程。

### 结论
该研究为HRI领域提供了一个多模态数据集构建的实验设计蓝图，填补了生理信号与行为数据整合方面的空白。通过定义任务复杂度层次和同步采集多模态数据，该协议有望支持更准确的参与度分析与预测模型开发。

## Overview

This paper presents an experimental design for constructing a multimodal dataset to analyze user engagement in human-robot interaction (HRI). Prior studies have mainly relied on observable behavioral cues, with limited frameworks integrating physiological signals. We therefore propose a structured data-collection protocol to build a multimodal dataset that includes wearable physiological signals, behavioral data, and self-report measures under different levels of task complexity defined in this experiment.

## 参考
- https://arxiv.org/abs/2609.03255
