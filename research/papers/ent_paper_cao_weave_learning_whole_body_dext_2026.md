---
$id: ent_paper_cao_weave_learning_whole_body_dext_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Weave: Learning Whole-Body Dexterous Loco-Manipulation from Human-Object Interactions'
  zh: 'Weave: Learning Whole-Body Dexterous Loco-Manipulation from Human-Object Interactions'
  ko: 'Weave: Learning Whole-Body Dexterous Loco-Manipulation from Human-Object Interactions'
summary:
  en: Learning humanoid-object interaction requires coordinating whole-body balance, locomotion, and dexterous hand contact
    to control both robot and object motion. Human demonstrations provide examples of coordinated interaction, but transferring
    these behaviors to humanoid robots requires learning how to establish and maintain effective contacts under different
    embodiments and dynamics. We present ...
  zh: Weave 是一个从真人演示中学习人形机器人全身灵巧物体交互的统一框架，由 Liu Cao、Xingze Wu、Jingzhi Cui、Botian Xu、Mingzhi Pei、Ruoqu Chen、Mengdi Xu 提出。它通过接触感知重定向与接近运动补全，将真人-物体交互数据转换为机器人可执行的参考轨迹，并用接触与几何感知策略同时控制
    29 个身体关节和 12 个主动手指关节。在九个物体上的评测中，已训练交互成功率达 92.5%，未训练序列在零额外训练下达到 65.0%。
  ko: Learning humanoid-object interaction requires coordinating whole-body balance, locomotion, and dexterous hand contact
    to control both robot and object motion. Human demonstrations provide examples of coordinated interaction, but transferring
    these behaviors to humanoid robots requires learning how to establish and maintain effective contacts under different
    embodiments and dynamics. We present ...
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
- whole_body_control
- dexterous_manipulation
- human_object_interaction
- contact_aware_retargeting
- robot_learning
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-09-21'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-09-21). Bibliographic metadata from arXiv API (2609.16683);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2609.16683 Weave: Learning Whole-Body Dexterous Loco-Manipulation from Human-Object Interactions'
  url: https://arxiv.org/abs/2609.16683
  date: '2026-09-15'
  accessed_at: '2026-09-21'
- id: src_002
  type: website
  title: Project page
  url: https://xiaohu-art.github.io/Weave/
  accessed_at: '2026-09-21'
---

## 概述

人形机器人要完成与物体的交互，需要同时协调全身平衡、行走与灵巧手接触，从而控制机器人和物体两者的运动。真人演示虽然提供了协调交互的样例，但由于本体结构与动力学的差异，如何建立并维持有效接触仍是迁移的难点。为此，作者提出 Weave，一个从采集到的真人演示中学习全身灵巧人形-物体交互的统一框架。该框架先通过接触感知重定向与接近运动补全，把真人-物体交互转换为机器人可执行的机器人-物体参考；其核心是一个接触与几何感知策略，可跨多种物体与交互序列联合控制 29 个身体关节和 12 个主动手指关节。在九个物体上的评测显示，已训练交互成功率为 92.5%，而在训练中从未见过的序列上，无需任何额外训练即可达到 65.0%。作者还发布了约 9,000 条实际执行的 rollout，总时长约 23 小时，包含带接触标注的机器人-物体轨迹。

## 核心内容

### 问题背景
人形机器人与物体交互时，必须同时协调全身平衡、行走以及灵巧手的接触，才能控制机器人与物体双方的运动。真人演示提供了协调交互的样例，但要把这些行为迁移到人形机器人上，需要解决不同本体结构与动力学条件下如何建立并维持有效接触的问题。

### 方法
作者提出 Weave，一个从采集到的真人演示中学习全身灵巧人形-物体交互的统一框架，主要包含两个环节：
- **数据转换**：通过接触感知重定向（contact-aware retargeting）与接近运动补全（approach-motion completion），将采集到的真人-物体交互转换为机器人可执行的机器人-物体参考。
- **策略学习**：核心是一个接触与几何感知（contact- and geometry-aware）策略，能够跨多种物体与交互序列，联合控制 29 个身体关节和 12 个主动手指关节。

### 实验设置与关键结果
- 评测覆盖九个物体。
- 在已训练的交互上成功率为 92.5%。
- 在训练中从未见过的序列上，不进行任何额外训练即可达到 65.0% 的成功率。

### 数据发布
作者额外发布了约 9,000 条实际执行的 rollout，总时长约 23 小时，提供带接触标注的机器人-物体轨迹，可用于下游交互策略学习以及物理一致的 HOI 运动生成。

### 结论
Weave 通过接触感知的数据转换与接触/几何感知的全身控制策略，实现了从真人演示到人形机器人全身灵巧物体交互的学习，并在已训练与未训练交互序列上分别取得 92.5% 与 65.0% 的成功率，同时公开了大规模带接触标注的执行轨迹数据。项目网站：https://xiaohu-art.github.io/Weave/

## Overview

Learning humanoid-object interaction requires coordinating whole-body balance, locomotion, and dexterous hand contact to control both robot and object motion. Human demonstrations provide examples of coordinated interaction, but transferring these behaviors to humanoid robots requires learning how to establish and maintain effective contacts under different embodiments and dynamics. We present Weave, a unified framework for learning whole-body dexterous humanoid-object interaction from captured human demonstrations. Weave first converts captured human-object interactions into executable robot-object references through contact-aware retargeting and approach-motion completion. At its core is a contact- and geometry-aware policy that jointly commands 29 body joints and 12 actuated finger joints across multiple objects and interaction sequences. Evaluation across nine objects yields a 92.5% success rate on trained interactions and, without any additional training, 65.0% on sequences never seen during training. We additionally release ~9,000 physically executed rollouts spanning ~23 hours, providing robot-object trajectories with contact annotations for downstream interaction-policy learning and physically consistent HOI motion generation. Project website: https://xiaohu-art.github.io/Weave/

## 参考
- https://arxiv.org/abs/2609.16683
- https://xiaohu-art.github.io/Weave/
