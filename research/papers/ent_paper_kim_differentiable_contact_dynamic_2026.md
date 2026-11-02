---
$id: ent_paper_kim_differentiable_contact_dynamic_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Differentiable Contact Dynamics for Legged Locomotion: Policy Learning and Contact-Implicit Trajectory Optimization'
  zh: 'Differentiable Contact Dynamics for Legged Locomotion: Policy Learning and Contact-Implicit Trajectory Optimization'
  ko: 'Differentiable Contact Dynamics for Legged Locomotion: Policy Learning and Contact-Implicit Trajectory Optimization'
summary:
  en: This paper proposes a smooth analytic gradient for frictional contact and applies it to policy learning and contact-implicit
    trajectory optimization for legged locomotion. The exact contact sensitivity is available in closed form but describes
    changes within the current contact mode, providing no first-order information toward neighboring contact modes. The proposed
    gradient replaces this ...
  zh: 本文提出一种面向摩擦接触的光滑解析梯度，并将其用于足式机器人运动的行为策略学习与接触隐式轨迹优化。作者为 Gijeong Kim、Seungbin Oh、Dongyun Kang 与 Hae-Won Park。该方法仅在反向传播中替换精确接触灵敏度，前向硬接触求解保持不变，从而保证
    rollout 可行；在桌面 PC 上用 100,000 个样本、不到 2 分钟训练得到的策略可直接迁移到硬件，无需微调。
  ko: This paper proposes a smooth analytic gradient for frictional contact and applies it to policy learning and contact-implicit
    trajectory optimization for legged locomotion. The exact contact sensitivity is available in closed form but describes
    changes within the current contact mode, providing no first-order information toward neighboring contact modes. The proposed
    gradient replaces this ...
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
- differentiable_contact_dynamics
- legged_locomotion
- contact_implicit_trajectory_optimization
- policy_learning
- frictional_contact
- complementarity_problem
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-11-02'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-11-02). Bibliographic metadata from arXiv API (2610.35852);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2610.35852 Differentiable Contact Dynamics for Legged Locomotion: Policy Learning and Contact-Implicit Trajectory
    Optimization'
  url: https://arxiv.org/abs/2610.35852
  date: '2026-10-26'
  accessed_at: '2026-11-02'
---

## 概述

论文关注足式机器人接触动力学中的梯度计算问题：精确接触灵敏度虽有闭式表达，却只描述当前接触模式内的变化，无法为相邻接触模式提供一阶信息。作者对经 de Saxcé 修正的 Coulomb 摩擦二阶锥互补问题做中心路径松弛，使分离、夹紧与滑动三种模式的定义条件变得光滑，并在由硬接触解初始化、经 Newton 迭代得到的中心路径点上求取松弛灵敏度。该灵敏度在接触模式切换处保持连续，并随松弛趋于零而收敛到精确灵敏度；它只用于反向传播，前向硬接触求解与最终 rollout 的可行性不受影响。策略学习实验使用 100,000 个样本、在桌面 PC 上训练不足 2 分钟，所得策略无需微调即可迁移到硬件，在 trotting 策略下可承受推力并穿越碎石与湿滑地面。在轨迹优化中，该梯度能找到精确梯度与 Signorini 松弛梯度均未触及的富接触解。

## 核心内容

### 问题背景

足式机器人运动依赖对接触的建模与优化。摩擦接触的精确灵敏度可以写成闭式形式，但它只刻画当前接触模式内部的变化，对相邻接触模式不提供一阶信息，因此难以支撑需要跨越接触模式切换的策略学习与轨迹优化。已有的 Signorini 松弛等做法在接触丰富场景中也会遗漏部分解。

### 方法

- 对经 de Saxcé 修正的 Coulomb 摩擦二阶锥互补问题引入中心路径松弛，使定义分离、夹紧与滑动模式的条件变得光滑。
- 松弛后的灵敏度在一个中心路径点上求值，该点由以硬接触解为初值的 Newton 迭代得到。
- 该梯度仅在反向传播中替换精确接触灵敏度，前向硬接触求解保持不变，因此实际 rollout 仍然可行。
- 灵敏度在接触模式切换过程中保持连续，并随松弛消失收敛到精确灵敏度。

### 实验设置与关键结果

- 策略学习：使用 100,000 个样本，在桌面 PC 上训练时间少于 2 分钟；所得策略无需微调即可迁移到硬件。
- 硬件表现：在 trotting 策略下，机器人能够承受推力，并可穿越碎石与湿滑地面。
- 轨迹优化：与精确梯度及 Signorini 松弛梯度相比，所提梯度能够到达接触丰富的解，而这些解是前两者未能找到的。

### 结论

通过在反向传播中引入中心路径松弛的光滑接触灵敏度，论文在保持前向硬接触求解与 rollout 可行性的同时，为足式运动的策略学习与接触隐式轨迹优化提供了可用于跨越接触模式切换的梯度信息，并在硬件迁移与富接触轨迹优化中验证了其效果。

## Overview

This paper proposes a smooth analytic gradient for frictional contact and applies it to policy learning and contact-implicit trajectory optimization for legged locomotion. The exact contact sensitivity is available in closed form but describes changes within the current contact mode, providing no first-order information toward neighboring contact modes. The proposed gradient replaces this sensitivity only in the backward pass, leaving the hard-contact forward solve unchanged and the realized rollout feasible. A central-path relaxation of the de Saxcé-corrected second-order-cone complementarity problem for Coulomb friction smooths the conditions defining the separating, clamping, and sliding modes. The relaxed sensitivity is evaluated at a point on the central path obtained by a Newton iteration initialized from the hard-contact solution. The sensitivity remains continuous through contact-mode transitions and converges to the exact sensitivity as the relaxation vanishes. Using 100,000 samples and less than 2 min of training on a desktop PC, policy learning with the proposed gradient produces a policy that transfers to hardware without fine-tuning. On hardware, the robot under a trotting policy withstands pushes and traverses debris and slippery ground. In trajectory optimization, the proposed gradient reaches contact-rich solutions missed by exact and Signorini-relaxed gradients. Project page: https://diffcontact.github.io

## 参考
- https://arxiv.org/abs/2610.35852
