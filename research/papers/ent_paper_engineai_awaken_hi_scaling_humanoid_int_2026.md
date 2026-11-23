---
$id: ent_paper_engineai_awaken_hi_scaling_humanoid_int_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Awaken-HI: Scaling Humanoid Intelligence with Whole-Body Human Experience'
  zh: 'Awaken-HI: Scaling Humanoid Intelligence with Whole-Body Human Experience'
  ko: 'Awaken-HI: Scaling Humanoid Intelligence with Whole-Body Human Experience'
summary:
  en: A central goal of humanoid robotics is for robots to perform the everyday work people do in homes and workplaces. Existing
    egocentric video datasets cover many of these activities but provide little synchronized whole-body motion data for learning
    loco-manipulation at scale. We build Awaken-Human, which pairs approximately 50,000 hours of egocentric stereo video with
    synchronized whole-body human ...
  zh: Awaken-HI 是 EngineAI 提出的人形机器人视觉-语言-动作模型，用于全身移动操作（loco-manipulation）。团队构建了 Awaken-Human 数据集，将约 5 万小时的第一人称立体视频与同步全身人体运动配对，覆盖
    100 多种技能。模型通过共享动作专家同时预测原始人体运动与重定向后的机器人动作，在 T800 适配后于八项任务上取得 93.75% 的平均成功率。
  ko: A central goal of humanoid robotics is for robots to perform the everyday work people do in homes and workplaces. Existing
    egocentric video datasets cover many of these activities but provide little synchronized whole-body motion data for learning
    loco-manipulation at scale. We build Awaken-Human, which pairs approximately 50,000 hours of egocentric stereo video with
    synchronized whole-body human ...
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
- vision_language_action_model
- egocentric_video_dataset
- whole_body_motion
- motion_retargeting
- scaling_law
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-11-23'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-11-23). Bibliographic metadata from arXiv API (2611.26420);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2611.26420 Awaken-HI: Scaling Humanoid Intelligence with Whole-Body Human Experience'
  url: https://arxiv.org/abs/2611.26420
  date: '2026-11-19'
  accessed_at: '2026-11-23'
- id: src_002
  type: website
  title: Project page
  url: https://engineai-robotics.github.io/Awaken-HI
  accessed_at: '2026-11-23'
---

## 概述

人形机器人的核心目标是承担人类在家庭与工作场所中的日常劳动，但现有第一人称视频数据集虽覆盖大量活动，却缺乏大规模学习移动操作所需的同步全身运动数据。为此，EngineAI 构建了 Awaken-Human，将约 5 万小时第一人称立体视频与同步的全身人体运动配对，覆盖 100 多种技能。在此基础上提出的 Awaken-HI 是一个面向人形移动操作的视觉-语言-动作模型，借助共享动作专家联合预测原始人体运动与重定向后的机器人动作。研究表明，当人体轨迹直接监督该共享动作专家时，技能从人到人形机器人的迁移更为有效；增加人体预训练数据可降低留出机器人动作预测误差，并提升下游真实机器人任务的平均成功率。经过全语料预训练与 T800 适配，Awaken-HI 在八项单项任务上平均成功率达 93.75%，在单项与长程评测中均优于 GR00T N1.7 与 $π_{0.5}$。

## 核心内容

### 问题背景
人形机器人的一个核心目标是让机器人完成人类在家庭和工作场所中从事的日常工作。现有的第一人称（egocentric）视频数据集虽然覆盖了其中许多活动，但几乎不提供同步的全身运动数据，难以支撑大规模的学习式移动操作（loco-manipulation）。

### 数据：Awaken-Human
- 将约 50,000 小时的第一人称立体视频与同步的全身人体运动配对。
- 覆盖超过 100 种技能。

### 方法：Awaken-HI
- Awaken-HI（Humanoid Intelligence）是一个面向人形移动操作的视觉-语言-动作模型。
- 模型通过一个共享动作专家（shared action expert）联合预测原始人体运动与重定向后的机器人动作。
- 关键设计在于：当人体轨迹直接监督该共享动作专家时，移动操作技能从人到人形机器人的迁移更为有效。

### 实验与结果
- 增加人体预训练数据可降低留出（held-out）机器人动作预测误差，并呈现出一条经验缩放规律（empirical scaling law）。
- 增加人体预训练数据同时提升下游真实机器人任务的平均成功率。
- 经过全语料预训练与 T800 适配后，Awaken-HI 在八项单项任务上的平均成功率为 93.75%。
- 在单项任务与长程（long-horizon）评测中，Awaken-HI 均优于 GR00T N1.7 与 $π_{0.5}$。
- 同一策略可泛化到机器人后训练阶段未见过的物体，以及熟悉物体与目标位置的新组合。

### 结论
将大规模同步全身人体运动数据与共享动作专家相结合，可有效实现人形机器人移动操作技能从人到机器人的规模化迁移，并在真实机器人任务上取得高成功率与良好泛化能力。

## Overview

A central goal of humanoid robotics is for robots to perform the everyday work people do in homes and workplaces. Existing egocentric video datasets cover many of these activities but provide little synchronized whole-body motion data for learning loco-manipulation at scale. We build Awaken-Human, which pairs approximately 50,000 hours of egocentric stereo video with synchronized whole-body human motion and covers more than 100 skills. Building on this, we also introduce Awaken-HI (Humanoid Intelligence), a vision-language-action model for humanoid loco-manipulation that jointly predicts original human motion and retargeted robot actions through a shared action expert. We show that loco-manipulation skills transfer more effectively from people to humanoids when human trajectories directly supervise the shared action expert. Increasing human pretraining data reduces held-out robot action prediction error according to an empirical scaling law and raises the mean success rate on downstream real-robot tasks. After full-corpus pretraining and T800 adaptation, Awaken-HI achieves a mean success rate of 93.75% across eight individual tasks and outperforms GR00T N1.7 and $π_{0.5}$ in both individual and long-horizon evaluations. The same policy generalizes to objects unseen during robot post-training and to new pairings of familiar objects and destinations.

## 参考
- https://arxiv.org/abs/2611.26420
- https://engineai-robotics.github.io/Awaken-HI
