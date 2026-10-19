---
$id: ent_paper_zhou_egoexplorer_a_vision_motion_to_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'EgoExplorer: A Vision-Motion-Touch Observatory for Human Loco-Manipulation In Situ'
  zh: 'EgoExplorer: A Vision-Motion-Touch Observatory for Human Loco-Manipulation In Situ'
  ko: 'EgoExplorer: A Vision-Motion-Touch Observatory for Human Loco-Manipulation In Situ'
summary:
  en: Learning humanoid loco-manipulation from human demonstrations rests on observing how locomotion, posture, and object
    interaction evolve together as tasks unfold. Scaling collection across diverse environments, in turn, favors lightweight,
    portable capture systems. Yet, existing datasets provide only partial views of this coordination. Thus, we introduce EgoExplorer,
    a 100-hour vision-motion-touch ...
  zh: EgoExplorer 是一个基于可穿戴系统构建的、时长 100 小时的人形机器人移动-操作（loco-manipulation）观测数据集，由 Yunsong Zhou、Xuekun Jiang 等人完成。它将以自我为中心的视频与重建的全身运动、细粒度手指关节运动及触觉观测对齐，并配有逐步描述。为在稀疏体感条件下实现这一覆盖，作者提出
    Calibrate-Complete-Constrain 流程，相比最强基线将身体点误差降低 71.9%。
  ko: Learning humanoid loco-manipulation from human demonstrations rests on observing how locomotion, posture, and object
    interaction evolve together as tasks unfold. Scaling collection across diverse environments, in turn, favors lightweight,
    portable capture systems. Yet, existing datasets provide only partial views of this coordination. Thus, we introduce EgoExplorer,
    a 100-hour vision-motion-touch ...
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
- human_loco_manipulation
- egocentric_vision
- wearable_motion_capture
- tactile_sensing
- humanoid_retargeting
- multimodal_dataset
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-10-19'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-10-19). Bibliographic metadata from arXiv API (2610.18872);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2610.18872 EgoExplorer: A Vision-Motion-Touch Observatory for Human Loco-Manipulation In Situ'
  url: https://arxiv.org/abs/2610.18872
  date: '2026-10-13'
  accessed_at: '2026-10-19'
---

## 概述

从人类演示中学习人形机器人移动-操作，关键在于观察移动、姿态与物体交互如何随任务推进而共同演化，而跨多样环境扩大采集规模则倾向于轻量便携的采集系统。现有数据集只能提供这种协调性的部分视图。为此，作者提出 EgoExplorer，一个用可穿戴系统构建的 100 小时视觉-运动-触觉观测库，侧重专业活动，其连续记录将以自我为中心的视频与重建的全身运动、细粒度手指关节运动、触觉观测对齐，并附有步骤级描述。为在稀疏体感条件下达成这一覆盖，作者开发了 Calibrate-Complete-Constrain 流程：可复用的标定在运动推断前固定参与者几何与传感器佩戴方式，以分离安装偏移与关节运动；时间先验补全未观测到的关节运动；分层约束促进测量一致性、时间连续性与几何一致性。与 tracker 拟合参考相比，该方法相对最强基线将身体点误差降低 71.9%，匹配评估还显示手部稳定性与接触估计有所提升。初步研究探索了多模态生成与条件化，以及在仿真中结合全身控制的人形机器人重定向。

## 核心内容

### 问题背景
从人类演示中学习人形机器人的移动-操作能力，依赖于观察移动、姿态与物体交互在任务展开过程中如何协同演化。要在多样环境中扩大采集规模，需要轻量、便携的采集系统。然而现有数据集仅提供这种协调性的部分视图，缺乏对全身运动、手指精细动作与触觉信息的同步覆盖。

### 方法与系统
作者提出 **EgoExplorer**，一个用可穿戴系统构建的 100 小时视觉-运动-触觉观测库，侧重专业活动。其连续记录将以自我为中心的视频与以下模态对齐：
- 重建的全身运动
- 细粒度手指关节运动
- 触觉观测
- 步骤级描述

为在稀疏体感条件下实现上述覆盖，作者开发了 **Calibrate-Complete-Constrain** 流程：
- **Calibrate（标定）**：可复用的标定在运动推断之前固定参与者几何与传感器佩戴方式，从而将安装偏移与关节运动分离。
- **Complete（补全）**：利用时间先验补全未观测到的关节运动。
- **Constrain（约束）**：分层约束促进测量一致性、时间连续性与几何一致性——这些性质仅靠运动合理性无法保证。

### 实验与关键结果
- 与 tracker 拟合的参考结果相比，该方法相对最强基线将身体点误差降低 **71.9%**。
- 匹配评估还显示手部稳定性与接触估计方面有所提升。

### 初步探索
初步研究探索了多模态生成与条件化，以及在仿真中结合全身控制的人形机器人重定向。

### 结论
EgoExplorer 通过可穿戴采集与 Calibrate-Complete-Constrain 流程，提供了对移动、姿态与物体交互协同演化的较完整观测，并在身体点精度、手部稳定性与接触估计上取得改进，为多模态生成与人形机器人重定向等下游研究提供了基础。

## Overview

Learning humanoid loco-manipulation from human demonstrations rests on observing how locomotion, posture, and object interaction evolve together as tasks unfold. Scaling collection across diverse environments, in turn, favors lightweight, portable capture systems. Yet, existing datasets provide only partial views of this coordination. Thus, we introduce EgoExplorer, a 100-hour vision-motion-touch observatory of human loco-manipulation built with a wearable system. With an emphasis on professional activities, its continuous recordings align egocentric video with reconstructed whole-body motion, fine-grained finger articulation, and tactile observations, accompanied by step-level descriptions. To achieve this coverage with sparse body sensing, we develop the Calibrate-Complete-Constrain pipeline. Concretely, reusable calibration fixes participant geometry and sensor attachments before motion inference to disentangle mounting offsets from articulation. A temporal prior then completes unobserved joint motion, while layered constraints promote measurement agreement, temporal continuity, and geometric consistency, properties that motion plausibility alone does not guarantee. Against tracker-fitted references, the method reduces body-point error by 71.9% relative to the strongest baseline; matched evaluations also show gains in hand stability and contact estimation. Preliminary studies explore multimodal generation and conditioning alongside humanoid retargeting with whole-body control in simulation.

## 参考
- https://arxiv.org/abs/2610.18872
