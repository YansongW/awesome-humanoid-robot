---
$id: ent_paper_cao_unified_motion_retargeting_for_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Unified Motion Retargeting for Humanoids with Learned Point Cloud Correspondence
  zh: Unified Motion Retargeting for Humanoids with Learned Point Cloud Correspondence
  ko: Unified Motion Retargeting for Humanoids with Learned Point Cloud Correspondence
summary:
  en: Humanoid learning increasingly relies on transforming vast and diverse human motion data into high-quality robot reference
    trajectories. However, retargeting human motion to humanoid robots is challenging due to substantial differences in morphology,
    degrees of freedom, joint ranges, and kinematic constraints between humans and robots. Existing retargeting methods typically
    address these ...
  zh: 本文提出统一运动重定向框架（UMR），通过学习点云稠密对应关系，无需人工设计的人-机器人映射即可将人类运动数据重定向到人形机器人。该方法以外部点云为统一接口，解耦源骨骼语义与机器人拓扑，实现表面级姿态对齐和交互接触直接迁移，在异构运动源、机器人形态及下游场景中优于现有方法。
  ko: Humanoid learning increasingly relies on transforming vast and diverse human motion data into high-quality robot reference
    trajectories. However, retargeting human motion to humanoid robots is challenging due to substantial differences in morphology,
    degrees of freedom, joint ranges, and kinematic constraints between humans and robots. Existing retargeting methods typically
    address these ...
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
- motion_retargeting
- point_cloud_correspondence
- humanoid_learning
- human_motion_data
- robot_trajectory
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-09-07'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-09-07). Bibliographic metadata from arXiv API (2609.02134);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: arXiv:2609.02134 Unified Motion Retargeting for Humanoids with Learned Point Cloud Correspondence
  url: https://arxiv.org/abs/2609.02134
  date: '2026-09-02'
  accessed_at: '2026-09-07'
---

## 概述

UMR由Hanyang Cao等人提出，针对人形机器人学习中人类运动数据重定向的形态差异挑战。现有方法依赖手工稀疏关键点或身体部位配对，质量受限于人工语义设计，难以扩展。UMR创新性地将外部点云作为人类运动与人形机器人之间的统一接口，学习稠密点云对应关系，为约束点云匹配优化提供细粒度几何锚点。实验表明，UMR在运动保真度和合理性上超越最先进方法，并统一了从运动到交互的多种重定向场景，为大规模人类运动参考转化为机器人训练数据提供了可扩展基础。

## 核心内容

### 问题背景
人形机器人学习日益依赖将海量多样的人类运动数据转化为高质量机器人参考轨迹。然而，人类与机器人在形态、自由度、关节范围及运动学约束上的显著差异，使重定向过程充满挑战。现有方法通常通过手工设计的稀疏关键点或身体部位配对来定义人-机器人对应关系，导致重定向质量高度依赖人工语义设计，限制了跨运动源和机器人形态的可扩展性，且仅能提供稀疏指导，难以复现精细姿态与交互细节。

### 方法核心
UMR框架摒弃了人工设计的人-机器人映射，转而学习稠密点云对应关系。其关键设计包括：
- **统一点云接口**：将外部点云作为人类运动与人形机器人之间的统一中间表示，从而解耦重定向与源骨骼语义及机器人特定拓扑的关联。
- **稠密对应学习**：通过学习得到的稠密对应关系，为后续的约束点云匹配优化提供细粒度几何锚点。
- **表面级对齐与接触迁移**：该机制支持表面级姿态对齐，并能直接迁移交互接触信息，无需依赖稀疏语义配对。

### 实验设置与结果
实验覆盖了异构运动源、不同机器人形态以及从运动到交互的下游场景。结果显示，UMR在运动保真度和合理性方面均优于最先进方法，并成功统一了多种重定向任务。摘要未提供具体数值指标或机器人型号细节。

### 结论
UMR为将大规模人类运动参考转化为机器人就绪训练数据提供了可扩展的基础框架，减少了对人工语义设计的依赖，有望推动人形机器人运动学习的数据规模化应用。

## Overview

Humanoid learning increasingly relies on transforming vast and diverse human motion data into high-quality robot reference trajectories. However, retargeting human motion to humanoid robots is challenging due to substantial differences in morphology, degrees of freedom, joint ranges, and kinematic constraints between humans and robots. Existing retargeting methods typically address these differences by defining human-robot correspondence through hand-crafted sparse keypoints or body-part pairs. As a result, retargeting quality depends heavily on manual semantic design, limiting scalability across motion sources and robot morphologies and providing only sparse guidance for reproducing detailed poses and interactions. In this paper, we present Unified Motion Retargeting (UMR), a framework that learns dense point cloud correspondence without requiring manually designed human-robot mappings. By treating exterior point clouds as a unified interface between human motion and humanoid robots, UMR decouples retargeting from source-specific skeletal semantics and robot-specific topology. The learned dense correspondence provides fine-grained geometric anchors for constrained point cloud matching optimization, enabling surface-level pose alignment and direct transfer of interaction contacts. Experiments demonstrate that UMR unifies retargeting across heterogeneous motion sources, robot embodiments, and downstream scenarios ranging from locomotion to interaction, while achieving higher motion fidelity and plausibility than state-of-the-art methods. UMR therefore provides a scalable foundation for transforming large-scale human motion references into robot-ready training data.

## 参考
- https://arxiv.org/abs/2609.02134
