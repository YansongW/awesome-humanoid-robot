---
$id: ent_paper_liu_ropedia_w0_scaling_loco_manipu_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Ropedia W0: Scaling Loco-Manipulation World Models across Embodiments with Human Experience'
  zh: 'Ropedia W0: Scaling Loco-Manipulation World Models across Embodiments with Human Experience'
  ko: 'Ropedia W0: Scaling Loco-Manipulation World Models across Embodiments with Human Experience'
summary:
  en: World models enable embodied agents to anticipate action consequences, yet jointly modeling locomotion and manipulation
    across diverse embodiments remains challenging due to heterogeneous action spaces and limited multimodal supervision.
    We present Ropedia W0, the first egocentric loco-manipulation world foundation model spanning humans and robots with diverse
    embodiments. We curate Xp-Data, ...
  zh: Ropedia W0 是首个覆盖人类与多种机器人本体的自我中心视角移动-操作世界基础模型，由 Tianqi Liu、Hanfei Zhao 等人提出。团队构建了 Xp-Data 数据集，包含 1 万小时人类自我中心数据与 3 千小时机器人数据，并采用统一运动学表示（相机位姿编码移动、投影骨架编码操作）。模型在五个跨本体基准及留出人类视频上取得领先性能，蒸馏后可支持实时、分钟级推演与
    VR 实时交互。
  ko: World models enable embodied agents to anticipate action consequences, yet jointly modeling locomotion and manipulation
    across diverse embodiments remains challenging due to heterogeneous action spaces and limited multimodal supervision.
    We present Ropedia W0, the first egocentric loco-manipulation world foundation model spanning humans and robots with diverse
    embodiments. We curate Xp-Data, ...
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
- world_model
- loco_manipulation
- cross_embodiment
- egocentric_data
- humanoid_teleoperation
- embodied_planning
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-10-26'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-10-26). Bibliographic metadata from arXiv API (2610.26855);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2610.26855 Ropedia W0: Scaling Loco-Manipulation World Models across Embodiments with Human Experience'
  url: https://arxiv.org/abs/2610.26855
  date: '2026-10-19'
  accessed_at: '2026-10-26'
- id: src_002
  type: website
  title: Project page
  url: https://ropedia.github.io/ropedia-w0/
  accessed_at: '2026-10-26'
- id: src_003
  type: website
  title: Project page
  url: https://github.com/Ropedia/ropedia-w0
  accessed_at: '2026-10-26'
---

## 概述

Ropedia W0 面向移动与操作联合建模这一难题：不同本体的动作空间异构，多模态监督数据稀缺，导致跨本体世界模型难以构建。作者整理了 Xp-Data，将 1 万小时人类自我中心数据与 3 千小时机器人数据统一标注并做系统质量控制；在表示层面，用相机位姿刻画移动、用投影骨架刻画操作，机器人骨架则由本体相关正运动学结合大量人工关键点标注与修正得到。团队还提出基于高质量灵巧人形遥操作数据的长时程基准 Xp-Teleop。在 DreamDojo、Ψ_0、ω-HOME、Xp-Teleop 与 AgiBot 五个跨本体基准以及留出的人类自我中心视频上，模型从零样本推理到少样本与全量数据后训练均表现领先；扩大人类预训练数据可同时提升人类与机器人评测表现。蒸馏后模型支持实时、分钟级推演，可用于 VR 实时交互，并在策略评估、基于模型的规划与世界-动作建模等应用中体现价值。

## 核心内容

### 问题背景
世界模型让具身智能体能够预判动作后果，但要在多种本体上同时建模移动与操作仍很困难：不同本体的动作空间差异大，多模态监督信号也有限。现有工作尚未给出同时覆盖人类与多种机器人的自我中心移动-操作世界基础模型。

### 数据与表示
- **Xp-Data**：包含 1 万小时自我中心人类数据与 3 千小时机器人数据，配有统一的多模态标注，并经过系统的质量控制。
- **统一运动学表示**：移动通过相机位姿编码，操作通过投影骨架编码；机器人骨架由本体相关的正运动学结合大量人工关键点标注与修正构成。

### 基准
作者提出 **Xp-Teleop**，这是一个基于高质量灵巧人形遥操作数据的长时程移动-操作基准。

### 评测与结果
- 在五个跨本体基准 **DreamDojo**、**Ψ_0**、**ω-HOME**、**Xp-Teleop** 与 **AgiBot** 上，以及留出的人类自我中心视频上，模型均取得领先性能。
- 评测覆盖从零样本推理到少样本与全量数据后训练的不同设定。
- 扩大人类预训练数据规模，可同时改善人类与机器人两侧的评测表现。
- 经蒸馏后，模型支持实时、分钟级的推演，可实现 VR 实时交互。

### 应用与结论
模型在策略评估、基于模型的规划以及世界-动作建模等场景中展示了实用性，说明其对具身决策具有价值。

## Overview

World models enable embodied agents to anticipate action consequences, yet jointly modeling locomotion and manipulation across diverse embodiments remains challenging due to heterogeneous action spaces and limited multimodal supervision. We present Ropedia W0, the first egocentric loco-manipulation world foundation model spanning humans and robots with diverse embodiments. We curate Xp-Data, comprising 10k hours of egocentric human data and 3k hours of robot data with unified multimodal annotations and systematic quality control. A unified kinematic representation encodes locomotion through camera poses and manipulation through projected skeletons, with robot skeletons combining embodiment-specific forward kinematics with extensive manual keypoint annotation and correction. We also introduce Xp-Teleop, a long-horizon loco-manipulation benchmark based on high-quality dexterous humanoid teleoperation data. Evaluations demonstrate state-of-the-art performance across five cross-embodiment benchmarks (DreamDojo, $Ψ_0$, $ω$-HOME, Xp-Teleop, and AgiBot) and on held-out human egocentric video, from zero-shot inference to few-shot and full-data post-training. Scaling human pre-training data improves performance on both human and robot evaluations. After distillation, our model supports real-time, minute-long rollouts, enabling live VR interaction. Applications in policy evaluation, model-based planning, and world-action modeling further demonstrate the model's utility for embodied decision-making.

## 参考
- https://arxiv.org/abs/2610.26855
- https://ropedia.github.io/ropedia-w0/
- https://github.com/Ropedia/ropedia-w0
