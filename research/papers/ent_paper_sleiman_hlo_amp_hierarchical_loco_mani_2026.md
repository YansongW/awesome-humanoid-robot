---
$id: ent_paper_sleiman_hlo_amp_hierarchical_loco_mani_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'HLO-AMP: Hierarchical Loco-Manipulation from Object-Aware Motion Priors'
  zh: 'HLO-AMP: Hierarchical Loco-Manipulation from Object-Aware Motion Priors'
  ko: 'HLO-AMP: Hierarchical Loco-Manipulation from Object-Aware Motion Priors'
summary:
  en: Hierarchical pipelines for humanoid loco-manipulation typically pair a task-agnostic whole-body controller (WBC) with
    a downstream task policy. Such WBCs are often trained through manual reward shaping, which yields visibly machine-like
    motions; more consequentially, they are trained without the manipulated object in the scene. Object dynamics are instead
    approximated through randomized ...
  zh: HLO-AMP 是一种面向人形机器人全身移动操作的分层框架，由 Jean-Pierre Sleiman 等人提出。其核心是将低层控制器训练为具备物体感知的运动先验：用重定向动作捕捉参考做运动模仿，并让被操作物体真实存在于场景中，从而继承类人协调性并吸收真实接触力旋量。高层策略无需参考轨迹，其动作通道被锚定在低层训练数据的经验包络内，以避免低层进入分布外状态。作者在
    Unitree G1 上以双臂箱子取放任务验证了该框架。
  ko: Hierarchical pipelines for humanoid loco-manipulation typically pair a task-agnostic whole-body controller (WBC) with
    a downstream task policy. Such WBCs are often trained through manual reward shaping, which yields visibly machine-like
    motions; more consequentially, they are trained without the manipulated object in the scene. Object dynamics are instead
    approximated through randomized ...
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
- motion_prior
- motion_imitation
- hierarchical_control
- whole_body_control
- sim_to_real
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-11-09'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-11-09). Bibliographic metadata from arXiv API (2611.05113);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2611.05113 HLO-AMP: Hierarchical Loco-Manipulation from Object-Aware Motion Priors'
  url: https://arxiv.org/abs/2611.05113
  date: '2026-11-03'
  accessed_at: '2026-11-09'
- id: src_002
  type: website
  title: Project page
  url: https://youtu.be/viR_ULnRDQQ
  accessed_at: '2026-11-09'
---

## 概述

传统人形机器人移动操作的分层流水线通常由一个与任务无关的全身控制器搭配下游任务策略，而这类控制器多依赖人工奖励塑形训练，动作显得机械，且训练时场景中并不存在被操作物体，只能用随机末端力扰动近似物体动力学，难以复现真实负载在手臂与躯干上产生的分布式多接触力旋量，在接近平台负载上限时问题尤为突出。HLO-AMP 改为把低层控制器本身训练成物体感知的运动先验：单一策略通过模仿覆盖下游任务核心运动原语的重定向 MoCap 参考来学习，训练时物体物理存在于场景中，因此既继承了参考中自然的人体协调性，也在源头吸收了真实接触力旋量，同时保留与指令跟踪型 WBC 相同的紧凑任务空间指令接口。在此之上训练一个无参考的高层策略，其动作通道被锚定在低层训练数据的经验包络内，从而把先验泛化到长时程多阶段任务，并在结构上防止查询把低层推离分布。作者在 Unitree G1 上实例化该框架用于双臂箱子取放，同一部署策略可泛化到不同物体质量与尺寸、不同初始与目标位姿，并能在搬运途中被故意掉落时做出反应性恢复。

## 核心内容

### 问题背景

- 人形机器人移动操作常采用分层流水线：任务无关的全身控制器（WBC）加下游任务策略。
- 此类 WBC 多通过人工奖励塑形训练，动作呈现明显的机械感。
- 更关键的是，WBC 训练时场景中没有被操作物体，物体动力学只能以随机末端执行器力扰动来近似。
- 这种代理无法复现真实负载在手臂与躯干上施加的分布式多接触力旋量，当接近平台负载上限时，差距变得尤为关键。

### 方法

- **低层（LL）控制器作为物体感知运动先验**：用单一策略在重定向的动作捕捉（MoCap）参考上做运动模仿训练，这些参考覆盖下游任务的核心运动原语，且训练时被操作物体物理存在于场景中。
- 该单阶段训练同时带来两点收益：从参考中继承自然的类人协调性；在源头吸收真实接触力旋量。
- 低层对外暴露与指令跟踪型 WBC 相同的紧凑任务空间指令接口。
- **高层（HL）策略**：无参考，训练于低层之上；其动作通道被锚定在低层训练数据的经验包络内，从而将先验泛化到长时程多阶段任务，并在结构上防止产生会把低层推离分布的查询。

### 实验设置

- 平台：Unitree G1。
- 任务：双臂箱子取放（bimanual box pick-and-place）。

### 关键结果

- 同一部署策略可泛化到不同的物体质量与尺寸。
- 可泛化到不同的初始位姿与目标位姿。
- 能在搬运途中被故意掉落时做出反应性恢复。

### 结论

将低层控制器本身训练为物体感知的运动先验，并以经验包络约束高层动作通道，可在无需人工奖励塑形与随机力扰动代理的情况下，获得类人协调的全身移动操作能力，并在 Unitree G1 的双臂取放任务上展现出对物体属性、位姿变化与中途掉落的泛化与恢复能力。

## Overview

Hierarchical pipelines for humanoid loco-manipulation typically pair a task-agnostic whole-body controller (WBC) with a downstream task policy. Such WBCs are often trained through manual reward shaping, which yields visibly machine-like motions; more consequentially, they are trained without the manipulated object in the scene. Object dynamics are instead approximated through randomized end-effector force disturbances, a proxy that fails to reproduce the distributed multi-contact wrench a real payload applies across the arms and torso, with the gap becoming critical near the platform's payload limit. In this work, we train the low-level (LL) controller itself as an object-aware motion prior: a single policy trained via motion imitation on retargeted motion-capture (MoCap) references that span the core motion primitives of the downstream task, with the manipulated object physically present in the scene. This single stage inherits natural human-like coordination from the references and absorbs the realistic contact wrench at its source, while exposing the same compact task-space command interface used by command-tracking WBCs. A reference-free high-level (HL) policy is then trained on top, with its action channel anchored to the empirical envelope of the low-level training data so that it generalizes the priors to a long-horizon multi-stage task while structurally preventing queries that would push the low level off-distribution. We instantiate the framework on a Unitree G1 for bimanual box pick-and-place: the same deployed policy generalizes across object masses and dimensions, initial and goal poses, and reactively recovers from intentional drops mid-carry. Video: https://youtu.be/viR_ULnRDQQ.

## 参考
- https://arxiv.org/abs/2611.05113
- https://youtu.be/viR_ULnRDQQ
