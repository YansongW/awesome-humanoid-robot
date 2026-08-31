---
$id: ent_paper_liu_lac_linear_and_angular_complia_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'LAC: Linear and Angular Compliance for Humanoid Whole-body Control'
  zh: 'LAC: Linear and Angular Compliance for Humanoid Whole-body Control'
  ko: 'LAC: Linear and Angular Compliance for Humanoid Whole-body Control'
summary:
  en: Real-world humanoid tasks involve physical interaction with objects and humans, yet current controllers either reject
    external forces as disturbances or restrict compliance to limited body links while ignoring angular effects. We present
    LAC, a general whole-body controller that simultaneously realizes commanded Linear and Angular Compliance for wrenches
    applied to the upper body. First, we ...
  zh: LAC 是一种用于人形机器人全身控制的通用控制器，可同时实现施加于上半身外力（力与力矩）的线性与角向柔顺响应。该方法由 Yang Liu、Zhongkai Gu、Wei Zhu 和 Mitsuhiro Hayashibe 提出，通过大规模增强数据集与师生强化学习训练单一策略，并在仿真与真实实验中验证了全身柔顺响应、刚度命令的单调调节能力及遥操作移动操作任务的适用性。
  ko: Real-world humanoid tasks involve physical interaction with objects and humans, yet current controllers either reject
    external forces as disturbances or restrict compliance to limited body links while ignoring angular effects. We present
    LAC, a general whole-body controller that simultaneously realizes commanded Linear and Angular Compliance for wrenches
    applied to the upper body. First, we ...
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
- whole_body_control
- compliance_control
- reinforcement_learning
- humanoid_robotics
- teleoperation
- admittance_control
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-08-31'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-08-31). Bibliographic metadata from arXiv API (2608.25405);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2608.25405 LAC: Linear and Angular Compliance for Humanoid Whole-body Control'
  url: https://arxiv.org/abs/2608.25405
  date: '2026-08-26'
  accessed_at: '2026-08-31'
---

## 概述

LAC 针对现有控制器要么将外力视为扰动拒绝、要么仅对有限身体链接提供柔顺且忽略角向效应的问题，提出了一种通用全身控制方案。其核心思路是先从人类交互数据中提取接触帧，施加采样力与力偶事件，合成大规模增强数据集，并在每个接触链接上利用被动屈服运动链产生的虚拟力矩驱动虚拟导纳。随后，通过师生强化学习训练单一策略，使其在外部力与力矩作用下跟踪柔顺运动。实验表明，LAC 能对上身各处的力与力矩产生全身柔顺响应，刚度命令在整个范围内呈单调调节，并适用于遥操作移动操作任务。

## 核心内容

### 问题背景
真实世界的人形机器人任务常涉及与物体和人的物理交互，但现有控制器通常将外力视为扰动加以拒绝，或仅对有限身体链接提供柔顺控制，且忽略角向（力矩）效应。这限制了机器人在复杂交互场景中的安全性与适应性。

### 方法
LAC 提出一种通用全身控制器，同时实现施加于上半身的力与力矩的线性与角向柔顺。方法分为三步：
1. **数据合成**：从人类交互数据中提取接触帧，在接触帧上施加采样的力与力偶事件，生成大规模增强数据集。在每个接触链接处，外部力与由被动屈服运动链产生的虚拟力矩共同驱动虚拟导纳，该导纳在命令刚度下运行。
2. **策略训练**：采用师生强化学习框架，训练单一策略以在外部力与力矩作用下跟踪柔顺运动。
3. **控制输出**：策略输出全身关节命令，实现协调的柔顺响应。

### 实验设置与关键结果
- **仿真实验**：在仿真环境中验证了上身各处力与力矩作用下的全身柔顺响应，并测试了刚度命令的调节范围。
- **真实实验**：在真实人形机器人上复现了全身柔顺响应，确认了刚度命令在整个范围内呈单调调节特性。
- **应用验证**：展示了 LAC 在遥操作移动操作任务中的适用性，表明其能处理实际交互场景。

### 结论
LAC 提供了一种通用且可扩展的全身柔顺控制方法，同时处理线性与角向柔顺，克服了现有方法的局限性。其单一策略设计简化了部署，并在仿真与真实环境中均表现出稳定、可调节的柔顺行为，适用于需要物理交互的遥操作任务。

## Overview

Real-world humanoid tasks involve physical interaction with objects and humans, yet current controllers either reject external forces as disturbances or restrict compliance to limited body links while ignoring angular effects. We present LAC, a general whole-body controller that simultaneously realizes commanded Linear and Angular Compliance for wrenches applied to the upper body. First, we synthesize whole-body compliant responses into a large-scale augmented dataset. Sampled force and couple events are imposed on contact frames extracted from human interaction data. At each contact link, the external force and a virtual torque from the passively yielding kinematic chain drive a virtual admittance under the commanded stiffness. Subsequently, teacher-student reinforcement learning trains a single policy to track the compliant motions under external wrenches. Finally, extensive simulation and real-world experiments demonstrate whole-body compliant responses to wrenches across the upper body, monotonic modulation over the full range of both stiffness commands, and applicability to teleoperated loco-manipulation tasks. Project website: https://lac-humanoid.github.io/

## 参考
- https://arxiv.org/abs/2608.25405
