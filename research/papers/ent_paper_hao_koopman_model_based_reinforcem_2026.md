---
$id: ent_paper_hao_koopman_model_based_reinforcem_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Koopman Model-Based Reinforcement Learning
  zh: Koopman Model-Based Reinforcement Learning
  ko: Koopman Model-Based Reinforcement Learning
summary:
  en: We propose a Koopman model-based reinforcement learning (K-MBRL) algorithm for controlling nonlinear robotic systems
    with unknown dynamics. The K-MBRL learns a control policy by minimizing an approximate policy objective that combines
    the analytical immediate cost with an estimate of the future cost evaluated at the one-step predicted state. To this end,
    we develop a stochastic Koopman ...
  zh: 本文提出一种基于 Koopman 模型的强化学习算法 K-MBRL，用于控制动力学未知的非线性机器人系统。作者为 Wenjian Hao、Paulo C. Heredia 与 Shaoshuai Mou。该方法利用随机 Koopman
    算子将未知非线性动力学近似为线性表示，并结合 critic 函数估计剩余未来代价，从而以计算高效的方式学习策略，并在 HalfCheetah、四足运动任务及实体四足机器人上验证了样本效率与性能优势。
  ko: We propose a Koopman model-based reinforcement learning (K-MBRL) algorithm for controlling nonlinear robotic systems
    with unknown dynamics. The K-MBRL learns a control policy by minimizing an approximate policy objective that combines
    the analytical immediate cost with an estimate of the future cost evaluated at the one-step predicted state. To this end,
    we develop a stochastic Koopman ...
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
- koopman_operator
- model_based_reinforcement_learning
- quadruped_locomotion
- sample_efficiency
- policy_gradient
- nonlinear_control
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-11-16'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-11-16). Bibliographic metadata from arXiv API (2611.14186);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: arXiv:2611.14186 Koopman Model-Based Reinforcement Learning
  url: https://arxiv.org/abs/2611.14186
  date: '2026-11-10'
  accessed_at: '2026-11-16'
---

## 概述

K-MBRL 面向动力学未知的非线性机器人控制问题，其核心是构造一个近似策略目标：由解析的即时代价与在一步预测状态处评估的未来代价估计共同组成。为得到该目标，作者开发了基于随机 Koopman 算子的学习方法，将未知非线性动力学拟合为线性表示，同时用 critic 函数补足剩余的未来代价。这一设计带来两点好处：线性 Koopman 动力学使依赖模型的策略梯度计算简化为常数矩阵乘积，策略改进因此计算高效；仅做一步模型传播则缓解了长时域 rollout 的预测误差累积，同时通过 critic 保留长期代价信息。学习到的策略可通过前馈求值实现实时控制，无需在线优化。作者在标准随机逼近假设下给出了策略学习的收敛性保证，并通过仿真与实体实验进行评估。

## 核心内容

### 问题背景

针对动力学未知的非线性机器人系统，传统基于模型的强化学习依赖长时域模型 rollout，容易累积预测误差；无模型方法则样本效率往往不足。作者希望在不牺牲长期代价信息的前提下，降低模型依赖的策略梯度计算成本并提升样本效率。

### 方法

- 构造近似策略目标：将解析的即时代价与未来代价估计相加，后者在一步预测状态处由 critic 函数评估。
- 使用基于随机 Koopman 算子的学习方法，把未知非线性动力学近似为线性表示。
- 由于 Koopman 动力学是线性的，模型相关的策略梯度计算被简化为常数矩阵乘积，使策略改进在计算上高效。
- 只进行一步模型传播，避免长时域 rollout 带来的误差累积，同时借助 critic 保留长期代价信息。
- 学习得到的策略通过前馈求值即可实时执行，不需要在线优化。
- 在标准随机逼近假设下建立了策略学习的收敛性保证。

### 实验设置与关键结果

- 仿真任务包括 HalfCheetah 与四足四腿运动任务，与经典的无模型和基于模型的强化学习基线相比，K-MBRL 表现出较强的样本效率和更好的性能。
- 使用 pendulum swing-up 任务评估策略梯度近似的精度，并就学习机制与关键超参数开展消融研究。
- 在实体四足机器人上进一步验证：完成一系列高难度动作，包括由两个圆形后足支撑起身至直立姿态、在双足行走过程中保持平衡，以及安全返回地面（见 Fig.1）。

### 结论

K-MBRL 通过线性 Koopman 表示与 critic 的结合，在保持长期代价信息的同时简化了策略梯度计算并抑制了预测误差累积，仿真与实体四足机器人实验均支持其有效性与样本效率。

## Overview

We propose a Koopman model-based reinforcement learning (K-MBRL) algorithm for controlling nonlinear robotic systems with unknown dynamics. The K-MBRL learns a control policy by minimizing an approximate policy objective that combines the analytical immediate cost with an estimate of the future cost evaluated at the one-step predicted state. To this end, we develop a stochastic Koopman operator-based learning method to approximate the unknown nonlinear dynamics in a linear representation, while a critic function estimates the remaining future cost. This formulation offers two key advantages. First, the linear Koopman dynamics simplify the model-dependent policy gradient computation to a constant matrix product, enabling computationally efficient policy improvement. Second, one-step model propagation mitigates the accumulation of prediction errors associated with long-horizon rollouts while retaining long-term cost information through the critic. The learned policy enables real-time control through feedforward evaluation without online optimization. We establish policy learning convergence guarantees under standard stochastic approximation assumptions. Simulations on HalfCheetah and quadruped four-legged locomotion tasks demonstrate strong sample efficiency and improved performance compared with classical model-free and model-based reinforcement learning baselines. A pendulum swing-up task is used to assess policy gradient approximation accuracy and conduct ablation studies on the learning mechanism and key hyperparameters. The proposed K-MBRL is further validated on a physical quadruped robot performing a challenging sequence of maneuvers: rising to an upright posture supported by two rounded rear feet, maintaining balance during bipedal walking, and safely returning to the ground, as shown in Fig.1.

## 参考
- https://arxiv.org/abs/2611.14186
