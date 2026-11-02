---
$id: ent_paper_jetti_llm_guided_planar_loco_manipul_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: LLM-guided Planar Loco-Manipulation for Quadruped Robots
  zh: LLM-guided Planar Loco-Manipulation for Quadruped Robots
  ko: LLM-guided Planar Loco-Manipulation for Quadruped Robots
summary:
  en: Robotic navigation typically assumes a collision-free route to the goal exists; in cluttered environments with movable
    obstacles, however, reaching the goal may require physical interaction. Classical solutions encode these behaviors through
    geometric rules and task-specific logic, while learning-based approaches often constrain the decision space to low-dimensional
    motion commands or predefined ...
  zh: 该工作提出一种面向四足机器人的语言引导平面移动-操作（loco-manipulation）框架，由 Georges Jetti 等人完成。其任务规划器基于 LoRA 在合成数据上微调，将自然语言任务与结构化场景表示映射为变长的参数化动作序列，并由低层强化学习策略执行。低层端到端全身平面推动策略在仿真中达到
    93.3% 成功率，优于分层基线的 83.5%，并将完成时间缩短 60% 以上。
  ko: Robotic navigation typically assumes a collision-free route to the goal exists; in cluttered environments with movable
    obstacles, however, reaching the goal may require physical interaction. Classical solutions encode these behaviors through
    geometric rules and task-specific logic, while learning-based approaches often constrain the decision space to low-dimensional
    motion commands or predefined ...
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
- loco_manipulation
- quadruped_robots
- language_conditioned_planning
- whole_body_control
- reinforcement_learning
- lora_fine_tuning
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-11-02'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-11-02). Bibliographic metadata from arXiv API (2610.40248);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: arXiv:2610.40248 LLM-guided Planar Loco-Manipulation for Quadruped Robots
  url: https://arxiv.org/abs/2610.40248
  date: '2026-10-29'
  accessed_at: '2026-11-02'
---

## 概述

在存在可移动障碍物的杂乱环境中，机器人到达目标往往需要与物体发生物理交互，而经典方法依赖几何规则与任务专用逻辑，学习类方法则常把决策空间压缩为低维运动指令或预定义动作集。该研究转而采用更宽的决策空间，联合选择技能、相关物体与几何目标。作者构建了一个语言条件任务规划器，通过 LoRA 在合成数据上微调，把自然语言任务和结构化场景表示转换为变长的参数化动作序列，交由低层强化学习策略执行。规划器学习到交互式导航背后的几何关系，在交互式导航任务上优于经典规划器与经提示的前沿模型。与从零训练的模型对比表明，当表示是结构化的时，组合能力并不依赖预训练，但预训练能带来更可靠的几何目标。低层方面，作者提出端到端全身平面推动策略，仿真成功率达 93.3%，高于分层基线的 83.5%，完成时间缩短逾 60%；在硬件上，该分层系统在 45 次试验中有 44 次给出正确的技能组合，端到端成功 34 次。

## 核心内容

### 问题背景

机器人导航通常假设通往目标的路径是无碰撞的；但在含有可移动障碍物的杂乱环境中，到达目标可能需要通过物理交互来推开或移动物体。经典方案用几何规则和任务专用逻辑来编码这类行为，而基于学习的方法往往把决策空间限制在低维运动指令或预定义动作集合内。本文主张采用更宽的决策空间，同时决定使用哪种技能、作用于哪个物体以及几何目标是什么。

### 方法

- **高层任务规划器**：语言条件规划器，使用 LoRA 在合成数据上微调，输入为自然语言任务与结构化场景表示，输出为变长的参数化动作序列。
- **低层执行**：由低层强化学习策略执行规划器给出的参数化动作。
- **低层新策略**：提出端到端的全身平面推动（whole-body planar pushing）策略。

### 实验设置与关键结果

- 规划器学习到交互式导航背后的几何关系，在交互式导航任务上优于经典规划器以及经提示的前沿模型。
- 与从零训练的模型对比显示：当表示是结构化的时，组合能力不需要预训练；而预训练能产生更可靠的几何目标。
- 仿真中，端到端全身平面推动策略成功率为 93.3%，分层基线为 83.5%，同时完成时间缩短 60% 以上。
- 硬件实验中，该分层系统在 45 次试验中有 44 次给出正确的技能组合，端到端成功为 34/45。

### 结论

联合选择技能、物体与几何目标的宽决策空间配合结构化场景表示，可有效支撑四足机器人在杂乱环境中的交互式导航；低层端到端全身平面推动策略在成功率与效率上均优于分层基线，并在真实硬件上验证了技能组合的可靠性。

## Overview

Robotic navigation typically assumes a collision-free route to the goal exists; in cluttered environments with movable obstacles, however, reaching the goal may require physical interaction. Classical solutions encode these behaviors through geometric rules and task-specific logic, while learning-based approaches often constrain the decision space to low-dimensional motion commands or predefined action sets. We instead consider a broader decision space, jointly selecting the skill, relevant object, and geometric target. Our language-conditioned task planner, fine-tuned with LoRA on synthetic data, maps natural-language tasks and a structured scene representation to variable-length sequences of parameterized actions, executed by low-level reinforcement-learning policies. The planner learns the geometric relations underlying interactive navigation and outperforms a classical planner and a prompted frontier model on interactive navigation tasks. Comparisons with models trained from scratch indicate that composition does not require pretraining when the representation is structured, whereas pretraining yields more reliable geometric targets. At the low level, we introduce an end-to-end whole-body planar pushing policy that achieves a 93.3% success rate in simulation, versus 83.5% for a hierarchical baseline, while reducing completion time by more than 60%. On hardware, the hierarchy yields the correct skill composition in 44/45 trials and end-to-end success in 34/45. Project website: https://anonymousprojects-dev.github.io/LLM-guided-LocoManipulation-Quadrupeds/

## 参考
- https://arxiv.org/abs/2610.40248
