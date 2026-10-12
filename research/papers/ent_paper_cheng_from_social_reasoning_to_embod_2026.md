---
$id: ent_paper_cheng_from_social_reasoning_to_embod_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'From Social Reasoning to Embodied Interaction: An Agentic Framework for Social Robots'
  zh: 'From Social Reasoning to Embodied Interaction: An Agentic Framework for Social Robots'
  ko: 'From Social Reasoning to Embodied Interaction: An Agentic Framework for Social Robots'
summary:
  en: 'Natural face-to-face human--robot interaction requires a robot to understand an evolving social situation, decide when
    to engage, and express its intent through coordinated physical behavior. Yet existing approaches rarely close this loop:
    foundation-model agents provide increasingly capable multimodal reasoning and memory but remain largely disembodied, while
    expressive virtual agents do not ...'
  zh: ARISE 是一个面向社交人形机器人的统一框架，旨在打通智能体推理与具身社交表达之间的闭环，由 Ziyu Cheng、Yuewen Guo、Zhirui Liu、Dong Zhang、Haotao Lu、Jingyi Yu、Ye Shi、Jingya
    Wang 提出。该框架部署在 Sophia 人形机器人上，整合多模态上下文理解、长期记忆以及反应式与主动式交互，决定何时交流、交流什么，并通过流式执行将社交意图转化为与语音和机械面部表情协调的机器人原生手势。在 Sophia 上的评估显示其具备较高的感知交互质量、富有表现力且协调良好的具身行为，并借助流式执行显著降低了延迟。
  ko: 'Natural face-to-face human--robot interaction requires a robot to understand an evolving social situation, decide when
    to engage, and express its intent through coordinated physical behavior. Yet existing approaches rarely close this loop:
    foundation-model agents provide increasingly capable multimodal reasoning and memory but remain largely disembodied, while
    expressive virtual agents do not ...'
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
- social_robotics
- humanoid_robot
- embodied_interaction
- multimodal_reasoning
- long_term_memory
- streaming_execution
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-10-12'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-10-12). Bibliographic metadata from arXiv API (2610.05964);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2610.05964 From Social Reasoning to Embodied Interaction: An Agentic Framework for Social Robots'
  url: https://arxiv.org/abs/2610.05964
  date: '2026-10-05'
  accessed_at: '2026-10-12'
---

## 概述

自然的人机面对面交互要求机器人理解不断演变的社会情境、判断何时介入，并通过协调的身体行为表达意图。现有方法难以形成闭环：基础模型智能体具备日益强大的多模态推理与记忆能力，但大多缺乏具身性；表现力强的虚拟智能体不受真实机器人物理约束；而实体社交机器人往往只部分解决社交推理或具身表达中的一方面。为此，作者提出 ARISE，一个在 Sophia 人形机器人上统一智能体推理与交互式社交具身的框架。ARISE 整合多模态上下文理解、长期记忆以及反应式与主动式交互，以确定何时交流与交流内容，并通过流式执行把社交意图转化为与语音和机械面部表情协调的机器人原生手势。在 Sophia 上的广泛评估表明，该框架在感知交互质量、具身行为的表达力与协调性方面表现良好，并通过流式执行大幅降低延迟。

## 核心内容

### 问题背景
自然的面对面人机交互要求机器人能够理解不断演变的社会情境、决定何时介入，并通过协调的物理行为表达自身意图。然而现有方法很少真正闭合这一循环：
- 基础模型智能体虽具备日益强大的多模态推理与记忆能力，但基本处于“无身体”状态；
- 表现力丰富的虚拟智能体不受真实机器人的物理约束；
- 实体社交机器人通常只部分地处理社交推理或具身表达。

### 方法
作者提出 ARISE，一个在 Sophia 人形机器人上统一 Agentic Reasoning 与 Interactive Social Embodiment 的框架。其核心组成包括：
- 多模态上下文理解；
- 长期记忆；
- 反应式与主动式交互，用于判断何时交流以及交流什么；
- 将社交意图转化为机器人原生手势，并与语音和机械面部表情相协调；
- 通过流式执行（streaming execution）实现上述过程。

### 实验设置
评估在 Sophia 人形机器人上进行，围绕感知交互质量、具身行为的表达力与协调性，以及流式执行带来的延迟表现展开。

### 关键结果
- 在 Sophia 上展现出较强的感知交互质量；
- 具身行为富有表现力且协调良好；
- 通过流式执行实现了显著的延迟降低。

### 结论
结果凸显了在人形机器人自然交互中，联合推理“交流什么”“何时介入”以及“如何物理地表达社交意图”的重要性。项目主页为 https://robosocial.github.io/。

## Overview

Natural face-to-face human--robot interaction requires a robot to understand an evolving social situation, decide when to engage, and express its intent through coordinated physical behavior. Yet existing approaches rarely close this loop: foundation-model agents provide increasingly capable multimodal reasoning and memory but remain largely disembodied, while expressive virtual agents do not face the physical constraints of real robots, and physical social robots typically address social reasoning and embodied expression only partially. We present ARISE, a unified framework that bridges Agentic Reasoning and Interactive Social Embodiment on the Sophia humanoid robot. ARISE integrates multimodal context understanding, long-term memory, and reactive and proactive interaction to determine when and what to communicate, and translates social intent into robot-native gestures coordinated with speech and mechanical facial expressions through streaming execution. Extensive evaluations on Sophia demonstrate strong perceived interaction quality, expressive and well-coordinated embodied behavior, and substantial latency reductions through streaming execution. These results highlight the importance of jointly reasoning about what to communicate, when to engage, and how to physically express social intent for natural interaction with humanoid robots. Project Page: https://robosocial.github.io/

## 参考
- https://arxiv.org/abs/2610.05964
