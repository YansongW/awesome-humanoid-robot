---
$id: ent_paper_miao_nexus_perceptive_whole_body_co_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'NEXUS: Perceptive Whole-Body Control for Terrain-Adaptive Teleoperation'
  zh: 'NEXUS: Perceptive Whole-Body Control for Terrain-Adaptive Teleoperation'
  ko: 'NEXUS: Perceptive Whole-Body Control for Terrain-Adaptive Teleoperation'
summary:
  en: Whole-body teleoperation requires a humanoid robot to reproduce a human operator's behavior even when their terrains
    differ. This demands that the robot perceive local terrain and adapt its posture and contacts accordingly, rather than
    copy the operator's motion frame by frame. However, paired motion data linking the same behaviors across flat ground and
    different terrains remain scarce, limiting ...
  zh: NEXUS 是一个面向人形机器人的感知式全身控制框架，由 Xiangyu Miao、Junsong Wu、Jiyuan Shi、Weiji Xie、Jinrui Han、Xingyi Wang、Weinan Zhang、Chenjia
    Bai 等人提出，旨在实现操作者与机器人所处地形不一致时的全身遥操作。其核心是可扩展的地形感知适配算法，能够跨动作与地形高效生成高质量配对运动数据，并基于总计近 1,000 小时的配对运动语料，通过 teacher-student 学习训练出感知式全身控制器。
  ko: Whole-body teleoperation requires a humanoid robot to reproduce a human operator's behavior even when their terrains
    differ. This demands that the robot perceive local terrain and adapt its posture and contacts accordingly, rather than
    copy the operator's motion frame by frame. However, paired motion data linking the same behaviors across flat ground and
    different terrains remain scarce, limiting ...
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
- humanoid_teleoperation
- whole_body_control
- terrain_adaptation
- teacher_student_learning
- perceptive_control
- motion_retargeting
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-10-05'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-10-05). Bibliographic metadata from arXiv API (2609.39000);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2609.39000 NEXUS: Perceptive Whole-Body Control for Terrain-Adaptive Teleoperation'
  url: https://arxiv.org/abs/2609.39000
  date: '2026-09-30'
  accessed_at: '2026-10-05'
---

## 概述

全身遥操作要求人形机器人在与操作者地形不同的情况下仍能复现操作者的行为，这需要机器人感知局部地形并相应调整姿态与接触，而非逐帧复制操作者动作。然而，同一行为在平地与不同地形上的配对运动数据十分稀缺，制约了地形自适应控制的学习监督。为此，作者提出 NEXUS 感知式全身控制框架，将人类运动指令与机载传感器反馈相结合。该工作首先设计了一种可扩展的地形感知适配算法，无需针对单个动作或地形调参即可高效生成高质量运动配对；随后利用总计近 1,000 小时的配对运动语料，通过 teacher-student 学习训练感知式全身控制器。实验表明该方法能高效、可扩展地生成高质量运动数据，NEXUS 在行为覆盖广度、地形适应性与跟踪保真度上均优于现有全身控制器，并实现零样本真机部署，在多种未见地形上完成实时全身遥操作。

## 核心内容

### 问题背景
全身遥操作的目标是让人形机器人复现人类操作者的行为，但当操作者与机器人所处地形不一致时，逐帧复制操作者动作的方式不再适用。机器人需要感知局部地形，并据此调整自身姿态与接触方式。制约这一能力学习的关键瓶颈在于数据：将同一行为在平地与不同地形上对应起来的配对运动数据仍然稀缺，导致地形自适应控制缺乏监督信号。

### 方法
- 提出 NEXUS，一个感知式全身控制框架，将人类运动指令与机载传感器反馈相结合，以支持跨不匹配地形的全身遥操作。
- 设计可扩展的地形感知适配算法，能够跨不同动作与不同地形高效生成高质量运动配对，且无需针对单个动作或单个地形进行调参。
- 构建总计近 1,000 小时的配对运动语料，并基于该语料通过 teacher-student 学习训练感知式全身控制器，使其能够在不同地形上复现被指令的行为。

### 实验与结果
- 实验验证了高质量运动数据生成的高效性与可扩展性。
- NEXUS 在行为覆盖广度、地形适应性与跟踪保真度方面表现良好，在所评估的基准上优于现有全身控制器。
- 实现零样本真机部署，可在多种未见地形上完成实时全身遥操作，进一步验证了方法的泛化能力。

### 结论
NEXUS 通过可扩展的地形感知适配数据生成与 teacher-student 学习，缓解了跨地形配对运动数据稀缺的问题，使感知式全身控制器兼具行为覆盖与地形适应能力，并成功迁移至真实世界的未见地形遥操作场景。项目网站为 https://nexus-humanoid.github.io。

## Overview

Whole-body teleoperation requires a humanoid robot to reproduce a human operator's behavior even when their terrains differ. This demands that the robot perceive local terrain and adapt its posture and contacts accordingly, rather than copy the operator's motion frame by frame. However, paired motion data linking the same behaviors across flat ground and different terrains remain scarce, limiting supervision for learning terrain-adaptive control. To enable whole-body teleoperation across mismatched terrains, we introduce NEXUS, a perceptive whole-body control framework that combines human motion commands with onboard sensory feedback. We first develop a scalable terrain-aware adaptation algorithm that efficiently generates high-quality motion pairs across motions and terrains without per-motion or per-terrain tuning. Using a paired motion corpus totaling nearly 1,000 hours, we train a perceptive whole-body controller through teacher-student learning to reproduce commanded behaviors across terrains. Experiments demonstrate efficient, scalable generation of high-quality motion data and show that NEXUS combines broad behavioral coverage with terrain adaptability and tracking fidelity, outperforming existing whole-body controllers on the evaluated benchmarks. Zero-shot real-world deployment enables real-time whole-body teleoperation on diverse unseen terrains, further validating the generalization of our method. Project website: https://nexus-humanoid.github.io/

## 参考
- https://arxiv.org/abs/2609.39000
