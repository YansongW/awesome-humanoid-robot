---
$id: ent_paper_pan_ironmind_scaling_humanoid_dext_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'IronMind: Scaling Humanoid Dexterous Manipulation via Camera-Space Ego-Centric Pretraining'
  zh: 'IronMind: Scaling Humanoid Dexterous Manipulation via Camera-Space Ego-Centric Pretraining'
  ko: 'IronMind: Scaling Humanoid Dexterous Manipulation via Camera-Space Ego-Centric Pretraining'
summary:
  en: 'Egocentric human video offers a scalable data source for dexterous manipulation, yet using it to train humanoid robots
    presents two challenges: (1) an embodiment gap, as human hands differ structurally from robot end-effectors and low-cost
    egocentric recordings lack the torso kinematics required by conventional retargeting; and (2) heterogeneous data quality,
    including noisy hand-pose tracking ...'
  zh: IronMind 是一种视觉-语言-动作（VLA）模型，由 Huimin Pan、Yufan Ren、Kunpeng Song 等人提出，利用第一视角人类视频与异构机器人数据为人形机器人灵巧操作预训练策略。其核心是采用相机空间动作表示绕开显式身体重定向，从而跨越人类手与机器人末端执行器之间的具身差异。预训练数据规模从
    250 小时扩展到 10,000 小时时，验证损失近似呈对数线性下降；10,000 小时模型在六项挑战性真机任务上取得 55.0% 成功率，远高于 5,000 小时以内各预算的至多 11.7% 以及无预训练的 5.0%。
  ko: 'Egocentric human video offers a scalable data source for dexterous manipulation, yet using it to train humanoid robots
    presents two challenges: (1) an embodiment gap, as human hands differ structurally from robot end-effectors and low-cost
    egocentric recordings lack the torso kinematics required by conventional retargeting; and (2) heterogeneous data quality,
    including noisy hand-pose tracking ...'
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
- humanoid_manipulation
- vision_language_action
- egocentric_video
- camera_space_action
- dexterous_manipulation
- pretraining_scaling
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-10-05'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-10-05). Bibliographic metadata from arXiv API (2609.39403);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2609.39403 IronMind: Scaling Humanoid Dexterous Manipulation via Camera-Space Ego-Centric Pretraining'
  url: https://arxiv.org/abs/2609.39403
  date: '2026-09-30'
  accessed_at: '2026-10-05'
- id: src_002
  type: website
  title: Project page
  url: https://xpeng-robotics.github.io/ironmind/
  accessed_at: '2026-10-05'
---

## 概述

第一视角人类视频为灵巧操作提供了可扩展的数据来源，但用于训练人形机器人时面临两重障碍：人类手与机器人末端执行器结构不同带来的具身差异，以及低成本第一视角录制缺少传统重定向所需的上肢运动学信息；同时数据质量参差不齐，手部姿态跟踪存在噪声、文本标注对齐较弱。为此，作者提出 IronMind，一种视觉-语言-动作模型，用第一视角人类视频与异构机器人数据预训练人形灵巧操作策略。该方法不做显式身体重定向，而是采用相机空间动作表示——即第一视角视频的原生参考空间——并在语义上对齐机器人与人类的动作维度。实验显示，在 250 至 10,000 小时的预训练预算范围内，验证损失随数据规模近似对数线性下降；更大的预训练预算还能在后期训练后提升分布外真机操作表现。在相同预训练预算下，相机空间动作表示也优于躯干坐标系基线。

## 核心内容

### 问题背景
第一视角人类视频是可扩展的灵巧操作数据来源，但直接用于训练人形机器人存在两个难题。其一是具身差异：人类手在结构上不同于机器人末端执行器，且低成本第一视角录制缺乏传统重定向方法所需的上肢运动学信息。其二是数据质量异构：手部姿态跟踪带有噪声，文本标注与动作的对齐也较弱。

### 方法
作者提出 IronMind，一种视觉-语言-动作（VLA）模型，使用第一视角人类视频与异构机器人数据，为人形机器人灵巧操作预训练策略。为跨越具身差异，IronMind 不做显式身体重定向，而是采用相机空间动作表示——这是第一视角视频的原生参考空间——并在语义层面对齐机器人与人类的动作维度。

### 实验设置与关键结果
- 预训练预算覆盖 250 至 10,000 小时；在此范围内，验证损失随数据规模近似呈对数线性下降。
- 更大的预训练预算在后期训练后带来更好的分布外真机操作表现。
- 在六项挑战性任务上（涉及未见过的物体、可供性与推理提示），10,000 小时模型达到 55.0% 成功率；而 5,000 小时及以下的所有预训练预算至多为 11.7%，无预训练时为 5.0%。
- 在相同预训练预算下，相机空间动作表示优于躯干坐标系基线。

### 结论
上述结果表明，基于相机空间动作表示、在大规模人类第一视角数据上进行预训练，可作为人形机器人操作的可扩展基础。

## Overview

Egocentric human video offers a scalable data source for dexterous manipulation, yet using it to train humanoid robots presents two challenges: (1) an embodiment gap, as human hands differ structurally from robot end-effectors and low-cost egocentric recordings lack the torso kinematics required by conventional retargeting; and (2) heterogeneous data quality, including noisy hand-pose tracking and weakly aligned text annotations. We introduce IronMind, a vision-language-action (VLA) model that uses egocentric human video and heterogeneous robot data to pretrain policies for humanoid dexterous manipulation. To bridge the embodiment gap, IronMind bypasses explicit body-retargeting by using a camera-space action representation, the native reference space of egocentric video, and semantically aligning robot and human action dimensions. Across total pretraining budgets from 250 to 10,000 hours, validation loss decreases approximately log-linearly with data scale. Larger pretraining budgets also improve out-of-distribution real-robot manipulation after post-training: across six challenging tasks with unseen objects, affordances, and reasoning prompts, the 10,000-hour model achieves a 55.0% success rate, compared with at most 11.7% for every pretraining budget up to 5,000 hours and 5.0% without pretraining. At the same pretraining budget, the camera-space action representation also outperforms the torso-frame baseline. Together, these findings support pretraining with a camera-space action representation on large-scale human egocentric data as a scalable foundation for humanoid robot manipulation.

## 参考
- https://arxiv.org/abs/2609.39403
- https://xpeng-robotics.github.io/ironmind/
