---
$id: ent_paper_fan_e2drl_end_to_end_differentiabl_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'E2DRL: End-to-End Differentiable Reinforcement Learning for 3D Obstacle Avoidance in Quadruped Robots'
  zh: 'E2DRL: End-to-End Differentiable Reinforcement Learning for 3D Obstacle Avoidance in Quadruped Robots'
  ko: 'E2DRL: End-to-End Differentiable Reinforcement Learning for 3D Obstacle Avoidance in Quadruped Robots'
summary:
  en: Differentiable reinforcement learning shows strong promise for robot policy learning, but its application to legged
    locomotion has remained limited to blind walking or simulated 2D tasks. Extending it to end-to-end visual obstacle avoidance
    is challenging because hard collision constraints and early termination upon contact corrupt first-order gradients, trapping
    optimizers in local minima. We ...
  zh: E2DRL 是一种面向四足机器人三维避障的端到端可微强化学习方法，由 Cheng Fan、Bingyang Zhou 等人提出。其核心是软化的可微障碍交互建模：在多个身体关键点上施加穿透惩罚，并配合速度条件化的 stop-gradient
    塑形，从而为三维避障提供一阶训练信号。作者在 Unitree Go2 上完成了该端到端可微强化学习方法的首次仿真到真实迁移验证。
  ko: Differentiable reinforcement learning shows strong promise for robot policy learning, but its application to legged
    locomotion has remained limited to blind walking or simulated 2D tasks. Extending it to end-to-end visual obstacle avoidance
    is challenging because hard collision constraints and early termination upon contact corrupt first-order gradients, trapping
    optimizers in local minima. We ...
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
- differentiable_reinforcement_learning
- quadruped_obstacle_avoidance
- sim_to_real
- teacher_student_distillation
- depth_based_policy
- soft_analytic_policy_optimization
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-10-19'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-10-19). Bibliographic metadata from arXiv API (2610.19627);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2610.19627 E2DRL: End-to-End Differentiable Reinforcement Learning for 3D Obstacle Avoidance in Quadruped
    Robots'
  url: https://arxiv.org/abs/2610.19627
  date: '2026-10-14'
  accessed_at: '2026-10-19'
---

## 概述

可微强化学习在机器人策略学习中颇具潜力，但在腿足运动领域此前仅限于盲走或仿真二维任务，扩展到端到端视觉避障的主要障碍在于硬碰撞约束与接触即终止会破坏一阶梯度，使优化陷入局部极小。E2DRL 通过软可微的障碍交互建模来应对这一问题，利用多身体关键点穿透惩罚与速度条件化的 stop-gradient 塑形产生一阶训练信号。为构建可部署的感知—控制系统，作者在可微仿真器中用 Soft Analytic Policy Optimization（SAPO）训练特权教师策略，再经 DAgger 蒸馏为基于深度的循环学生策略，并在部署时通过地形感知门控模块与基础运动策略融合。仿真中该方法样本效率高于 PPO，速度跟踪与三维避障能力优于 PPO 及基于 Duality 的 DCBF NMPC。作者还在 Unitree Go2 上于静态与动态环境完成了首次仿真到真实验证。

## 核心内容

### 问题背景
可微强化学习为机器人策略学习提供了利用一阶梯度直接优化策略的途径，但其在腿足运动中的应用长期局限于盲走或仿真中的二维任务。将这一范式扩展到端到端视觉三维避障面临两个核心困难：硬碰撞约束与接触即终止的设定会破坏一阶梯度，导致优化器陷入局部极小。

### 方法
- **软可微障碍交互建模**：E2DRL 不采用硬碰撞约束，而是在多个身体关键点上施加穿透惩罚，并引入速度条件化的 stop-gradient 塑形，从而为三维避障提供可用的一阶训练信号。
- **教师—学生蒸馏流程**：在可微仿真器中，使用 Soft Analytic Policy Optimization（SAPO）训练特权教师策略；随后通过 DAgger 将其蒸馏为基于深度的循环学生策略。
- **部署融合**：部署阶段通过地形感知门控模块，将蒸馏得到的学生策略与基础运动策略进行融合，形成完整的感知—控制系统。

### 实验设置与关键结果
- 仿真实验中，E2DRL 的样本效率高于 PPO。
- 与 PPO 以及基于 Duality 的 DCBF NMPC 相比，E2DRL 在速度跟踪性能和三维避障能力上均表现更优。
- 真实机器人实验在 Unitree Go2 上进行，覆盖静态与动态环境，构成端到端可微强化学习用于三维避障的首次仿真到真实验证。

### 结论
E2DRL 通过软可微的障碍交互建模解决了硬约束破坏梯度的问题，并结合 SAPO 教师训练、DAgger 蒸馏与地形感知门控融合，实现了可部署的四足机器人三维避障系统，且在仿真与真实环境中均得到验证。

## Overview

Differentiable reinforcement learning shows strong promise for robot policy learning, but its application to legged locomotion has remained limited to blind walking or simulated 2D tasks. Extending it to end-to-end visual obstacle avoidance is challenging because hard collision constraints and early termination upon contact corrupt first-order gradients, trapping optimizers in local minima. We present E2DRL, which addresses this with a soft differentiable obstacle-interaction formulation: penetration penalties across multiple body keypoints with velocity-conditioned stop-gradient shaping to provide the first-order training signals for 3D obstacle avoidance. To realize a deployable perception-control system, a privileged teacher trained via Soft Analytic Policy Optimization (SAPO) in a differentiable simulator is distilled into a recurrent depth-based student via DAgger, then blended with a base locomotion policy using a terrain-aware gating module for deployment. In simulation, E2DRL achieves higher sample efficiency than PPO and demonstrates superior velocity-tracking performance and 3D obstacle-avoidance capability compared with both PPO and Duality-based DCBF NMPC. We present the first sim-to-real validation of end-to-end differentiable RL for 3D obstacle avoidance on a Unitree Go2 in static and dynamic environments.

## 参考
- https://arxiv.org/abs/2610.19627
