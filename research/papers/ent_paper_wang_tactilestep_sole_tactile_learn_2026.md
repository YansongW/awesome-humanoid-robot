---
$id: ent_paper_wang_tactilestep_sole_tactile_learn_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'TactileStep: Sole Tactile Learning for Regulating Foot-Terrain Interaction in Humanoid Locomotion'
  zh: 'TactileStep: Sole Tactile Learning for Regulating Foot-Terrain Interaction in Humanoid Locomotion'
  ko: 'TactileStep: Sole Tactile Learning for Regulating Foot-Terrain Interaction in Humanoid Locomotion'
summary:
  en: 'Humanoid parkour policies can traverse various terrains, but task completion may mask challenges of harsh landings,
    edge contacts, and unstable stance contacts. Humans naturally regulate foot-terrain interaction through tactile feedback,
    modulating contact compliance according to terrain stiffness. This highlights a key domain gap between humans and humanoid
    robots: the absence of rich tactile ...'
  zh: TactileStep 是一个可部署的足底触觉学习框架，将足底压力感知引入人形机器人运动控制，以实现更柔和的落地与更稳定的支撑。该工作由 Zizhuo Wang、Ming-ju Lee、Shaoting Zhu、Haozhe Lou、Hang
    Zhao、Yiming Li 完成。其核心在于让触觉仿真与真实压力鞋垫对齐，并通过接触相位感知奖励调节足-地交互，在 Unitree G1 上使峰值触地力最多降低 48.8%。
  ko: 'Humanoid parkour policies can traverse various terrains, but task completion may mask challenges of harsh landings,
    edge contacts, and unstable stance contacts. Humans naturally regulate foot-terrain interaction through tactile feedback,
    modulating contact compliance according to terrain stiffness. This highlights a key domain gap between humans and humanoid
    robots: the absence of rich tactile ...'
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
- tactile_sensing
- foot_terrain_interaction
- contact_phase_reward
- sim_to_real
- unitree_g1
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-09-28'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-09-28). Bibliographic metadata from arXiv API (2609.28959);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2609.28959 TactileStep: Sole Tactile Learning for Regulating Foot-Terrain Interaction in Humanoid Locomotion'
  url: https://arxiv.org/abs/2609.28959
  date: '2026-09-24'
  accessed_at: '2026-09-28'
---

## 概述

现有人形机器人跑酷策略虽能穿越多种地形，但任务完成可能掩盖了生硬落地、边缘接触与支撑不稳等问题。人类会借助触觉反馈依据地形刚度调节接触柔顺性，而多数人形系统缺乏丰富的触觉感知，构成了人与机器人之间的关键差距。TactileStep 通过将足底压力传感引入运动控制来应对这一问题，其做法是让触觉仿真与真实压力鞋垫对齐，使策略能够学习硬件上同样可获得的接触特征。训练中利用触觉与运动线索识别不同足接触相位，并施加相位感知奖励以鼓励更安全的落地与更稳定的支撑。在仿真与 Unitree G1 人形机器人上的多种地形评测中，该方法相较强感知基线显著降低了触地冲击。

## 核心内容

### 问题背景
人形机器人跑酷策略已能穿越多种地形，但任务完成本身可能掩盖落地生硬、边缘接触以及支撑接触不稳定等隐患。人类会自然地通过触觉反馈调节足-地交互，根据地形刚度调整接触柔顺性。这一对比揭示了人与机器人之间的关键领域差距：大多数现有人形系统缺乏丰富的触觉感知。

### 方法
TactileStep 是一个可部署的触觉学习框架，将足底压力感知引入人形运动控制，目标是实现更柔和的触地与更稳定的支撑。其关键设计包括：
- 触觉仿真与真实压力鞋垫对齐，使策略能够从硬件上同样可获得的接触特征中学习。
- 训练阶段结合触觉与运动线索，识别不同的足接触相位。
- 采用相位感知奖励，鼓励更安全的落地与更稳定的支撑姿态。

### 实验设置
方法在仿真环境以及 Unitree G1 人形机器人上进行了评测，覆盖多种地形，并与一个强感知基线进行对比。

### 关键结果
相较强感知基线，TactileStep 实现了：
- 峰值触地力最多降低 48.8%；
- 峰值 A 计权冲击噪声最多降低 30.1 dB；
- 支撑接触面积最多增加 23.8%。

### 结论
通过将足底触觉感知与仿真-硬件对齐的接触特征引入运动控制，并结合接触相位感知奖励，TactileStep 能在多种地形上改善人形机器人的落地柔顺性与支撑稳定性，验证了足底触觉在调节足-地交互方面的价值。

## Overview

Humanoid parkour policies can traverse various terrains, but task completion may mask challenges of harsh landings, edge contacts, and unstable stance contacts. Humans naturally regulate foot-terrain interaction through tactile feedback, modulating contact compliance according to terrain stiffness. This highlights a key domain gap between humans and humanoid robots: the absence of rich tactile sensing in most humanoid systems. We address this problem with TactileStep, a deployable tactile learning framework that brings sole pressure sensing into humanoid locomotion control for softer touchdowns and more stable support. TactileStep aligns tactile simulation with the real pressure insole, allowing the policy to learn from the same contact features available on hardware. During training, we use tactile and motion cues to recognize different foot-contact phases and apply phase-aware rewards that encourage safer landing and more stable stance. Evaluated in simulation and on a Unitree G1 humanoid across diverse terrains, TactileStep reduces peak touchdown force by up to 48.8% and peak A-weighted impact noise by up to 30.1 dB over a strong perceptive baseline, while increasing stance contact area by up to 23.8%.

## 参考
- https://arxiv.org/abs/2609.28959
