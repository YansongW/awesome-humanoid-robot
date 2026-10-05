---
$id: ent_paper_chen_egohumanoid_v2_human_to_humano_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'EgoHumanoid-V2: Human-to-Humanoid Transfer of Coordinated Whole-Body Skills for Loco-Manipulation'
  zh: 'EgoHumanoid-V2: Human-to-Humanoid Transfer of Coordinated Whole-Body Skills for Loco-Manipulation'
  ko: 'EgoHumanoid-V2: Human-to-Humanoid Transfer of Coordinated Whole-Body Skills for Loco-Manipulation'
summary:
  en: Human demonstrations capture diverse scenes and rich whole-body skills without requiring robot teleoperation. Prior
    work on egocentric transfer has emphasized scene generalization in loco-manipulation under decoupled control, leaving
    direct transfer of coordinated whole-body skills less explored. We present EgoHumanoid-V2, the first egocentric human-to-humanoid
    skill transfer framework for ...
  zh: EgoHumanoid-V2 是首个面向协调全身 loco-manipulation 的自我中心（egocentric）人到人形机器人技能迁移框架，由 Jin Chen、Yiming Jiang、Chongyang Xu、Modi
    Shi、Shijia Peng、Li Chen、Tianyu Li、Mu Xu 等人提出。其核心是粗到细的动作对齐，将运动学参考校正与动力学感知精修相结合，在保持全身协调的同时提升末端执行器位姿精度。在四个真实世界任务上，基于对齐后人类数据训练的
    VLA 策略实现了零样本技能迁移，任务得分与遥操作数据训练的策略相当，且采集成本更低。
  ko: Human demonstrations capture diverse scenes and rich whole-body skills without requiring robot teleoperation. Prior
    work on egocentric transfer has emphasized scene generalization in loco-manipulation under decoupled control, leaving
    direct transfer of coordinated whole-body skills less explored. We present EgoHumanoid-V2, the first egocentric human-to-humanoid
    skill transfer framework for ...
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
- human_to_humanoid_transfer
- whole_body_loco_manipulation
- egocentric_learning
- vision_language_action
- action_alignment
- zero_shot_skill_transfer
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-10-05'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-10-05). Bibliographic metadata from arXiv API (2609.37181);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2609.37181 EgoHumanoid-V2: Human-to-Humanoid Transfer of Coordinated Whole-Body Skills for Loco-Manipulation'
  url: https://arxiv.org/abs/2609.37181
  date: '2026-09-29'
  accessed_at: '2026-10-05'
---

## 概述

该工作关注如何直接利用人类演示中的协调全身技能，而非依赖机器人遥操作。作者指出，以往自我中心迁移研究多聚焦于解耦控制下的场景泛化，对协调全身技能的直接迁移探讨不足。EgoHumanoid-V2 通过粗到细的动作对齐实现迁移，其中结合了运动学参考校正与动力学感知精修，从而在维持全身协调的前提下改善末端执行器位姿精度。为缩小视觉具身差异并提升视角鲁棒性，框架还采用了机器人手臂渲染与训练时图像增强。在四个真实世界任务上，用对齐人类数据训练的 VLA 策略无需目标任务的机器人演示即可零样本迁移，任务得分与遥操作数据训练的策略相当，而采集成本更低，表明人类数据可作为直接的技能监督信号。

## 核心内容

### 问题背景
人类演示能够覆盖多样场景并蕴含丰富的全身技能，且无需机器人遥操作。已有自我中心迁移工作主要强调解耦控制下 loco-manipulation 的场景泛化，而对协调全身技能的直接迁移研究较少。

### 方法
EgoHumanoid-V2 被定位为首个面向协调全身 loco-manipulation 的自我中心人到人形机器人技能迁移框架。其核心机制为粗到细的动作对齐，包含两个环节：
- 运动学参考校正
- 动力学感知精修

该对齐在提升末端执行器位姿精度的同时保持全身协调性。此外，框架引入机器人手臂渲染与训练时图像增强，用于缩小视觉具身差异并提升视角鲁棒性。

### 实验设置
在四个真实世界任务上进行评估。训练数据为对齐后的人类数据，训练对象为 vision-language-action（VLA）策略。评估关注零样本技能迁移，即不使用目标任务的机器人演示。

### 关键结果
- 在四个真实世界任务上，基于对齐人类数据训练的 VLA 策略实现了零样本技能迁移，无需目标任务的机器人演示。
- 任务得分与基于遥操作数据训练的策略相当。
- 数据采集成本低于遥操作。

### 结论
结果支持将人类数据作为直接的技能监督信号，用于协调全身 loco-manipulation 的人到人形机器人技能迁移。

## Overview

Human demonstrations capture diverse scenes and rich whole-body skills without requiring robot teleoperation. Prior work on egocentric transfer has emphasized scene generalization in loco-manipulation under decoupled control, leaving direct transfer of coordinated whole-body skills less explored. We present EgoHumanoid-V2, the first egocentric human-to-humanoid skill transfer framework for coordinated whole-body loco-manipulation. At its core, coarse-to-fine action alignment combines kinematic reference correction with dynamics-aware refinement. It improves end-effector pose accuracy while preserving whole-body coordination. We also use robot-arm rendering and training-time image augmentation to reduce the visual embodiment gap and improve viewpoint robustness. On four real-world tasks, vision-language-action (VLA) policies trained on aligned human data show zero-shot skill transfer without target-task robot demonstrations. Task scores are comparable to those of policies trained on teleoperation data at a lower collection cost. These results support human data as direct skill supervision.

## 参考
- https://arxiv.org/abs/2609.37181
