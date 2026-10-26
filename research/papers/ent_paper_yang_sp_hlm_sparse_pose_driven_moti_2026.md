---
$id: ent_paper_yang_sp_hlm_sparse_pose_driven_moti_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'SP-HLM: Sparse-Pose-Driven Motion Generation and Whole-Body Control for Humanoid Loco-Manipulation'
  zh: 'SP-HLM: Sparse-Pose-Driven Motion Generation and Whole-Body Control for Humanoid Loco-Manipulation'
  ko: 'SP-HLM: Sparse-Pose-Driven Motion Generation and Whole-Body Control for Humanoid Loco-Manipulation'
summary:
  en: Humanoid loco-manipulation requires an effective interface between high-level task policies and whole-body control.
    Existing interfaces typically rely on a single action representation for both task intent and whole-body coordination.
    This may burden the high-level policy or leave one aspect underspecified. We present SP-HLM, a framework built on a sparse-pose-driven
    interface. The interface ...
  zh: SP-HLM 是一个面向人形机器人移动操作（loco-manipulation）的框架，由 Zhaohui Yang、Quanbao Lin 等人提出，核心是采用稀疏姿态驱动的接口来连接高层任务策略与全身控制。该接口将五个任务关键身体姿态与学习到的隐式运动先验相结合，分别表达空间意图与全身协调。系统由
    SP-VLA、SP-MGM 与 SP-GMT 三个模块组成，在仿真与真实人形机器人上均取得优于现有方法的运动跟踪、全身协调与移动操作成功率。
  ko: Humanoid loco-manipulation requires an effective interface between high-level task policies and whole-body control.
    Existing interfaces typically rely on a single action representation for both task intent and whole-body coordination.
    This may burden the high-level policy or leave one aspect underspecified. We present SP-HLM, a framework built on a sparse-pose-driven
    interface. The interface ...
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
- sparse_pose_interface
- vision_language_action
- motion_generation
- whole_body_control
- motion_tracking
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-10-26'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-10-26). Bibliographic metadata from arXiv API (2610.30044);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2610.30044 SP-HLM: Sparse-Pose-Driven Motion Generation and Whole-Body Control for Humanoid Loco-Manipulation'
  url: https://arxiv.org/abs/2610.30044
  date: '2026-10-21'
  accessed_at: '2026-10-26'
---

## 概述

现有的人形机器人移动操作接口通常用单一动作表示同时承载任务意图与全身协调，这要么给高层策略带来过重负担，要么使其中某一方面的表达不够充分。SP-HLM 提出以稀疏姿态作为驱动接口，把五个任务关键身体姿态与一个学习到的隐式运动先验组合起来，用互补的形式分别刻画空间意图和全身协调。在该框架中，SP-VLA 作为视觉-语言-动作模型，从多模态观测与语言指令出发，通过异步动作分块推理预测任务相关的稀疏姿态与手指关节位置；SP-MGM 则经两阶段蒸馏训练，依据这些稀疏目标实时重建协调的全身运动，并由预训练运动编码器压缩为紧凑的隐式表示。最后，通用运动跟踪器 SP-GMT 将显式稀疏目标与隐式运动先验融合，用于全身控制。仿真与真实人形机器人实验表明，该方法在运动跟踪、全身协调和移动操作成功率上均优于现有方法。

## 核心内容

### 问题背景

人形机器人移动操作需要在高层任务策略与全身控制之间建立有效的接口。现有接口往往用单一动作表示同时承担任务意图与全身协调两项职责，这可能导致高层策略负担过重，或使其中某一方面的表达不够充分。SP-HLM 针对这一问题，提出以稀疏姿态驱动的接口作为替代方案。

### 方法

SP-HLM 的接口由两部分互补构成：五个任务关键身体姿态，以及一个学习到的隐式运动先验，分别用于表达空间意图与全身协调。框架包含三个模块：

- **SP-VLA**：视觉-语言-动作模型，从多模态观测与语言指令中预测任务相关的稀疏姿态与手指关节位置，推理时采用异步动作分块（asynchronous action-chunk inference）。
- **SP-MGM**：运动生成模型，通过两阶段蒸馏训练，在给定稀疏目标的情况下实时重建协调的全身运动；随后由预训练运动编码器将该运动映射为紧凑的隐式表示。
- **SP-GMT**：通用运动跟踪器，将显式稀疏目标与上述隐式运动先验相结合，实现全身控制。

### 实验设置

实验在仿真环境与真实人形机器人上开展，用于评估运动跟踪、全身协调以及移动操作任务的表现。

### 关键结果

实验结果显示，与现有方法相比，SP-HLM 在运动跟踪、全身协调和移动操作成功率方面均有提升。更多结果与视频见项目主页。

### 结论

以稀疏姿态为驱动、显式目标与隐式运动先验互补的接口设计，能够有效衔接高层任务策略与全身控制，并在仿真与真实平台上验证了其效果。

## Overview

Humanoid loco-manipulation requires an effective interface between high-level task policies and whole-body control. Existing interfaces typically rely on a single action representation for both task intent and whole-body coordination. This may burden the high-level policy or leave one aspect underspecified. We present SP-HLM, a framework built on a sparse-pose-driven interface. The interface combines five task-critical body poses with a learned latent motion prior to represent spatial intent and whole-body coordination in complementary forms. SP-VLA, a vision-language-action model, first predicts task-relevant sparse poses and finger joint positions from multimodal observations and language instructions using asynchronous action-chunk inference. Given these sparse targets, SP-MGM, a motion generation model trained through two-stage distillation, reconstructs coordinated full-body motion in real time. A pretrained motion encoder maps this motion to a compact latent representation. SP-GMT, a general motion tracker, then integrates the explicit sparse targets with this implicit motion prior for whole-body control. Experiments in simulation and on a real humanoid robot demonstrate improved motion tracking, whole-body coordination, and loco-manipulation success over existing approaches. Additional results and videos are available on our \href{https://sp-hlm.github.io/}{\textcolor{blue}{project page}}.

## 参考
- https://arxiv.org/abs/2610.30044
