---
$id: ent_paper_liu_trajectory_level_automatic_cur_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Trajectory-Level Automatic Curriculum Learning for Legged Locomotion on Unstructured Terrain
  zh: Trajectory-Level Automatic Curriculum Learning for Legged Locomotion on Unstructured Terrain
  ko: Trajectory-Level Automatic Curriculum Learning for Legged Locomotion on Unstructured Terrain
summary:
  en: Training locomotion policies for complex unstructured terrain requires a curriculum to avoid early exploration failures.
    However, since unstructured terrain lacks explicit difficulty ordering for curriculum design, existing methods resort
    to heuristic curricula over parameterized terrains. This abstraction limits generalization, as policies can overadapt
    to near-fixed perceptual patterns. To ...
  zh: 本文提出了一种名为 TACL（Trajectory-level Automatic Curriculum Learning）的轨迹级自动课程学习框架，用于在非结构化地形上训练腿部运动策略。该方法由 Rocky Liu 等人提出，通过评估器学习难度函数并引导采样器生成新轨迹，形成闭环课程更新，显著提升了轨迹成功率。
  ko: Training locomotion policies for complex unstructured terrain requires a curriculum to avoid early exploration failures.
    However, since unstructured terrain lacks explicit difficulty ordering for curriculum design, existing methods resort
    to heuristic curricula over parameterized terrains. This abstraction limits generalization, as policies can overadapt
    to near-fixed perceptual patterns. To ...
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
- curriculum_learning
- legged_locomotion
- unstructured_terrain
- trajectory_generation
- reinforcement_learning
- adaptive_training
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-08-24'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-08-24). Bibliographic metadata from arXiv API (2608.16164);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: arXiv:2608.16164 Trajectory-Level Automatic Curriculum Learning for Legged Locomotion on Unstructured Terrain
  url: https://arxiv.org/abs/2608.16164
  date: '2026-08-17'
  accessed_at: '2026-08-24'
---

## 概述

TACL 框架针对非结构化地形缺乏显式难度排序的问题，直接从地形图生成训练任务，避免了传统启发式课程对参数化地形的依赖。其核心是一个闭环系统：评估器为当前策略学习轨迹难度函数，采样器据此提出新轨迹作为下一轮策略更新的课程。实验表明，该方法在非结构化地形上持续提供有效课程，轨迹成功率比无课程直接训练提升 56.3%，比手工课程在最难任务上提升 18.5%，并在不同接近方向评估中提升高达 39.74%。

## 核心内容

### 问题背景
在复杂非结构化地形上训练腿部运动策略时，早期探索失败常导致训练崩溃，因此需要课程学习。然而，非结构化地形缺乏显式的难度排序，现有方法多依赖参数化地形的启发式课程，这种抽象限制了泛化能力，因为策略可能过度适应近乎固定的感知模式。

### 方法
TACL 框架提出从非结构化地形图直接生成训练任务，而非使用参数化抽象。其工作流程如下：
- **评估器**：在每次课程更新时，学习一个针对当前策略的难度函数，将给定的轨迹任务映射为难度分数。
- **采样器**：基于评估器学习的难度，提出新的轨迹作为下一轮策略更新的课程。
- **闭环机制**：课程迭代地与不断演化的策略相匹配，形成自动化的课程生成循环。

### 实验设置与结果
- **对比基准**：包括无课程直接训练和手工设计的课程学习。
- **关键结果**：
  - 与无课程直接训练相比，TACL 将轨迹成功率提升了 56.3%。
  - 在最难地形任务上，比手工课程学习提升 18.5% 的成功率。
  - 在相同障碍类型上从不同接近方向评估穿越时，成功率提升高达 39.74%。
- **定性与定量实验**：均显示 TACL 能在非结构化地形上持续提供有效课程，适应策略演化。

### 结论
TACL 通过轨迹级自动课程学习，有效解决了非结构化地形课程设计的难题，显著提升了腿部运动策略的泛化能力和成功率，尤其在多样接近方向的任务中表现突出。

## Overview

Training locomotion policies for complex unstructured terrain requires a curriculum to avoid early exploration failures. However, since unstructured terrain lacks explicit difficulty ordering for curriculum design, existing methods resort to heuristic curricula over parameterized terrains. This abstraction limits generalization, as policies can overadapt to near-fixed perceptual patterns. To address this, we propose \textbf{\ourname{}}, an \textbf{T}rajectory-level \textbf{A}utomatic \textbf{C}urriculum \textbf{L}earning framework that generates training tasks directly from unstructured terrain maps. At each curriculum update, the evaluator learns a difficulty function for the current policy that maps a given trajectory task to a difficulty score. The sampler then proposes new trajectories guided by the learned evaluator as the curriculum for the next policy update. This forms a closed loop in which the curriculum is iteratively matched to the evolving policy. Quantitative and qualitative experiments show that \ourname{} continuously provides effective curricula on unstructured terrain, improving trajectory success rate by \(56.3\%\) over direct training without curriculum. Compared with handcrafted curriculum learning, our method improves success rate by \(18.5\%\) on the hardest terrain tasks and by up to \(39.74\%\) when evaluating traversal from diverse approach directions on the same obstacle type.

## 参考
- https://arxiv.org/abs/2608.16164
