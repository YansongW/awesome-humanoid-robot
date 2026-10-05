---
$id: ent_paper_wang_counterfactual_video_generatio_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Counterfactual Video Generation Enables Scalable Humanoid Loco-Manipulation
  zh: Counterfactual Video Generation Enables Scalable Humanoid Loco-Manipulation
  ko: Counterfactual Video Generation Enables Scalable Humanoid Loco-Manipulation
summary:
  en: Teaching humanoids loco-manipulation skills, such as carrying diverse objects, via visual imitation is a promising path
    toward generalist robots. However, collecting diverse, high-quality interaction videos, such as clips that clearly show
    a person's full body and unoccluded interactions with objects, poses a practical barrier to scaling this approach. We
    propose PRISM, a real-to-sim-to-real ...
  zh: PRISM 是一个 real-to-sim-to-real 框架，由 Zihan Wang、Pieter Abbeel、Jitendra Malik、C. Karen Liu、Guanya Shi 等人提出，旨在通过视觉模仿让 humanoid
    掌握 loco-manipulation 技能。该方法从少量真实视频出发，利用 video-to-video（V2V）生成数百段"反事实"人-物交互视频，再经 contact-anchored real-to-sim 流程重建人与物体运动并重定向为物理可行的轨迹，从而训练出单一策略。该策略无需真实世界微调即可部署到真实机器人上，仅凭机载深度观测完成对箱子、桶、收纳箱和球的抓取、搬运与放置。
  ko: Teaching humanoids loco-manipulation skills, such as carrying diverse objects, via visual imitation is a promising path
    toward generalist robots. However, collecting diverse, high-quality interaction videos, such as clips that clearly show
    a person's full body and unoccluded interactions with objects, poses a practical barrier to scaling this approach. We
    propose PRISM, a real-to-sim-to-real ...
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
- counterfactual_video_generation
- real_to_sim_to_real
- video_to_video_generation
- visual_imitation_learning
- contact_anchored_retargeting
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-10-05'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-10-05). Bibliographic metadata from arXiv API (2609.38172);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: arXiv:2609.38172 Counterfactual Video Generation Enables Scalable Humanoid Loco-Manipulation
  url: https://arxiv.org/abs/2609.38172
  date: '2026-09-29'
  accessed_at: '2026-10-05'
- id: src_002
  type: website
  title: Project page
  url: https://prism-real2sim2real.github.io/
  accessed_at: '2026-10-05'
---

## 概述

PRISM 针对 humanoid loco-manipulation 视觉模仿学习中高质量交互视频稀缺这一瓶颈，提出了一套 real-to-sim-to-real 框架。它先从少量真实示例视频出发，通过 video-to-video 生成扩充出数百段多样化的"反事实"人-物交互视频，再借助 contact-anchored real-to-sim 流程重建人与物体的运动，将不完美的视频数据重定向为物理上合理的轨迹。这些反事实视频所具备的类内多样性，使得单一策略能够泛化到同一类别中未见过的物体。作者将训练好的策略直接部署到真实机器人上，未做任何真实世界微调，仅使用机载深度观测，就实现了对箱子、桶、收纳箱和球的抓取、搬运与放置，并适应新实例、新尺寸和新初始构型。

## 核心内容

### 问题背景
通过视觉模仿教 humanoid 掌握 loco-manipulation 技能（例如搬运各类物体）是通向通用机器人的一条有前景的路径。但该路线的规模化面临实际障碍：难以采集多样且高质量的交互视频，尤其是能清晰呈现人物全身、且人与物体交互不被遮挡的片段。

### 方法
作者提出 PRISM，一个 real-to-sim-to-real 框架，通过把少量真实视频放大为大规模、多样化的训练集来突破上述限制。流程包含两个核心环节：

- **反事实视频生成**：基于少量真实示例视频，通过 video-to-video（V2V）生成数百段多样化的"反事实"人-物交互视频。
- **contact-anchored real-to-sim 重建**：重建人与物体的运动，将这批不完美的视频数据重定向为物理上合理的轨迹。

这些反事实视频之间的类内差异（intra-class variability），使得可以训练出单一策略，并泛化到每个类别中未见过的物体。

### 实验设置与关键结果
作者通过将策略部署到真实机器人上验证了完整流程，且未进行任何真实世界微调。策略仅使用机载深度观测，humanoid 即可完成对物体的抓取、搬运与放置，涵盖箱子、桶、收纳箱和球等类别，并能适应新的实例、尺寸与初始构型。

### 结论
PRISM 表明，借助反事实视频生成与 contact-anchored real-to-sim 重定向，可以从极少量真实视频中规模化地获取 humanoid loco-manipulation 训练数据，并训练出可直接零微调部署、具备类别内泛化能力的单一策略。

## Overview

Teaching humanoids loco-manipulation skills, such as carrying diverse objects, via visual imitation is a promising path toward generalist robots. However, collecting diverse, high-quality interaction videos, such as clips that clearly show a person's full body and unoccluded interactions with objects, poses a practical barrier to scaling this approach. We propose PRISM, a real-to-sim-to-real framework that overcomes this limitation by amplifying a handful of real videos into a large, diverse training set. PRISM first generates hundreds of diverse "counterfactual" human-object interaction videos via video-to-video (V2V) generation from a few exemplar real videos. Our contact-anchored real-to-sim pipeline then reconstructs both human and object motions, retargeting this imperfect video data into physically plausible trajectories. The intra-class variability across these counterfactual videos lets us train a single policy that generalizes to unseen objects within each category. We demonstrate the full pipeline by deploying this policy on a real robot without any real-world fine-tuning. Using only onboard depth observations, our humanoid picks up, carries, and drops objects, including boxes, barrels, bins, and balls, across novel instances, sizes, and initial configurations.

## 参考
- https://arxiv.org/abs/2609.38172
- https://prism-real2sim2real.github.io/
