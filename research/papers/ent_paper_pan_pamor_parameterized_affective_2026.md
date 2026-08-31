---
$id: ent_paper_pan_pamor_parameterized_affective_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'PAMoR: Parameterized Affective Motion Generation in Real Time for Humanoid Robots'
  zh: 'PAMoR: Parameterized Affective Motion Generation in Real Time for Humanoid Robots'
  ko: 'PAMoR: Parameterized Affective Motion Generation in Real Time for Humanoid Robots'
summary:
  en: 'People read a humanoid robot''s motion in social settings not only for the action performed but for the affect conveyed.
    Motion carrying that affect has so far been generated for human avatars, where style is taken from a reference clip or
    an emotion word, neither of which can be quantitatively parameterized. We present PAMoR, which turns affect into a measured
    control parameter: a valence-arousal ...'
  zh: PAMoR 是一种面向人形机器人的参数化情感运动生成方法，由 Yan Pan、Lingfan Bao、Tianhu Peng 和 Chengxu Zhou 提出。它将情感转化为基于机器人运动学的效价-唤醒（V-A）坐标作为可量化控制参数，在
    29 自由度 Unitree G1 上实时生成全身运动，无需人工标注，且动作与情感均可编辑。
  ko: 'People read a humanoid robot''s motion in social settings not only for the action performed but for the affect conveyed.
    Motion carrying that affect has so far been generated for human avatars, where style is taken from a reference clip or
    an emotion word, neither of which can be quantitatively parameterized. We present PAMoR, which turns affect into a measured
    control parameter: a valence-arousal ...'
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
- affective_motion_generation
- humanoid_robots
- valence_arousal
- real_time_control
- diffusion_model
- whole_body_motion
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-08-31'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-08-31). Bibliographic metadata from arXiv API (2608.28213);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2608.28213 PAMoR: Parameterized Affective Motion Generation in Real Time for Humanoid Robots'
  url: https://arxiv.org/abs/2608.28213
  date: '2026-08-28'
  accessed_at: '2026-08-31'
---

## 概述

PAMoR 的核心创新在于将情感从定性描述（如参考片段或情感词）转化为定量控制参数：通过姿态扩展和运动能量以闭式解计算 V-A 坐标，并直接作为生成条件。该方法在共享潜在空间中训练一个动作先验和两个情感先验，在每次去噪步骤中组合，以分别控制“做什么”和“怎么做”。在感知实验中，PAMoR 生成的运动在情感识别率上超过基线，接近真人表演水平，同时保持文本到动作的保真度。

## 核心内容

### 问题背景
在社交场景中，人们不仅关注人形机器人执行的动作，还关注其传达的情感。以往的情感运动生成主要面向人类虚拟形象，风格来源为参考片段或情感词，两者均无法进行定量参数化，限制了在机器人上的精确控制与实时应用。

### 方法
PAMoR 将情感转化为可测量的控制参数：一个在机器人运动学上原生计算的效价-唤醒（V-A）坐标。该坐标通过姿态扩展和运动能量以闭式解获得，无需任何人工标注。系统在共享潜在空间中训练一个动作先验和两个情感先验，并在每个去噪步骤中组合：动作先验固定执行内容，情感先验调节执行方式。全身运动以自回归方式在 29 自由度 Unitree G1 上实时生成，动作和情感均可编辑。

### 实验设置与关键结果
- 生成的运动在完整 V-A 范围内跟踪命令坐标，同时文本到动作的保真度与仅文本基线相当。
- 在感知研究中，评估者识别命令情感的正确率为 0.38，高于两个基线，接近真人表演身体报告的 0.44。

### 结论
PAMoR 展示了将情感定量参数化并用于人形机器人实时运动生成的有效性，在保持动作保真度的同时提升了情感表达的可控性与可识别性。

## Overview

People read a humanoid robot's motion in social settings not only for the action performed but for the affect conveyed. Motion carrying that affect has so far been generated for human avatars, where style is taken from a reference clip or an emotion word, neither of which can be quantitatively parameterized. We present PAMoR, which turns affect into a measured control parameter: a valence-arousal (V-A) coordinate computed natively on robot kinematics. It is obtained in closed form from postural expansion and movement energy, and these measurements serve directly as generation conditions, with no human annotation. An action prior and two affect priors, trained in a shared latent space, are composed at each denoising step: the action prior fixes what is performed, the affect priors modulate how. Whole-body motion rolls out autoregressively on a 29-DoF Unitree G1 in real time, with action and affect both editable. Generated motion tracks the commanded V-A over its full range while text-to-motion fidelity still matches text-only baselines. In a perceptual study, raters identify the commanded emotion on 0.38 of trials, above both baselines and approaching the 0.44 reported for acted human bodies.

## 参考
- https://arxiv.org/abs/2608.28213
