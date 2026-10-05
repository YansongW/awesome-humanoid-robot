---
$id: ent_paper_jiang_egoalign_bridging_the_human_hu_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'EgoAlign: Bridging the Human-Humanoid Gap for Long-Range Loco-Manipulation'
  zh: 'EgoAlign: Bridging the Human-Humanoid Gap for Long-Range Loco-Manipulation'
  ko: 'EgoAlign: Bridging the Human-Humanoid Gap for Long-Range Loco-Manipulation'
summary:
  en: Egocentric human demonstrations offer an accessible source of task experience, but differences in body scale and controller
    response, together with missing robot states, limit their value as humanoid training supervision. We present EgoAlign,
    a data-construction framework that converts these demonstrations into action and state supervision compatible with a general-purpose,
    continuous whole-body ...
  zh: EgoAlign 是一个数据构建框架，用于将第一视角人类演示转化为适用于通用连续全身控制器的动作与状态监督信号，从而在无需采集实体机器人演示的情况下训练人形机器人。该方法由 Yiming Jiang、Jin Chen、Chongyang
    Xu、Yilun Chen、Aimin Hao、Yisheng He 提出，通过执行反馈引导采集、尺度对齐与控制器在环精修，并用因果回放重建机器人状态与运动 token 标签。仅用适配后的人类演示微调视觉-语言-动作模型，即可在实体人形机器人上零样本部署，完成长程物体搬运、导航至未见目标位置以及足部交互任务。
  ko: Egocentric human demonstrations offer an accessible source of task experience, but differences in body scale and controller
    response, together with missing robot states, limit their value as humanoid training supervision. We present EgoAlign,
    a data-construction framework that converts these demonstrations into action and state supervision compatible with a general-purpose,
    continuous whole-body ...
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
- loco_manipulation
- egocentric_demonstration
- vision_language_action
- whole_body_control
- sim_to_real
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-10-05'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-10-05). Bibliographic metadata from arXiv API (2609.38046);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2609.38046 EgoAlign: Bridging the Human-Humanoid Gap for Long-Range Loco-Manipulation'
  url: https://arxiv.org/abs/2609.38046
  date: '2026-09-29'
  accessed_at: '2026-10-05'
---

## 概述

EgoAlign 关注的是如何把第一视角人类演示变成人形机器人可用的训练监督。由于人体与机器人在体型尺度和控制器响应上存在差异，且人类演示缺少机器人状态，这类数据难以直接用于人形机器人学习。该框架借助目标机器人模型与仿真器，通过执行反馈引导演示采集，在保留视觉引导周期性迈步的运动参考的同时，利用尺度对齐与控制器在环精修来适配上半身交互几何，并通过因果回放重建机器人状态与运动 token 标签。作者仅用适配后的人类演示微调一个视觉-语言-动作模型，并在实体人形机器人上零样本部署，验证了长程物体搬运、导航到未见目标位置和足部交互能力。结果显示，精修相比纯运动学对齐提升了仿真中的手部对齐与实体抓取成功率，且人类采集相比遥操作减少了现场采集时间。

## 核心内容

### 问题背景
第一视角人类演示是获取任务经验的便捷来源，但人体与机器人在体型尺度和控制器响应上的差异，以及演示中缺失的机器人状态，限制了其作为人形机器人训练监督的价值。EgoAlign 的目标是在不采集实体机器人演示的前提下，把这类演示转化为与通用连续全身控制器兼容的动作与状态监督。

### 方法
- 数据构建框架 EgoAlign 使用目标机器人模型与仿真器，通过执行反馈引导演示采集过程。
- 在保留视觉引导周期性迈步所需运动参考的同时，通过尺度对齐与控制器在环精修来适配上半身交互几何。
- 最后通过因果回放重建对应的机器人状态与运动 token 标签，使其可与人类观测一起用于训练。

### 实验设置
- 仅使用适配后的人类演示微调一个视觉-语言-动作模型。
- 将所得策略零样本部署到实体人形机器人上。

### 关键结果
- 所得策略能够执行长程物体搬运、导航至未见目标位置，以及独立评估的足部交互。
- 相比仅做运动学对齐，精修提升了仿真中的手部对齐效果与实体抓取成功率。
- 相比遥操作，人类采集方式减少了现场采集时间。

### 结论
EgoAlign 表明，经过执行反馈引导、尺度对齐与控制器在环精修处理的人类演示，可以作为人形机器人全身连续控制的有效监督来源，并支持在实体平台上零样本执行长程移动操作任务。

## Overview

Egocentric human demonstrations offer an accessible source of task experience, but differences in body scale and controller response, together with missing robot states, limit their value as humanoid training supervision. We present EgoAlign, a data-construction framework that converts these demonstrations into action and state supervision compatible with a general-purpose, continuous whole-body controller, without collecting physical-robot demonstrations. Using the target-robot model and simulator, EgoAlign guides demonstration collection through execution feedback. It preserves locomotion references for visually guided periodic stepping while adapting upper-body interaction geometry through scale alignment and controller-in-the-loop refinement. A final causal replay reconstructs the corresponding robot states and motion-token labels for training with the human observations. We assess the resulting supervision by fine-tuning a vision--language--action model solely on adapted human demonstrations and deploying it zero-shot on a physical humanoid. The resulting policies perform long-range object relocation, navigation to unseen goal positions, and independently evaluated foot interaction. Refinement improves simulated hand alignment and physical pickup success over kinematic alignment alone, while human collection reduces on-site acquisition time relative to teleoperation. https://lambdahumanoid.github.io/EgoAlign/

## 参考
- https://arxiv.org/abs/2609.38046
