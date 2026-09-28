---
$id: ent_paper_lin_mira_real_time_full_duplex_hum_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'MIRA: Real-Time Full-Duplex Human-Robot Interaction for Embodied Companions'
  zh: 'MIRA: Real-Time Full-Duplex Human-Robot Interaction for Embodied Companions'
  ko: 'MIRA: Real-Time Full-Duplex Human-Robot Interaction for Embodied Companions'
summary:
  en: '% !TEX root = ../main.tex Real-time embodied companion interaction requires a robot to infer user intent from streaming
    speech, generate timely responses, and execute expressive, interruptible motions. Existing systems typically decouple
    dialogue orchestration from gesture synthesis, relying on offline motion generation from complete audio. This separation
    leaves open how a deployed robot can ...'
  zh: MIRA 是一个面向具身陪伴场景的实时全双工人机交互统一框架，由 Lijian Lin、Ye Zhu、Fan Zhang 等作者提出。该框架在流式语音输入下同时预测回复文本与显式具身线索，将离散社交行为映射到已验证的机器人轨迹，并用
    ROSCO 前缀条件扩散模型生成流式共语动作。系统部署于 Astribot S1 人形机器人，在音频-动作对齐上相对当前最优动作生成基线具有竞争力，并实测了流式响应与打断处理能力。
  ko: '% !TEX root = ../main.tex Real-time embodied companion interaction requires a robot to infer user intent from streaming
    speech, generate timely responses, and execute expressive, interruptible motions. Existing systems typically decouple
    dialogue orchestration from gesture synthesis, relying on offline motion generation from complete audio. This separation
    leaves open how a deployed robot can ...'
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
- human_robot_interaction
- full_duplex_dialogue
- co_speech_motion_generation
- diffusion_model
- humanoid_robot
- real_time_inference
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-09-28'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-09-28). Bibliographic metadata from arXiv API (2609.24547);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2609.24547 MIRA: Real-Time Full-Duplex Human-Robot Interaction for Embodied Companions'
  url: https://arxiv.org/abs/2609.24547
  date: '2026-09-21'
  accessed_at: '2026-09-28'
---

## 概述

MIRA 针对的是实时具身陪伴交互中的核心难题：机器人需要从流式语音中推断用户意图、及时生成回复，并执行富有表现力且可被打断的动作。现有系统通常把对话编排与手势合成解耦，依赖完整音频做离线动作生成，因而难以在增量输入和不确定的轮次边界下同步回复内容、韵律时序与物理安全。为此，作者提出统一框架 MIRA，在给定流式用户语音、对话历史与语音情感时，同时预测回复文本和一个显式的具身线索，用于把回复路由到相应的物理行为。离散社交行为（如倾听、问候）被映射到经过验证的机器人轨迹，而说话类回复则配以流式生成式共语动作。共语动作由前缀条件扩散模型 ROSCO 生成，推理方案 RHPC 在保持足够长时序上下文的同时，把物理执行承诺限制在短且可打断的前缀内。交互层面由双时间尺度的 CORTEX 策略负责，结合低延迟抢话抢占与流式回复生成以及审慎的轮次决策，并由机器人侧执行层在运行中施加物理安全约束。MIRA 已部署在 Astribot S1 人形机器人上。

## 核心内容

### 问题背景

实时具身陪伴交互要求机器人从流式语音中推断用户意图、生成及时回复，并执行富有表现力且可被打断的动作。现有系统往往将对话编排与手势合成解耦，依赖完整音频进行离线动作生成。这种分离使得在增量输入与不确定轮次边界条件下，部署中的机器人如何动态同步回复内容、韵律时序与物理安全仍是一个未解问题。

### 方法

MIRA 是一个面向实时全双工具身陪伴交互的统一框架。其输入包括流式用户语音、对话历史与语音情感，输出为回复文本以及一个显式的具身线索，该线索负责把回复路由到合适的物理行为。

- **行为路由**：离散社交行为（例如倾听、问候）被映射到经过验证的机器人轨迹；说话类回复则伴随流式、生成式的共语动作。
- **ROSCO**：面向流式音频到关节动作生成的前缀条件扩散模型，用于共语动作生成。
- **RHPC**：一种推理方案，在保持足够长的时序上下文以支撑动作预测的同时，把物理执行承诺限制在一个短且可被打断的前缀内。
- **CORTEX**：交互层面的双时间尺度交互策略，将低延迟抢话抢占与流式回复生成同审慎的轮次决策相结合。
- **执行层**：机器人侧执行层在动作执行过程中施加物理安全约束。

### 实验设置与结果

MIRA 部署于 Astribot S1 人形机器人。定量评估显示，其音频-动作对齐效果相对当前最优的动作生成基线具有竞争力；真实机器人部署测量则刻画了系统的流式响应能力与打断处理表现。

### 结论

MIRA 通过统一对话编排、共语动作生成与安全执行，实现了实时全双工具身陪伴交互，并在真实人形机器人上验证了流式响应与打断处理能力。

## Overview

% !TEX root = ../main.tex Real-time embodied companion interaction requires a robot to infer user intent from streaming speech, generate timely responses, and execute expressive, interruptible motions. Existing systems typically decouple dialogue orchestration from gesture synthesis, relying on offline motion generation from complete audio. This separation leaves open how a deployed robot can dynamically synchronize response content, prosodic timing, and physical safety under incremental inputs and uncertain turn boundaries. We present MIRA, a unified framework for real-time full-duplex embodied companion interaction. Given streaming user speech, dialogue history, and vocal affect, MIRA predicts both the response text and an explicit embodiment cue that routes the response to the appropriate physical behavior. Discrete social behaviors (\eg listening and greeting) are mapped to validated robot trajectories, while speaking responses are accompanied by streaming, generative co-speech motion. For co-speech motion generation, we propose ROSCO, a prefix-conditioned diffusion model for streaming audio-to-joint motion generation. We further design RHPC, an inference scheme that maintains a sufficiently long temporal context for motion prediction while bounding physical commitment to a short, interruptible prefix. At the interaction level, we design CORTEX, a dual-timescale interaction policy that combines low-latency barge-in preemption and streaming response generation with deliberative turn decisions, backed by a robot-side execution layer that enforces physical safety constraints during execution. MIRA is deployed on an Astribot S1 humanoid robot. Quantitative evaluations demonstrate competitive audio-motion alignment relative to state-of-the-art motion-generation baselines, while real-robot deployment measurements characterize streaming responsiveness and interruption handling.

## 参考
- https://arxiv.org/abs/2609.24547
