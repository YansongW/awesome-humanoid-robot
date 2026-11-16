---
$id: ent_paper_gade_reading_the_table_sim_to_real_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Reading the Table: Sim-to-Real Game State Detection for the Chef''s Hat Card Game'
  zh: 'Reading the Table: Sim-to-Real Game State Detection for the Chef''s Hat Card Game'
  ko: 'Reading the Table: Sim-to-Real Game State Detection for the Chef''s Hat Card Game'
summary:
  en: Tabletop games offer a compelling scenario to study the interaction between artificial and human agents, combining social
    interaction with game state tracking and physical manipulation. To assess the game state, a robot needs to precisely detect
    closely related game objects, such as different card designs, requiring dedicated training data that is costly to annotate
    in the real world. Instead, we ...
  zh: 该论文面向人形机器人自主进行 Chef's Hat 卡牌游戏的需求，提出一套全自动合成数据采集流程，通过已知 3D 坐标重投影自动生成标注，并结合域随机化缩小仿真与现实的差距。作者采集了 25413 个样本用于微调目标检测与分割模型，并将二者结合把检测到的卡牌分配到游戏相关区域以推断游戏状态。在真实
    NICO 人形机器人上评估时，卡牌到区域分配的 F1-score 达到 0.906。
  ko: Tabletop games offer a compelling scenario to study the interaction between artificial and human agents, combining social
    interaction with game state tracking and physical manipulation. To assess the game state, a robot needs to precisely detect
    closely related game objects, such as different card designs, requiring dedicated training data that is costly to annotate
    in the real world. Instead, we ...
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
- sim_to_real
- synthetic_data
- object_detection
- humanoid_robot
- game_state_detection
- domain_randomization
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-11-16'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-11-16). Bibliographic metadata from arXiv API (2611.15524);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2611.15524 Reading the Table: Sim-to-Real Game State Detection for the Chef''s Hat Card Game'
  url: https://arxiv.org/abs/2611.15524
  date: '2026-11-11'
  accessed_at: '2026-11-16'
- id: src_002
  type: website
  title: Project page
  url: https://dnd-sidc.github.io/
  accessed_at: '2026-11-16'
---

## 概述

桌游场景同时涉及社交互动、游戏状态跟踪与物理操作，是研究人机交互的理想载体，但机器人要判断游戏状态，必须精确识别外观相近的卡牌等对象，而真实世界标注训练数据成本高昂。为此，作者构建了一条全自动的合成数据采集流水线，利用已知 3D 坐标的重投影自动生成标签，并借助域随机化弥合仿真与现实的差距。基于该流程采集的 25413 个样本被用于微调目标检测模型与分割模型，两者组合后将检测到的卡牌归属到游戏相关区域，从而推断游戏状态。在真实 NICO 人形机器人上的评估显示，卡牌到区域分配的 F1-score 为 0.906，为机器人自主与人类玩家对弈 Chef's Hat 提供了感知基础。

## 核心内容

### 问题背景
桌游为人机交互研究提供了兼具社交性与物理操作的综合场景。机器人要参与游戏，首先需要准确判断游戏状态，而这依赖于对高度相似的游戏对象（例如不同设计的卡牌）进行精确检测。直接在真实世界采集并标注此类数据成本很高，因此作者转向合成数据方案。

### 方法
- **自动化数据流水线**：构建全自动合成数据采集流程，利用已知 3D 坐标的重投影自动生成标注，避免人工标注。
- **域随机化**：通过域随机化缩小仿真数据与真实场景之间的差距。
- **模型组合**：用采集数据微调一个目标检测模型和一个分割模型，并将两者结合，把检测到的卡牌分配到游戏相关区域，进而推断游戏状态。

### 实验设置
- 数据集规模为 25413 个样本，全部由上述自动化流程生成。
- 评估在真实的 NICO 人形机器人上进行。

### 关键结果
- 卡牌到区域分配任务取得 F1-score 0.906。

### 结论
该流水线为机器人提供了可靠的感知基础，使其能够自主与人类玩家进行 Chef's Hat 对弈。

## Overview

Tabletop games offer a compelling scenario to study the interaction between artificial and human agents, combining social interaction with game state tracking and physical manipulation. To assess the game state, a robot needs to precisely detect closely related game objects, such as different card designs, requiring dedicated training data that is costly to annotate in the real world. Instead, we develop a fully automated synthetic data collection pipeline, using re-projection of known 3D coordinates to generate labels automatically and domain randomization to bridge the reality gap. This approach is used to collect a dataset of 25413 samples to finetune an object detection and a segmentation model, which are combined to assign detected cards to game-relevant zones and infer the game state. When evaluated on a real NICO humanoid robot, our pipeline achieves an F1-score of 0.906 for card-to-zone assignment, thus providing the perceptual foundation for a robot that can autonomously play Chef's Hat against human players.

## 参考
- https://arxiv.org/abs/2611.15524
- https://dnd-sidc.github.io/
