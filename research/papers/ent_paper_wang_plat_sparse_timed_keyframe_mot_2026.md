---
$id: ent_paper_wang_plat_sparse_timed_keyframe_mot_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'PLAT: Sparse Timed Keyframe Motion Tracking for Humanoid Control via Privileged Latent Transition Learning'
  zh: 'PLAT: Sparse Timed Keyframe Motion Tracking for Humanoid Control via Privileged Latent Transition Learning'
  ko: 'PLAT: Sparse Timed Keyframe Motion Tracking for Humanoid Control via Privileged Latent Transition Learning'
summary:
  en: Humanoid motion tracking policies rely on dense frame-by-frame references, limiting their use as high-level motion controllers
    for planning and interactive motion generation. We study \emph{Sparse Timed Keyframe Motion Tracking}, where a policy
    receives only sparse future keyframes and their desired arrival times, and must execute stable whole-body motions that
    reach successive goals. We propose ...
  zh: PLAT 是一种面向人形机器人的稀疏定时关键帧运动跟踪策略学习框架，由 Zepeng Wang、Jiangxing Wang、Chao Ma、Xiaochuan Shi、Zongqing Lu 提出。它通过三阶段训练，把稠密运动跟踪与稀疏目标条件控制连接起来：训练时利用稠密目标序列作为特权监督，部署时只需稀疏的定时关键帧指令。仿真实验表明其在不同规划时域下均能保持准确稳定的跟踪，长时域指令下表现尤为突出，并已在
    Unitree G1 人形机器人上完成部署。
  ko: Humanoid motion tracking policies rely on dense frame-by-frame references, limiting their use as high-level motion controllers
    for planning and interactive motion generation. We study \emph{Sparse Timed Keyframe Motion Tracking}, where a policy
    receives only sparse future keyframes and their desired arrival times, and must execute stable whole-body motions that
    reach successive goals. We propose ...
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
- humanoid_control
- motion_tracking
- sparse_keyframes
- privileged_learning
- latent_transition
- reinforcement_learning
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-09-28'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-09-28). Bibliographic metadata from arXiv API (2609.25754);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2609.25754 PLAT: Sparse Timed Keyframe Motion Tracking for Humanoid Control via Privileged Latent Transition
    Learning'
  url: https://arxiv.org/abs/2609.25754
  date: '2026-09-22'
  accessed_at: '2026-09-28'
---

## 概述

该工作研究的是「稀疏定时关键帧运动跟踪」问题：策略只接收少量未来关键帧及其期望到达时间，却需要执行稳定的全身运动以依次到达各个目标。作者指出，传统人形运动跟踪策略依赖逐帧的稠密参考，因而难以充当规划与交互式运动生成所需的高层运动控制器。为此提出 PLAT，一个包含三阶段、以特权隐变量转移学习为核心的运动跟踪策略学习框架。其关键思路是在训练阶段把稠密目标序列当作特权监督，从而在稠密跟踪与稀疏目标条件控制之间架起桥梁，而部署阶段仅需稀疏定时关键帧指令。方法上先由预训练的稠密跟踪专家提供稳健的运动先验，再通过 DAgger 风格的模仿学习获得特权隐变量先验，最后用隐变量残差强化学习来优化隐变量转移而非直接优化动作。仿真实验显示，PLAT 在不同规划时域下都能保持准确稳定的稀疏定时关键帧跟踪，长时域指令下优势尤其明显，并已成功部署到 Unitree G1 人形机器人上。

## 核心内容

### 问题背景

人形机器人的运动跟踪策略通常依赖稠密的逐帧参考。这种依赖使其难以作为高层运动控制器使用，限制了在规划与交互式运动生成场景中的适用性。本文研究 **Sparse Timed Keyframe Motion Tracking**（稀疏定时关键帧运动跟踪）：策略仅接收稀疏的未来关键帧及其期望到达时间，必须执行稳定的全身运动并依次到达各个目标。

### 方法：PLAT

作者提出 **PLAT**，一个三阶段的稀疏定时关键帧运动跟踪策略学习框架，其核心为 **P**rivileged **LA**tent **T**ransition learning（特权隐变量转移学习）。PLAT 在稠密运动跟踪与稀疏目标条件控制之间建立联系：训练时利用稠密目标序列作为特权监督，部署时仅需稀疏的定时关键帧指令。

三阶段流程为：

- 首先，由预训练的稠密跟踪专家提供稳健的运动先验。
- 其次，通过 DAgger 风格的模仿学习获得特权隐变量先验。
- 最后，采用隐变量残差强化学习，对隐变量转移进行优化，而不是直接优化动作。

### 实验与结果

- 大量仿真实验表明，PLAT 在不同规划时域下都能维持准确且稳定的稀疏定时关键帧跟踪。
- 在长时域指令下，其性能表现尤为突出。
- 该策略已成功部署于 Unitree G1 人形机器人，验证了 PLAT 在稀疏人形运动控制中的有效性与实用性。

### 结论

PLAT 通过特权隐变量转移学习，将稠密跟踪先验迁移到稀疏定时关键帧控制中，在仿真与真实人形机器人上均展现出可行性与实用性。

## Overview

Humanoid motion tracking policies rely on dense frame-by-frame references, limiting their use as high-level motion controllers for planning and interactive motion generation. We study \emph{Sparse Timed Keyframe Motion Tracking}, where a policy receives only sparse future keyframes and their desired arrival times, and must execute stable whole-body motions that reach successive goals. We propose \textbf{PLAT}, a three-stage sparse timed keyframe motion tracking policy learning framework with \textbf{P}rivileged \textbf{LA}tent \textbf{T}ransition learning. PLAT bridges dense motion tracking and sparse goal-conditioned control by exploiting dense goal sequences as privileged supervision during training while requiring only sparse timed keyframe commands at deployment. A pretrained dense tracking expert first provides robust motion priors. A privileged latent prior is then learned through DAgger-style imitation, followed by latent residual reinforcement learning that refines latent transitions instead of directly optimizing actions. Extensive simulation experiments demonstrate that PLAT maintains accurate and stable sparse timed keyframe tracking across varying planning horizons, with particularly strong performance under long-horizon commands. Successful deployment on a Unitree G1 humanoid robot further demonstrates the effectiveness and practicality of PLAT for sparse humanoid motion control.

## 参考
- https://arxiv.org/abs/2609.25754
