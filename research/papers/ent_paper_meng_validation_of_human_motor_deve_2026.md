---
$id: ent_paper_meng_validation_of_human_motor_deve_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Validation of Human Motor Development Scales with Humanoid Robots
  zh: Validation of Human Motor Development Scales with Humanoid Robots
  ko: Validation of Human Motor Development Scales with Humanoid Robots
summary:
  en: We investigate how humanoid robots can learn a series of motor skills defined by human infant motor development scales,
    and we evaluate which scales are comprehensive enough to serve as self-contained guides for developing gross motor skills
    up to standing and walking. We represent each motor development scale as a developmental graph that guides the training
    of a humanoid robot. We then apply ...
  zh: 本研究探讨人形机器人能否依据人类婴儿运动发育量表学习一系列运动技能，并评估哪些量表足以作为发展至站立与行走的完整指南。作者将每个运动发育量表表示为引导人形机器人训练的发展图，并在强化学习框架中应用该图，使机器人按量表描述的人类运动发育自然阶段学习技能。结果表明，四种常用儿科运动量表中的三种所导出的图能成功引导人形机器人习得这些技能；第四种量表因缺少其他量表具有的某些中间里程碑而导致部分失败，在图中补入缺失里程碑后也能成功。
  ko: We investigate how humanoid robots can learn a series of motor skills defined by human infant motor development scales,
    and we evaluate which scales are comprehensive enough to serve as self-contained guides for developing gross motor skills
    up to standing and walking. We represent each motor development scale as a developmental graph that guides the training
    of a humanoid robot. We then apply ...
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
- motor_skill_learning
- reinforcement_learning
- developmental_scales
- developmental_graph
- milestone_learning
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-10-26'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-10-26). Bibliographic metadata from arXiv API (2610.25701);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: arXiv:2610.25701 Validation of Human Motor Development Scales with Humanoid Robots
  url: https://arxiv.org/abs/2610.25701
  date: '2026-10-19'
  accessed_at: '2026-10-26'
- id: src_002
  type: website
  title: Project page
  url: https://youtu.be/SR3LUVhohV4
  accessed_at: '2026-10-26'
---

## 概述

该工作关注人形机器人运动技能学习与人类婴儿运动发育量表之间的对应关系，核心问题是哪些量表足够完整，可作为发展粗大运动技能直至站立和行走的自足指南。作者把每个运动发育量表形式化为一张发展图，用其组织人形机器人的训练过程，并将该图嵌入强化学习框架，使机器人依照量表所描述的人类运动发育阶段逐步习得技能。实验对四种常用儿科运动量表进行了验证，其中三种量表导出的发展图能够成功引导机器人发展出相应技能。第四种量表由于缺少其他量表所包含的某些中间里程碑，导致部分学习失败；在为其发展图补充缺失的里程碑后，机器人同样能够成功习得这些技能。这一结果说明量表的结构完整性对机器人运动技能发展具有直接影响。

## 核心内容

### 问题背景
人形机器人需要习得从站立到行走等一系列粗大运动技能。人类婴儿运动发育量表描述了运动技能出现的自然阶段，但尚不清楚这些量表是否足够完整，能够作为机器人技能发展的自足指南。作者据此提出：将运动发育量表转化为可指导训练的结构，并检验不同量表引导人形机器人学习的效果。

### 方法
- 将每个运动发育量表表示为一个**发展图**（developmental graph），用以指导人形机器人的训练。
- 把该发展图应用于**强化学习**框架中，使机器人按照量表所描述的人类运动发育自然阶段依次学习技能。

### 实验设置
研究对四种常用儿科运动量表进行了验证，比较由各量表导出的发展图在引导人形机器人发展运动技能时的表现。

### 关键结果
- 四种量表中有三种所导出的图能够成功引导人形机器人发展出这些技能。
- 第四种量表缺少其他量表具有的某些中间里程碑，因而导致部分失败。
- 在该量表的发展图中补入缺失的里程碑后，机器人同样能够成功发展这些技能。

### 结论
运动发育量表可作为人形机器人粗大运动技能训练的指导结构；量表是否包含完整的中间里程碑，直接影响技能学习的成败，补充缺失里程碑可恢复其引导能力。

## Overview

We investigate how humanoid robots can learn a series of motor skills defined by human infant motor development scales, and we evaluate which scales are comprehensive enough to serve as self-contained guides for developing gross motor skills up to standing and walking. We represent each motor development scale as a developmental graph that guides the training of a humanoid robot. We then apply this graph within a reinforcement learning framework so that the robot learns skills following the natural phases of human motor development described by the scale. Our work demonstrates that graphs derived from three out of four popular pediatric motor scales can successfully guide humanoid robots to develop these skills. The fourth scale misses some intermediate milestones that the other scales have, which causes some failures. After adding a missing milestone in its graph, it also enables the robot to develop those skills successfully.

## 参考
- https://arxiv.org/abs/2610.25701
- https://youtu.be/SR3LUVhohV4
