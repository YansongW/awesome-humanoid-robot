---
$id: ent_paper_ioannidis_primoretarget_humanoid_motion_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'PriMoRetarget: Humanoid Motion Transfer Through Prioritized Motion Retargeting'
  zh: 'PriMoRetarget: Humanoid Motion Transfer Through Prioritized Motion Retargeting'
  ko: 'PriMoRetarget: Humanoid Motion Transfer Through Prioritized Motion Retargeting'
summary:
  en: Motion retargeting is a critical preprocessing step for transferring human motion data to humanoid robots. While existing
    methods are effective for single-character motions, interactions involving multiple characters and objects introduce additional
    contacts and spatial relationships that must be preserved. Retargeting is commonly formulated as a weighted multi-objective
    optimization problem, ...
  zh: PriMoRetarget 是一种面向人形机器人的动作重定向框架，由 Nicholas Ioannidis、Dun Yang、Max Smith、Tue Vu、Ziyu Zhang、Shayegan Omidshafiei 与 Xue
    Bin Peng 提出。它用显式的优先级层级替代传统加权多目标优化中的相对权重，使低优先级更新受高优先级目标的约束。该方法在覆盖单角色动作、角色-物体操作与角色-角色交互的四类数据集上进行了评估。
  ko: Motion retargeting is a critical preprocessing step for transferring human motion data to humanoid robots. While existing
    methods are effective for single-character motions, interactions involving multiple characters and objects introduce additional
    contacts and spatial relationships that must be preserved. Retargeting is commonly formulated as a weighted multi-objective
    optimization problem, ...
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
- humanoid_robots
- multi_objective_optimization
- priority_hierarchy
- human_motion_transfer
- character_interaction
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-10-12'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-10-12). Bibliographic metadata from arXiv API (2610.12642);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2610.12642 PriMoRetarget: Humanoid Motion Transfer Through Prioritized Motion Retargeting'
  url: https://arxiv.org/abs/2610.12642
  date: '2026-10-08'
  accessed_at: '2026-10-12'
---

## 概述

将人类动作数据迁移到人形机器人时，动作重定向是关键的前置步骤。已有方法在单角色动作上表现良好，但当多个角色与物体发生交互时，会引入额外的接触与空间关系，这些关系必须被保留。常见做法是把重定向建模为加权多目标优化问题，而目标之间相互冲突，往往需要仔细调参，即便如此仍可能损害重要的动作特征。PriMoRetarget 提出以显式的优先级层级取代相对权重：低优先级的更新被约束为不破坏高优先级目标，从而让足部落点、交互接触等关键特征优先于较低优先级的姿态目标。作者在四个数据集上评估了该方法，涵盖单角色动作、角色-物体操作与角色-角色交互。

## 核心内容

### 问题背景

把人类动作数据迁移到人形机器人时，动作重定向是不可或缺的预处理环节。现有方法在单角色动作场景下效果良好，但一旦涉及多个角色与物体的交互，就会产生额外的接触与空间关系，这些关系在重定向过程中必须得到保持。该问题通常被表述为加权多目标优化：不同目标之间存在冲突，需要谨慎调节相对权重，而即便调参得当，仍可能牺牲重要的动作特征。

### 方法

PriMoRetarget 的核心是用显式的优先级层级替代相对目标权重。在这一框架下，低优先级的更新受到约束，必须保留高优先级目标已经达成的结果。由此，足部落点、交互接触等关键动作特征可以优先于优先级较低的姿态目标得到满足。

### 实验设置

评估覆盖四个数据集，场景跨度包括：

- 单角色动作
- 角色-物体操作
- 角色-角色交互

### 关键结果

与广泛使用的重定向方法相比，PriMoRetarget 生成的动作能更好地保留与任务相关的交互，并且所产生的参考轨迹可以被更可靠地跟踪。

### 结论

通过引入优先级层级而非相对权重，PriMoRetarget 缓解了多目标冲突下的调参负担与动作特征损失问题，为包含多角色、多物体交互的动作重定向提供了更可靠的参考轨迹。

## Overview

Motion retargeting is a critical preprocessing step for transferring human motion data to humanoid robots. While existing methods are effective for single-character motions, interactions involving multiple characters and objects introduce additional contacts and spatial relationships that must be preserved. Retargeting is commonly formulated as a weighted multi-objective optimization problem, where conflicting objectives can require careful tuning of relative weights and can still compromise important motion characteristics. We introduce PriMoRetarget, a prioritized motion-retargeting framework that replaces relative objective weighting with an explicit priority hierarchy. Lower-priority updates are constrained to preserve higher-priority objectives, allowing critical characteristics such as foot placement and interaction contacts to take precedence over lower-priority pose objectives. The method is evaluated on four datasets spanning single-character motion, character-object manipulation, and character-character interactions. The resulting motions better preserve task-relevant interactions and provide reference trajectories that can be tracked more reliably than those produced by widely used retargeting methods.

## 参考
- https://arxiv.org/abs/2610.12642
