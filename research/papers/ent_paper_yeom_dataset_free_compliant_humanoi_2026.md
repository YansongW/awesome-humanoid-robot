---
$id: ent_paper_yeom_dataset_free_compliant_humanoi_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Dataset-Free Compliant Humanoid Loco-Manipulation with Dynamic Online Posture
  zh: Dataset-Free Compliant Humanoid Loco-Manipulation with Dynamic Online Posture
  ko: Dataset-Free Compliant Humanoid Loco-Manipulation with Dynamic Online Posture
summary:
  en: Most humanoid loco-manipulation controllers require human motion data to learn whole-body coordination and posture,
    leaving policies reliant on external sources to provide this data. We present OCLO (Online-posture Compliant LOco-manipulation),
    a humanoid loco-manipulation system trained without human motion data and commanded only through two end-effector targets.
    Because these targets do not ...
  zh: OCLO 是一套无需人类运动数据训练的人形机器人全身移动操作（loco-manipulation）系统，由 Seungho Yeom、Zhenyu Wu、Jaeyoung Huh、Diego Williams、Yuheng Zhi、Soofiyan
    Atar、Michael Yip 提出，仅通过两个末端执行器目标进行指令控制。由于末端目标无法唯一确定全身姿态，OCLO 利用解析可达性先验在线生成骨盆高度与躯干朝向，并通过策略在环采样与任务无关代价进一步精修，同时借助弹簧-阻尼模型学习全身柔顺性。仿真中可达性先验将指令参考获取成功率从
    37.8% 提升至 77.8%，并在 Unitree G1 上完成七项移动操作任务。
  ko: Most humanoid loco-manipulation controllers require human motion data to learn whole-body coordination and posture,
    leaving policies reliant on external sources to provide this data. We present OCLO (Online-posture Compliant LOco-manipulation),
    a humanoid loco-manipulation system trained without human motion data and commanded only through two end-effector targets.
    Because these targets do not ...
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
- compliant_control
- whole_body_control
- data_free_training
- online_posture_generation
- unitree_g1
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-10-12'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-10-12). Bibliographic metadata from arXiv API (2610.05678);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: arXiv:2610.05678 Dataset-Free Compliant Humanoid Loco-Manipulation with Dynamic Online Posture
  url: https://arxiv.org/abs/2610.05678
  date: '2026-10-05'
  accessed_at: '2026-10-12'
---

## 概述

OCLO（Online-posture Compliant LOco-manipulation）面向人形机器人移动操作中普遍依赖人类运动数据的问题，提出一种完全无需此类数据的训练方案，控制接口仅有两个末端执行器目标。由于末端目标本身不足以唯一确定全身姿态，系统引入解析可达性先验在线生成骨盆高度与躯干朝向，并利用策略在环采样配合任务无关代价进行精修。为应对外部扰动，OCLO 通过弹簧-阻尼模型依据实测力偏移末端参考，从而学习全身柔顺行为，使腿、腰与骨盆能够顺应外载。仿真结果显示，可达性先验使指令参考获取成功率由 37.8% 提升至 77.8%，精修环节则在所有评估任务上降低末端朝向误差，同一姿态模块还能在五项任务中的四项上改进预训练的 SONIC 控制器。在 Unitree G1 实机上，OCLO 能在导致消融版本失败的末端扰动下保持平衡，并完成包括蹲姿行走与从低矮表面拾取箱子在内的七项移动操作任务。

## 核心内容

### 问题背景
现有人形机器人移动操作控制器大多依赖人类运动数据来学习全身协调与姿态，导致策略必须依靠外部数据源提供姿态信息。OCLO 的目标是在不使用人类运动数据的前提下实现全身移动操作，且仅以两个末端执行器目标作为指令输入。

### 方法
- **姿态生成**：由于两个末端目标无法唯一确定全身姿态，OCLO 使用解析可达性先验在线生成骨盆高度与躯干朝向。
- **在线精修**：在可达性先验基础上，通过策略在环采样（policy-in-the-loop sampling）与任务无关代价（task-agnostic cost）对姿态进一步精修。
- **柔顺性学习**：依据实测力，通过弹簧-阻尼模型偏移末端执行器参考，使腿、腰与骨盆能够顺应外部载荷，从而学习全身柔顺行为。

### 实验设置与关键结果
- 仿真中，使用可达性先验时获取指令参考的成功率为 77.8%，不使用先验时为 37.8%。
- 姿态精修在所有评估任务上均降低了末端执行器朝向误差。
- 同一姿态模块在五项任务中的四项上改进了预训练的 SONIC 控制器。
- 未经过柔顺性训练的策略在扰动下倾向于失去平衡，而非牺牲跟踪精度。
- 在 Unitree G1 实机上，OCLO 能在导致其消融版本失败的末端执行器扰动下保持平衡，并完成七项移动操作任务，包括蹲姿行走以及从低矮表面拾取箱子。

### 结论
OCLO 表明，无需人类运动数据、仅凭两个末端目标即可训练出具备全身协调与柔顺能力的人形移动操作策略；解析可达性先验与在线精修显著提升参考获取成功率与朝向精度，柔顺性训练则是在扰动下维持平衡的关键。项目网站为 https://oclo-humanoid.github.io/。

## Overview

Most humanoid loco-manipulation controllers require human motion data to learn whole-body coordination and posture, leaving policies reliant on external sources to provide this data. We present OCLO (Online-posture Compliant LOco-manipulation), a humanoid loco-manipulation system trained without human motion data and commanded only through two end-effector targets. Because these targets do not uniquely determine whole-body posture, OCLO generates pelvis height and torso orientation online using an analytic reachability prior, further refined through policy-in-the-loop sampling with a task-agnostic cost. OCLO also learns whole-body compliance by displacing end-effector references according to measured forces through a spring-damper model, encouraging the legs, waist, and pelvis to yield to external loads. In simulation, using the reachability prior leads to a 77.8% success rate in acquiring the commanded reference, a vast improvement over the 37.8% success rate accomplished without the prior. Further, refinement reduces end-effector orientation error across all evaluated tasks. The same posture module improves a pretrained SONIC controller on four of five tasks. Without compliance training, policies tend to lose balance under disturbances rather than sacrifice tracking. On a Unitree G1, OCLO maintains balance under end-effector disturbances that cause its ablations to fail and performs seven loco-manipulation tasks, including crouched walking and picking up a box from a low surface. Project website: https://oclo-humanoid.github.io/

## 参考
- https://arxiv.org/abs/2610.05678
