---
$id: ent_paper_meng_developing_combined_manipulati_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Developing Combined Manipulation and Locomotion Skills with Interaction Representation and Skill Composition
  zh: Developing Combined Manipulation and Locomotion Skills with Interaction Representation and Skill Composition
  ko: Developing Combined Manipulation and Locomotion Skills with Interaction Representation and Skill Composition
summary:
  en: This paper addresses how to enable a humanoid robot to learn motion policies based on developmental principles and combine
    policies to create more sophisticated and useful behaviors. Specifically, we present an approach to (1) learning a whole-body
    reaching and grasping policy and (2) combining it and a standing-up and walking policy to compose a more complex policy
    of manipulation and ...
  zh: 本文提出一种基于发展原理的人形机器人技能学习方法，通过谐波分析表示手-物空间关系，并结合抓取与站立行走策略实现复杂操作与移动技能。实验显示对未见物体的零样本抓取成功率达93%，持物站立成功率为96-100%。
  ko: This paper addresses how to enable a humanoid robot to learn motion policies based on developmental principles and combine
    policies to create more sophisticated and useful behaviors. Specifically, we present an approach to (1) learning a whole-body
    reaching and grasping policy and (2) combining it and a standing-up and walking policy to compose a more complex policy
    of manipulation and ...
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
- humanoid_manipulation
- locomotion_skill
- skill_composition
- developmental_robotics
- grasping_policy
- whole_body_control
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-08-04'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-08-04). Bibliographic metadata from arXiv API (2608.00208);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: arXiv:2608.00208 Developing Combined Manipulation and Locomotion Skills with Interaction Representation and Skill
    Composition
  url: https://arxiv.org/abs/2608.00208
  date: '2026-07-31'
  accessed_at: '2026-08-04'
- id: src_002
  type: website
  title: Project page
  url: https://youtu.be/x-7x89fSJWY
  accessed_at: '2026-08-04'
---

## 概述

本文由Fanxing Meng和Jing Xiao撰写，针对人形机器人如何基于发展原理学习运动策略并组合成更复杂行为的问题。方法分为两部分：一是利用三次谐波作为权重，通过空间卷积表示手-物关系，并采用基于发展原理的指关节解耦课程，使机器人自主学习泛化抓取策略；二是将抓取策略与独立学习的站立行走策略组合，通过各自观测向量和手-物交互分数决定策略控制权。实验验证了组合策略的有效性，并强调策略学习需在同一全身模型上进行。

## 核心内容

### 问题背景
人形机器人需要具备操作与移动的复合技能，但现有方法常依赖外部数据集或预训练模型，且难以将独立学习的策略有效组合。本文探索基于发展原理的自主学习路径，使机器人从零开始学习抓取，并组合站立行走策略形成更复杂行为。

### 方法
#### 抓取策略学习
- 借鉴谐波分析，采用三次谐波作为权重，通过空间卷积表示手-物空间关系，无需显式特征工程。
- 引入基于发展原理的指关节解耦课程（intra-episode finger joint decoupling curriculum），在单个回合内逐步解耦手指关节控制，使机器人自主探索抓取，不依赖外部数据或预训练模型。

#### 策略组合
- 将抓取策略与独立学习的站立行走策略组合，两者各自接收观测向量。
- 使用手-物交互分数（hand-object interaction scores）动态决定何时由哪个策略控制哪些机器人关节，实现平滑切换。

### 实验设置与结果
- 在仿真环境中训练，测试未见物体的零样本抓取，成功率达93%。
- 持物站立（standing up while holding the object）成功率为96-100%。
- 关键发现：组合策略仅在两个策略均在同一全身人形模型上学习时有效，即使移动策略看似不需要手指等身体部位，也必须保持全身一致性。

### 结论
本文展示了基于发展原理的自主技能学习与组合方法，验证了全身模型在策略组合中的必要性，为复杂人形行为学习提供了新思路。

## Overview

This paper addresses how to enable a humanoid robot to learn motion policies based on developmental principles and combine policies to create more sophisticated and useful behaviors. Specifically, we present an approach to (1) learning a whole-body reaching and grasping policy and (2) combining it and a standing-up and walking policy to compose a more complex policy of manipulation and locomotion: grasping, standing up, and walking. In (1), our method draws inspiration from harmonic analysis and adopts cubic harmonics as weights to represent the hand-object spatial relationship via spatial convolution. Utilizing an intra-episode finger joint decoupling curriculum based on developmental principles, a robot can autonomously learn a generalizable grasping policy without relying on external datasets or pretrained models. In (2), our method combines the grasping policy with a separately learned getting-up policy by providing both policies with their respective observation vectors and using hand-object interaction scores to determine when each policy should control which robot joints. Our results show a 93% zero-shot success rate for grasping unseen objects and a 96-100% success rate for standing up while holding the object. Our work also demonstrates that combining different policies is only effective if each policy learning happens on the same whole humanoid body even if a policy (such as for locomotion) does not seem to need all the body parts (such as fingers).

## 参考
- https://arxiv.org/abs/2608.00208
- https://youtu.be/x-7x89fSJWY
