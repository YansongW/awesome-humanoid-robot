---
$id: ent_paper_mohnot_filter_aware_fine_tuning_for_s_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Filter-Aware Fine-Tuning for Safe Humanoid Whole-Body Tracking
  zh: Filter-Aware Fine-Tuning for Safe Humanoid Whole-Body Tracking
  ko: Filter-Aware Fine-Tuning for Safe Humanoid Whole-Body Tracking
summary:
  en: Safe whole-body motion is essential for deploying humanoid robots in unstructured environments. Modern humanoid control
    commonly separates reference specification from execution, with a planner, teleoperator, or motion generator providing
    a reference that a reinforcement-learning policy tracks through dynamically feasible whole-body control. Runtime safety
    filters, such as control barrier ...
  zh: 该工作研究人形机器人全身跟踪中跟踪策略与运行时安全滤波器（如 CBF）之间的不匹配问题，指出将二者独立处理会因滤波改变执行动作与状态分布而引发根本性冲突。作者提出 CoFiT（Constrained Filter-aware Tuning），一种面向预训练跟踪器的滤波器感知微调方法。在
    TWIST2 与 SONIC 上，CoFiT 相比仅用滤波器训练分别将违规时间降低 91% 与 21%，并在 Unitree G1 硬件上使 TWIST2 的违规时间降低 83%，全部试验无需操作员干预。
  ko: Safe whole-body motion is essential for deploying humanoid robots in unstructured environments. Modern humanoid control
    commonly separates reference specification from execution, with a planner, teleoperator, or motion generator providing
    a reference that a reinforcement-learning policy tracks through dynamically feasible whole-body control. Runtime safety
    filters, such as control barrier ...
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
- humanoid_whole_body_control
- safety_filter
- control_barrier_function
- fine_tuning
- reinforcement_learning
- sim_to_real
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-10-05'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-10-05). Bibliographic metadata from arXiv API (2610.02341);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: arXiv:2610.02341 Filter-Aware Fine-Tuning for Safe Humanoid Whole-Body Tracking
  url: https://arxiv.org/abs/2610.02341
  date: '2026-10-01'
  accessed_at: '2026-10-05'
---

## 概述

该研究聚焦于非结构化环境中人形机器人安全全身运动的问题。现代人形控制通常将参考生成与执行分离，由规划器、遥操作或运动生成器给出参考，强化学习策略负责跟踪，而控制屏障函数等运行时安全滤波器则通过干预跟踪器输出施加新约束。作者指出，把跟踪策略与安全滤波器视为相互独立会带来根本性不匹配，因为滤波同时改变了实际执行的动作与由此产生的状态分布。为此他们通过案例研究分离出动力学、目标与信息三类不匹配，并据此提出滤波器感知的微调方法 CoFiT。实验表明该方法在多种约束场景下显著减少违规时间，并在 Unitree G1 硬件上实现无需操作员介入的完整试验。

## 核心内容

### 问题背景
在非结构化环境中部署人形机器人，安全的全身边运动是必要条件。当前主流的人形控制架构将参考指定与执行分离：由规划器、遥操作者或运动生成器提供参考，强化学习策略通过动力学可行的全身控制对其进行跟踪。运行时安全滤波器（例如 control barrier functions, CBFs）被视为一种有前景的手段，可在跟踪器输出上施加干预，从而执行新引入的约束。

### 核心问题
作者指出，将跟踪策略与安全滤波器独立对待会引发根本性的不匹配。原因在于滤波不仅改变实际执行的动作，也改变了由此诱导的状态分布。作者通过案例研究分离出三类不匹配：动力学不匹配、目标不匹配与信息不匹配，并分析其根本成因。

### 方法
基于上述洞察，作者提出 CoFiT（Constrained Filter-aware Tuning），一种面向预训练跟踪器的滤波器感知微调方法。

### 关键结果
- 在多种约束场景下，CoFiT 相比仅使用滤波器训练（filter-only training），将违规时间在 TWIST2 上降低 91%，在 SONIC 上降低 21%，同时所需的安滤波器修正更小。
- 在 Unitree G1 硬件上，CoFiT 使 TWIST2 的违规时间降低 83%，且每一次试验都无需操作员干预完成；而基线试验中有 50% 需要操作员中止。

### 结论
这些结果为策略与滤波器之间的交互提供了可操作的见解，并确立了将学习型跟踪器与运行时安全滤波器相结合的设计原则。

## Overview

Safe whole-body motion is essential for deploying humanoid robots in unstructured environments. Modern humanoid control commonly separates reference specification from execution, with a planner, teleoperator, or motion generator providing a reference that a reinforcement-learning policy tracks through dynamically feasible whole-body control. Runtime safety filters, such as control barrier functions (CBFs), offer a promising approach for enforcing newly introduced constraints via interventions on the tracker's outputs. We show, however, that treating the tracking policy and safety filter independently induces fundamental mismatches, as filtering alters both the executed actions and the induced state distribution. We study this policy-filter interface through case studies that isolate dynamics, objective, and information mismatches, highlight their root causes, and use these insights to develop CoFiT (Constrained Filter-aware Tuning), a filter-aware fine-tuning method for pretrained trackers. Across diverse constraint scenes, CoFiT reduces violation time relative to filter-only training by 91% on TWIST2 and 21% on SONIC, while requiring smaller safety filter corrections. On Unitree G1 hardware, CoFiT reduces violation time by 83% for TWIST2 and completes every trial without operator intervention, whereas 50% of baseline trials require an operator stop. Together, these results provide actionable insights into policy-filter interactions and establish design principles for integrating learned trackers with runtime safety filters.

## 参考
- https://arxiv.org/abs/2610.02341
