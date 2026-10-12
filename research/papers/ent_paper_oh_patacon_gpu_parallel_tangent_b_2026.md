---
$id: ent_paper_oh_patacon_gpu_parallel_tangent_b_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'PATACON: GPU-Parallel Tangent-Bundle RRT-Connect for Constrained Motion Planning'
  zh: 'PATACON: GPU-Parallel Tangent-Bundle RRT-Connect for Constrained Motion Planning'
  ko: 'PATACON: GPU-Parallel Tangent-Bundle RRT-Connect for Constrained Motion Planning'
summary:
  en: Fast whole-body motion planning enables continuous replanning for humanoid robots in dynamic environments while satisfying
    collision avoidance and kinematic constraints. However, constrained motion planning incurs substantial computational cost
    due to repeated constraint projection in addition to collision checking and nearest-neighbor search. Recently, GPU-based
    massively parallel planners have ...
  zh: PATACON 是一种面向约束运动规划的 GPU 并行双向规划器，由 Gahyun Oh、Junho An、Suhyun Jeon、Suhan Park 提出。它通过在切空间中探索来利用已知约束函数诱导的局部流形几何，从而减少约束投影开销。在双臂闭链与人形全身约束规划任务上，其性能随构型空间维度与约束余维数增长而提升，最高实现
    11.25 倍加速。
  ko: Fast whole-body motion planning enables continuous replanning for humanoid robots in dynamic environments while satisfying
    collision avoidance and kinematic constraints. However, constrained motion planning incurs substantial computational cost
    due to repeated constraint projection in addition to collision checking and nearest-neighbor search. Recently, GPU-based
    massively parallel planners have ...
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
- constrained_motion_planning
- gpu_parallel_planning
- tangent_space_exploration
- whole_body_control
- humanoid_robotics
- rrt_connect
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-10-12'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-10-12). Bibliographic metadata from arXiv API (2610.13195);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2610.13195 PATACON: GPU-Parallel Tangent-Bundle RRT-Connect for Constrained Motion Planning'
  url: https://arxiv.org/abs/2610.13195
  date: '2026-10-09'
  accessed_at: '2026-10-12'
---

## 概述

快速全身运动规划使人形机器人能够在动态环境中持续重规划，同时满足避碰与运动学约束。但约束运动规划除了碰撞检测与最近邻搜索外，还需反复进行约束投影，计算开销巨大。已有的 GPU 大规模并行规划器虽能降低开销，却仍在环境构型空间中引导，导致偏离流形的候选点投影成为主要瓶颈，在高约束、高维问题中尤为突出。为此，作者提出 PATACON，一种 GPU 并行双向规划器，通过探索切空间来利用已知约束函数诱导的局部流形几何。在双臂闭链与人形全身约束规划任务上的实验表明，随着构型空间维度与约束余维数增大，PATACON 优于先前工作，最高取得 11.25 倍加速，使约束全身运动规划更接近实时性能。

## 核心内容

### 问题背景
人形机器人在动态环境中需要持续重规划全身运动，且必须同时满足避碰与运动学约束。约束运动规划的计算代价不仅来自碰撞检测和最近邻搜索，还来自反复的约束投影。近期提出的 GPU 大规模并行规划器虽降低了计算成本，但它们仍在环境构型空间（ambient configuration space）中进行引导，因此对偏离流形的候选点进行投影仍是显著的开销来源，在高约束、高维问题中尤其严重。

### 方法
作者提出 PATACON，一种 GPU 并行双向规划器。其核心思路是探索切空间（tangent space），以利用由已知约束函数诱导的局部流形几何，从而减少在环境构型空间中引导所带来的投影开销。

### 实验设置
实验涵盖两类任务：
- 双臂闭链（dual-arm closed-chain）约束规划任务
- 人形全身（humanoid whole-body）约束规划任务

### 关键结果
实验显示，随着构型空间维度与约束余维数（constraint codimension）的增长，PATACON 的表现优于先前工作，最高实现 11.25 倍加速。

### 结论
结果表明，GPU 并行的切空间探索使约束全身运动规划更接近实时性能。

## Overview

Fast whole-body motion planning enables continuous replanning for humanoid robots in dynamic environments while satisfying collision avoidance and kinematic constraints. However, constrained motion planning incurs substantial computational cost due to repeated constraint projection in addition to collision checking and nearest-neighbor search. Recently, GPU-based massively parallel planners have been proposed to reduce computational cost. Nevertheless, these planners still steer in the ambient configuration space, so projecting candidates that deviate from the manifold remains a significant source of overhead, particularly in highly constrained, high-dimensional problems. In this work, we introduce PATACON, a GPU-parallel bidirectional planner that explores tangent space to exploit the local manifold geometry induced by known constraint functions. Experiments on dual-arm closed-chain and humanoid whole-body constrained planning tasks show that PATACON outperforms the prior work as configuration-space dimension and constraint codimension grow, achieving up to an 11.25 times speedup. These results suggest that GPU-parallel tangent-space exploration brings constrained whole-body motion planning closer to real-time performance.

## 参考
- https://arxiv.org/abs/2610.13195
