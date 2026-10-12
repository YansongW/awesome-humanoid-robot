---
$id: ent_paper_zhang_intermimicgen_scaling_humanoid_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'InterMimicGen: Scaling Humanoid Loco-Manipulation through Self-Evolving Motion Imitation'
  zh: 'InterMimicGen: Scaling Humanoid Loco-Manipulation through Self-Evolving Motion Imitation'
  ko: 'InterMimicGen: Scaling Humanoid Loco-Manipulation through Self-Evolving Motion Imitation'
summary:
  en: Captured human-object interactions provide rich supervision for humanoid loco-manipulation, but they are sparse, heterogeneous,
    and not directly executable by robots. We introduce InterMimicGen, a self-evolving motion-imitation framework in which
    robot motion data and a tracking policy improve each other. First, we consolidate motion-captured human-object interaction
    datasets and retarget them ...
  zh: InterMimicGen 是一个面向人形机器人全身移动操作（loco-manipulation）的自演化动作模仿框架，由 Yucheng Zhang、Sirui Xu、Jinhong Li 等研究者提出。它通过整合并重定向人-物交互动捕数据、训练基于物理的通用跟踪器，并构建数据飞轮来持续扩充可执行动作资源。该框架在仿真中实现了跨机器人构型的接触保持重定向与单一通用策略的广泛跟踪，并成功迁移到真实机器人。
  ko: Captured human-object interactions provide rich supervision for humanoid loco-manipulation, but they are sparse, heterogeneous,
    and not directly executable by robots. We introduce InterMimicGen, a self-evolving motion-imitation framework in which
    robot motion data and a tracking policy improve each other. First, we consolidate motion-captured human-object interaction
    datasets and retarget them ...
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
- motion_retargeting
- motion_imitation
- data_flywheel
- dexterous_manipulation
- sim_to_real
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-10-12'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-10-12). Bibliographic metadata from arXiv API (2610.06850);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2610.06850 InterMimicGen: Scaling Humanoid Loco-Manipulation through Self-Evolving Motion Imitation'
  url: https://arxiv.org/abs/2610.06850
  date: '2026-10-05'
  accessed_at: '2026-10-12'
- id: src_002
  type: website
  title: Project page
  url: https://sirui-xu.github.io/InterMimicGen
  accessed_at: '2026-10-12'
---

## 概述

InterMimicGen 针对人-物交互动捕数据稀疏、异构且无法被机器人直接执行的问题，提出了一套自演化的动作模仿框架。该框架首先整合动捕人-物交互数据集，并将其重定向为人形机器人参考动作，同时保留全身协调性与灵巧的手-物关系。随后，研究者训练了一个基于物理的通用跟踪器，在仿真中驱动机器人执行这些参考动作，其规模与多样性超越了以往的人形移动操作跟踪系统。框架的核心是一个数据飞轮：每一轮对交互发生的位置和身体执行方式进行小幅且保持任务语义的修改，微调跟踪器，并仅保留仿真执行能完成任务的变体作为下一轮种子。随着迭代增加，这些微小编辑在稀疏原始演示周围累积出更广的覆盖范围，同时保持任务语义与动作质量。

## 核心内容

### 问题背景
捕获的人-物交互数据为人形机器人的移动操作提供了丰富监督信号，但这类数据存在稀疏、异构的问题，且无法被机器人直接执行。如何将异构的人类演示转化为可持续扩展的机器人可执行动作资源，是人形机器人学习中的关键挑战。

### 方法
InterMimicGen 由三个相互衔接的部分组成：

- **数据整合与重定向**：整合动作捕捉的人-物交互数据集，并将其重定向为人形机器人参考动作。重定向过程保留全身协调性以及灵巧的手-物关系，从而生成一个规模大、多样性高的人形机器人参考动作集合，面向灵巧全身移动操作。
- **通用跟踪器训练**：训练一个基于物理的通用跟踪器，在仿真中由带灵巧手的人形机器人执行上述参考动作。该跟踪器覆盖的规模与多样性超过以往面向移动操作的人形跟踪系统。
- **数据飞轮**：每一轮对交互发生的位置以及身体的执行方式进行小幅、保持任务语义的修改，在这些变体上微调跟踪器，并仅保留仿真执行能够完成任务的变体，将其作为下一轮的种子。随着迭代次数增加，这些微小编辑在稀疏的原始演示周围复合出更广的覆盖范围，同时保持任务语义与动作质量。

### 实验与关键结果
实验展示了以下方面的能力：

- 跨机器人构型的接触保持重定向；
- 使用单一通用策略实现广泛跟踪；
- 可执行动作在增广轮次中持续增长；
- 向真实机器人的迁移。

### 结论
InterMimicGen 提供了一条统一路径，将异构的人类演示转化为面向人形机器人学习的、持续扩展的动作资源。

## Overview

Captured human-object interactions provide rich supervision for humanoid loco-manipulation, but they are sparse, heterogeneous, and not directly executable by robots. We introduce InterMimicGen, a self-evolving motion-imitation framework in which robot motion data and a tracking policy improve each other. First, we consolidate motion-captured human-object interaction datasets and retarget them into humanoid robot references while preserving whole-body coordination and dexterous hand-object relationships. This produces a large and diverse humanoid robot reference collection for dexterous whole-body loco-manipulation. Second, we train a physics-based generalist tracker that executes these references in simulation on a humanoid with dexterous hands, covering a scale and diversity beyond prior humanoid tracking systems for loco-manipulation. Third, we close a data flywheel: each round makes small, task-preserving changes to where an interaction takes place and how the body performs it, fine-tunes the tracker on them, and keeps only the variants whose simulated execution completes the task, which seed the next round. With more iterations, these small edits compound into broader coverage around the sparse original demonstrations while preserving task semantics and motion quality. Experiments show contact-preserving retargeting across robot configurations, broad tracking with a single generalist policy, executable motions that keep growing over augmentation rounds, and transfer to real robots. InterMimicGen provides a unified path from heterogeneous human demonstrations to a continually expanding motion resource for humanoid robot learning.

## 参考
- https://arxiv.org/abs/2610.06850
- https://sirui-xu.github.io/InterMimicGen
