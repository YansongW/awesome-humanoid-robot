---
$id: ent_paper_yuan_jeplo_joint_embedding_predicti_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'JEPLO: Joint-Embedding Predictive Learning for LiDAR-Based Legged Locomotion'
  zh: 'JEPLO: Joint-Embedding Predictive Learning for LiDAR-Based Legged Locomotion'
  ko: 'JEPLO: Joint-Embedding Predictive Learning for LiDAR-Based Legged Locomotion'
summary:
  en: Light detection and ranging (LiDAR) remains less explored than RGB-D sensing for perceptive legged locomotion, and existing
    LiDAR-based approaches often rely on explicit mapping. We present JEPLO (Joint-Embedding Predictive learning for legged
    LOcomotion), a single-stage learning framework for mapping-free, LiDAR-based perceptive locomotion for legged robots.
    We introduce a proprio-exteroceptive ...
  zh: JEPLO 是一个面向腿足机器人的单阶段学习框架，利用机载 LiDAR 原始扫描实现无建图的感知式运动控制。作者来自 Qihao Yuan、Yixuan Qiu、Ziyu Cao、Ming Cao、Kailai Li 团队，核心是提出
    proprio-exteroceptive JEPA（PE-JEPA）世界模型与 concurrent JEPA-teacher-student（CJTS）训练流程。该框架成功实现 sim-to-real 迁移，可全向穿越长楼梯、高箱等多样地形，并在遮挡、稀疏与噪声导致的感知退化条件下表现出更强鲁棒性。
  ko: Light detection and ranging (LiDAR) remains less explored than RGB-D sensing for perceptive legged locomotion, and existing
    LiDAR-based approaches often rely on explicit mapping. We present JEPLO (Joint-Embedding Predictive learning for legged
    LOcomotion), a single-stage learning framework for mapping-free, LiDAR-based perceptive locomotion for legged robots.
    We introduce a proprio-exteroceptive ...
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
- lidar_perceptive_locomotion
- legged_robotics
- jepa_world_model
- sim_to_real
- reinforcement_learning
- mapping_free
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-09-21'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-09-21). Bibliographic metadata from arXiv API (2609.15770);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2609.15770 JEPLO: Joint-Embedding Predictive Learning for LiDAR-Based Legged Locomotion'
  url: https://arxiv.org/abs/2609.15770
  date: '2026-09-14'
  accessed_at: '2026-09-21'
---

## 概述

JEPLO 针对 LiDAR 在感知式腿足运动中被探索不足、现有方法多依赖显式建图的问题，提出了一种无建图的单阶段学习框架。其核心是 PE-JEPA 世界模型，从包括原始 LiDAR 扫描在内的机载观测中学习预测性的自我中心地形表征。作者进一步设计 CJTS 流程，在仿真中用深度强化学习与简洁的奖励设计，训练由 JEPA 隐表征引导的运动策略。该框架实现了成功的 sim-to-real 迁移，支持全向穿越长楼梯与高箱等多样地形，且机载计算开销轻量。评估显示其在遮挡、稀疏和噪声造成的感知退化下比现有感知运动框架更鲁棒，分析也验证了其在此类条件下保留任务相关信息的能力。

## 核心内容

### 问题背景
在感知式腿足运动领域，LiDAR 相比 RGB-D 传感受到的关注更少，且现有基于 LiDAR 的方法通常依赖显式建图。JEPLO 旨在解决这一空白，实现无建图、基于 LiDAR 的感知式运动。

### 方法
- 提出 **PE-JEPA**（proprio-exteroceptive JEPA）世界模型，从机载观测（含原始 LiDAR 扫描）中学习预测性的自我中心地形表征。
- 提出 **CJTS**（concurrent JEPA-teacher-student）流程，在仿真中利用深度强化学习训练运动策略，该策略由 JEPA 隐表征引导，并采用简洁的奖励设计。
- 整体为单阶段学习框架，无需显式建图。

### 实验设置与关键结果
- 框架实现了成功的 sim-to-real 迁移。
- 支持全向穿越多样地形，包括长楼梯与高箱。
- 机载计算开销轻量。
- 评估表明其鲁棒性优于现有感知运动框架，尤其在遮挡、稀疏和噪声导致的感知退化条件下。
- 进一步分析验证了 JEPLO 在这些挑战性条件下保留任务相关信息的能力。

### 结论
JEPLO 为腿足机器人提供了无建图、基于 LiDAR 的感知运动方案，在感知退化场景下具备更强鲁棒性。作者已开源实现、实验数据集与硬件设置设计，地址为 https://github.com/ASIG-X/JEPLO。

## Overview

Light detection and ranging (LiDAR) remains less explored than RGB-D sensing for perceptive legged locomotion, and existing LiDAR-based approaches often rely on explicit mapping. We present JEPLO (Joint-Embedding Predictive learning for legged LOcomotion), a single-stage learning framework for mapping-free, LiDAR-based perceptive locomotion for legged robots. We introduce a proprio-exteroceptive JEPA (PE-JEPA) world model to learn predictive egocentric terrain representations from onboard observations, including raw LiDAR scans. A concurrent JEPA-teacher-student (CJTS) pipeline is further proposed to train a locomotion policy informed by JEPA latent representations in simulation using deep reinforcement learning with a simple reward formulation. The framework achieves successful sim-to-real transfer, enabling omnidirectional traversal of diverse terrains, including long staircases and high boxes, with lightweight onboard computation. Evaluations demonstrate greater robustness than existing perceptive locomotion frameworks, particularly under degraded perception caused by occlusion, sparsity and noise. Further analysis validates JEPLO's ability to retain task-relevant information under these challenging conditions. We open-source our implementation, experimental datasets, and hardware setup designs https://github.com/ASIG-X/JEPLO.

## 参考
- https://arxiv.org/abs/2609.15770
