---
$id: ent_paper_shi_motion_retargeting_with_spatio_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Motion Retargeting with Spatiotemporal Preferences for Humanoid Loco-Manipulation
  zh: Motion Retargeting with Spatiotemporal Preferences for Humanoid Loco-Manipulation
  ko: Motion Retargeting with Spatiotemporal Preferences for Humanoid Loco-Manipulation
summary:
  en: Human motion retargeting bridges the embodiment gap between humans and humanoid robots by converting human demonstrations
    into reference trajectories for whole-body control and loco-manipulation. For object-interaction tasks, successful execution
    depends on accurately preserving body--object relations at critical stages. However, uniform per-frame iteration budgets
    do not account for these ...
  zh: 本文提出 Spatiotemporal Retargeting（STR），一种面向人形机器人全身控制与 loco-manipulation 的运动重定向方法，由 Xiongbo Shi、Shihang Du 等完成。STR 借助视觉语言模型挑选关键运动信号与身体部位，并据此在关键帧上分配更多求解迭代、对选定部位施加更高交互权重，从而在降低计算开销的同时提升接触精度。作者还引入
    Mechanics-Aware Contact Anchoring（MCA）细化物体表面接触位置，并基于所得参考设计 Spatiotemporal Reinforcement Learning（STRL）用于下游控制。
  ko: Human motion retargeting bridges the embodiment gap between humans and humanoid robots by converting human demonstrations
    into reference trajectories for whole-body control and loco-manipulation. For object-interaction tasks, successful execution
    depends on accurately preserving body--object relations at critical stages. However, uniform per-frame iteration budgets
    do not account for these ...
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
- motion_retargeting
- humanoid_loco_manipulation
- whole_body_control
- contact_anchoring
- reinforcement_learning
- vision_language_model
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-10-26'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-10-26). Bibliographic metadata from arXiv API (2610.30540);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: arXiv:2610.30540 Motion Retargeting with Spatiotemporal Preferences for Humanoid Loco-Manipulation
  url: https://arxiv.org/abs/2610.30540
  date: '2026-10-21'
  accessed_at: '2026-10-26'
---

## 概述

人形机器人要利用人类演示完成物体交互任务，需要把人体运动转换为可供全身控制器使用的参考轨迹，而这类任务的成功与否取决于关键阶段身体与物体关系能否被准确保持。现有方法对每一帧采用统一的迭代预算，无法兼顾这种局部化的精度需求，导致重定向的计算效率受限。为此作者提出 Spatiotemporal Retargeting（STR），用关键帧与关键身体部位来分配优化资源：由视觉语言模型选择相关运动信号与身体部位，再依据所选信号的变化确定关键帧，并对关键帧增加求解器迭代、对选定部位提高交互权重。为进一步改善接触保真度，作者引入 Mechanics-Aware Contact Anchoring（MCA），在保留所选表面方向的前提下，利用近似物体力旋量模型细化物体表面接触位置。在所得参考基础上，作者开发了 Spatiotemporal Reinforcement Learning（STRL），将自适应关键阶段采样与基于目标接近度和物体接触力的接触奖励结合用于下游控制。在 Unitree G1 上的仿真实验与在 Unitree R1 上的真实实验表明，STR 以更低计算成本提升了几何接触覆盖度与连续性，所得参考也改善了多种物体交互运动的下游任务完成情况。

## 核心内容

### 问题背景
人形机器人通过运动重定向把人类演示转换为参考轨迹，从而跨越人与机器人之间的 embodiment gap，支撑全身控制与 loco-manipulation。对于物体交互任务，执行成功与否取决于能否在关键阶段准确保持身体与物体之间的关系。然而，现有重定向方法对每一帧使用统一的迭代预算，没有考虑这些局部化的精度要求，因而限制了重定向的计算效率。

### 方法
- **Spatiotemporal Retargeting（STR）**：以关键帧和关键身体部位为依据分配优化努力。具体而言，由一个视觉语言模型选择相关的运动信号与身体部位，关键帧则根据所选信号的变化来识别。基于这些选择，STR 对关键帧分配额外的求解器迭代，并对选定部位赋予更高的交互权重。
- **Mechanics-Aware Contact Anchoring（MCA）**：用于进一步提升接触保真度。它借助一个近似的物体力旋量（object-wrench）模型来细化物体表面的接触位置，同时保留所选的表面方向。
- **Spatiotemporal Reinforcement Learning（STRL）**：在 STR 生成的参考基础上构建，用于下游控制。它结合了自适应关键阶段采样，以及一个基于目标接近度与物体接触力的接触奖励。

### 实验设置
仿真实验在 Unitree G1 上进行，真实世界实验在 Unitree R1 上进行。

### 关键结果
实验表明，STR 在更低的计算成本下提升了几何接触覆盖度与连续性；由 STR 生成的参考还改善了多种物体交互运动在下游任务中的完成情况。

### 结论
通过将优化资源集中到关键帧与关键身体部位，并结合接触锚定与面向关键阶段的强化学习，STR 在效率与接触精度之间取得了更好的平衡，并验证了其在仿真与真实人形机器人平台上的有效性。

## Overview

Human motion retargeting bridges the embodiment gap between humans and humanoid robots by converting human demonstrations into reference trajectories for whole-body control and loco-manipulation. For object-interaction tasks, successful execution depends on accurately preserving body--object relations at critical stages. However, uniform per-frame iteration budgets do not account for these localized accuracy requirements, limiting the computational efficiency of retargeting. To address this limitation, we present Spatiotemporal Retargeting (STR), which uses keyframes and key body parts to allocate optimization effort. Specifically, a vision-language model selects relevant motion signals and body parts, and keyframes are identified from changes in the selected signals. Based on these selections, STR assigns additional solver iterations to keyframes and higher interaction weights to the selected parts. To further improve contact fidelity, we introduce Mechanics-Aware Contact Anchoring (MCA) to refine object-surface contact positions using an approximate object-wrench model while retaining the selected surface directions. Building on the resulting references, we develop Spatiotemporal Reinforcement Learning (STRL), which combines adaptive key-stage sampling with a contact reward based on target proximity and object contact forces for downstream control. Simulation experiments on a Unitree G1 and real-world experiments on a Unitree R1 demonstrate that STR improves geometric contact coverage and continuity at lower computational cost, while the resulting references improve downstream task completion across diverse object-interaction motions.

## 参考
- https://arxiv.org/abs/2610.30540
