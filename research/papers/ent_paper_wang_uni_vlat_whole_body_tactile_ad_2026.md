---
$id: ent_paper_wang_uni_vlat_whole_body_tactile_ad_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Uni-VLaT: Whole-Body Tactile Adaptation of VLA Policies for Humanoid Loco-Manipulation'
  zh: 'Uni-VLaT: Whole-Body Tactile Adaptation of VLA Policies for Humanoid Loco-Manipulation'
  ko: 'Uni-VLaT: Whole-Body Tactile Adaptation of VLA Policies for Humanoid Loco-Manipulation'
summary:
  en: Physical contact often determines how a humanoid should respond during loco-manipulation, yet vision and proprioception
    alone are often insufficient to characterize physical interaction, especially when the contact region is occluded. Unlike
    sparse force or torque measurements at predefined regions, distributed tactile sensing preserves spatially resolved contact
    patterns across the robot body. ...
  zh: Uni-VLaT 是一种将全身分布式触觉信息融入视觉-语言-动作（VLA）策略的方法，用于人形机器人的接触密集型 loco-manipulation 控制。该方法由 Zihao Wang、Shutong Liu、Siqi Zheng、Liu
    Cao、Ruoqu Chen、Rundong Liu、Yanchao Yang、Mengdi Xu 提出，其触觉通路的隐状态除用于动作生成外，还用于预测未来的触觉、本体感觉与视觉表征。在五项真实机器人任务上，Uni-VLaT 取得 75%
    的平均成功率，比无触觉输入的基线高 43 个百分点，比无预测监督的触觉基线高 7 个百分点。
  ko: Physical contact often determines how a humanoid should respond during loco-manipulation, yet vision and proprioception
    alone are often insufficient to characterize physical interaction, especially when the contact region is occluded. Unlike
    sparse force or torque measurements at predefined regions, distributed tactile sensing preserves spatially resolved contact
    patterns across the robot body. ...
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
- humanoid_loco_manipulation
- whole_body_tactile_sensing
- vision_language_action
- tactile_prediction
- multimodal_representation
- contact_rich_control
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-10-05'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-10-05). Bibliographic metadata from arXiv API (2609.35450);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2609.35450 Uni-VLaT: Whole-Body Tactile Adaptation of VLA Policies for Humanoid Loco-Manipulation'
  url: https://arxiv.org/abs/2609.35450
  date: '2026-09-28'
  accessed_at: '2026-10-05'
---

## 概述

物理接触往往决定人形机器人在 loco-manipulation 中应如何响应，但仅靠视觉与本体感觉难以刻画物理交互，尤其在接触区域被遮挡时。与在预设区域进行稀疏的力或力矩测量不同，分布式触觉感知能够保留机器人全身空间分辨的接触模式。为此，作者研究如何将这种全身触觉信息整合进 VLA 策略以实现接触密集型控制，并提出 Uni-VLaT：它引入一条触觉通路，其隐状态不仅用于动作生成，还用于预测未来的触觉、本体感觉与视觉表征。这一预测目标构建了以触觉为锚点的多模态上下文，促使模型对物理世界形成更结构化的理解。在覆盖触觉触发行走、持续物理交互、人机接触与 loco-manipulation 的五项真实机器人任务上，Uni-VLaT 达到 75% 的平均成功率。

## 核心内容

### 问题背景
在 humanoid loco-manipulation 中，物理接触常常决定机器人应如何响应。然而仅依赖视觉与本体感觉往往不足以刻画物理交互，特别是当接触区域被遮挡时。与在预设区域进行稀疏的力或力矩测量不同，分布式触觉感知能够保留机器人全身空间分辨的接触模式。因此，本文研究如何将全身触觉信息整合进 vision-language-action（VLA）策略，用于接触密集型控制。

### 方法
作者提出 Uni-VLaT，其核心是引入一条触觉通路。该通路的隐状态不仅被训练用于动作生成，还被训练用于预测未来的触觉、本体感觉与视觉表征。这一预测目标构建了以触觉为锚点的多模态上下文，促使模型对物理世界形成更结构化的理解。

### 实验设置
评估覆盖五项真实机器人任务，涉及触觉触发行走、持续物理交互、人机接触以及 loco-manipulation。

### 关键结果
- Uni-VLaT 取得 75% 的平均成功率。
- 相比无触觉输入的基线高出 43 个百分点。
- 相比有触觉输入但无预测监督的基线高出 7 个百分点。
- 在两个预训练 VLA 主干上，该方法使 Table Sweeping 在两个主干上均提升 30 个百分点，使 Back-Tap Walking 提升 85–90 个百分点。
- 消融实验进一步表明，上下文化的触觉预测与绝对未来目标对性能至关重要。

### 结论
结果表明，预测式触觉学习为将预训练 VLA 策略扩展到全身物理交互提供了一条有效路径。

## Overview

Physical contact often determines how a humanoid should respond during loco-manipulation, yet vision and proprioception alone are often insufficient to characterize physical interaction, especially when the contact region is occluded. Unlike sparse force or torque measurements at predefined regions, distributed tactile sensing preserves spatially resolved contact patterns across the robot body. We therefore study how to integrate such whole-body tactile information into vision-language-action (VLA) policies for contact-rich control. Our approach, Uni-VLaT, introduces a tactile pathway whose latent state is trained not only for action generation, but also to predict future tactile, proprioceptive, and visual representations. This predictive objective builds a tactile-anchored multimodal context, encouraging a more structured understanding of the physical world. We evaluate Uni-VLaT on five real-robot tasks covering tactile-triggered locomotion, sustained physical interaction, human-robot contact, and loco-manipulation. Uni-VLaT achieves a 75% average success rate, outperforming a baseline without tactile input by 43 points and a tactile-input baseline without predictive supervision by 7 points. Across two pretrained VLA backbones, our method improves Table Sweeping by 30 points on both backbones and Back-Tap Walking by 85-90 points. Ablations further show that contextualized tactile prediction and absolute future targets are critical to performance. These results indicate that predictive tactile learning provides an effective route for extending pretrained VLA policies to whole-body physical interaction.

## 参考
- https://arxiv.org/abs/2609.35450
