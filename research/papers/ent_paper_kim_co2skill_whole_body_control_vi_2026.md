---
$id: ent_paper_kim_co2skill_whole_body_control_vi_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Co${}^{2}$Skill: Whole-Body Control via Skill Composition for Long-Horizon Human-Environment Interaction'
  zh: 'Co${}^{2}$Skill: Whole-Body Control via Skill Composition for Long-Horizon Human-Environment Interaction'
  ko: 'Co${}^{2}$Skill: Whole-Body Control via Skill Composition for Long-Horizon Human-Environment Interaction'
summary:
  en: Achieving human-level dexterity in complex, unstructured environments requires the seamless integration of whole-body
    scene interaction and dexterous object manipulation skills. While existing physics-based controllers generate physically
    plausible behaviors in each domain, they largely address these two capabilities independently. In this paper, we present
    Co${}^{2}$Skill that integrates scene ...
  zh: Co${}^{2}$Skill 是 Jeonghwan Kim、Hyeonwoo Kim 与 Hanbyul Joo 提出的一种统一策略框架，通过技能组合将全身场景交互与灵巧物体操作整合到同一控制公式中。该方法基于预训练运动先验，利用任务与阶段相关的观测掩码筛选当前目标所需信息，并借助目标条件化的移动-操作课程与跨任务课程实现长时程顺序执行。作者在坐、站、攀爬、上下楼梯及目标导向操作等任务上进行了评估，并展示了室内环境中的技能组合。
  ko: Achieving human-level dexterity in complex, unstructured environments requires the seamless integration of whole-body
    scene interaction and dexterous object manipulation skills. While existing physics-based controllers generate physically
    plausible behaviors in each domain, they largely address these two capabilities independently. In this paper, we present
    Co${}^{2}$Skill that integrates scene ...
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
- whole_body_control
- skill_composition
- loco_manipulation
- motion_prior
- human_environment_interaction
- curriculum_learning
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-10-12'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-10-12). Bibliographic metadata from arXiv API (2610.09291);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2610.09291 Co${}^{2}$Skill: Whole-Body Control via Skill Composition for Long-Horizon Human-Environment Interaction'
  url: https://arxiv.org/abs/2610.09291
  date: '2026-10-07'
  accessed_at: '2026-10-12'
---

## 概述

该工作针对复杂非结构化环境中全身场景交互与灵巧物体操作长期被分开处理的问题，提出统一策略 Co${}^{2}$Skill。策略建立在预训练运动先验之上，通过任务与阶段相关的观测掩码，让控制器只关注与当前交互目标相关的信息。为兼顾精度与探索，作者设计了目标条件化的移动-操作课程，在部分参考引导之外允许从多样初始状态出发、并执行超出示范轨迹的目标导向行为。此外，跨任务课程将单项技能与选定任务序列联合训练，在任务边界处保持物理状态、并在后续场景交互中维持抓取。由此，系统支持顺序任务执行以及场景交互与物体操作的同时进行。

## 核心内容

### 问题背景
在复杂、非结构化的环境中达到人类水平的灵巧性，需要全身场景交互与灵巧物体操作两类能力的无缝结合。现有基于物理的控制器虽能在各自领域生成物理上合理的行为，但大多将这两种能力分开处理，缺乏统一框架。

### 方法
- **统一策略公式**：Co${}^{2}$Skill 通过统一的策略公式整合场景交互与灵巧操作。
- **预训练运动先验**：策略构建在预训练运动先验之上。
- **观测掩码**：采用任务与阶段相关的观测掩码，选择与当前交互目标相关的信息。
- **目标条件化移动-操作课程**：结合部分参考引导以保证精度，同时从多样初始状态进行探索，并允许执行超出示范轨迹的目标导向行为。
- **跨任务课程**：联合训练单项技能与选定任务序列，在任务边界处保持物理状态，并在后续场景交互中维持抓取。

### 实验设置与评估任务
评估任务包括坐、站、攀爬、上下楼梯以及目标导向操作，并涵盖顺序执行与随机不同条件的测试。此外，作者在室内环境中展示了技能组合，说明这些技能可在同一控制公式内集成。

### 结论
上述两类课程共同支持顺序任务执行，以及场景交互与物体操作的同时进行，表明场景交互与灵巧操作可以在统一策略框架下协同完成。

## Overview

Achieving human-level dexterity in complex, unstructured environments requires the seamless integration of whole-body scene interaction and dexterous object manipulation skills. While existing physics-based controllers generate physically plausible behaviors in each domain, they largely address these two capabilities independently. In this paper, we present Co${}^{2}$Skill that integrates scene interaction and dexterous manipulation through a unified policy formulation. Built on a pretrained motion prior, the policy uses task and phase dependent observation masks to select information relevant to the current interaction goals. We introduce a goal-conditioned loco-manipulation curriculum that combines partial reference guidance for precision with exploration from varied initial states while allowing goal-directed execution beyond the demonstrated trajectories. We further introduce a cross-task curriculum that jointly trains individual skills and selected task sequences, preserving physical states across task boundaries and maintaining grasps during subsequent scene interactions. Together, these support sequential task execution and simultaneous scene interaction with object manipulation. We evaluate sitting, standing, climbing, stair traversal, and goal-directed manipulation, together with sequential execution and with random different conditions. Additionally, we demonstrate skill compositions in indoor environments, illustrating their integration within the same control formulation.

## 参考
- https://arxiv.org/abs/2610.09291
