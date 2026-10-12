---
$id: ent_paper_yue_being_m07_a_latent_world_actio_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Being-M0.7: A Latent World-Action Model for Humanoid Robots'
  zh: 'Being-M0.7: A Latent World-Action Model for Humanoid Robots'
  ko: 'Being-M0.7: A Latent World-Action Model for Humanoid Robots'
summary:
  en: Humanoid loco-manipulation requires coordinated locomotion and manipulation informed by future scene evolution and whole-body
    motion, yet learning these capabilities is constrained by scarce robot demonstrations. Human video and motion datasets
    offer scalable supervision, but many contain only video or motion rather than paired video-motion data. Moreover, human
    motion does not directly specify ...
  zh: Being-M0.7 是一种面向人形机器人的潜在世界-动作模型（latent world-action model），由 Junpeng Yue、Boyuan Li 等研究者提出。该方法通过预训练、机器人中训练与动作后训练三阶段，将混合模态人类数据中学到的视觉-运动先验迁移到人形控制中。其数据语料来自超过
    10,000 小时的以人为中心的原始数据，在 SIMPLE 基准上取得对比基线中最高的综合成功率，并在真实 Unitree G1 的移动操作任务上达到与最强基线相当的水平。
  ko: Humanoid loco-manipulation requires coordinated locomotion and manipulation informed by future scene evolution and whole-body
    motion, yet learning these capabilities is constrained by scarce robot demonstrations. Human video and motion datasets
    offer scalable supervision, but many contain only video or motion rather than paired video-motion data. Moreover, human
    motion does not directly specify ...
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
- world_action_model
- visual_motion_pretraining
- whole_body_control
- cross_attention
- humanoid_robot
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-10-12'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-10-12). Bibliographic metadata from arXiv API (2610.11283);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2610.11283 Being-M0.7: A Latent World-Action Model for Humanoid Robots'
  url: https://arxiv.org/abs/2610.11283
  date: '2026-10-08'
  accessed_at: '2026-10-12'
---

## 概述

人形机器人的移动操作需要协调的行走与操作能力，并依赖对未来场景演化与全身运动的预测，但机器人示教数据稀缺限制了这类能力的学习。人类视频与运动数据集提供了可扩展的监督来源，然而许多数据只包含视频或只包含运动，缺少成对的视频-运动数据，且人类运动并不能直接给出可执行的机器人动作。为此，作者提出 Being-M0.7，一个潜在世界-动作模型，通过预训练、机器人中训练和动作后训练，把从混合模态人类数据中学到的视觉-运动先验迁移到人形控制。模型通过联合预测未来潜在视觉状态与运动，促使视觉表征编码未来运动学信息；中训练阶段将粗粒度先验适配到机器人视角与身体动力学；后训练阶段则由动作专家结合冻结的适配先验的视觉预测表征、当前图像与本体感受，经门控交叉注意力输出可执行的全身指令。

## 核心内容

### 问题背景
人形机器人的移动操作（loco-manipulation）要求行走与操作相互协调，并且需要依据未来场景的演化以及全身运动来做出决策。学习这类能力的主要瓶颈在于机器人示教数据稀缺。人类视频与运动数据规模大、可作为监督来源，但存在两个问题：一是许多数据只有视频或只有运动，缺少成对的视频-运动样本；二是人类运动本身并不直接对应可执行的机器人动作。

### 方法
作者提出 Being-M0.7，一个潜在世界-动作模型，将混合模态人类数据中学到的视觉-运动先验迁移到人形控制，整体分为三个阶段：

- **预训练**：从超过 10,000 小时的以人为中心的原始数据中整理语料，整合仅有视频、仅有运动以及成对视频-运动三类数据流，以学习互补的视觉动态与全身运动学结构。模型联合预测未来的潜在视觉状态与运动，从而促使视觉表征编码未来的运动学信息。
- **机器人中训练**：将上述粗粒度先验适配到机器人的视角与身体动力学。
- **动作后训练**：一个动作专家（action expert）通过门控交叉注意力（gated cross-attention），把来自冻结且已适配先验的视觉预测表征，与当前图像和本体感受结合起来，将预测性上下文落地为可执行的全身指令。

### 实验设置与关键结果
- 在 SIMPLE 基准上，Being-M0.7 在所比较的基线中取得最高的综合成功率（aggregate success rate）。
- 在真实世界的 Unitree G1 移动操作任务上，其表现与最强基线相当。

### 结论
Being-M0.7 表明，借助混合模态人类数据的预训练、机器人中训练与动作后训练，可以把视觉-运动先验有效迁移到人形机器人的全身控制中，在仿真基准与真实机器人任务上均取得有竞争力的表现。

## Overview

Humanoid loco-manipulation requires coordinated locomotion and manipulation informed by future scene evolution and whole-body motion, yet learning these capabilities is constrained by scarce robot demonstrations. Human video and motion datasets offer scalable supervision, but many contain only video or motion rather than paired video-motion data. Moreover, human motion does not directly specify executable robot actions. We present Being-M0.7, a latent world-action model that transfers visual-motion priors learned from mixed-modality human data to humanoid control through pre-training, robot mid-training, and action post-training. We curate a corpus from more than 10,000 hours of raw human-centric data, integrating video-only, motion-only, and paired video-motion streams to learn complementary visual dynamics and whole-body kinematic structure. Joint prediction of future latent visual states and motion encourages visual representations to encode future kinematics. Robot mid-training adapts this coarse-grained prior to robot viewpoints and body dynamics. During action post-training, an action expert combines visual predictive representations from the frozen, adapted prior with current images and proprioception through gated cross-attention, grounding predictive context in executable whole-body commands. Being-M0.7 achieves the highest aggregate success rate among the compared baselines on SIMPLE and matches the strongest baseline on real-world Unitree G1 loco-manipulation tasks.

## 参考
- https://arxiv.org/abs/2610.11283
