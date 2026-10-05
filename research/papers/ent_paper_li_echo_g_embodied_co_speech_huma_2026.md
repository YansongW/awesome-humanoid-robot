---
$id: ent_paper_li_echo_g_embodied_co_speech_huma_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ECHO-G: Embodied Co-speech Humanoid mOtion Generation'
  zh: 'ECHO-G: Embodied Co-speech Humanoid mOtion Generation'
  ko: 'ECHO-G: Embodied Co-speech Humanoid mOtion Generation'
summary:
  en: Generating full-body co-speech motion for humanoid robots requires coordinating speech prosody, linguistic content,
    and embodiment-specific motion. To this end, we present ECHO-G, a framework jointly conditioned on speech audio and timed
    transcripts. Its Speech-Grounded Diffusion Transformer (SGDiT) combines frame-aligned acoustic features with token-level
    linguistic context, preserving their ...
  zh: ECHO-G 是一个面向人形机器人的全身共语手势动作生成框架，由 Yizhao Li、Pusen Gao、Ming Wang、Shaojie Shen、Shuo Yang、Hao Xu 提出。其核心是 Speech-Grounded
    Diffusion Transformer（SGDiT），同时以语音音频与带时间戳文本为条件，并采用 rectified flow matching 训练，直接在机器人动作空间中建模一对多的语句—动作关系。作者还构建了基于 BEAT2
    的音频—文本—机器人数据集与配套基准，并在实体人形机器人上完成了部署验证。
  ko: Generating full-body co-speech motion for humanoid robots requires coordinating speech prosody, linguistic content,
    and embodiment-specific motion. To this end, we present ECHO-G, a framework jointly conditioned on speech audio and timed
    transcripts. Its Speech-Grounded Diffusion Transformer (SGDiT) combines frame-aligned acoustic features with token-level
    linguistic context, preserving their ...
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
- co_speech_motion_generation
- humanoid_robots
- diffusion_transformer
- rectified_flow_matching
- audio_text_conditioning
- robot_motion_benchmark
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-10-05'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-10-05). Bibliographic metadata from arXiv API (2609.39575);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2609.39575 ECHO-G: Embodied Co-speech Humanoid mOtion Generation'
  url: https://arxiv.org/abs/2609.39575
  date: '2026-09-30'
  accessed_at: '2026-10-05'
- id: src_002
  type: website
  title: Project page
  url: https://echo-g-project.github.io/
  accessed_at: '2026-10-05'
---

## 概述

ECHO-G 针对的是人形机器人全身共语动作生成问题，需要同时协调语音韵律、语言内容与机器人自身形态带来的运动约束。该框架以语音音频和带时间戳的文本作为联合条件，通过 Speech-Grounded Diffusion Transformer（SGDiT）将帧对齐的声学特征与 token 级语言上下文结合，并保留两者在粒度上的差异。模型使用 rectified flow matching 训练，直接在机器人动作空间中建模一对多的语句—动作映射关系。为支撑训练与评测，作者提出了一个由 BEAT2 衍生的音频—文本—机器人数据集，以及覆盖共语特征、机器人动作质量和运行时效率的基准。对比评测表明，直接在机器人空间生成优于所评估的人类动作生成加重定向流程，模态消融也显示音频与文本联合条件带来的收益；作者进一步在实体人形机器人上完成部署，并通过视频评分研究验证了联合条件的优势。

## 核心内容

### 问题背景
为人形机器人生成全身共语动作，需要同时协调三个层面：语音韵律、语言内容，以及机器人本体特有的运动约束。摘要指出，现有做法中一类是先做人类动作生成再重定向到机器人，而 ECHO-G 选择直接在机器人动作空间中生成。

### 方法
- 框架以语音音频与带时间戳的文本（timed transcripts）作为联合条件。
- 核心组件为 Speech-Grounded Diffusion Transformer（SGDiT），将帧对齐的声学特征与 token 级语言上下文结合，并保留二者不同的粒度。
- 训练采用 rectified flow matching，直接在机器人空间中建模一对多的语句—动作关系。

### 数据集与基准
- 作者提出一个由 BEAT2 衍生的音频—文本—机器人数据集，用于支持训练与评测。
- 同时提出一个基准，覆盖共语特征、机器人动作质量与运行时效率三个方面。
- 数据集以及训练、推理、评测代码均通过项目主页公开。

### 关键结果
- 对比评测支持直接在机器人空间生成，优于所评估的人类动作生成与重定向流程。
- 模态消融实验显示，音频与文本联合条件相比其他方案具有优势。
- 作者在实体人形机器人上展示了部署。
- 一项补充的视频评分研究同样更倾向于联合条件方案。

### 结论
ECHO-G 通过音频—文本联合条件与机器人空间中的直接生成，为人形机器人共语动作生成提供了可行路径，并配套开放了数据集、基准与代码。

## Overview

Generating full-body co-speech motion for humanoid robots requires coordinating speech prosody, linguistic content, and embodiment-specific motion. To this end, we present ECHO-G, a framework jointly conditioned on speech audio and timed transcripts. Its Speech-Grounded Diffusion Transformer (SGDiT) combines frame-aligned acoustic features with token-level linguistic context, preserving their distinct granularities. Trained with rectified flow matching, it models one-to-many utterance-motion relationships directly in robot space. To support training and evaluation, we introduce a BEAT2-derived audio-text-robot dataset and a benchmark covering co-speech characteristics, robot-motion quality, and runtime efficiency. Comparative evaluation supports direct robot-space generation over the evaluated human-motion generation and retargeting pipelines, while modality ablations highlight the benefits of joint audio-text conditioning. We further demonstrate deployment on a physical humanoid robot. A complementary video-rating study also favors joint conditioning over the alternatives. The dataset and training, inference, and evaluation code are available through our project page.

## 参考
- https://arxiv.org/abs/2609.39575
- https://echo-g-project.github.io/
