---
$id: ent_paper_magrini_r2ri_a_multi_view_event_and_rg_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'R2RI: A Multi-View Event and RGB Dataset for Robot-to-Robot Interaction'
  zh: 'R2RI: A Multi-View Event and RGB Dataset for Robot-to-Robot Interaction'
  ko: 'R2RI: A Multi-View Event and RGB Dataset for Robot-to-Robot Interaction'
summary:
  en: Understanding and modeling interactions between autonomous agents is a fundamental challenge in robotics, with broad
    implications for collaborative systems, social robotics, and human-robot coexistence. Although the study of robot interactions
    has emerged as a compelling research direction, progress has been severely hampered by the absence of large-scale benchmarks.
    In this paper, we introduce ...
  zh: R2RI 是首个专门面向机器人-机器人交互（RRI）任务的数据集，由 Gabriele Magrini 等人构建。该数据集包含多种人形机器人及模拟真实人类社会行为的交互场景，提供自我中心与外部中心两类互补视角，涵盖 Event 与
    RGB 两种模态，规模超过 650 万帧、约 5000 段 120 fps 视频。作者还对比了各模态下现有先进方法在多项感知与交互任务上的表现，并公开了数据集与标注。
  ko: Understanding and modeling interactions between autonomous agents is a fundamental challenge in robotics, with broad
    implications for collaborative systems, social robotics, and human-robot coexistence. Although the study of robot interactions
    has emerged as a compelling research direction, progress has been severely hampered by the absence of large-scale benchmarks.
    In this paper, we introduce ...
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
- robot_to_robot_interaction
- event_camera
- multimodal_dataset
- humanoid_robots
- egocentric_vision
- social_robotics
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-10-12'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-10-12). Bibliographic metadata from arXiv API (2610.07117);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2610.07117 R2RI: A Multi-View Event and RGB Dataset for Robot-to-Robot Interaction'
  url: https://arxiv.org/abs/2610.07117
  date: '2026-10-05'
  accessed_at: '2026-10-12'
---

## 概述

理解并建模自主智能体之间的交互是机器人学中的基础性难题，对协作系统、社交机器人以及人机共处都有广泛意义，但该方向长期受限于缺乏大规模基准。为此，作者提出 R2RI，这是首个专为机器人-机器人交互（RRI）任务设计的数据集。数据集涵盖多种人形机器人，交互行为参照真实人类社会行为建模，并提供互补视角：来自每个机器人机载传感器的自我中心视角，以及来自外部固定相机的外部中心视角。数据规模超过 650 万帧、约 5000 段 120 fps 视频，同时包含 Event 与 RGB 两种模态。作者进一步分析了各模态的优劣，并在多项关键感知与交互任务上比较了现有先进方法，最终公开数据集及其全部任务与模态的标注。

## 核心内容

### 问题背景
建模自主智能体之间的交互是机器人学的核心挑战之一，对协作系统、社交机器人和人机共存具有广泛影响。尽管机器人交互研究已成为一个有吸引力的方向，但该领域进展严重受限于缺乏大规模基准。

### 方法
作者提出 Robot-to-Robot Interaction（R2RI），这是首个专门针对机器人-机器人交互（RRI）任务设计的数据集。其特点包括：
- 包含多种人形机器人，交互行为基于真实人类社会行为建模。
- 提供互补视角：每个机器人机载传感器给出的自我中心视角，以及外部固定相机给出的外部中心视角，从而支持对交互动态的丰富空间与上下文理解。
- 同时覆盖 Event 与 RGB 两种模态。

### 实验设置与关键结果
作者考察了各模态的优缺点，并针对多项关键感知与交互任务，对现有先进方法进行了比较。摘要未给出具体数值结果。

### 结论
R2RI 数据集及其全部任务与模态的标注已在 https://github.com/MagriniGabriele/R2RI 公开。数据集规模超过 650 万帧、约 5000 段 120 fps 视频。

## Overview

Understanding and modeling interactions between autonomous agents is a fundamental challenge in robotics, with broad implications for collaborative systems, social robotics, and human-robot coexistence. Although the study of robot interactions has emerged as a compelling research direction, progress has been severely hampered by the absence of large-scale benchmarks. In this paper, we introduce Robot-to-Robot Interaction (R2RI), the first dataset specifically designed to address the Robot-Robot Interaction (RRI) task. R2RI consists of different humanoid robots and realistic interactions modeled on real human social behaviors. Complementary viewpoints are available, \textit{i.e.}, an egocentric perspective from each robot's onboard sensors, and an exocentric perspective from external fixed cameras, thus enabling rich spatial and contextual understanding of the interaction dynamics. The dataset comprises more than $6.5$M frames and $\approx5000$ videos at $120$ fps, including Event and RGB domains. We investigate pros and cons of each domain, comparing state-of-the-art approaches for a number of key sensing and interaction based tasks. We publicly release the dataset and its annotations for all tasks and modalities at https://github.com/MagriniGabriele/R2RI.

## 参考
- https://arxiv.org/abs/2610.07117
