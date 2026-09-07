---
$id: ent_paper_viet_development_of_a_humanoid_robo_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Development of a Humanoid Robot Prototype for Multimodal Human-Robot Interaction
  zh: Development of a Humanoid Robot Prototype for Multimodal Human-Robot Interaction
  ko: Development of a Humanoid Robot Prototype for Multimodal Human-Robot Interaction
summary:
  en: Human-robot interaction (HRI) enables intuitive and intelligent collaboration between humans and robots in real-world
    environments. This paper introduces a humanoid robot prototype designed as a flexible testbed for developing and integrating
    artificial intelligence (AI) modules in HRI tasks. The system features a 12 degree-of-freedom (DOFs) dual-arm mechanism
    and a 2 DOFs head with an expressive ...
  zh: 本文介绍了一款用于多模态人机交互（HRI）研究的人形机器人原型，由越南研究团队开发，作为集成人工智能模块的灵活测试平台。该系统配备12自由度双臂和2自由度头部（带表情LCD屏），集成手势识别、物体检测和语音命令处理三大AI模块，实验显示平均操作误差约1.83厘米，任务准确率超90%。
  ko: Human-robot interaction (HRI) enables intuitive and intelligent collaboration between humans and robots in real-world
    environments. This paper introduces a humanoid robot prototype designed as a flexible testbed for developing and integrating
    artificial intelligence (AI) modules in HRI tasks. The system features a 12 degree-of-freedom (DOFs) dual-arm mechanism
    and a 2 DOFs head with an expressive ...
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
- multimodal_hri
- gesture_recognition
- object_detection
- voice_command
- ai_testbed
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-09-07'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-09-07). Bibliographic metadata from arXiv API (2609.05361);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: arXiv:2609.05361 Development of a Humanoid Robot Prototype for Multimodal Human-Robot Interaction
  url: https://arxiv.org/abs/2609.05361
  date: '2026-09-04'
  accessed_at: '2026-09-07'
---

## 概述

该人形机器人原型旨在为HRI任务中AI模块的开发与集成提供可复现的测试平台。硬件上采用定制控制器板配合机载Jetson模块实现实时AI处理，软件层面整合了基于MediaPipe和LSTM的手势识别、基于YOLO的物体检测与3D定位，以及结合语音识别和LLM语义解析的语音命令处理。通过定位精度实验验证，系统平均操作误差约1.83厘米，手势识别准确率达96%，语音识别达92%，整体任务准确率超90%，证明了其作为研究平台的实用性和可访问性。

## 核心内容

### 问题背景
人机交互（HRI）旨在实现人类与机器人在真实环境中的直观智能协作。然而，现有平台往往缺乏灵活性或可复现性，难以作为AI模块开发的通用测试床。为此，本研究设计了一款人形机器人原型，专注于多模态交互能力的集成与验证。

### 系统设计
- **硬件架构**：采用12自由度双臂机构，支持精细操作；头部具有2自由度，配备可表达面部情感的LCD屏幕。所有硬件由定制设计的控制器板统一控制，并搭载机载Jetson模块，支持实时AI处理。
- **AI模块集成**：
  1. **手势识别**：使用MediaPipe Pose提取姿态关键点，结合LSTM分类器进行动作分类。
  2. **物体检测**：基于YOLO实现目标检测，并完成3D空间定位。
  3. **语音命令处理**：通过语音识别技术获取输入，再利用大语言模型（LLM）进行语义解析，以理解用户指令。

### 实验设置与结果
- **定位精度实验**：评估机械臂的操作准确性，结果显示平均操作误差约为1.83厘米。
- **任务性能验证**：为展示系统多功能性，进行了多模态交互任务测试，整体任务准确率超过90%。其中，手势识别准确率达到96%，语音识别准确率达到92%。

### 结论
实验结果证实了该系统作为人形机器人研究平台的有效性，其设计强调可复现性和易用性，为HRI领域的AI模块开发与原型验证提供了实用工具。

## Overview

Human-robot interaction (HRI) enables intuitive and intelligent collaboration between humans and robots in real-world environments. This paper introduces a humanoid robot prototype designed as a flexible testbed for developing and integrating artificial intelligence (AI) modules in HRI tasks. The system features a 12 degree-of-freedom (DOFs) dual-arm mechanism and a 2 DOFs head with an expressive LCD screen to express facial emotions. All hardware components are controlled by a custom-designed controller board with real-time AI processing supported by an onboard Jetson module. The system incorporates three AI modules: (1) gesture recognition using MediaPipe Pose and an LSTM classifier, (2) object detection with YOLO and 3D localization, and (3) voice-command processing through speech recognition and large language model(LLM)-based semantic parsing. The platform is validated through experiments on positioning accuracy, with results showing average manipulation errors of approximately 1.83 cm. To demonstrate its versatility, experimental results show over 90% task accuracy, with gesture recognition reaching 96%, speech recognition reaching 92%. The results confirm the effectiveness of the proposed system as a reproducible and accessible humanoid platform for research and prototyping in HRI.

## 参考
- https://arxiv.org/abs/2609.05361
