---
$id: ent_paper_li_0_a_latent_predictive_world_a_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: '$ω$-0: A Latent Predictive World Action Model for Concurrent Humanoid Loco-Manipulation'
  zh: '$ω$-0: A Latent Predictive World Action Model for Concurrent Humanoid Loco-Manipulation'
  ko: '$ω$-0: A Latent Predictive World Action Model for Concurrent Humanoid Loco-Manipulation'
summary:
  en: Humanoid household tasks often require concurrent loco-manipulation, where the robot must move, adjust posture, maintain
    balance, and manipulate objects as a single coordinated behavior. Yet existing humanoid policies typically decompose locomotion
    and manipulation, while recent world-action models remain either arm-centric or video-centered. We present $ω$-0, a latent
    predictive whole-body ...
  zh: $ω$-0 是一种用于人形机器人并发移动-操作任务的潜在预测全身世界动作模型，由 Zhe Li 等人提出。它直接预测控制器兼容的全身动作潜在变量，并通过轻量级未来观测嵌入实现视觉前瞻，在 11 项真实世界家务任务中优于多种基线方法。
  ko: Humanoid household tasks often require concurrent loco-manipulation, where the robot must move, adjust posture, maintain
    balance, and manipulate objects as a single coordinated behavior. Yet existing humanoid policies typically decompose locomotion
    and manipulation, while recent world-action models remain either arm-centric or video-centered. We present $ω$-0, a latent
    predictive whole-body ...
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
- whole_body_control
- world_action_model
- latent_prediction
- loco_manipulation
- household_robotics
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-08-10'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-08-10). Bibliographic metadata from arXiv API (2608.06375);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2608.06375 $ω$-0: A Latent Predictive World Action Model for Concurrent Humanoid Loco-Manipulation'
  url: https://arxiv.org/abs/2608.06375
  date: '2026-08-06'
  accessed_at: '2026-08-10'
---

## 概述

$ω$-0 针对人形机器人在家务场景中需要同时移动、调整姿态、保持平衡和操作物体的并发移动-操作问题，提出了一种统一的潜在预测世界动作模型。该模型以语言指令、当前视觉观测和机器人本体感受状态为输入，直接输出控制器兼容的全身动作潜在变量，避免了传统方法中移动与操作分离或仅关注手臂/视频的局限。通过耦合潜在视觉前瞻与扩散式全身动作生成，$ω$-0 支持第一人称 RGB、第三人称 RGB 和第三人称深度输入，并利用基于控制器的仿真回放将人类/公共视觉-运动先验转化为机器人可执行的动作潜在变量。作者还收集了 $ω$-HOME 数据集，包含 40 多小时的真实世界家务数据，并在 11 项任务上验证了模型的优越性能。

## 核心内容

### 问题背景
人形机器人在真实家庭环境中执行任务时，往往需要并发移动-操作（concurrent loco-manipulation），即同时进行移动、姿态调整、平衡维持和物体操作，这些行为必须作为一个协调的整体。然而，现有的人形机器人策略通常将移动和操作分解为独立模块，而近期出现的世界动作模型要么以手臂为中心，要么以视频重建为中心，难以满足全身协调的需求。

### 方法
$ω$-0 是一个潜在预测的全身世界动作模型，其核心设计包括：
- **输入与输出**：模型接收语言指令、当前视觉观测（支持第一人称 RGB、第三人称 RGB 和第三人称深度）以及机器人本体感受状态，直接预测控制器兼容的全身动作潜在变量，用于真实机器人执行。
- **潜在预测目标**：不同于重建未来视频，$ω$-0 学习紧凑的未来观测嵌入作为轻量级预测目标，将潜在视觉前瞻与基于扩散的全身动作生成相结合。
- **仿真回放机制**：利用基于控制器的仿真回放，将人类/公共视觉-运动先验（如 SMPL 动作）转化为机器人可执行的动作潜在变量，弥合仿真与真实之间的差距。

### 数据集
作者收集了 $ω$-HOME 数据集，包含 40 多小时的真实世界家务人形机器人数据，具有同步的多视角观测、全身 SMPL 动作、机器人状态和动作潜在变量，为模型训练提供了丰富的多模态数据。

### 实验与结果
在 11 项真实世界家务任务上进行了实验，结果表明：
- 单个 $ω$-0 模型能够生成平滑的“边移动边操作”行为，无需任务特定微调。
- 与代表性的模仿学习（IL）、视觉-语言-动作（VLA）模型、人形机器人策略和世界动作模型（WAM）基线相比，$ω$-0 在任务成功率、行为平滑性和全身协调性方面均表现出一致的优势。

### 结论
$ω$-0 通过潜在预测和全身动作生成的统一框架，有效解决了人形机器人并发移动-操作问题，展示了在真实世界家务场景中的实用性和泛化能力。

## Overview

Humanoid household tasks often require concurrent loco-manipulation, where the robot must move, adjust posture, maintain balance, and manipulate objects as a single coordinated behavior. Yet existing humanoid policies typically decompose locomotion and manipulation, while recent world-action models remain either arm-centric or video-centered. We present $ω$-0, a latent predictive whole-body world-action model for real-world humanoid concurrent loco-manipulation. Given a language instruction, current visual observation, and robot proprioceptive state, $ω$-0 directly predicts controller-compatible whole-body action latents for real-robot execution. Rather than reconstructing future videos, $ω$-0 learns compact future observation embeddings as a lightweight predictive objective, coupling latent visual foresight with diffusion-based whole-body action generation. The model supports egocentric RGB, exocentric RGB, and exocentric depth inputs, and leverages controller-based simulation replay to ground human/public visual-motion priors into robot-executable action latents. We further collect $ω$-HOME, a 40+ hour real-world household humanoid dataset with synchronized multi-view observations, whole-body SMPL motions, robot states, and action latents. Real-world experiments on 11 household tasks demonstrate that a single $ω$-0 model can produce smooth manipulate-while-moving behaviors and consistently outperform representative imitation learning, VLA, humanoid, and WAM baselines.

## 参考
- https://arxiv.org/abs/2608.06375
