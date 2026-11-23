---
$id: ent_paper_fu_rose_a_shared_cross_embodiment_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ROSE: A Shared Cross-Embodiment Facial-Motion Latent Space for Humanoid Robot Expression'
  zh: 'ROSE: A Shared Cross-Embodiment Facial-Motion Latent Space for Humanoid Robot Expression'
  ko: 'ROSE: A Shared Cross-Embodiment Facial-Motion Latent Space for Humanoid Robot Expression'
summary:
  en: Natural, coherent full-face dynamic expressions are central to making humanoid robots socially approachable, yet existing
    systems commonly realize only limited lip motion or scripted expressions. The limitation is both physical and algorithmic.
    A compact head leaves little room for densely packed, independently controllable actuation; meanwhile, learned systems
    often generate an avatar video, ...
  zh: ROSE 是一个面向人形机器人面部表情的框架，由 Yongji Fu、Man Cao、Yi Zhou、Fei Lin、Mark F. Hansen、Guanqun Cao 提出，整合了仿生硬件、跨具身运动表征学习与多模态运动生成。硬件上采用柔性腱鞘传动结构，在
    19.5 cm 的仿生头部内集成 34 个执行器；算法上通过 ROSE-VAE 学习身份无关的共享面部运动隐空间，ROSE-Flow 将文本、音频或其组合直接映射为该空间中的轨迹，再由 ROSE-ACT 转换为受约束的执行器指令。
  ko: Natural, coherent full-face dynamic expressions are central to making humanoid robots socially approachable, yet existing
    systems commonly realize only limited lip motion or scripted expressions. The limitation is both physical and algorithmic.
    A compact head leaves little room for densely packed, independently controllable actuation; meanwhile, learned systems
    often generate an avatar video, ...
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
- facial_expression
- humanoid_robot
- cross_embodiment
- motion_latent_space
- multimodal_generation
- tendon_driven_actuation
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-11-23'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-11-23). Bibliographic metadata from arXiv API (2611.20950);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2611.20950 ROSE: A Shared Cross-Embodiment Facial-Motion Latent Space for Humanoid Robot Expression'
  url: https://arxiv.org/abs/2611.20950
  date: '2026-11-16'
  accessed_at: '2026-11-23'
---

## 概述

现有机器人面部表达系统通常只能实现有限的唇部运动或预设脚本化表情，其限制既来自紧凑头部内难以布置密集且独立可控的驱动，也来自“先渲染再反解”的算法路径——先生成虚拟人视频、关键点或面部参数，再通过视觉重定向推断执行器指令，带来延迟与伪影且难以可靠迁移到实体机器人。ROSE 从硬件与算法两端应对这一问题：硬件上以柔性腱鞘传动将执行器布局与面部动作点解耦，在 19.5 cm 仿生头内集成 34 个执行器，实现紧凑体积下的全脸协同表情；算法上构建跨人类、数字人与机器人观测的共享面部运动隐空间，并让文本、音频或其组合直接生成该空间中的运动轨迹，最终转换为受约束的执行器指令，从而把跨具身学习、多模态生成与实体机器人表情统一起来。

## 核心内容

### 问题背景

自然连贯的全脸动态表情是人形机器人具备社会亲和力的关键，但现有系统多局限于有限的唇部运动或脚本化表情。作者指出限制同时存在于物理与算法两个层面：紧凑头部难以容纳密集且可独立控制的驱动机构；而学习式系统往往先生成虚拟人视频、关键点或面部参数，再通过视觉重定向反推执行器指令，这种“渲染—反解”路径引入延迟与伪影，且生成的行为无法可靠迁移到实体机器人。

### 方法

ROSE（RObot facial expression through Shared motion Embeddings）框架由硬件与算法两部分构成。

- **仿生硬件**：构建柔性腱鞘传动结构，将 34 个执行器集成进一个 19.5 cm 的仿生头部。该结构使执行器放置与面部动作点解耦，从而在紧凑体积内实现协调的全脸表情。
- **ROSE-VAE**：从人类、数字人与机器人观测中学习一个身份无关的共享面部运动隐空间。
- **ROSE-Flow**：将文本、音频或二者的组合直接映射为该运动空间中的轨迹，且不以视频作为生成器输入。
- **ROSE-ACT**：将上述轨迹转换为受约束的执行器指令。

### 实验设置

摘要未给出具体的数据集规模、对比基线、评测指标或定量实验设置。

### 关键结果

摘要未报告定量结果。作者总结称，该系统展示了高密度仿生硬件与共享的可执行面部运动表征如何共同统一跨具身学习、多模态生成与实体机器人表情。

### 结论

ROSE 通过硬件层面的腱鞘传动解耦与算法层面的共享运动隐空间，绕开了渲染—反解路径，为跨具身的面部运动学习与实体机器人表情生成提供了一体化方案。

## Overview

Natural, coherent full-face dynamic expressions are central to making humanoid robots socially approachable, yet existing systems commonly realize only limited lip motion or scripted expressions. The limitation is both physical and algorithmic. A compact head leaves little room for densely packed, independently controllable actuation; meanwhile, learned systems often generate an avatar video, landmarks, or facial parameters and then infer actuator commands through visual retargeting. This render-and-invert path adds latency and artifacts, and it does not reliably transfer generated behavior to a physical robot. We present ROSE (RObot facial expression through Shared motion Embeddings), a framework that integrates biomimetic hardware, cross-embodiment motion representation learning, and multimodal motion generation. On the hardware side, we build a flexible tendon-sheath transmission structure that integrates 34 actuators into a 19.5 cm biomimetic head. By decoupling actuator placement from facial action points, it enables coordinated full-face expression within a compact volume. On the algorithmic side, ROSE-VAE learns an identity-independent shared facial-motion latent space from human, digital-human, and robot observations. ROSE-Flow directly maps text, audio, or their combination to trajectories in this motion space without using video as a generator input. ROSE-ACT then converts these trajectories into constrained actuator commands. Our system demonstrates how high-density biomimetic hardware and a shared executable facial-motion representation can jointly unify cross-embodiment learning, multimodal generation, and physical robot expression.

## 参考
- https://arxiv.org/abs/2611.20950
