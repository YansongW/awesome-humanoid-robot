---
$id: ent_paper_hu_eye_robot_learning_expressive_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Eye, Robot: Learning Expressive Gaze Dynamics via a VLM-Guided Transformer-VAE'
  zh: 'Eye, Robot: Learning Expressive Gaze Dynamics via a VLM-Guided Transformer-VAE'
  ko: 'Eye, Robot: Learning Expressive Gaze Dynamics via a VLM-Guided Transformer-VAE'
summary:
  en: Gaze coordinates attention in human interaction through coupled eye, head, and eyelid motion. A humanoid robot must
    choose where to look while generating a suitable movement toward that target; fixed tracking rules alone do not model
    the temporal structure of human gaze. We separate these tasks with an asynchronous vision-language model that selects
    a scene referent, a reactive perception module ...
  zh: 该研究提出一套面向人形机器人的注视行为生成框架，将“看哪里”与“如何看”解耦：由异步 VLM 选择场景指涉目标，由反应式感知模块维持注视，并由 Realistic Gaze Transformer（RGT）生成目标条件下的眼颈运动。RGT
    是基于 Transformer-VAE 的模型，在无标记人体记录重定向到机器人 11 自由度关节空间的数据上训练，采用自监督预训练与自回归微调。在两秒基准测试中，RGT-Base 取得所报告的最低七关节总体 MSE。
  ko: Gaze coordinates attention in human interaction through coupled eye, head, and eyelid motion. A humanoid robot must
    choose where to look while generating a suitable movement toward that target; fixed tracking rules alone do not model
    the temporal structure of human gaze. We separate these tasks with an asynchronous vision-language model that selects
    a scene referent, a reactive perception module ...
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
- gaze_generation
- humanoid_robot
- transformer_vae
- vision_language_model
- motion_retargeting
- blink_prediction
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-10-19'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-10-19). Bibliographic metadata from arXiv API (2610.19635);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2610.19635 Eye, Robot: Learning Expressive Gaze Dynamics via a VLM-Guided Transformer-VAE'
  url: https://arxiv.org/abs/2610.19635
  date: '2026-10-14'
  accessed_at: '2026-10-19'
---

## 概述

人类注视由眼、头与眼睑的耦合运动共同构成，而固定跟踪规则难以刻画其时间结构，因此该工作将注视目标选择与注视运动生成拆分为异步模块。目标选择由视觉语言模型完成，反应式感知模块负责保持注视，Realistic Gaze Transformer（RGT）则生成以目标为条件的运动。RGT 采用 Transformer-VAE 结构，训练数据为无标记人体记录并重定向至机器人 11 自由度关节空间，先进行自监督预训练以编码近期全头历史，再通过自回归微调让模型在 rollout 中接触自身预测。推理时，四维双眼轨迹条件化颈部与眼部的协同运动，辅助眨眼预测器在回放阶段触发眼睑模板。在两秒基准中所有控制器接收相同真值目标，RGT-Base 取得所报告的最低七关节总体 MSE，物理演示展示了目标选择与控制的一体化流程；感知自然度与开放词汇目标选择准确率仍待受控评估。

## 核心内容

### 问题背景
人类交互中的注视通过眼、头与眼睑的耦合运动来协调注意力。人形机器人不仅需要决定看向何处，还需生成朝向该目标的合适运动；仅依赖固定跟踪规则无法建模人类注视的时间结构。作者据此将注视任务分解为目标选择与运动生成两部分。

### 方法
- **异步目标选择**：使用异步 vision-language model 选择场景中的指涉目标。
- **注视维持**：由反应式感知模块保持对目标的注视。
- **运动生成**：Realistic Gaze Transformer（RGT）生成以目标为条件的运动，为 Transformer-VAE 结构。
- **训练数据与空间**：在无标记人体记录上训练，并重定向到机器人的 11-DoF 关节空间。
- **训练策略**：自监督预训练编码近期全头历史；自回归微调使模型在 rollout 过程中接触自身预测。
- **推理条件**：四维双眼轨迹作为条件，驱动颈部与眼部的协同运动；辅助眨眼预测器在回放时触发眼睑模板。

### 实验设置
构建了一个两秒基准，其中所有控制器接收相同的真值目标，用于比较七关节总体 MSE。此外通过物理演示展示集成的目标选择与控制流程。

### 关键结果
- RGT-Base 在该两秒基准上取得所报告的最低七关节总体 MSE。
- 物理演示验证了目标选择与控制流水线的集成运行。
- 证据支持机器人空间中的运动学保真度与 RGT 的实时推理能力。

### 结论与局限
研究确立了机器人空间运动学保真度与实时 RGT 推理；感知自然度与开放词汇目标选择准确率仍属于需要受控评估的问题。

## Overview

Gaze coordinates attention in human interaction through coupled eye, head, and eyelid motion. A humanoid robot must choose where to look while generating a suitable movement toward that target; fixed tracking rules alone do not model the temporal structure of human gaze. We separate these tasks with an asynchronous vision-language model that selects a scene referent, a reactive perception module that maintains fixation, and a Realistic Gaze Transformer (RGT) that generates target-conditioned motion. RGT is a Transformer-VAE trained on markerless human recordings retargeted to the robot's 11-DoF joint space: self-supervised pretraining encodes recent full-head history, and autoregressive fine-tuning exposes the model to its own predictions during rollout. At inference, a four-dimensional binocular-eye trajectory conditions coordinated neck and eye motion; an auxiliary blink predictor triggers eyelid templates during playback. On a two-second benchmark in which all controllers receive the same ground-truth target, RGT-Base obtains the lowest reported overall seven-joint MSE, and physical demonstrations show the integrated targeting and control pipeline. The evidence establishes robot-space kinematic fidelity and real-time RGT inference; perceived naturalness and open-vocabulary target-selection accuracy remain questions for controlled evaluation.

## 参考
- https://arxiv.org/abs/2610.19635
