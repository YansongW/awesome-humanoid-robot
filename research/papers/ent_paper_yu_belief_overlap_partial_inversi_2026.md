---
$id: ent_paper_yu_belief_overlap_partial_inversi_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Belief-Overlap Partial Inversion: Object-Centric Flow Replanning for Humanoid Loco-Manipulation'
  zh: 'Belief-Overlap Partial Inversion: Object-Centric Flow Replanning for Humanoid Loco-Manipulation'
  ko: 'Belief-Overlap Partial Inversion: Object-Centric Flow Replanning for Humanoid Loco-Manipulation'
summary:
  en: 'People often learn how an unfamiliar object moves through a small exploratory push, using its response to guide their
    next motion. Inspired by this behavior, we study humanoids pushing carts whose mass and caster stiffness are initially
    unknown. Our object-centric framework closes online estimation, flow-based planning, and whole-body control into a loop,
    creating a tension: replacing the plan ...'
  zh: 该论文提出 Belief-Overlap Partial Inversion（BOPI），面向质量与脚轮刚度未知的推车任务，将在线估计、基于流的规划与全身控制闭环结合。BOPI 依据新旧信念的一致程度来缩放修正幅度：仅在信念不一致的范围内对旧信念下的流进行反转，再在新信念下重建。在
    18 个仿真目标上，相比固定深度重规划，最终位置误差与偏航误差分别降低约 33% 和 47%，并在硬件上实现了对非完整约束推车的平移与转向。
  ko: 'People often learn how an unfamiliar object moves through a small exploratory push, using its response to guide their
    next motion. Inspired by this behavior, we study humanoids pushing carts whose mass and caster stiffness are initially
    unknown. Our object-centric framework closes online estimation, flow-based planning, and whole-body control into a loop,
    creating a tension: replacing the plan ...'
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
- humanoid_loco_manipulation
- object_centric_planning
- flow_based_planning
- whole_body_control
- online_estimation
- nonholonomic_cart
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-10-12'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-10-12). Bibliographic metadata from arXiv API (2610.13087);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2610.13087 Belief-Overlap Partial Inversion: Object-Centric Flow Replanning for Humanoid Loco-Manipulation'
  url: https://arxiv.org/abs/2610.13087
  date: '2026-10-09'
  accessed_at: '2026-10-12'
---

## 概述

论文受人类通过一次小幅探索性推动来学习陌生物体运动方式的启发，研究人形机器人推动质量与脚轮刚度初始未知的推车。作者将在线估计、基于流的规划与全身控制闭合成一个环路，并指出其中的矛盾：一旦信念发生变化就替换规划会打断正在进行的动作，而坚持原规划又会让机器人停留在已被证据排除的路径上。为此提出 Belief-Overlap Partial Inversion（BOPI），按新旧信念的一致程度来缩放修正：只在信念分歧的范围内反转旧信念下的流，然后在新信念下重建。在 18 个仿真目标上，该方法相比固定深度重规划将汇总的最终位置误差与偏航误差分别降低约 33% 与 47%，并在硬件上完成了对非完整约束推车的平移与转向。

## 核心内容

### 问题背景
人类在面对陌生物体时，常通过一次小幅探索性推动来感知其运动响应，并据此决定下一步动作。论文将这一行为迁移到人形机器人场景：机器人需要推动质量和脚轮刚度事先未知的推车。由于物体属性未知，机器人必须一边估计、一边规划、一边控制。

### 方法
作者构建了一个以物体为中心的框架，把在线估计、基于流的规划与全身控制闭合成一个环路。该环路存在内在张力：
- 若信念一旦变化就替换规划，会打断正在进行的操作动作；
- 若坚持原有规划，机器人则会被困在已被新证据排除的路径上。

为解决这一矛盾，论文提出 Belief-Overlap Partial Inversion（BOPI）。其核心思想是让修正幅度与新旧信念的一致程度相匹配：仅在两个信念出现分歧的范围内，对旧信念下生成的流进行反转，随后在新信念下重建规划。这样既不会全盘丢弃正在执行的计划，也不会无视新的估计证据。

### 实验设置与关键结果
- 仿真：在 18 个目标上进行评估。
- 对比基线：固定深度重规划（fixed-depth replanning）。
- 结果：BOPI 将汇总的最终位置误差降低约 33%，偏航误差降低约 47%。
- 硬件：在真实硬件上实现了对非完整约束推车的平移与转向。

### 结论
BOPI 通过按信念一致程度缩放规划修正，缓解了在线估计与规划替换之间的冲突，在仿真中显著降低位置与偏航误差，并在硬件上验证了对未知属性非完整推车的操作能力。

## Overview

People often learn how an unfamiliar object moves through a small exploratory push, using its response to guide their next motion. Inspired by this behavior, we study humanoids pushing carts whose mass and caster stiffness are initially unknown. Our object-centric framework closes online estimation, flow-based planning, and whole-body control into a loop, creating a tension: replacing the plan whenever the belief shifts disrupts the maneuver under way, while keeping it strands the robot on a path its evidence has ruled out. Belief-Overlap Partial Inversion (BOPI) scales revision to agreement, inverting the flow under the old belief only as far as the beliefs disagree before reconstructing under the new one. Across 18 simulated goals it lowers pooled final position and yaw error by roughly 33% and 47% against fixed-depth replanning, and on hardware it translates and turns a non-holonomic cart.

## 参考
- https://arxiv.org/abs/2610.13087
