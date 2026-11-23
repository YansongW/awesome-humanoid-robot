---
$id: ent_paper_yang_beyondego_learning_to_act_beyo_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'BeyondEgo: Learning to Act Beyond Egocentric Perception via Humanoid Ego-Exo Foresight'
  zh: 'BeyondEgo: Learning to Act Beyond Egocentric Perception via Humanoid Ego-Exo Foresight'
  ko: 'BeyondEgo: Learning to Act Beyond Egocentric Perception via Humanoid Ego-Exo Foresight'
summary:
  en: Humanoid loco-manipulation requires coordinating whole-body motion to perform manipulation tasks in complex environments.
    Yet egocentric vision-language-action (VLA) policies can miss critical body--scene relationships, and action imitation
    alone provides no explicit supervision for future scene evolution. We propose BeyondEgo to extend VLA perception in space
    and time. Spatially, we encode a ...
  zh: BeyondEgo 是一种面向人形机器人全身移动操作（loco-manipulation）的视觉-语言-动作（VLA）策略框架，由 Zhaoshan Yang、Chenglei Li 等人提出。该方法在空间上引入同步的外视角（exocentric）观测，在时间上利用未来观测作为特权监督来训练残差适配器，从而突破纯第一人称感知的局限。团队同时发布了
    HELM——据称首个具备同步第一人称与外视角的闭环人形移动操作基准，在五个全身任务上，BeyondEgo 将分布内成功率从 48.0% 提升至 92.0%。
  ko: Humanoid loco-manipulation requires coordinating whole-body motion to perform manipulation tasks in complex environments.
    Yet egocentric vision-language-action (VLA) policies can miss critical body--scene relationships, and action imitation
    alone provides no explicit supervision for future scene evolution. We propose BeyondEgo to extend VLA perception in space
    and time. Spatially, we encode a ...
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
- vision_language_action
- ego_exo_perception
- foresight_supervision
- residual_adapter
- benchmark
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-11-23'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-11-23). Bibliographic metadata from arXiv API (2611.27047);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2611.27047 BeyondEgo: Learning to Act Beyond Egocentric Perception via Humanoid Ego-Exo Foresight'
  url: https://arxiv.org/abs/2611.27047
  date: '2026-11-20'
  accessed_at: '2026-11-23'
---

## 概述

人形机器人在复杂环境中执行移动操作时，需要协调全身运动完成操作任务，但仅依赖第一人称视觉的 VLA 策略容易忽略关键的身体-场景关系，而单纯的动作模仿也缺乏对未来场景演化的显式监督。BeyondEgo 从空间与时间两个维度扩展 VLA 的感知能力：空间上，用冻结的 DINOv3 编码同步外视角画面，并将其 token 与第一人称 VLM token 拼接后送入动作专家；时间上，以两个视角的未来观测作为特权监督，训练任务条件 VLM 特征上的残差适配器，并由前瞻专家回归 0.6 秒后的 DINOv3 表示。部署时前瞻专家被丢弃，仅保留 4.2M 参数的适配器。作者还提出了 HELM 基准，覆盖五个全身任务并同步提供第一人称与外视角。在 HELM 上，该方法将分布内成功率从 48.0% 提升到 92.0%，在 200 个存在布局、资产、材质与光照变化的留出场景上从 23.5% 提升到 65.0%。

## 核心内容

### 问题背景

人形机器人的移动操作（loco-manipulation）要求协调全身运动，在复杂环境中完成操作任务。现有基于第一人称视觉的视觉-语言-动作（VLA）策略存在两方面不足：

- 第一人称视角可能遗漏关键的身体-场景关系；
- 仅靠动作模仿进行学习，无法为未来场景的演化提供显式监督。

### 方法

BeyondEgo 从空间与时间两个维度扩展 VLA 的感知范围。

**空间扩展**

- 引入与第一人称同步的外视角（exocentric）画面；
- 使用冻结的 DINOv3 编码外视角图像，得到对应 token；
- 将这些 token 与第一人称 VLM token 拼接，作为动作专家的条件输入。

**时间扩展**

- 将两个视角的未来观测作为特权监督，作用于任务条件 VLM 特征上的残差适配器；
- 前瞻专家（foresight expert）负责回归 0.6 秒之后两个视角的 DINOv3 表示；
- 部署阶段丢弃前瞻专家，仅保留 4.2M 参数的适配器。

### 实验设置

作者提出 HELM 基准，据其所知是首个具备同步第一人称与外视角的闭环人形移动操作基准，覆盖五个全身任务。评估包括分布内测试，以及 200 个留出场景，这些场景在布局、资产、材质与光照上均存在变化。

### 关键结果

- 分布内成功率：由 48.0% 提升至 92.0%；
- 200 个留出场景（布局、资产、材质、光照变化）：由 23.5% 提升至 65.0%；
- 消融实验表明，双视角 DINOv3 前瞻带来最佳的迁移效果。

### 结论

通过空间上融合外视角感知、时间上以未来观测作为特权监督，BeyondEgo 在部署时仅需保留轻量适配器，即可显著提升人形机器人移动操作的成功率与跨场景迁移能力。

## Overview

Humanoid loco-manipulation requires coordinating whole-body motion to perform manipulation tasks in complex environments. Yet egocentric vision-language-action (VLA) policies can miss critical body--scene relationships, and action imitation alone provides no explicit supervision for future scene evolution. We propose BeyondEgo to extend VLA perception in space and time. Spatially, we encode a synchronized exocentric view with frozen DINOv3 and concatenate the resulting tokens with egocentric VLM tokens to condition the action expert. Temporally, we use future observations from both views as privileged supervision for a residual adapter on task-conditioned VLM features. A foresight expert regresses DINOv3 representations of both views 0.6s ahead. At deployment, the foresight expert is discarded and the 4.2M-parameter adapter is retained. We also introduce HELM, to our knowledge, the first closed-loop humanoid loco-manipulation benchmark with synchronized egocentric and exocentric views across five whole-body tasks.On HELM, BeyondEgo improves success from 48.0% to 92.0% in distribution and from 23.5% to 65.0% on 200 held-out scenes with layout, asset, material, and lighting shifts. Ablations show that dual-view DINOv3 foresight yields the best transfer results.

## 参考
- https://arxiv.org/abs/2611.27047
