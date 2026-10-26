---
$id: ent_paper_gu_haf_vla_hierarchical_action_fl_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'HAF-VLA: Hierarchical Action Flow Framework for Humanoid Vision-Language-Action Control'
  zh: 'HAF-VLA: Hierarchical Action Flow Framework for Humanoid Vision-Language-Action Control'
  ko: 'HAF-VLA: Hierarchical Action Flow Framework for Humanoid Vision-Language-Action Control'
summary:
  en: Humanoid robots hold great promise as general-purpose agents in human-centered environments, yet adapting generalist
    vision-language-action (VLA) policies to real-world humanoid loco-manipulation remains challenging. Unlike fixed-base
    or wheeled manipulators, humanoids must coordinate locomotion, posture, gaze, and dual-arm manipulation over a high-dimensional
    whole-body action space, where ...
  zh: HAF-VLA 是一种面向人形机器人视觉-语言-动作控制的分层动作流框架，由 Langzhe Gu、Chengkai Hou、Meng Li 等人提出。该方法在预训练的 flow-matching VLA 基础上继承视觉-语言前缀编码器与动作专家权重，通过可学习阶段嵌入与跨阶段
    KV-cache 条件机制，将全身动作分阶段逐步去噪生成。在六个真实世界任务上的实验表明，该框架显著提升了现有人形机器人移动操作模型的性能。
  ko: Humanoid robots hold great promise as general-purpose agents in human-centered environments, yet adapting generalist
    vision-language-action (VLA) policies to real-world humanoid loco-manipulation remains challenging. Unlike fixed-base
    or wheeled manipulators, humanoids must coordinate locomotion, posture, gaze, and dual-arm manipulation over a high-dimensional
    whole-body action space, where ...
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
- humanoid_loco_manipulation
- hierarchical_action_flow
- flow_matching
- whole_body_control
- cross_stage_kv_cache
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-10-26'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-10-26). Bibliographic metadata from arXiv API (2610.26584);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2610.26584 HAF-VLA: Hierarchical Action Flow Framework for Humanoid Vision-Language-Action Control'
  url: https://arxiv.org/abs/2610.26584
  date: '2026-10-19'
  accessed_at: '2026-10-26'
---

## 概述

人形机器人有望成为以人为中心环境中的通用智能体，但将通用 VLA 策略迁移到真实人形移动操作仍具挑战：人形机器人需在高维全身动作空间中协调移动、姿态、视线与双臂操作，基座或腰部动作不准确容易引发上身的不稳定补偿。为此，作者提出 HAF-VLA 分层动作流框架，基于预训练 flow-matching VLA 构建，继承其视觉-语言前缀编码器与动作专家权重，并借助可学习阶段嵌入和跨阶段 KV-cache 条件机制适配人形全身移动操作。该方法不再一次性生成完整动作块，而是在共享全身动作空间中渐进去噪：先生成移动与头部指令，再细化腰部，最后生成全身操作动作。跨阶段 KV cache 条件机制使后续阶段能够基于前序阶段的动作表示进行细化与增补，从而保持阶段间的结构依赖。六个真实世界任务的实验结果显示，该框架显著提升了现有模型在人形移动操作任务上的表现。

## 核心内容

### 问题背景

人形机器人被视为以人为中心环境中的通用智能体，但将通用视觉-语言-动作（VLA）策略适配到真实世界的人形移动操作仍存在困难。与固定基座或轮式操作平台不同，人形机器人必须在高维全身动作空间中协调移动、姿态、视线与双臂操作；基座或腰部动作若不准确，容易导致上身出现不稳定且激进的补偿动作。

### 方法

HAF-VLA 是一个分层动作流框架，构建于预训练的 flow-matching VLA 之上：

- **权重继承**：沿用预训练模型的视觉-语言前缀编码器与动作专家权重。
- **阶段适配**：引入可学习阶段嵌入与跨阶段 KV-cache 条件机制，将模型适配到人形全身移动操作。
- **渐进去噪**：不一次性生成完整动作块，而是在共享全身动作空间中分阶段去噪——先生成移动与头部指令，再细化腰部，最后生成全身操作动作。
- **跨阶段条件**：跨阶段 KV cache 条件机制让后续动作生成阶段能够基于前序阶段的动作表示细化并增补输出，从而保持各阶段之间的结构依赖。

### 实验设置

实验在六个真实世界任务上进行，用于评估该框架在人形移动操作场景中的表现。

### 关键结果

实验结果表明，该框架在六个真实世界任务上显著提升了现有模型在人形移动操作任务中的性能。

### 结论

HAF-VLA 为将强力的移动操作 VLA 模型适配到人形全身移动操作提供了一条有效路径。

## Overview

Humanoid robots hold great promise as general-purpose agents in human-centered environments, yet adapting generalist vision-language-action (VLA) policies to real-world humanoid loco-manipulation remains challenging. Unlike fixed-base or wheeled manipulators, humanoids must coordinate locomotion, posture, gaze, and dual-arm manipulation over a high-dimensional whole-body action space, where inaccurate base or waist motions can easily induce unstable and aggressive upper-body compensation. We propose HAF-VLA, a hierarchical action-flow framework for humanoid VLA control. Built upon a pretrained flow-matching VLA, HAF-VLA inherits the vision-language prefix encoder and action expert weights, and adapts them to humanoid whole-body loco-manipulation with learnable stage embeddings and cross-stage KV-cache conditioning. Instead of generating the full action chunk in a single pass, HAF-VLA progressively denoises a shared whole-body action space: first locomotion and head commands, then waist refinement, and finally full-body manipulation. To preserve structural dependencies across stages, we introduce a cross-stage KV cache conditioning mechanism, enabling subsequent action generation stages to refine and augment their outputs based on the action representations from preceding stages. Experimental results across six real-world tasks demonstrate that our framework significantly enhances the performance of existing models in humanoid loco-manipulation tasks, demonstrating an effective pathway for adapting strong mobile-manipulation VLAs to humanoid whole-body loco-manipulation.

## 参考
- https://arxiv.org/abs/2610.26584
