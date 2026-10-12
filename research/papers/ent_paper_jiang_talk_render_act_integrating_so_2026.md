---
$id: ent_paper_jiang_talk_render_act_integrating_so_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Talk, Render, Act: Integrating Social Gesture and Digital Face with Synchronized Speech for Conversational Humanoid
    Robot'
  zh: 'Talk, Render, Act: Integrating Social Gesture and Digital Face with Synchronized Speech for Conversational Humanoid
    Robot'
  ko: 'Talk, Render, Act: Integrating Social Gesture and Digital Face with Synchronized Speech for Conversational Humanoid
    Robot'
summary:
  en: Expressive humanoid interaction requires speech, facial animation, and body gestures to form a coherent response. However,
    many full-body humanoid robots produce speech and gestures without a visually expressive face, while talking-face animation
    and robot gesture generation are typically developed separately. We present Talk, Render, Act (TRABot), an agent-based
    framework comprising specialized ...
  zh: TRABot 是一个面向人形机器人对话交互的智能体框架，由 Jin Jiang、Kun Li、Jiancong Ma、Shengcai Liao 提出，通过多个专用智能体分别负责动作原子构建、对话生成、动作规划与面部动画。该框架构建了
    Robot-Ready Semantic Motion Atoms，并引入 Semantic-Conditioned Compositional Planner，最终在实体 G1 人形机器人上部署了流式面部—语音—身体一体化系统。实验表明其在自然度、表现力与多模态一致性上取得所比较条件中的最佳整体表现。
  ko: Expressive humanoid interaction requires speech, facial animation, and body gestures to form a coherent response. However,
    many full-body humanoid robots produce speech and gestures without a visually expressive face, while talking-face animation
    and robot gesture generation are typically developed separately. We present Talk, Render, Act (TRABot), an agent-based
    framework comprising specialized ...
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
- humanoid_robot
- conversational_agent
- gesture_generation
- facial_animation
- multimodal_integration
- motion_planning
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-10-12'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-10-12). Bibliographic metadata from arXiv API (2610.06153);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2610.06153 Talk, Render, Act: Integrating Social Gesture and Digital Face with Synchronized Speech for Conversational
    Humanoid Robot'
  url: https://arxiv.org/abs/2610.06153
  date: '2026-10-05'
  accessed_at: '2026-10-12'
---

## 概述

人形机器人要实现富有表现力的交互，需要语音、面部动画与身体手势协同构成连贯回应，但现有全身体人形机器人往往只输出语音与手势而缺乏可视化面部，且说话人脸动画与机器人手势生成通常各自独立开发。为此，作者提出 TRABot，一个由动作原子构建、对话生成、动作规划与面部动画等专用智能体组成的智能体框架。为生成自然且具语义意义的手势，作者将经 G1 重定向的长时 BEAT2 动作切分为具有自然手势边界、经人工验证交际功能且轨迹可行的动作单元，即 Robot-Ready Semantic Motion Atoms。随后引入 Semantic-Conditioned Compositional Planner，在给定有序语义功能序列与估计回应时长的情况下，选择已审核的动作原子以构成最长可行动作序列，并考虑过渡与中性恢复。最后在实体 G1 人形机器人上部署流式面部—语音—身体一体化系统，将流式对话音频、音频驱动面部动画与语义规划的身体动作整合进统一的实时交互回路。

## 核心内容

### 问题背景
富有表现力的人形交互要求语音、面部动画与身体手势共同构成连贯回应。然而现实中存在两方面割裂：许多全身体人形机器人只产生语音与手势，却没有视觉上富有表现力的面部；而说话人脸动画与机器人手势生成通常被分开研发。TRABot 正是针对这一割裂提出的整合方案。

### 方法
TRABot 是一个基于智能体的框架，包含若干专用智能体，分别负责：
- 动作原子构建
- 对话生成
- 动作规划
- 面部动画

其中两项关键设计如下：

**Robot-Ready Semantic Motion Atoms（机器人可用语义动作原子）**
为产生自然且具语义意义的手势，作者将长时、经 G1 重定向的 BEAT2 动作进行切分，得到满足以下条件的动作单元：
- 具有自然的手势边界
- 交际功能经人工验证
- 轨迹可行

**Semantic-Conditioned Compositional Planner（语义条件组合规划器）**
为保持语义顺序并使身体动作与语音回应相协调，该规划器接收有序的语义功能序列与估计的回应时长，从已审核的动作原子中进行选择，以在考虑过渡与中性恢复的前提下，实现最长的可行动作序列。

### 实验设置与部署
作者在实体 G1 人形机器人上部署了 Streaming Face-Speech-Body Integration（流式面部—语音—身体一体化）系统，在统一的实时交互回路中结合：
- 流式对话音频
- 音频驱动的面部动画
- 语义规划的身体动作

### 关键结果
定量与定性实验表明，在自然度、表现力与多模态一致性方面，TRABot 在所有被比较的条件中取得了最佳的整体表现。

### 结论
TRABot 通过智能体化分工与语义条件化的动作组合规划，将语音、面部动画与身体手势统一到实时交互回路中，验证了在实体 G1 人形机器人上实现连贯多模态对话交互的可行性。

## Overview

Expressive humanoid interaction requires speech, facial animation, and body gestures to form a coherent response. However, many full-body humanoid robots produce speech and gestures without a visually expressive face, while talking-face animation and robot gesture generation are typically developed separately. We present Talk, Render, Act (TRABot), an agent-based framework comprising specialized agents for motion-atom construction, dialogue generation, motion planning, and facial animation. First, to produce natural and semantically meaningful gestures, we construct Robot-Ready Semantic Motion Atoms by segmenting long-form, G1-retargeted BEAT2 motion into units with natural gesture boundaries, human-verified communicative functions, and feasible trajectories. Second, to preserve semantic order and coordinate body motion with the spoken response, we introduce a Semantic-Conditioned Compositional Planner. Given an ordered semantic function sequence and an estimated response duration, the planner selects approved atoms to realize the longest feasible action sequence while accounting for transitions and neutral recovery. Finally, we deploy a Streaming Face-Speech-Body Integration system on a physical G1 humanoid, combining streaming dialogue audio, audio-driven facial animation, and semantically planned body motion in a unified real-time interaction loop. Quantitative and qualitative experiments demonstrate that TRAbot achieves the best overall performance among all compared conditions in terms of naturalness, expressiveness, and multimodal coherence.

## 参考
- https://arxiv.org/abs/2610.06153
