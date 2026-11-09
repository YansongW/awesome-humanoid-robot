---
$id: ent_paper_hu_perceptive_humanoid_motion_fro_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Perceptive Humanoid Motion from Simulation
  zh: Perceptive Humanoid Motion from Simulation
  ko: Perceptive Humanoid Motion from Simulation
summary:
  en: 'Humanoid robots have the potential to automate a wide range of physical tasks. Progress toward generalist humanoid
    autonomy, however, remains constrained by a data bottleneck: mapping pixels and free-form language to low-level joint
    commands requires paired supervision, and no corpus of such data exists at sufficiently large scale. Some approaches rely
    on human teleoperation and wearable capture ...'
  zh: HALO 是一个由仿真数据驱动的人形机器人自主系统，其训练数据来自在千余个程序化生成的家庭场景中合成的视觉-语言-运动数据，数据规模随算力扩展而非依赖人力采集。该系统习得坐下、导航至指定物体、侧身穿半开门、蹲爬过桌底和推箱子等多项物理技能，并能组合这些技能完成长程复合任务。在训练中从未见过真实家庭环境的情况下，HALO
    零样本迁移到物理世界，在六个未建图的真实环境中完成 360 次试验，成功率达 91%。
  ko: 'Humanoid robots have the potential to automate a wide range of physical tasks. Progress toward generalist humanoid
    autonomy, however, remains constrained by a data bottleneck: mapping pixels and free-form language to low-level joint
    commands requires paired supervision, and no corpus of such data exists at sufficiently large scale. Some approaches rely
    on human teleoperation and wearable capture ...'
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
- humanoid_robotics
- vision_language_action
- sim_to_real_transfer
- synthetic_data
- long_horizon_tasks
- zero_shot_transfer
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-11-09'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-11-09). Bibliographic metadata from arXiv API (2611.06908);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: arXiv:2611.06908 Perceptive Humanoid Motion from Simulation
  url: https://arxiv.org/abs/2611.06908
  date: '2026-11-04'
  accessed_at: '2026-11-09'
- id: src_002
  type: website
  title: Project page
  url: https://apple-aiml-research.github.io/ml-halo/
  accessed_at: '2026-11-09'
---

## 概述

人形机器人有望自动化大量物理任务，但通向通用自主的瓶颈在于数据：把像素与自由语言映射到低层关节指令需要成对的监督数据，而此类数据尚无足够大规模的语料。现有做法依赖人类遥操作与可穿戴捕捉设备，产出与人类投入时间大致一比一，难以扩展。HALO 通过一条在千余个程序化生成家庭中合成视觉-语言-运动数据的流水线来绕开这一瓶颈，使数据规模随算力增长而非随人力增长。系统由此获得包括坐椅、导航到命名物体、侧身穿半开门、蹲伏爬行过桌底与推箱在内的技能库，并能编排这些技能求解长程复合任务。值得注意的是，HALO 训练期间从未接触真实家庭，却能零样本迁移到物理世界，在六个未建图真实环境的 360 次试验中取得 91% 的成功率。

## 核心内容

### 问题背景

人形机器人具备自动化广泛物理任务的潜力，但迈向通用人形自主仍受制于数据瓶颈。将像素与自由形式的语言映射为低层关节指令，需要成对的监督信号，而目前不存在规模足够大的此类数据语料。部分方法借助人类遥操作与可穿戴捕捉设备采集数据，其代价是产出与人类投入时间大致相当——至少需要一小时的人力才能产生一小时的数据，因而难以规模化。

### 方法

作者提出 HALO，一个由数据合成流水线驱动的人形自主系统。该流水线的核心是在一千余个程序化生成的家庭场景中合成视觉-语言-运动数据，使数据语料的规模随算力扩展，而不随人类劳动扩展。

在能力层面，HALO 习得了一组物理技能库，摘要中列举的包括：

- 坐上椅子
- 导航至被命名的物体
- 侧身穿过半开的门
- 蹲伏并爬行通过桌子下方
- 推动箱子

除单一技能外，HALO 还能编排这些技能以求解复合的长程任务。

### 实验设置与关键结果

训练阶段完全不涉及真实家庭环境。评估采用零样本迁移方式，直接部署到物理世界，覆盖六个未建图的真实环境，共进行 360 次试验。

关键结果：在上述 360 次试验中成功率达到 91%。

### 结论

结果表明，完全由程序化仿真合成的视觉-语言-运动数据足以支撑人形机器人在真实环境中执行多样物理技能并完成长程复合任务，且无需任何真实家庭数据即可实现零样本迁移。代码与视频见 https://apple-aiml-research.github.io/ml-halo/ 。

## Overview

Humanoid robots have the potential to automate a wide range of physical tasks. Progress toward generalist humanoid autonomy, however, remains constrained by a data bottleneck: mapping pixels and free-form language to low-level joint commands requires paired supervision, and no corpus of such data exists at sufficiently large scale. Some approaches rely on human teleoperation and wearable capture devices, which require at least an hour of human time to produce an hour of data. We present HALO, a humanoid autonomy system powered by a pipeline that synthesizes vision-language-motion data across a thousand procedurally generated homes. The corpus scales with compute rather than human labor. HALO acquires a repertoire of physical skills, including sitting on chairs, navigating to named objects, stepping sideways through half-open doors, crouching and crawling beneath tables, and pushing boxes. It orchestrates these skills to solve composite, long-horizon tasks. Without ever seeing a real home during training, HALO transfers zero-shot to the physical world, achieving a 91% success rate across 360 trials in six unmapped real-world environments. See https://apple-aiml-research.github.io/ml-halo/ for code and videos.

## 参考
- https://arxiv.org/abs/2611.06908
- https://apple-aiml-research.github.io/ml-halo/
