---
$id: ent_paper_minelli_from_tabletop_to_walking_bot_d_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'From Tabletop to Walking Bot: Deploying a VLA Model on a Legged Manipulator Robot'
  zh: 'From Tabletop to Walking Bot: Deploying a VLA Model on a Legged Manipulator Robot'
  ko: 'From Tabletop to Walking Bot: Deploying a VLA Model on a Legged Manipulator Robot'
summary:
  en: Vision-language-action (VLA) models are typically pretrained on broad, diverse datasets and subsequently fine-tuned
    on a comparatively small dataset tailored to a specific target robot. Such adaptation recipe is now widely established,
    achieving its most mature results on fixed-base arms due to their static base dynamics and consistent reference frame.
    Mounting the same arm on a quadruped extends ...
  zh: 本文研究将视觉-语言-动作（VLA）模型从固定基座机械臂迁移到四足移动操作机器人时所面临的实际需求，实验平台为 Unitree Go2 四足机器人搭载 AgileX Piper 机械臂。作者围绕数据采集、模型适配与推理设计，报告了使真机闭环
    loco-manipulation 部署可行的关键选择，包括模型变体、动作时域与示教约定。在 pick-and-place 任务上的研究表明，扩大示教覆盖可使留出的末端执行器误差降低 30%，而引入推而非抓等次级技能可在不损害基线性能的前提下带来新的行为模式。
  ko: Vision-language-action (VLA) models are typically pretrained on broad, diverse datasets and subsequently fine-tuned
    on a comparatively small dataset tailored to a specific target robot. Such adaptation recipe is now widely established,
    achieving its most mature results on fixed-base arms due to their static base dynamics and consistent reference frame.
    Mounting the same arm on a quadruped extends ...
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
- vision_language_action
- loco_manipulation
- legged_manipulator
- quadruped_robot
- imitation_learning
- sim_to_real
- end
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-10-26'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-10-26). Bibliographic metadata from arXiv API (2610.32271);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2610.32271 From Tabletop to Walking Bot: Deploying a VLA Model on a Legged Manipulator Robot'
  url: https://arxiv.org/abs/2610.32271
  date: '2026-10-23'
  accessed_at: '2026-10-26'
---

## 概述

VLA 模型通常先在大规模多样数据上预训练，再针对特定目标机器人用小规模数据微调，这一范式在基座静态、参考系一致的固定基座机械臂上最为成熟。将同一机械臂安装到四足机器人上虽把工作空间扩展到整个地面，却从根本上改变了具身形态：策略不再孤立控制机械臂，而须联合协调基座导航、身体姿态与末端执行器运动。本文以 Unitree Go2 与 AgileX Piper 机械臂为平台，系统考察这一具身变化在数据采集、模型适配与推理设计三方面的实际要求，以实现闭环 loco-manipulation。作者报告了使真机部署可行的具体选择——模型变体、动作时域与示教约定，并针对 pick-and-place 任务开展研究，将数据覆盖与模型容量两个因素分开考察。结果显示扩大示教覆盖使留出的末端执行器误差降低 30%，加入推等次级技能可引入新行为模式而不降低基线性能；闭环真机实验进一步表明数据集构成会塑造成功与失败的模式。

## 核心内容

### 问题背景

VLA 模型的一般做法是先在大规模、多样化的数据集上预训练，再在针对特定目标机器人构建的较小数据集上微调。这一适配流程已被广泛采用，并在固定基座机械臂上取得最成熟的结果，原因在于其基座动力学静态、参考系一致。把同一机械臂装到四足机器人上，工作空间从桌面扩展到整个地面，但具身形态发生根本变化：策略不能只控制机械臂本身，而必须同时协调基座导航、身体姿态与末端执行器运动。本文关注这一具身变化在数据采集、模型适配与推理设计上的实际需求。

### 方法

- 平台：Unitree Go2 四足机器人搭载 AgileX Piper 机械臂。
- 目标：实现闭环 loco-manipulation。
- 作者报告了使真机部署可行的关键设计选择，包括模型变体、动作时域（action horizon）与示教约定（demonstration conventions）。
- 针对 pick-and-place 任务开展专门研究，将数据覆盖（data coverage）与模型容量（model capacity）两个因素分开考察。

### 关键结果

- 扩大示教覆盖使留出的末端执行器误差降低 30%。
- 引入次级技能（例如用推代替抓取）可带来新的行为模式，且不降低基线性能。
- 闭环真机实验显示，数据集构成会影响成功与失败的模式，从而验证了该流程可支撑更复杂的 loco-manipulation。

### 结论

在四足移动操作平台上部署 VLA 模型，需要在数据采集、模型适配与推理设计上做出一系列具体取舍；数据覆盖的扩大与次级技能的加入是提升性能与拓展行为模式的有效手段，数据集构成对真机闭环任务的成功与否具有决定性影响。

## Overview

Vision-language-action (VLA) models are typically pretrained on broad, diverse datasets and subsequently fine-tuned on a comparatively small dataset tailored to a specific target robot. Such adaptation recipe is now widely established, achieving its most mature results on fixed-base arms due to their static base dynamics and consistent reference frame. Mounting the same arm on a quadruped extends the workspace to the entire floor, but fundamentally changes the embodiment: rather than controlling the arm in isolation, the policy must jointly coordinate base navigation, body posture, and end-effector motion. In this work, we study the practical demands of this embodiment change across data collection, model adaptation, and inference design to achieve closed-loop loco-manipulation on a Unitree Go2 with an AgileX Piper arm. We report the choices that made this real-robot deployment feasible, namely model variant, action horizon, and demonstration conventions, together with a study tailored to a pick-and-place task, separating data coverage from model capacity. We show that expanding demonstration coverage reduces held-out end-effector error by 30%, and incorporating secondary skills (such as pushing rather than grasping) introduces new behavioral modes without degrading baseline performance. Finally, closed-loop real-world experiments show how dataset composition shapes success and failure, validating the pipeline for more complex loco-manipulation.

## 参考
- https://arxiv.org/abs/2610.32271
