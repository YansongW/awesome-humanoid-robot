---
$id: ent_paper_ding_gestadapt_workspace_conditione_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'GestAdapt: Workspace-Conditioned Co-Speech Gesture Generation for Humanoid Robots'
  zh: 'GestAdapt: Workspace-Conditioned Co-Speech Gesture Generation for Humanoid Robots'
  ko: 'GestAdapt: Workspace-Conditioned Co-Speech Gesture Generation for Humanoid Robots'
summary:
  en: Co-speech gestures for robots must adapt not only to speech and embodiment, but also to the workspace available for
    performing the motion. Since the same speech can be accompanied by different gestures, a robot can respond to workspace
    constraints, e.g., gestures for speech next to a wall. In these scenarios, the robot should gesture in a suitable motion
    rather than simply correcting an ...
  zh: GestAdapt 是一个以工作空间为条件的共语手势生成框架，由 Bosong Ding、Xianglin Zhang、Miao Xin、Murat Kirtay 与 Giacomo Spigler 提出。它让机器人在生成手势时就考虑手腕可动工作空间的约束，而非事后修正无约束轨迹，并支持向不同机器人本体迁移。用户研究中对修改后工作空间约束下生成的手势给出
    3.24/5 的平均质量分，在 Reachy2 人形机器人上的对比中，该框架生成的动作在 69.7% 的比较中排名第一。
  ko: Co-speech gestures for robots must adapt not only to speech and embodiment, but also to the workspace available for
    performing the motion. Since the same speech can be accompanied by different gestures, a robot can respond to workspace
    constraints, e.g., gestures for speech next to a wall. In these scenarios, the robot should gesture in a suitable motion
    rather than simply correcting an ...
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
- co_speech_gesture
- workspace_conditioning
- humanoid_robot
- motion_retargeting
- reachy2
- gesture_generation
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-10-05'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-10-05). Bibliographic metadata from arXiv API (2609.38400);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2609.38400 GestAdapt: Workspace-Conditioned Co-Speech Gesture Generation for Humanoid Robots'
  url: https://arxiv.org/abs/2609.38400
  date: '2026-09-29'
  accessed_at: '2026-10-05'
---

## 概述

机器人共语手势不仅要适配语音与本体形态，还需适配执行动作时可用的工作空间：同一句话可以配以不同手势，因此机器人能够针对诸如"在墙边说话"这类空间限制做出相应调整，生成合适动作，而不是先做无约束动作再加以修正。为此作者提出 GestAdapt，一个以规定的手腕工作空间为条件的共语手势生成框架。该框架借助共享的运动表示，从六个互补的共语语料库中学习，并支持重定向到不同的机器人本体。定量评估显示，生成动作既贴近真实动作分布，又满足工作空间约束。用户研究中，修改工作空间约束下生成的手势平均质量分为 3.24/5，高于无工作空间变体（2.43/5），低于参考动作（3.68/5）；在真实机器人评估中，所有对比动作在相同工作空间约束下重定向到 Reachy2 人形机器人，该框架生成的动作在 69.7% 的比较中排名第一。

## 核心内容

### 问题背景
机器人共语手势的生成需要同时适配语音内容与机器人本体形态。然而，同一段语音可以对应多种不同的手势，因此当机器人处于受限空间（例如在墙边说话）时，它应当直接生成适合该空间的动作，而不是先生成无约束动作、再对其进行修正。后一种做法可能损害手势的自然性。

### 方法
作者提出 GestAdapt，一个以工作空间为条件的共语手势生成框架，其核心是将共语手势生成条件化于一个预先规定的手腕工作空间。该框架通过共享的运动表示，从六个互补的共语语料库中学习，并支持将生成动作重定向到不同的机器人本体。

### 实验设置与关键结果
- **定量评估**：生成的动作在满足工作空间约束的同时，仍保持与真实动作分布接近。
- **用户研究**：在修改后的工作空间约束下生成的手势获得平均质量分 3.24/5；该分数高于无工作空间变体（2.43/5），低于参考动作（3.68/5）。
- **真实机器人评估**：所有参与比较的动作均在相同工作空间约束下重定向到 Reachy2 人形机器人。使用该框架生成的动作在 69.7% 的比较中排名第一，优于无工作空间变体基线，也优于先重定向、后施加约束的真实动作。

### 结论
实验结果支持在生成阶段就将手势适配到可用工作空间，而不是在生成无约束轨迹之后再修改以满足工作空间约束——后者可能牺牲手势的自然性。

## Overview

Co-speech gestures for robots must adapt not only to speech and embodiment, but also to the workspace available for performing the motion. Since the same speech can be accompanied by different gestures, a robot can respond to workspace constraints, e.g., gestures for speech next to a wall. In these scenarios, the robot should gesture in a suitable motion rather than simply correcting an unconstrained one. To achieve this goal, we present GestAdapt, a workspace-conditioned framework that conditions co-speech gesture generation on a prescribed wrist workspace. The GestAdapt framework learns from six complementary co-speech corpora through a shared motion representation and supports retargeting to different robot embodiments. Quantitative evaluation shows that generated motions remain close to the real-motion distribution while respecting the workspace. In a user study, gestures generated under modified workspace constraints receive a mean quality score of 3.24/5, above our no-workspace variant (2.43/5) and below the reference motions (3.68/5). In a real robot evaluation, all compared motions are retargeted to the Reachy2 humanoid robot under identical workspace constraints. Motions generated with our framework rank first in 69.7\% of comparisons, higher than our no-workspace variant baseline and retargeted ground-truth motions constrained afterward. Overall, the results support adapting gestures to the available workspace during generation, rather than modifying unconstrained trajectories afterward to satisfy workspace constraints, potentially compromising gesture naturalness.

## 参考
- https://arxiv.org/abs/2609.38400
