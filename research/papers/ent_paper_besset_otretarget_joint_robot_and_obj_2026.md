---
$id: ent_paper_besset_otretarget_joint_robot_and_obj_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'OTRetarget: Joint Robot and Object Motion Retargeting via Optimal Transport'
  zh: 'OTRetarget: Joint Robot and Object Motion Retargeting via Optimal Transport'
  ko: 'OTRetarget: Joint Robot and Object Motion Retargeting via Optimal Transport'
summary:
  en: Transferring human motion to humanoid robots requires adapting the demonstrated motion to the robot morphology while
    preserving interactions with the environment. This is particularly challenging for loco-manipulation tasks, where contacts
    with the ground and manipulated objects must remain consistent despite differences in body proportions. Yet, skeletal
    motion alone does not fully describe ...
  zh: OTRetarget 是一种将人类演示中的机器人与多物体运动联合重定向的统一方法，由 Guillaume Besset 等人提出。该方法用带符号距离、最近表面点和相对方向表示表面交互，并借助熵最优传输在人体、机器人与物体几何之间迁移这些量，再将其纳入带约束的逆运动学求解中。在
    OMOMO 上，它取得 87% 的机器人-物体交互 Jaccard 分数与 8.7 mm 的深度误差，并成功迁移到实体 G1 人形机器人。
  ko: Transferring human motion to humanoid robots requires adapting the demonstrated motion to the robot morphology while
    preserving interactions with the environment. This is particularly challenging for loco-manipulation tasks, where contacts
    with the ground and manipulated objects must remain consistent despite differences in body proportions. Yet, skeletal
    motion alone does not fully describe ...
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
- optimal_transport
- humanoid_loco_manipulation
- inverse_kinematics
- whole_body_control
- human_to_robot_transfer
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-10-05'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-10-05). Bibliographic metadata from arXiv API (2609.36602);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2609.36602 OTRetarget: Joint Robot and Object Motion Retargeting via Optimal Transport'
  url: https://arxiv.org/abs/2609.36602
  date: '2026-09-29'
  accessed_at: '2026-10-05'
---

## 概述

将人类动作迁移到人形机器人时，需要在保持与环境交互的前提下适配机器人形态，这对同时涉及移动与操作的 loco-manipulation 任务尤为困难，因为地面接触和被操作物体的接触都必须保持一致。仅靠骨骼运动无法完整描述这些交互，而固定物体轨迹又会限制对新本体的适配。为此，作者提出 OTRetarget，一种从人类演示中联合重定向机器人与多物体运动的方法。它用带符号距离、最近表面点和相对方向刻画表面交互，并通过熵最优传输在人体、机器人与物体几何之间传递这些量。这些交互目标被纳入带约束的逆运动学公式，在保持接触与维持运动风格之间取得平衡，并逐帧联合优化机器人与物体位姿，且无需对场景或演示进行重新缩放。

## 核心内容

### 问题背景
把人类动作迁移到人形机器人，需要把演示动作适配到机器人形态，同时保留其与环境的交互。对 loco-manipulation 任务而言这一点尤其困难：地面接触与被操作物体的接触必须在身体比例不同的情况下仍然保持一致。然而，单纯的骨骼运动不足以完整描述这些交互，而固定物体轨迹又会限制动作对新本体的适配能力。

### 方法
作者提出 OTRetarget，一种从人类演示中联合重定向机器人与多物体运动的统一方法，其核心思路包括：
- 用带符号距离、最近表面点和相对方向来表示表面交互；
- 使用熵最优传输（entropic optimal transport）在人体、机器人与物体的几何之间迁移这些交互量；
- 将得到的交互目标纳入带约束的逆运动学公式，在接触保持与运动风格之间进行平衡，并逐帧联合优化机器人与物体位姿。

该公式能够处理机器人-物体以及物体-物体之间的交互，且不需要对场景或演示进行重新缩放。

### 实验设置与关键结果
方法在 OMOMO 上进行验证：
- 机器人-物体交互 Jaccard 分数达到 87%，深度误差为 8.7 mm；
- 对比方法 OmniRetarget 的对应结果为 28% 与 29.3 mm。

### 结论与实机验证
作者进一步展示了向实体 G1 人形机器人的迁移：使用在重定向参考上通过强化学习训练的全身体策略，覆盖包括双手将箱子拾取并放置到桌面在内的多种动作。

## Overview

Transferring human motion to humanoid robots requires adapting the demonstrated motion to the robot morphology while preserving interactions with the environment. This is particularly challenging for loco-manipulation tasks, where contacts with the ground and manipulated objects must remain consistent despite differences in body proportions. Yet, skeletal motion alone does not fully describe these interactions, and fixing object trajectories limits the adaptation to a new embodiment. In this paper, we introduce OTR ETARGET, a unified approach to jointly retarget robot and multi-object motion from human demonstrations. Our approach represents surface interactions through signed distances, closest surface points, and relative directions, and uses entropic optimal transport to transfer these quantities across human, robot, and object geometries. We incorporate the resulting interaction targets into a constrained inverse kinematics formulation that balances contact preservation with motion style and jointly optimizes robot and object poses at each frame. This formulation accommodates robot-object and object-object interactions without rescaling the scene or the demonstration. We validate the proposed approach on OMOMO, where it achieves a robot- object interaction Jaccard score of 87% and a depth error of 8.7 mm, compared with 28% and 29.3 mm for OmniRetarget. Finally, we demonstrate transfer to a physical G1 humanoid using whole-body policies trained with reinforcement learning on the retargeted references, across motions including two-handed box pick-and-place onto a table.

## 参考
- https://arxiv.org/abs/2609.36602
