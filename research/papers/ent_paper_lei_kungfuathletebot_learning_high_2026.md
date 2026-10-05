---
$id: ent_paper_lei_kungfuathletebot_learning_high_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'KungfuAthleteBot: learning high-dynamic humanoid motion from video with unified robust recovery'
  zh: 'KungfuAthleteBot: learning high-dynamic humanoid motion from video with unified robust recovery'
  ko: 'KungfuAthleteBot: learning high-dynamic humanoid motion from video with unified robust recovery'
summary:
  en: 'Video is an abundant, inexpensive source of human motion data that is rich in extreme athletic behaviors. Making it
    usable for humanoid robots, however, is not a matter of simply retargeting a reconstructed trajectory: video-derived motion
    is physically inconsistent, devoid of actuation information, and says nothing about failure or recovery. We present KungfuAthleteBot
    (KAB), a framework that ...'
  zh: KungfuAthleteBot（KAB）是一个从视频中学习高动态人形机器人运动的框架，由 Zhongxiang Lei、Lulu Cao、Xuyang Wang、Tianyi Qian、Jinyan Liu、Xuesong Li
    提出。该工作构建了来自国家级武术运动员视频的 KungfuAthlete 数据集，并针对视频动作物理不一致、缺乏驱动力信息、不含失败与恢复信息这三类问题分别给出解决方案。其核心机制是物理驱动的伪低动能（LKE）采样，使不可行的空中参考轨迹变得可学习，并在统一策略中同时实现抗扰与跌倒恢复，约
    0.7 s 内可从任意跌倒状态恢复。
  ko: 'Video is an abundant, inexpensive source of human motion data that is rich in extreme athletic behaviors. Making it
    usable for humanoid robots, however, is not a matter of simply retargeting a reconstructed trajectory: video-derived motion
    is physically inconsistent, devoid of actuation information, and says nothing about failure or recovery. We present KungfuAthleteBot
    (KAB), a framework that ...'
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
- humanoid_locomotion
- learning_from_video
- motion_retargeting
- fall_recovery
- disturbance_rejection
- physics_guided_learning
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-10-05'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-10-05). Bibliographic metadata from arXiv API (2610.03388);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2610.03388 KungfuAthleteBot: learning high-dynamic humanoid motion from video with unified robust recovery'
  url: https://arxiv.org/abs/2610.03388
  date: '2026-10-02'
  accessed_at: '2026-10-05'
---

## 概述

该工作把从视频学习高动态人形运动本身视为核心问题，而非简单地对重建轨迹做重定向。作者指出视频来源的动作存在三重缺陷：物理上不自洽、不含驱动力信息、也不提供失败与恢复的示范。为此，KAB 首先基于国家级武术运动员视频构建 KungfuAthlete 数据集，并用物理引导的抛物线轨迹修正消除腾空与落地阶段的高度漂浮、穿地和抖动。其次，由于视频不携带力信息，严格跟踪重建轨迹在动力学上不可行，作者提出物理驱动的伪低动能（LKE）采样，将初始化偏向动力学可行状态，让策略自行发现可行的驱动模式。最后，KAB 采用直接训练范式，在跟踪视频动作的同一策略内学习抗扰与跌倒恢复，无需恢复参考数据，也无需人工模式切换。在真实人形机器人上，该统一策略能从任意跌倒中约 0.7 s 恢复，为已报道的统一策略中最快恢复速度。

## 核心内容

### 问题背景
视频是丰富且廉价的人体运动数据来源，包含大量极端运动行为。但要让这些人形机器人可用，并不能只靠对重建轨迹做重定向，原因有三：视频推导出的运动在物理上不自洽、不包含驱动力（actuation）信息，并且完全没有关于失败与恢复的信息。作者将“从视频学习高动态运动”本身作为核心问题，并逐一解决上述三种失效模式。

### 方法
- **C1：KungfuAthlete 数据集与物理引导轨迹修正。** 作者从国家级武术运动员的视频构建 KungfuAthlete 数据集，并提出物理引导的抛物线轨迹修正，用于去除重建后腾空与落地阶段中的高度漂浮、地面穿透和高频抖动。
- **C2：物理驱动的伪低动能（LKE）采样。** 由于视频不携带力信息，严格跟踪重建轨迹在动力学上不可行，而误差驱动的初始化会不断把策略从不可行的空中姿态重新启动。LKE 采样作为核心机制，将初始化偏向动力学可行的状态，使策略能够发现可行的驱动模式，而不是去模仿不可行的动作。
- **C3：直接训练范式。** 抗扰与跌倒恢复在与视频动作跟踪相同的策略内学习，不需要恢复参考数据，也不需要人工模式切换。

### 实验设置与关键结果
- 在真实人形机器人上，KAB 能够从视频中学习动态技能。
- 该统一策略可从任意跌倒中恢复，恢复时间约为 0.7 s，作者称这是已报道的统一策略中最快的恢复速度。
- 针对统一策略的消融实验确认了其各组件的必要性。

### 结论
作者认为，解锁高动态人形技能的关键在于修复与补偿视频数据，而不仅仅是收集更多视频数据。

## Overview

Video is an abundant, inexpensive source of human motion data that is rich in extreme athletic behaviors. Making it usable for humanoid robots, however, is not a matter of simply retargeting a reconstructed trajectory: video-derived motion is physically inconsistent, devoid of actuation information, and says nothing about failure or recovery. We present KungfuAthleteBot (KAB), a framework that treats learning high-dynamic motion from video as the central problem and resolves each of these three failure modes in turn. (C1) We build the KungfuAthlete dataset from videos of national-level martial artists and introduce a physics-guided parabolic trajectory correction that removes height floating, ground penetration, and high-frequency jitter from reconstructed aerial and landing phases. (C2) Because video carries no force information, strict tracking of a reconstructed trajectory is dynamically infeasible, and error-driven initialization keeps re-launching the policy from infeasible aerial poses. We introduce physics-driven pseudo-low-kinetic-energy (LKE) sampling, our central mechanism for making such references learnable: it biases initialization towards dynamically feasible states, letting the policy discover feasible actuation patterns instead of imitating infeasible ones. (C3) Finally, we introduce a direct training paradigm in which disturbance rejection and fall recovery are learned inside the same policy that tracks the video motion, requiring no recovery reference data and no manual mode switching. On a humanoid robot, KAB learns dynamic skills from video and recovers from arbitrary falls in about 0.7 s, the fastest reported recovery for a unified policy. Ablations on the unified policy confirm the necessity of its components, supporting the view that repairing and compensating video data, rather than only collecting more of it, is what unlocks high-dynamic humanoid skills.

## 参考
- https://arxiv.org/abs/2610.03388
