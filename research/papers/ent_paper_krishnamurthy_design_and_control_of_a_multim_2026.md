---
$id: ent_paper_krishnamurthy_design_and_control_of_a_multim_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Design and Control of a Multimodal Legged-Aerial Robot Through Separate Control Contraction Metrics
  zh: Design and Control of a Multimodal Legged-Aerial Robot Through Separate Control Contraction Metrics
  ko: Design and Control of a Multimodal Legged-Aerial Robot Through Separate Control Contraction Metrics
summary:
  en: The integration of dynamic legged locomotion and aerial mobility offers versatility that is deterred by challenges in
    payload distribution, actuation, and the contrasting requirements of both domains. In this paper, we present the design
    and operation of a multimodal quadrupedal aerial-legged robot. The presence of legged aerial systems also allows for thruster-assisted
    legged locomotion, which ...
  zh: 本文设计并控制了一种多模态四足空中腿式机器人，由 Kaushik Venkatesh Krishnamurthy、Eric Sihite、Alireza Ramezani 和 Morteza Gharib 完成。其核心贡献是采用 Control
    Contraction Metrics（CCM）的统一控制框架：离线分别为行走与飞行搜索领域特定的收缩度量，再通过在线基于能量的 Control Lyapunov Function Quadratic Program（CLF QP）将二者统一，从而实现跨域的最优控制分配。研究通过仿真展示了该分配方式，并用实验验证了硬件的机械可行性以及推力辅助小跑这一范式。
  ko: The integration of dynamic legged locomotion and aerial mobility offers versatility that is deterred by challenges in
    payload distribution, actuation, and the contrasting requirements of both domains. In this paper, we present the design
    and operation of a multimodal quadrupedal aerial-legged robot. The presence of legged aerial systems also allows for thruster-assisted
    legged locomotion, which ...
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
- multimodal_robot
- legged_aerial_robot
- control_contraction_metrics
- clf_qp
- thruster_assisted_locomotion
- quadrupedal_robot
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-10-26'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-10-26). Bibliographic metadata from arXiv API (2610.27315);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: arXiv:2610.27315 Design and Control of a Multimodal Legged-Aerial Robot Through Separate Control Contraction Metrics
  url: https://arxiv.org/abs/2610.27315
  date: '2026-10-19'
  accessed_at: '2026-10-26'
---

## 概述

该工作面向动态腿式运动与空中机动相结合的多模态机器人，指出载荷分布、驱动方式以及两个领域相互冲突的需求是主要障碍。作者提出一种四足空中腿式机器人设计，并借助 Control Contraction Metrics（CCM）构建统一控制框架，使推力辅助的腿式运动成为可能。方法上，行走与飞行各自离线求解领域特定的收缩度量，随后由在线基于能量的 Control Lyapunov Function Quadratic Program（CLF QP）将两者统一，实现跨域的最优控制分配。仿真结果展示了该控制分配的效果，实验则验证了硬件的机械可行性以及推力辅助小跑范式，实验中的稳定性进一步支持将该框架用于多模态作业。

## 核心内容

### 问题背景

动态腿式运动与空中机动的结合能够带来更强的 versatility，但受到载荷分布、驱动以及两个领域需求相互冲突等挑战的制约。本文针对这一矛盾，提出一种多模态四足空中腿式机器人的设计与运行方案。腿式空中系统还使推力辅助的腿式运动成为可能，作者希望以统一控制框架实现这一能力。

### 方法

- 采用 Control Contraction Metrics（CCM）作为统一控制框架的基础。
- 离线阶段：分别为行走与飞行独立搜索领域特定的收缩度量。
- 在线阶段：使用基于能量的 Control Lyapunov Function Quadratic Program（CLF QP）将两个收缩度量统一起来。
- 该统一方式实现最优的跨域控制分配。

### 实验设置与结果

- 通过仿真展示跨域控制分配的效果。
- 通过实验验证硬件的机械可行性，以及推力辅助小跑（thruster-assisted trotting）范式。
- 实验中所表现出的稳定性，支持将该控制框架进一步部署于多模态作业。

### 结论

作者提出的统一 CCM 框架能够将分别针对行走与飞行设计的收缩度量在线融合，实现跨域最优控制分配；仿真与实验共同支持该硬件设计与推力辅助腿式运动范式的可行性，并为多模态运行的控制部署提供了依据。

## Overview

The integration of dynamic legged locomotion and aerial mobility offers versatility that is deterred by challenges in payload distribution, actuation, and the contrasting requirements of both domains. In this paper, we present the design and operation of a multimodal quadrupedal aerial-legged robot. The presence of legged aerial systems also allows for thruster-assisted legged locomotion, which we make possible with a unified control framework using Control Contraction Metrics (CCM). We search for separate domain-specific contraction metrics for walking and flight independently offline and unify them using an online energy-based Control Lyapunov Function Quadratic Program (CLF QP). This enables optimal, cross-domain control allocation, which we show using simulations. We also show experimental results that validate the mechanical viability of our hardware and the paradigm of thruster-assisted trotting. The stability of said experiments motivates the deployment of the control framework for multimodal operations.

## 参考
- https://arxiv.org/abs/2610.27315
