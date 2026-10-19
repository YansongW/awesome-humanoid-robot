---
$id: ent_paper_zhou_koda_kinematics_observation_da_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'KODA: Kinematics--Observation Data Alignment for Humanoid Learning from Human Egocentric Demonstration'
  zh: 'KODA: Kinematics--Observation Data Alignment for Humanoid Learning from Human Egocentric Demonstration'
  ko: 'KODA: Kinematics--Observation Data Alignment for Humanoid Learning from Human Egocentric Demonstration'
summary:
  en: Training humanoid whole-body vision-language-action (VLA) policies requires costly robot demonstrations with aligned
    robot-view observations and controller-compatible whole-body state-action labels. Egocentric human demonstrations offer
    scalable supervision but have misaligned views and sparse motion cues. Existing approaches either pretrain policies that
    still require robot data for adaptation ...
  zh: KODA（Kinematics–Observation Data Alignment）由 Zibo Zhou、Yueru Chen 等人提出，用于将第一人称人类演示转换为人形机器人全身 VLA 训练数据。该方法借助可复用的规范轨迹同时引导机器人视角观测合成与控制器相关的全身状态-动作监督生成，从而避免重复采集机器人数据。在
    Unitree G1 的四项移动操作任务上，使用 SONIC 与 HEFT 两种全身控制器时，人类演示覆盖但机器人数据缺失条件下的宏平均成功率分别提升 45.0 与 46.25 个百分点。
  ko: Training humanoid whole-body vision-language-action (VLA) policies requires costly robot demonstrations with aligned
    robot-view observations and controller-compatible whole-body state-action labels. Egocentric human demonstrations offer
    scalable supervision but have misaligned views and sparse motion cues. Existing approaches either pretrain policies that
    still require robot data for adaptation ...
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
- humanoid_robot
- vision_language_action
- egocentric_demonstration
- data_alignment
- whole_body_control
- loco_manipulation
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-10-19'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-10-19). Bibliographic metadata from arXiv API (2610.21152);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2610.21152 KODA: Kinematics--Observation Data Alignment for Humanoid Learning from Human Egocentric Demonstration'
  url: https://arxiv.org/abs/2610.21152
  date: '2026-10-15'
  accessed_at: '2026-10-19'
---

## 概述

训练人形机器人全身视觉-语言-动作策略通常依赖昂贵的机器人演示，且需要机器人视角观测与控制器兼容的全身状态-动作标签。第一人称人类演示虽可扩展，却存在视角不匹配与运动线索稀疏的问题。KODA 的核心思路是构建一条可复用的规范轨迹：先用稀疏跟踪器配合基于采样的指令优化生成经仿真器校验的全身轨迹，再由该轨迹确定机载相机位姿并合成机器人视角观测，与运动、任务指令共同构成规范记录。针对不同部署控制器，KODA 在保留规范记录的前提下重新优化跟踪指令并记录动作标签与本体状态，从而在切换控制器时无需重采数据。实验在 Unitree G1 的四项移动操作任务上以 SONIC 和 HEFT 两种控制器验证，在机器人数据固定的条件下，人类演示覆盖而机器人数据未覆盖条件的宏平均成功率分别提升 45.0 与 46.25 个百分点，且随人类数据预算增加呈上升趋势。

## 核心内容

### 问题背景

人形机器人全身 VLA 策略的训练需要大量机器人演示，且每条演示必须同时具备与机器人视角对齐的观测，以及控制器可执行的全身体状态-动作标签，采集成本高昂。第一人称人类演示提供了可扩展的监督来源，但存在两方面障碍：其视角与机器人视角不一致，且运动线索稀疏。已有方法要么预训练后仍需机器人数据做适配，要么直接生成特定控制器的指令，导致数据难以复用。此外，将人类演示转换为训练数据时，还需要与生成的全身体运动相匹配的机器人视角观测。

### 方法

KODA（Kinematics–Observation Data Alignment）将第一人称 RGB 演示转换为全身 VLA 训练数据，其关键设计是一条可复用的规范轨迹，同时服务于机器人视角合成与控制器相关监督生成。

- **规范轨迹生成**：使用稀疏跟踪器结合基于采样的指令优化，生成经仿真器校验的全身轨迹。
- **机器人视角观测合成**：由生成的全身体轨迹直接确定机载相机位姿，据此合成对应的机器人视角观测。
- **规范记录构建**：将运动、观测与任务指令组合为一条规范记录。
- **控制器相关监督生成**：针对每个部署控制器，优化指令以跟踪已存储的运动，并记录相应的动作标签与本体状态。
- **控制器切换复用**：切换控制器时保留规范记录，仅为新控制器重新生成全身状态-动作监督，并与匹配的机器人演示联合训练。

### 实验设置

实验在 Unitree G1 上开展，覆盖四项移动操作（loco-manipulation）任务，使用两种全身控制器 SONIC 与 HEFT。评估关注人类演示已覆盖但机器人数据中缺失的条件，并在机器人数据保持固定的前提下考察不同人类数据预算的影响。

### 关键结果

- 在机器人数据固定的条件下，上述条件的宏平均成功率在 SONIC 与 HEFT 下分别提升 45.0 与 46.25 个百分点。
- 在两种控制器下，该指标随所评估的人类数据预算增加呈上升趋势，表明存在进一步扩展的潜力。

### 结论

KODA 通过规范轨迹将人类第一人称演示解耦为可复用的运动与观测记录，并按控制器重新生成状态-动作监督，为人形机器人全身 VLA 策略提供了可扩展且控制器可复用的数据转换路径。

## Overview

Training humanoid whole-body vision-language-action (VLA) policies requires costly robot demonstrations with aligned robot-view observations and controller-compatible whole-body state-action labels. Egocentric human demonstrations offer scalable supervision but have misaligned views and sparse motion cues. Existing approaches either pretrain policies that still require robot data for adaptation or generate controller-specific commands that limit reuse. Conversion also requires robot-view observations aligned with the generated whole-body motion. We present KODA (Kinematics-Observation Data Alignment), which converts egocentric RGB demonstrations into whole-body VLA training data using a reusable canonical trajectory to guide robot-view synthesis and generate controller-specific whole-body state-action supervision. KODA first generates a simulator-checked whole-body trajectory using a sparse tracker with sampling-based command optimization. This generated trajectory directly determines the onboard camera poses used to synthesize corresponding robot-view observations. The motion, observations, and task instruction form a canonical record. For each deployment controller, KODA optimizes commands to track the stored motion and records the corresponding action labels and proprioceptive states. When switching controllers, KODA retains this canonical record and regenerates whole-body state-action supervision for co-training with matching robot demonstrations. We evaluate KODA on four Unitree G1 loco-manipulation tasks using two whole-body controllers, SONIC and HEFT. With robot data held fixed, macro-average success on conditions covered by human demonstrations but absent from robot data improves by 45.0 and 46.25 percentage points, respectively. Under both controllers, this metric shows an upward trend across the evaluated human-data budgets, suggesting potential for further scaling.

## 参考
- https://arxiv.org/abs/2610.21152
