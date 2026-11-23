---
$id: ent_paper_gan_humanoidpose_monocular_3d_pose_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'HumanoidPose: Monocular 3D Pose Estimation for Humanoid Robots'
  zh: 'HumanoidPose: Monocular 3D Pose Estimation for Humanoid Robots'
  ko: 'HumanoidPose: Monocular 3D Pose Estimation for Humanoid Robots'
summary:
  en: As humanoid robots increasingly enter real-world environments, recovering their 3D whole-body pose from monocular imagery
    is becoming increasingly important for external state perception, motion analysis, and robot learning. However, Humanoid
    Robot Pose Estimation (HRPE) lies at the intersection of conventional Robot Pose Estimation (RPE) and Human Pose Estimation
    (HPE), while not being fully ...
  zh: 本文提出 HumanoidPose，一个面向人形机器人单目 3D 全身姿态估计的框架，并构建了配套基准 Humanoids。该工作由 Jinlin Gan、Mingzhe Li、Junsheng Zhang、Zhibo Zhou、Jiahan
    Geng、Yuhua Luo、Changwang Zhang、Chenglu Wen 等人完成。核心贡献在于将类人视觉感知与机器人关节建模及显式运动学接地相结合，并在 Humanoids 与 DHRP-H1 基准上验证了关节恢复与 3D
    姿态估计性能，包括零样本迁移到真实世界 2D 与 3D 评估。
  ko: As humanoid robots increasingly enter real-world environments, recovering their 3D whole-body pose from monocular imagery
    is becoming increasingly important for external state perception, motion analysis, and robot learning. However, Humanoid
    Robot Pose Estimation (HRPE) lies at the intersection of conventional Robot Pose Estimation (RPE) and Human Pose Estimation
    (HPE), while not being fully ...
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
- humanoid_pose_estimation
- monocular_3d_pose
- kinematic_grounding
- robot_articulation_modeling
- benchmark_dataset
- zero_shot_transfer
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-11-23'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-11-23). Bibliographic metadata from arXiv API (2611.27181);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2611.27181 HumanoidPose: Monocular 3D Pose Estimation for Humanoid Robots'
  url: https://arxiv.org/abs/2611.27181
  date: '2026-11-20'
  accessed_at: '2026-11-23'
---

## 概述

人形机器人逐步进入真实环境后，仅凭单目图像恢复其 3D 全身姿态对外部状态感知、运动分析和机器人学习愈发关键。然而人形机器人姿态估计（HRPE）处于传统机器人姿态估计（RPE）与人体姿态估计（HPE）的交叉地带，却未被两者充分覆盖：RPE 主要面向非人形机器人尤其是固定基座机械臂，HPE 则依赖人类特有的骨架拓扑、人体模型与运动先验。尽管人形 2D 关键点检测与 HPE 适配已有进展，人形原生 3D 姿态恢复研究仍不充分，也缺少具备合适训练数据与评测协议的专用基准。为此作者提出基准 Humanoids 与框架 HumanoidPose，前者提供跨多种人形本体的合成 3D 监督、人工标注的真实 2D 数据，以及在实体 Roban 人形机器人上采集的 RGB 序列与机器人状态配对数据用于 3D 评估。HumanoidPose 将类人视觉感知、机器人关节建模与显式运动学接地融合，在 Humanoids 与 DHRP-H1 上展现出较强的关节恢复与 3D 姿态估计能力，并支持零样本迁移到真实世界评估。

## 核心内容

### 问题背景

- 人形机器人进入真实环境后，从单目图像恢复 3D 全身姿态对外部状态感知、运动分析与机器人学习十分重要。
- 人形机器人姿态估计（HRPE）横跨机器人姿态估计（RPE）与人体姿态估计（HPE），但两者均未完整覆盖该问题：RPE 主要针对非人形机器人，尤其是固定基座机械臂；HPE 则建立在人类特有的骨架拓扑、人体模型与运动先验之上。
- 现有工作多集中于人形 2D 关键点检测与 HPE 适配，人形原生的 3D 姿态恢复研究不足，且缺乏具备合适训练数据与评测协议的专用基准。

### 方法

- 提出基准 **Humanoids**，用于单目 3D 人形机器人姿态估计，包含三类数据：
  - 覆盖多种人形本体的合成 3D 监督数据；
  - 人工标注的真实世界 2D 数据；
  - 在实体 **Roban** 人形机器人上采集的真实 RGB 序列，并与机器人状态配对，用于 3D 评估。
- 提出框架 **HumanoidPose**，将类人视觉感知与机器人关节建模、显式运动学接地相结合。

### 实验设置

- 在 **Humanoids** 与 **DHRP-H1** 两个基准上进行评测。
- 评估涵盖关节恢复与 3D 姿态估计，并包含零样本迁移到真实世界 2D 与 3D 评估。
- 通过消融实验考察机器人原生关节建模与显式运动学接地的贡献。

### 关键结果

- 在 Humanoids 与 DHRP-H1 上，方法在关节恢复与 3D 姿态估计方面表现良好。
- 零样本迁移到真实世界 2D 与 3D 评估同样取得有效结果。
- 消融研究显示，机器人原生关节建模与显式运动学接地均有实际贡献。

### 结论

- 该工作填补了人形原生 3D 姿态恢复及专用基准的空白，数据集与代码将公开以支持后续研究。

## Overview

As humanoid robots increasingly enter real-world environments, recovering their 3D whole-body pose from monocular imagery is becoming increasingly important for external state perception, motion analysis, and robot learning. However, Humanoid Robot Pose Estimation (HRPE) lies at the intersection of conventional Robot Pose Estimation (RPE) and Human Pose Estimation (HPE), while not being fully addressed by either paradigm: RPE primarily focuses on non-humanoid robots, particularly fixed-base manipulators, whereas HPE is built upon human-specific skeletal topologies, body models, and motion priors. Despite recent progress in humanoid 2D keypoint detection and HPE adaptation, humanoid-native 3D pose recovery remains insufficiently studied, and a dedicated benchmark with suitable training data and evaluation protocols is still lacking. To address this gap, we introduce Humanoids, a benchmark for monocular 3D humanoid robot pose estimation, and propose HumanoidPose, a framework for this task. Humanoids provides synthetic 3D supervision across diverse humanoid embodiments, manually annotated real-world 2D data, and real-world RGB sequences paired with robot states for 3D evaluation on a physical Roban humanoid. HumanoidPose combines human-inspired visual perception with robot articulation modeling and explicit kinematic grounding. Experiments on Humanoids and the DHRP-H1 benchmark demonstrate strong performance in articulation recovery and 3D pose estimation, including zero-shot transfer to real-world 2D and 3D evaluation. Ablation studies further show the contribution of robot-native articulation modeling and explicit kinematic grounding. The dataset and code will be publicly released to support future research in the community.

## 参考
- https://arxiv.org/abs/2611.27181
