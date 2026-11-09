---
$id: ent_paper_dong_coordinating_humanoid_loco_man_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Coordinating Humanoid Loco-Manipulation through Action-Conditioned Latent Foresight
  zh: Coordinating Humanoid Loco-Manipulation through Action-Conditioned Latent Foresight
  ko: Coordinating Humanoid Loco-Manipulation through Action-Conditioned Latent Foresight
summary:
  en: Humanoid loco-manipulation requires coordinated body motion and hand interaction over time, and a plausible-looking
    command sequence can still drop a held object or leave an interaction incomplete. We present action-conditioned latent
    foresight, a latent world-action model (WAM) that evaluates proposed command sequences before execution. An action generator
    proposes joint motion-hand command ...
  zh: 本文提出“动作条件潜在预见”（action-conditioned latent foresight），一种在执行前评估候选指令序列的潜在世界-动作模型（WAM），用于人形机器人移动操作中的身体运动与手部交互协调。方法由动作生成器、动作条件端点预测器与联合时间先验组成，并通过动作一致性正则化训练。在
    SIMPLE 仿真基准的十项任务上平均成功率达 89.7%，在七项真机任务上标准条件为 85.7%、未见物体配置下为 65.7%。
  ko: Humanoid loco-manipulation requires coordinated body motion and hand interaction over time, and a plausible-looking
    command sequence can still drop a held object or leave an interaction incomplete. We present action-conditioned latent
    foresight, a latent world-action model (WAM) that evaluates proposed command sequences before execution. An action generator
    proposes joint motion-hand command ...
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
- humanoid_loco_manipulation
- world_action_model
- latent_foresight
- action_conditioned_prediction
- motion_planning
- sim_to_real
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-11-09'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-11-09). Bibliographic metadata from arXiv API (2611.04839);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: arXiv:2611.04839 Coordinating Humanoid Loco-Manipulation through Action-Conditioned Latent Foresight
  url: https://arxiv.org/abs/2611.04839
  date: '2026-11-03'
  accessed_at: '2026-11-09'
---

## 概述

人形机器人移动操作需要身体运动与手部交互在时间上协调，看似合理的指令序列仍可能导致物体掉落或交互中断。作者提出动作条件潜在预见，即一种潜在世界-动作模型，在真正执行前对候选指令序列进行评估。动作生成器依据视觉、语言与机器人状态提出关节运动-手部指令序列；动作条件端点预测器估计各序列前缀所到达的视觉特征，并衡量其向演示导出的子目标推进的程度；联合时间先验则在给定机器人状态与先前指令的条件下评估时间一致性。机器人执行得分最高序列的首批指令，并从下一观测重新规划；训练时通过动作一致性正则化，从观测与预测的特征变化中重建首个演示指令，促使预测器保留与动作相关的信息。

## 核心内容

### 问题背景
人形机器人移动操作要求身体运动与手部交互随时间协调。仅凭外观合理的指令序列，仍可能在执行中掉落所持物体或使交互无法完成，因此需要在执行前对候选指令序列进行评判。

### 方法
- **动作生成器**：从视觉、语言与机器人状态出发，提出关节运动-手部指令序列。
- **动作条件端点预测器**：估计每条序列前缀所到达的视觉特征，并度量其向演示导出的子目标推进的进度。
- **联合时间先验**：在给定机器人状态与先前指令的条件下，对序列的时间一致性打分。
- **执行方式**：机器人执行得分最高序列的首批指令，并从下一观测重新规划。
- **训练正则化**：动作一致性正则化从观测与预测的特征变化中重建首个演示指令，促使预测器保留与动作相关的信息。

### 实验设置与关键结果
- 在 humanoid loco-manipulation 仿真基准 **SIMPLE** 的十项任务上，方法平均成功率为 **89.7%**，对比 **Psi-Zero** 的 **73.7%** 与 **DiT4DiT** 的 **82.0%**。
- 在七项真机任务上，标准条件下成功率为 **85.7%**，未见物体配置下为 **65.7%**；**GR00T N1.7** 在相同设置下分别为 **70.0%** 与 **48.6%**。

### 结论
通过在执行前以动作条件潜在预见评估候选指令序列，并结合端点预测与时间一致性打分，该方法在仿真与真机任务上均取得高于对比基线的成功率，且在未见物体配置下仍保持一定泛化能力。

## Overview

Humanoid loco-manipulation requires coordinated body motion and hand interaction over time, and a plausible-looking command sequence can still drop a held object or leave an interaction incomplete. We present action-conditioned latent foresight, a latent world-action model (WAM) that evaluates proposed command sequences before execution. An action generator proposes joint motion-hand command sequences from vision, language, and the robot state. An action-conditioned endpoint predictor estimates the visual features each sequence prefix reaches and measures progress toward a demonstration-derived subgoal, while a joint temporal prior scores temporal consistency given the robot state and preceding commands. The robot executes the first commands of the best-scoring sequence and replans from the next observation. During training, action consistency regularization reconstructs the first demonstrated command from observed and predicted feature changes, encouraging the predictor to retain action-relevant information. On ten tasks in the humanoid loco-manipulation simulation benchmark SIMPLE, our method achieves 89.7% average success, compared with 73.7% for Psi-Zero and 82.0% for DiT4DiT. On seven real-robot tasks, it achieves 85.7% under standard conditions and 65.7% under unseen object configurations, while GR00T N1.7 achieves 70.0% and 48.6%, respectively. Project page: https://ju6276.github.io/Action-Grounded-Foresight/

## 参考
- https://arxiv.org/abs/2611.04839
