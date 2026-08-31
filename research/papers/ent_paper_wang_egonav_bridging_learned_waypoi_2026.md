---
$id: ent_paper_wang_egonav_bridging_learned_waypoi_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'EgoNav: Bridging Learned Waypoints and Geometry-Aware Local Control for Robust Indoor Navigation'
  zh: 'EgoNav: Bridging Learned Waypoints and Geometry-Aware Local Control for Robust Indoor Navigation'
  ko: 'EgoNav: Bridging Learned Waypoints and Geometry-Aware Local Control for Robust Indoor Navigation'
summary:
  en: 'Image-goal navigation using lightweight topological maps is a practical paradigm for indoor robot deployment: the map
    requires only geotagged images, and localization relies on visual matching rather than precise pose estimation. However,
    learned waypoint predictors can produce targets that violate geometric constraints or deviate from the global path. Executing
    these waypoints safely further ...'
  zh: EgoNav 是一个用于室内图像目标导航的分层系统，由 Jing Wang、Shiqi Zhao、Hairong Qu 和 Peng Yin 提出。它通过从语义分割的可通行区域生成候选点，并与学习到的路标点进行几何安全、方向一致性和先验保真度评分，再结合自适应局部路径规划器执行，在
    Habitat-sim 仿真和实体人形机器人上均优于现有基线。
  ko: 'Image-goal navigation using lightweight topological maps is a practical paradigm for indoor robot deployment: the map
    requires only geotagged images, and localization relies on visual matching rather than precise pose estimation. However,
    learned waypoint predictors can produce targets that violate geometric constraints or deviate from the global path. Executing
    these waypoints safely further ...'
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
- indoor_navigation
- image_goal_navigation
- hierarchical_control
- semantic_segmentation
- adaptive_planning
- humanoid_robot
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-08-31'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-08-31). Bibliographic metadata from arXiv API (2608.25642);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2608.25642 EgoNav: Bridging Learned Waypoints and Geometry-Aware Local Control for Robust Indoor Navigation'
  url: https://arxiv.org/abs/2608.25642
  date: '2026-08-26'
  accessed_at: '2026-08-31'
---

## 概述

EgoNav 旨在解决基于轻量拓扑地图的图像目标导航中，学习式路标预测器可能产生违反几何约束或偏离全局路径的目标，以及现有系统缺乏自适应局部规划器的问题。该系统采用分层架构，先生成候选点并评分，再通过参数自适应的局部规划器执行精炼后的路标点。实验在 Habitat-sim 和实体人形机器人上进行，结果显示 EgoNav 在成功率和路径效率上均持续优于当代基线。

## 核心内容

### 问题背景
室内机器人部署常采用基于轻量拓扑地图的图像目标导航范式，该地图仅需地理标记图像，定位依赖视觉匹配而非精确位姿估计。然而，学习式路标预测器可能输出违反几何约束或偏离全局路径的目标，且现有系统要么缺少局部规划器，要么依赖无法适应狭窄空间的固定参数。

### 方法
EgoNav 采用分层系统设计：
- **候选生成与评分**：从语义分割的可通行区域生成候选点，并与学习到的路标点一起，基于几何安全性、方向一致性和对学习先验的保真度进行评分。
- **自适应局部路径规划**：根据精炼结果调制参数，执行精炼后的路标点，实现碰撞避免并适应受限空间。

### 实验设置与结果
- 实验在 Habitat-sim 仿真环境和实体人形机器人上进行。
- 与当代基线相比，EgoNav 在成功率（success rate）和路径效率（path efficiency）上均持续表现更优。
- 具体数值未在摘要中提供，但强调了一致性的性能优势。

### 结论
EgoNav 通过结合学习式导航直觉与几何感知的局部控制，有效提升了室内导航的鲁棒性，验证了其在仿真和实体平台上的有效性。

## Overview

Image-goal navigation using lightweight topological maps is a practical paradigm for indoor robot deployment: the map requires only geotagged images, and localization relies on visual matching rather than precise pose estimation. However, learned waypoint predictors can produce targets that violate geometric constraints or deviate from the global path. Executing these waypoints safely further requires a local planner capable of collision avoidance, yet existing systems either lack one or rely on fixed parameters that cannot adapt to confined spaces. To address these limitations while retaining the navigational intuition of the learned predictor, we present EgoNav, a hierarchical system that implements this idea by generating candidates from semantically segmented traversable regions and scoring them alongside the learned waypoint for geometric safety, directional coherence, and fidelity to the learned prior. An adaptive local path planner then executes the refined waypoint with parameters modulated based on the refinement outcome. Experiments in Habitat-sim and on a physical humanoid robot show that EgoNav consistently outperforms contemporary baselines in both success rate and path efficiency.

## 参考
- https://arxiv.org/abs/2608.25642
