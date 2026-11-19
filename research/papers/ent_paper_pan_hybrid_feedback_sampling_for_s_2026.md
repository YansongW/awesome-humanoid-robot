---
$id: ent_paper_pan_hybrid_feedback_sampling_for_s_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Hybrid Feedback Sampling for Sample-Efficient Model Predictive Control
  zh: Hybrid Feedback Sampling for Sample-Efficient Model Predictive Control
  ko: Hybrid Feedback Sampling for Sample-Efficient Model Predictive Control
summary:
  en: Thanks to its parallelizability and flexibility, sampling-based Model Predictive Control (MPC) has become widely popular
    for controlling real-world robotic systems. However, for high-dimensional and open-loop unstable dynamical systems, the
    required number of samples to improve the control sequence will grow exponentially with the horizon, leading to poor sample
    efficiency and numerical ...
  zh: 本文提出了一种名为反馈采样模型预测控制（FS-MPC）的混合采样方法，用于提升采样型MPC在复杂机器人任务中的样本效率与稳定性。该方法由Chaoyi Pan等人提出，结合局部与全局搜索策略，在理论分析和仿真实验中均优于标准MPPI和纯反馈采样方法，并在真实人形机器人上得到验证。
  ko: Thanks to its parallelizability and flexibility, sampling-based Model Predictive Control (MPC) has become widely popular
    for controlling real-world robotic systems. However, for high-dimensional and open-loop unstable dynamical systems, the
    required number of samples to improve the control sequence will grow exponentially with the horizon, leading to poor sample
    efficiency and numerical ...
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
- sampling_based_mpc
- feedback_sampling
- hybrid_sampling
- humanoid_control
- dexterous_manipulation
- sample_efficiency
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-08-24'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-08-24). Bibliographic metadata from arXiv API (2608.19443);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: arXiv:2608.19443 Hybrid Feedback Sampling for Sample-Efficient Model Predictive Control
  url: https://arxiv.org/abs/2608.19443
  date: '2026-08-19'
  accessed_at: '2026-08-24'
---

## 概述

针对高维、开环不稳定系统中采样型MPC样本需求随预测时域指数增长的问题，本文揭示了射击法的不稳定性，并证明最优采样提议分布可通过优化反馈策略实现。FS-MPC采用混合采样设计，根据系统稳定性和计算预算平衡局部与全局搜索，理论分析表明其收敛速度快于标准MPPI，最优性优于纯反馈采样。在接触丰富的任务（如人形机器人操作和灵巧操作）中，FS-MPC成功应对动态不稳定任务，并在真实人形机器人上验证了有效性。

## 核心内容

### 问题背景
采样型模型预测控制（MPC）因其并行性和灵活性，在真实机器人控制中广泛应用。然而，对于高维且开环不稳定的系统，为提升控制序列质量所需的样本数量随预测时域呈指数增长，导致样本效率低下和数值不稳定。本文聚焦于采样型MPC中射击法的不稳定性问题。

### 方法
- 核心理论：证明最优采样提议分布可通过带有优化反馈策略的采样实现，由此提出FS-MPC算法。
- 混合采样设计：FS-MPC结合局部搜索（基于反馈策略）与全局搜索（随机采样），依据系统稳定性与可用计算预算动态调整两者权重。
- 理论分析：证明混合采样方法在收敛速度上优于标准MPPI（模型预测路径积分），在最优性上优于纯反馈采样。

### 实验设置与结果
- 仿真任务：涵盖人形机器人移动操作（loco-manipulation）和灵巧操作（dexterous manipulation）等接触丰富的控制任务。
- 关键结果：FS-MPC成功处理了标准采样方法难以应对的动态不稳定任务，并严格优于仅使用反馈策略的方法。
- 真实世界验证：在人形机器人行走与操作任务中进行了实际测试，确认了方法的实用性。

### 结论
FS-MPC通过混合采样策略有效缓解了高维不稳定系统中的样本爆炸问题，在理论和实验层面均展示了优越性，为采样型MPC在复杂机器人控制中的应用提供了新思路。

## Overview

Thanks to its parallelizability and flexibility, sampling-based Model Predictive Control (MPC) has become widely popular for controlling real-world robotic systems. However, for high-dimensional and open-loop unstable dynamical systems, the required number of samples to improve the control sequence will grow exponentially with the horizon, leading to poor sample efficiency and numerical instability. This paper investigates the instability of shooting methods in sampling-based MPC and shows that the optimal sampling proposal distribution can be realized by sampling with an optimized feedback policy. We refer to this algorithm as Feedback Sampling MPC (FS-MPC). FS-MPC involves a hybrid sampling design which balances local and global search based on the system stability and the available computation budget. Our theoretical analysis shows that our hybrid sampling approach achieves faster convergence than standard MPPI and better optimality than standard feedback sampling. Empirically, in diverse contact-rich control tasks like humanoid loco-manipulation and dexterous manipulation, we show that FS-MPC successfully tackles dynamically unstable tasks where standard sample-based approaches struggle, and strictly outperforms feedback policies alone. Finally, we validate our method on humanoid robot locomotion and manipulation tasks in the real world.

## 参考
- https://arxiv.org/abs/2608.19443
