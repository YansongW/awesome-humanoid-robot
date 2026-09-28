---
$id: ent_paper_kolesnichenko_learning_expressive_humanoid_l_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning Expressive Humanoid Locomotion from Monocular Runway Videos for Robot Fashion Shows
  zh: Learning Expressive Humanoid Locomotion from Monocular Runway Videos for Robot Fashion Shows
  ko: Learning Expressive Humanoid Locomotion from Monocular Runway Videos for Robot Fashion Shows
summary:
  en: Runway walking requires coordinated control of posture, stride, foot placement, and whole-body motion to effectively
    present clothing and convey a distinctive style. However, humanoid robots used in fashion shows typically rely on locomotion
    policies optimized primarily for stability and walking speed, limiting their ability to reproduce expressive, human-like
    runway motions. In this work, we ...
  zh: 本文提出一个端到端框架，可将单目走秀视频转化为可部署的人形机器人运动策略，作者为 Kyrylo Kolesnichenko、Irvin Steve Cardenas 与 Jong-Hoon Kim。该框架在 Booster K1 人形机器人上验证，学习到的策略在所有实体试验中均未摔倒，并复现了窄步幅落脚与腿、躯干、手臂的协调运动。
  ko: Runway walking requires coordinated control of posture, stride, foot placement, and whole-body motion to effectively
    present clothing and convey a distinctive style. However, humanoid robots used in fashion shows typically rely on locomotion
    policies optimized primarily for stability and walking speed, limiting their ability to reproduce expressive, human-like
    runway motions. In this work, we ...
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
- humanoid_locomotion
- motion_retargeting
- monocular_video
- expressive_motion
- sim_to_real
- fashion_show
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-09-28'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-09-28). Bibliographic metadata from arXiv API (2609.27003);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: arXiv:2609.27003 Learning Expressive Humanoid Locomotion from Monocular Runway Videos for Robot Fashion Shows
  url: https://arxiv.org/abs/2609.27003
  date: '2026-09-22'
  accessed_at: '2026-09-28'
---

## 概述

走秀行走需要姿态、步幅、落脚位置与全身运动的协调控制，以展示服装并传达独特风格，但时装秀中的人形机器人通常依赖以稳定性和行走速度为主要目标的运动策略，难以复现富有表现力、类人的走秀动作。为此，作者提出一个端到端框架，通过动作恢复、机器人重定向、动作修正、策略训练、仿真评估与实体部署，把单目走秀视频转化为可部署的人形运动策略。该框架在 Booster K1 人形机器人上以走秀式台步动作进行评估，学习到的策略完成了全部实体试验且未摔倒，同时复现了窄步幅落脚以及腿、躯干与手臂的协调运动。结果表明该训练框架使 Booster K1 能够执行稳定且富有表现力的台步动作，展现了人形机器人在时装秀及其他表演导向场景中的应用潜力。

## 核心内容

### 问题背景
走秀行走要求对姿态、步幅、落脚位置与全身运动进行协调控制，从而有效展示服装并传达独特风格。然而，时装秀中使用的人形机器人通常依赖主要针对稳定性与行走速度优化的运动策略，这限制了它们复现富有表现力、类人走秀动作的能力。

### 方法
作者提出一个端到端框架，将单目走秀视频转化为可部署的人形机器人运动策略，流程包含以下环节：
- 动作恢复（motion recovery）
- 机器人重定向（robot retargeting）
- 动作修正（motion correction）
- 策略训练（policy training）
- 基于仿真的评估（simulation-based evaluation）
- 实体部署（physical deployment）

### 实验设置
该框架在 Booster K1 人形机器人上进行评估，使用的动作类型为走秀式台步（runway-style catwalk motions）。

### 关键结果
学习到的策略完成了全部实体试验且未发生摔倒，同时复现了走秀动作中具有代表性的窄步幅落脚，以及腿部、躯干与手臂之间的协调运动。

### 结论
结果表明，所提出的训练框架使 Booster K1 能够执行稳定且富有表现力的台步动作，凸显了人形机器人在时装秀及其他表演导向场景中的应用潜力。

## Overview

Runway walking requires coordinated control of posture, stride, foot placement, and whole-body motion to effectively present clothing and convey a distinctive style. However, humanoid robots used in fashion shows typically rely on locomotion policies optimized primarily for stability and walking speed, limiting their ability to reproduce expressive, human-like runway motions. In this work, we present an end-to-end framework that transforms monocular runway videos into deployable humanoid locomotion policies through motion recovery, robot retargeting, motion correction, policy training, simulation-based evaluation, and physical deployment. We evaluate the proposed framework on the Booster K1 humanoid robot using runway-style catwalk motions. The learned policy completed every physical trial without falling, while reproducing the characteristic narrow foot placement and coordinated movement of the legs, torso, and arms. The results demonstrate that our proposed training framework enables the Booster K1 to perform stable and expressive catwalk motions, highlighting its potential for humanoid robotic applications in fashion shows and other performance-oriented scenarios.

## 参考
- https://arxiv.org/abs/2609.27003
