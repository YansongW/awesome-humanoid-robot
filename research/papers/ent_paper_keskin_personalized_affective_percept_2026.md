---
$id: ent_paper_keskin_personalized_affective_percept_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Personalized Affective Perception via Continual Learning in Human-Agent Negotiation
  zh: Personalized Affective Perception via Continual Learning in Human-Agent Negotiation
  ko: Personalized Affective Perception via Continual Learning in Human-Agent Negotiation
summary:
  en: Self-interested intelligent agents that negotiate with humans should interpret nonverbal expressions and adapt their
    behavior accordingly. However, generic facial-affect models degrade across individuals and contexts, creating a generalization
    gap. We introduce an affect-adaptive negotiation strategy that incorporates Continual Learning with Imagination for Facial
    Expression Recognition (CLIFER) ...
  zh: 该研究提出一种情感自适应谈判策略，将基于想象力的持续学习面部表情识别方法 CLIFER 用于实时个性化效价-唤醒感知，并通过差分反馈把效价-唤醒的方向与强度变化转化为智能体目标效用的调整。作者包括 Mehmet Onur Keskin、Berk
    Buzcu、Nikhil Churamani、Reyhan Aydogan、Hatice Gunes 与 Catholijn Jonker。在 66 名参与者与人形机器人谈判的被试内实验中，启用持续学习的智能体相比 FaceChannel
    基线取得显著更高的个体效用，并引发更高的参与者让步率。
  ko: Self-interested intelligent agents that negotiate with humans should interpret nonverbal expressions and adapt their
    behavior accordingly. However, generic facial-affect models degrade across individuals and contexts, creating a generalization
    gap. We introduce an affect-adaptive negotiation strategy that incorporates Continual Learning with Imagination for Facial
    Expression Recognition (CLIFER) ...
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
- continual_learning
- facial_expression_recognition
- human_agent_negotiation
- affective_perception
- humanoid_robot
- personalization
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-11-16'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-11-16). Bibliographic metadata from arXiv API (2611.14247);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: arXiv:2611.14247 Personalized Affective Perception via Continual Learning in Human-Agent Negotiation
  url: https://arxiv.org/abs/2611.14247
  date: '2026-11-10'
  accessed_at: '2026-11-16'
---

## 概述

针对通用面部情感模型在个体与情境间泛化不足的问题，本文提出一种情感自适应谈判策略，把持续学习与想象力结合的面部表情识别方法 CLIFER 引入效价-唤醒感知的实时个性化。系统通过差分反馈将效价-唤醒变化的方向和强度映射为智能体目标效用的调整，并采用异步架构在交互过程中于后台更新 CLIFER。研究采用平衡化的被试内设计，66 名参与者与人形机器人进行谈判，比较持续学习条件与 FaceChannel 基线。结果显示持续学习条件在个体效用与参与者让步率上显著更优，平均唤醒估计更高且输出范围更宽，而参与者效用与 Nash 距离在两种条件间无显著差异。

## 核心内容

### 问题背景
与人类谈判的自利智能体需要解读非语言表达并据此调整行为。然而，通用的面部情感模型在不同个体与情境下性能下降，形成泛化差距，难以支撑面向具体用户的实时情感感知。

### 方法
- 提出情感自适应谈判策略，将 Continual Learning with Imagination for Facial Expression Recognition（CLIFER）用于效价-唤醒感知的实时个性化。
- 通过差分反馈机制，把效价-唤醒变化的方向与强度转换为智能体目标效用的调整量。
- 采用异步架构，在实时交互过程中于后台更新 CLIFER，避免更新过程阻塞谈判交互。

### 实验设置
- 采用平衡化（counterbalanced）被试内研究设计。
- 共 66 名参与者与人形机器人进行谈判。
- 对照条件为 FaceChannel 基线。

### 关键结果
- 启用持续学习（CL）的智能体取得显著更高的个体效用。
- CL 条件引发显著更高的参与者让步率。
- CL 条件得到显著更高的平均唤醒估计，且输出范围更宽。
- 参与者效用与 Nash 距离在两种条件之间无显著变化。

### 结论
结果支持将持续情感个性化与差分反馈相结合用于实时谈判的实用价值。

## Overview

Self-interested intelligent agents that negotiate with humans should interpret nonverbal expressions and adapt their behavior accordingly. However, generic facial-affect models degrade across individuals and contexts, creating a generalization gap. We introduce an affect-adaptive negotiation strategy that incorporates Continual Learning with Imagination for Facial Expression Recognition (CLIFER) to personalize valence-arousal perception in real time. Differential feedback converts changes in valence-arousal direction and intensity into adjustments of the agent's target utility. An asynchronous architecture updates CLIFER in the background during live interaction. In a counterbalanced within-subject study in which 66 participants negotiated with a humanoid robot, the CL-enabled agent achieved significantly higher individual utility and elicited higher participant concession rates than the FaceChannel baseline. The CL condition yielded significantly higher mean arousal estimates, alongside a broader output range. Participant utility and Nash distance did not change significantly between conditions. These outcomes support the practical value of coupling continual affective personalization with differential feedback for real-time negotiation.

## 参考
- https://arxiv.org/abs/2611.14247
