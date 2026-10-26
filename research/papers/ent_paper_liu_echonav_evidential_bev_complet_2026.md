---
$id: ent_paper_liu_echonav_evidential_bev_complet_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'EchoNav: Evidential BEV Completion from Historical Observations for Visual Navigation'
  zh: 'EchoNav: Evidential BEV Completion from Historical Observations for Visual Navigation'
  ko: 'EchoNav: Evidential BEV Completion from Historical Observations for Visual Navigation'
summary:
  en: Visual navigation in cluttered environments requires robots to recover previously observed structure and infer obstacles
    and free space that remain occluded. We present a framework that combines temporal aggregation and occupancy completion
    in an evidential bird's-eye-view (BEV) representation predicted from short RGB sequences. A decoder adapts frozen VGGT-Omega
    features and combines historical ...
  zh: EchoNav 是一个面向杂乱环境视觉导航的框架，它从短 RGB 序列预测证据式鸟瞰图（BEV）表示，将时序聚合与占据补全结合起来。该工作由 Diwen Liu、Yiyang Shao、Borui Wang、Chi Zhang、Yunhui
    Liu 完成。其解码器适配冻结的 VGGT-Omega 特征，并用逐单元权重与可学习的“不更新”选项融合历史残差提议；在仿真双目标序贯导航中达到 89.6% 成功率，比最强基线高 32.5 个百分点。
  ko: Visual navigation in cluttered environments requires robots to recover previously observed structure and infer obstacles
    and free space that remain occluded. We present a framework that combines temporal aggregation and occupancy completion
    in an evidential bird's-eye-view (BEV) representation predicted from short RGB sequences. A decoder adapts frozen VGGT-Omega
    features and combines historical ...
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
- visual_navigation
- bird_eye_view
- occupancy_completion
- evidential_learning
- temporal_aggregation
- humanoid_robot
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-10-26'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-10-26). Bibliographic metadata from arXiv API (2610.27616);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2610.27616 EchoNav: Evidential BEV Completion from Historical Observations for Visual Navigation'
  url: https://arxiv.org/abs/2610.27616
  date: '2026-10-20'
  accessed_at: '2026-10-26'
---

## 概述

EchoNav 针对杂乱环境中的视觉导航问题，目标是让机器人恢复此前观测到的结构，并推断仍被遮挡的障碍物与自由空间。方法上，它从短 RGB 序列预测证据式 BEV 表示，把时序聚合与占据补全统一在同一框架内；解码器适配冻结的 VGGT-Omega 特征，并借助逐单元权重和可学习的“不更新”选项来组合历史残差提议。BEV 预测器在最新自车坐标系下生成局部地图，不需要深度或相机位姿输入，也不做显式几何变换。证据模型将已观测自由空间单独处理，并在其余受支持区域预测占据及其置信度。训练使用仿真 RGB 序列，配以完整占据标注与可见性掩码占据标注。实验涵盖仿真导航与轮式机器人试验，并在四足与 humanoid 机器人上做了额外演示；仿真双目标序贯导航成功率 89.6%，20 个场景 60 次轮式机器人试验成功率 73.3%。

## 核心内容

### 问题背景

杂乱环境中的视觉导航要求机器人能够恢复此前观测到的结构，并对仍处于遮挡状态的障碍物与自由空间做出推断。仅依赖当前帧的感知难以覆盖被遮挡区域，因此需要把历史观测与占据补全结合起来。

### 方法

- **表示与输入**：从短 RGB 序列预测证据式鸟瞰图（BEV）表示，将时序聚合与占据补全统一在同一框架中。
- **解码器设计**：适配冻结的 VGGT-Omega 特征，并使用逐单元权重（cellwise weights）与一个可学习的“不更新”选项来组合历史残差提议。
- **局部地图预测**：BEV 预测器在最新自车坐标系下生成局部地图，不需要深度输入、相机位姿输入，也不进行显式几何变换（explicit geometric warping）。
- **证据建模**：证据模型将已观测自由空间单独处理，并在其余受支持区域内预测占据及其关联置信度。

### 实验设置

- 预测器在仿真 RGB 序列上训练，训练数据配有完整占据标注与可见性掩码（visibility-masked）占据标注。
- 实验在仿真中评估导航，并在轮式机器人上开展试验；此外在四足机器人与 humanoid 机器人上提供了额外演示。

### 关键结果

- 仿真序贯双目标导航：成功率达 89.6%，比所评估的最强基线高出 32.5 个百分点。
- 轮式机器人：在 20 个场景中共进行 60 次试验，成功率为 73.3%，而所评估的最强基线为 33.3%。

### 结论

EchoNav 表明，基于短 RGB 序列的证据式 BEV 时序聚合与占据补全，能够在不依赖深度与相机位姿输入的情况下支撑杂乱环境中的视觉导航，并在仿真与真实轮式机器人试验中均显著优于所评估的基线。

## Overview

Visual navigation in cluttered environments requires robots to recover previously observed structure and infer obstacles and free space that remain occluded. We present a framework that combines temporal aggregation and occupancy completion in an evidential bird's-eye-view (BEV) representation predicted from short RGB sequences. A decoder adapts frozen VGGT-Omega features and combines historical residual proposals using cellwise weights and a learned no-update option. The BEV predictor produces a local map in the latest ego frame without depth or camera-pose inputs or explicit geometric warping. The evidential model treats observed free space separately and predicts occupancy with associated confidence across the remaining supported region. We train the predictor on simulated RGB sequences paired with complete and visibility-masked occupancy annotations. Our experiments evaluate navigation in simulation and on a wheeled robot, with additional demonstrations on quadruped and humanoid robots. In simulated sequential two-goal navigation, our system achieves 89.6% success, outperforming the strongest evaluated baseline by 32.5 percentage points. Across 60 wheeled-robot trials in 20 scenes, it achieves 73.3% success, compared with 33.3% for the strongest evaluated baseline.

## 参考
- https://arxiv.org/abs/2610.27616
