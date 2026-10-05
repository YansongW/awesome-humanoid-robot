---
$id: ent_paper_shao_humanoid_loco_manipulation_wit_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Humanoid Loco-Manipulation With Discrete VLA Model
  zh: Humanoid Loco-Manipulation With Discrete VLA Model
  ko: Humanoid Loco-Manipulation With Discrete VLA Model
summary:
  en: Vision-language-action (VLA) models using discrete action tokens have proven effective for controling robotic arms on
    manipulation tasks. For a humanoid, however, the whole-body action space -- legs, torso, arms, and hands -- is far higher-dimensional
    and heterogeneous, raising tokenization, training, and real-time inference challenges that the previous VLA models do
    not address. We present ...
  zh: Holo-M 是首个面向人形机器人移动操作（loco-manipulation）的离散 VLA 模型，由 Wenxin Shao、Siqi Chai、Kun Li、Kerou Zhang、Xinzhou Jiang、Wei Xu、Qiang
    Liu 提出。它通过统一动作分词器将人形动作空间拆分为末端执行器、身体、手部与运动学四个部位专属分词器，并把动作 token 扩充进语言模型词表，从而避免使用独立连续动作专家带来的知识隔离问题。在 SIMPLE 人形移动操作基准上，Holo-M
    在通用与专用两类评测中均取得最高成功率，且明显领先第二名。
  ko: Vision-language-action (VLA) models using discrete action tokens have proven effective for controling robotic arms on
    manipulation tasks. For a humanoid, however, the whole-body action space -- legs, torso, arms, and hands -- is far higher-dimensional
    and heterogeneous, raising tokenization, training, and real-time inference challenges that the previous VLA models do
    not address. We present ...
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
- vision_language_action
- discrete_action_tokens
- action_tokenizer
- discrete_diffusion_decoding
- whole_body_control
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-10-05'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-10-05). Bibliographic metadata from arXiv API (2609.35709);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: arXiv:2609.35709 Humanoid Loco-Manipulation With Discrete VLA Model
  url: https://arxiv.org/abs/2609.35709
  date: '2026-09-28'
  accessed_at: '2026-10-05'
---

## 概述

该工作针对人形机器人全身动作空间维度高、结构异构的问题，指出现有面向机械臂的离散动作 token VLA 模型难以直接适用。作者提出 Holo-M，将其称为首个用于人形移动操作的离散 VLA 模型，核心思路是把动作 token 直接加入语言模型词表，从模型内部利用语言模型能力。为统一不同本体与数据来源，模型设计了统一动作分词器，按身体部位分解为末端执行器、身体、手部和运动学四个分词器，可支持人形遥操作、第一人称人类视频与仿真数据的训练。为满足实时控制需求，各部位动作 token 采用分组离散扩散解码而非自回归解码。在 SIMPLE 基准的通用与专用评测中，Holo-M 均取得最高成功率并显著领先第二名，作者表示将公开全部代码与模型权重。

## 核心内容

### 问题背景
使用离散动作 token 的 vision-language-action（VLA）模型已在机械臂操作任务上被证明有效。但人形机器人的全身动作空间涵盖腿、躯干、手臂与手，维度远高于机械臂且高度异构，由此带来分词、训练与实时推理方面的挑战，此前的 VLA 模型并未解决这些问题。

### 方法
- 提出 Holo-M，作者称其为首个面向人形 loco-manipulation 的离散 VLA 模型，其核心做法是扩展语言模型的词表，加入动作 token，从而在模型内部直接利用语言模型能力。
- 设计统一动作分词器，将人形动作空间分解为四个身体部位专属分词器：end-effector、body、hand 与 kinematics。
- 该分词方案使模型能够跨差异极大的本体与数据来源进行训练，包括人形遥操作数据、第一人称人类视频以及仿真数据。
- 通过把动作 token 加入语言模型词表，避免了使用独立连续动作专家的模型所固有的知识隔离（knowledge-insulation）问题。
- 为满足实时控制要求，各身体部位的动作 token 采用分组离散扩散解码（grouped discrete diffusion decoding），而非对动作 token 进行自回归解码。

### 实验设置
在 SIMPLE 人形 loco-manipulation 基准上开展了大量实验，评测分为 generalist 与 specialist 两类。

### 关键结果
Holo-M 在 generalist 与 specialist 两项评测中均取得最高成功率，并以显著幅度领先第二名。

### 结论
作者表示将公开全部代码与模型权重。

## Overview

Vision-language-action (VLA) models using discrete action tokens have proven effective for controling robotic arms on manipulation tasks. For a humanoid, however, the whole-body action space -- legs, torso, arms, and hands -- is far higher-dimensional and heterogeneous, raising tokenization, training, and real-time inference challenges that the previous VLA models do not address. We present Holo-M, to our knowledge the first discrete VLA model for humanoid loco-manipulation that intrinsically exploits the language model by extending its vocabulary with action tokens. In this model, we devise a unified action tokenizer that decomposes the humanoid action space into four body-part-specific tokenizers -- end-effector, body, hand, and kinematics -- enabling training across drastically different embodiments and data sources, including humanoid teleoperation, ego-centric human video, and simulation. By extending the language model's vocabulary with these action tokens, we avoid the knowledge-insulation problem inherent to the models that use separate continuous action experts. To meet real-time control requirements, we decode each body part's action tokens through grouped discrete diffusion decoding, rather than using autoregression on the action tokens. We have conducted extensive experiments on the SIMPLE humanoid loco-manipulation benchmark, in which Holo-M achieves the highest success rates in both the generalist and specialist evaluations, leading the second best by significant margins. We will release all the code and model weights.

## 参考
- https://arxiv.org/abs/2609.35709
