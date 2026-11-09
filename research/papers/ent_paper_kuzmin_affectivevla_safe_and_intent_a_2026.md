---
$id: ent_paper_kuzmin_affectivevla_safe_and_intent_a_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'AffectiveVLA: Safe and Intent-Aware VLA Control for Human-Humanoid Social Interaction'
  zh: 'AffectiveVLA: Safe and Intent-Aware VLA Control for Human-Humanoid Social Interaction'
  ko: 'AffectiveVLA: Safe and Intent-Aware VLA Control for Human-Humanoid Social Interaction'
summary:
  en: Social touch interactions, such as handshakes, fist bumps, and hugs, require humanoid robots to infer human intent,
    generate contact-rich motions, and maintain safe physical contact. We present AffectiveVLA, an intent-gated Vision-Language-Action
    (VLA) pipeline deployed on a Unitree G1 humanoid with dexterous hands. A lightweight RGB-based model recognizes interaction
    intent from two onboard ...
  zh: AffectiveVLA 是一套面向人形机器人社交接触交互的意图门控 VLA 控制流程，由 Nikita Kuzmin、Dzmitry Tsetserukou 等人提出，并部署在配备灵巧手的 Unitree G1 上。该系统用轻量级
    RGB 模型从两路机载相机识别交互意图并转为语言提示，低置信度时抑制动作执行；团队通过 VR 遥操作采集约 1,300 条多模态交互片段，微调了 GR00T、RLDX-1、Being-H0.5 与 UnifoLM-VLA-0 四个 VLA
    模型。机器人实测中 GR00T 表现最佳，引入意图识别后其 macro-F1 从 0.75 提升至 0.90，意图模型 p95 推理延迟为 6.27 ms。
  ko: Social touch interactions, such as handshakes, fist bumps, and hugs, require humanoid robots to infer human intent,
    generate contact-rich motions, and maintain safe physical contact. We present AffectiveVLA, an intent-gated Vision-Language-Action
    (VLA) pipeline deployed on a Unitree G1 humanoid with dexterous hands. A lightweight RGB-based model recognizes interaction
    intent from two onboard ...
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
- vision_language_action
- humanoid_robot
- social_interaction
- intent_recognition
- safe_control
- unitree_g1
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-11-09'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-11-09). Bibliographic metadata from arXiv API (2611.07712);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2611.07712 AffectiveVLA: Safe and Intent-Aware VLA Control for Human-Humanoid Social Interaction'
  url: https://arxiv.org/abs/2611.07712
  date: '2026-11-05'
  accessed_at: '2026-11-09'
---

## 概述

该工作聚焦握手、碰拳、拥抱等社交触摸场景，要求人形机器人推断人类意图、生成富含接触的运动并保证物理接触安全。作者构建了意图门控的 VLA 流程：轻量级 RGB 模型基于两路机载相机判断交互意图，输出语言提示给 VLA 策略，低置信度预测会抑制动作执行以减少误触发。接触过程中按交互类型切换柔顺性配置来调节手臂阻抗，另有独立的语音触发机制启动锁存式安全停止流程。数据方面通过 VR 遥操作采集约 1,300 条多模态交互片段，用于微调 GR00T、RLDX-1、Being-H0.5 和 UnifoLM-VLA-0 四个模型。在 Unitree G1 上的实测显示 GR00T 是表现最好的单模型，加入意图识别后 macro-F1 由 0.75 升至 0.90，意图模型 p95 推理延迟 6.27 ms，说明显式意图门控能在不牺牲实时性的前提下提升社交交互可靠性。

## 核心内容

### 问题背景
社交触摸交互（握手、碰拳、拥抱）对人形机器人提出了三重挑战：推断人类意图、生成富含接触的运动、在物理接触中保持安全。作者提出 AffectiveVLA，将意图识别与 VLA 策略控制结合，部署于带灵巧手的 Unitree G1 人形机器人。

### 方法
- **意图门控**：轻量级 RGB 模型从两路机载相机识别交互意图，并转换为供 VLA 策略使用的语言提示；置信度低的预测会抑制动作执行，从而减少非预期激活。
- **接触安全**：在物理接触阶段，按交互类型采用不同的柔顺性配置来调节手臂阻抗；另设独立的语音触发机制，用于启动锁存式安全停止流程。
- **策略微调**：通过 VR 遥操作采集约 1,300 条多模态交互片段，并据此微调四个 VLA 模型：GR00T、RLDX-1、Being-H0.5、UnifoLM-VLA-0。

### 实验设置与关键结果
- 在机器人本体上进行评估，GR00T 被识别为表现最好的独立模型。
- 将意图识别集成进 GR00T 后，其 macro-F1 分数从 0.75 提升到 0.90。
- 意图模型的 p95 推理延迟为 6.27 ms。

### 结论
结果表明，显式意图门控能够提升基于 VLA 的社交交互可靠性，同时不损害实时运行性能。

## Overview

Social touch interactions, such as handshakes, fist bumps, and hugs, require humanoid robots to infer human intent, generate contact-rich motions, and maintain safe physical contact. We present AffectiveVLA, an intent-gated Vision-Language-Action (VLA) pipeline deployed on a Unitree G1 humanoid with dexterous hands. A lightweight RGB-based model recognizes interaction intent from two onboard cameras and converts it into a language prompt for the VLA policy. Low-confidence predictions suppress motion execution, reducing unintended activations. During physical contact, interaction-specific compliance profiles adjust arm impedance, while an independent voice-triggered mechanism initiates a latched safe-stop procedure. Using VR teleoperation, we collected approximately 1,300 multimodal interaction episodes and fine-tuned four VLA models: GR00T, RLDX-1, Being-H0.5, and UnifoLM-VLA-0. On-robot evaluation identifies GR00T as the best-performing standalone model. Integrating intent recognition increases its macro-F1 score from 0.75 to 0.90, while the intent model achieves a p95 inference latency of 6.27 ms. These results demonstrate that explicit intent gating improves the reliability of VLA-based social interaction without compromising real-time operation.

## 参考
- https://arxiv.org/abs/2611.07712
