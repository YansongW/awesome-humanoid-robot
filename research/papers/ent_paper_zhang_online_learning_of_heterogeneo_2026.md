---
$id: ent_paper_zhang_online_learning_of_heterogeneo_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Online Learning of Heterogeneous Locomotion Dynamics under Reinforcement Learning Policies for Precise Loco-Manipulation
  zh: Online Learning of Heterogeneous Locomotion Dynamics under Reinforcement Learning Policies for Precise Loco-Manipulation
  ko: Online Learning of Heterogeneous Locomotion Dynamics under Reinforcement Learning Policies for Precise Loco-Manipulation
summary:
  en: How to reuse a pretrained locomotion policy for precise loco-manipulation is still an open problem. We propose an online
    method to learn the closed-loop dynamics under a frozen locomotion policy. The learned model predicts floating-base motion
    and improves loco-manipulation accuracy. However, unobserved latent conditions of the policy introduce heterogeneous responses,
    meaning that the same ...
  zh: 本文提出一种在线学习方法，用于在冻结的运动策略下学习闭环动力学，以支持精确的移动操作（loco-manipulation）。作者来自 Tianlin Zhang、Weipeng Xia、Lingwei Zhang、Yiyang Shao、Zhongyu
    Li、Yun-Hui Liu 团队。核心贡献是提出受污染高斯模型（contaminated Gaussian model）结合高斯过程与随机傅里叶特征（RFFs）的在线学习器，用以处理策略潜在条件导致的异构响应，并给出有限样本误差界；仿真与硬件实验中末端执行器跟踪误差为
    0.01 m。
  ko: How to reuse a pretrained locomotion policy for precise loco-manipulation is still an open problem. We propose an online
    method to learn the closed-loop dynamics under a frozen locomotion policy. The learned model predicts floating-base motion
    and improves loco-manipulation accuracy. However, unobserved latent conditions of the policy introduce heterogeneous responses,
    meaning that the same ...
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
- loco_manipulation
- online_learning
- gaussian_process
- model_predictive_control
- heterogeneous_dynamics
- random_fourier_features
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-11-02'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-11-02). Bibliographic metadata from arXiv API (2610.41892);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: arXiv:2610.41892 Online Learning of Heterogeneous Locomotion Dynamics under Reinforcement Learning Policies for Precise
    Loco-Manipulation
  url: https://arxiv.org/abs/2610.41892
  date: '2026-10-30'
  accessed_at: '2026-11-02'
- id: src_002
  type: website
  title: Project page
  url: https://youtu.be/H-u8buk86C0
  accessed_at: '2026-11-02'
---

## 概述

复用预训练运动策略完成精确移动操作仍是一个开放问题。作者提出在冻结运动策略下在线学习其闭环动力学，用学习到的模型预测浮动基座运动，从而提升移动操作精度。难点在于策略的未观测潜在条件会带来异构响应：相同观测状态可能对应不同运动，直接学习会引入偏差与波动。为此，作者用受污染高斯模型以两个高斯分量分别刻画可预测与不可预测响应，并将其与高斯过程结合，借助随机傅里叶特征（RFFs）构建在线学习器，按样本属于可预测分量的概率加权更新。该方法给出有限样本误差界以保证在线学习的一致收敛，并在仿真与硬件实验中实现不同机械臂构型与任务下一致的末端跟踪，误差为 0.01 m。

## 核心内容

### 问题背景

预训练运动策略的复用是精确移动操作的关键瓶颈。在策略参数冻结的情况下，机器人需要准确预知其闭环动力学，才能规划并跟踪末端执行器轨迹。然而策略内部存在未观测的潜在条件，使得同一观测状态产生不同运动响应，即异构响应。若忽略这种异构性直接学习动力学，估计中会混入偏差与波动，进而损害浮动基座运动预测与末端跟踪精度。

### 方法

- **受污染高斯模型**：用两个高斯分量近似同一观测状态下的响应，分别对应可预测响应与不可预测响应，以刻画潜在条件的影响。
- **在线学习器**：将受污染高斯模型与高斯过程结合，并使用随机傅里叶特征（RFFs）实现在线更新。
- **加权更新机制**：学习器估计每个响应属于可预测分量的概率，并以此对在线更新加权，从而捕捉可预测响应、抑制异构观测带来的偏差与波动。
- **控制集成**：在获得一致且无偏的动力学估计后，由模型预测控制（MPC）预测浮动基座运动，实现精确移动操作。
- **理论保证**：建立有限样本误差界，确保在线学习的一致收敛。

### 实验设置与关键结果

在仿真与硬件实验中，方法在不同机械臂构型与不同任务下均实现一致的末端执行器跟踪，跟踪误差为 0.01 m。

### 结论

在冻结运动策略下在线学习闭环动力学时，显式建模潜在条件引起的异构响应可显著改善动力学估计质量，进而支撑高精度的移动操作；有限样本误差界为在线学习的收敛性提供了理论依据。

## Overview

How to reuse a pretrained locomotion policy for precise loco-manipulation is still an open problem. We propose an online method to learn the closed-loop dynamics under a frozen locomotion policy. The learned model predicts floating-base motion and improves loco-manipulation accuracy. However, unobserved latent conditions of the policy introduce heterogeneous responses, meaning that the same observed state will lead to different motions. Direct learning without accounting for this heterogeneity introduces bias and fluctuations into dynamics estimates, degrading floating-base prediction and end-effector tracking. To address this problem, a contaminated Gaussian model is proposed to approximate the effects of latent conditions. The model uses two Gaussian components to approximate predictable and unpredictable responses under the same observed state. Then, the contaminated Gaussian model is combined with a Gaussian process to construct an online learner using random Fourier features (RFFs). The learner estimates each response's probability of belonging to the predictable component and uses it to weight online updates, capturing predictable responses while reducing bias and fluctuations caused by heterogeneous observations. With consistent and unbiased dynamics estimates, model predictive control (MPC) predicts floating-base motion accurately and enables precise loco-manipulation. A finite-sample error bound is established to ensure uniform convergence in online learning. Simulation and hardware experiments demonstrate consistent end-effector tracking across different manipulator configurations and tasks, with errors of 0.01 m.

## 参考
- https://arxiv.org/abs/2610.41892
- https://youtu.be/H-u8buk86C0
