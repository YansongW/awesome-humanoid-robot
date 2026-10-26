---
$id: ent_paper_liu_humanoid_srl_augmenting_humano_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Humanoid SRL: Augmenting Humanoids with Supernumerary Limbs for Coordinated Loco-Manipulation'
  zh: 'Humanoid SRL: Augmenting Humanoids with Supernumerary Limbs for Coordinated Loco-Manipulation'
  ko: 'Humanoid SRL: Augmenting Humanoids with Supernumerary Limbs for Coordinated Loco-Manipulation'
summary:
  en: Humanoid robots are envisioned to perform diverse human-level tasks through their anthropomorphic morphology. Their
    dual-arm configuration enables a broad range of everyday actions. Yet, as in humans, this morphology can constrain loco-manipulation
    when both arms are occupied or additional contacts are required beyond their reach. Supernumerary robotic limbs (SRLs)
    offer a way to extend these ...
  zh: 该研究将一条额外机械臂（supernumerary arm）集成到人形机器人平台上，探究形态增强如何改变其可行动作空间。作者结合基于模型的轨迹优化（TO）生成动态可行运动，并用于训练目标条件强化学习（RL）控制器，控制器在仿真中训练后零样本迁移到硬件。实验表明，额外肢体使操作与支撑能够超越原生双臂构型的限制协同进行，并借助扩散策略实现了部分任务的视觉引导自主执行。
  ko: Humanoid robots are envisioned to perform diverse human-level tasks through their anthropomorphic morphology. Their
    dual-arm configuration enables a broad range of everyday actions. Yet, as in humans, this morphology can constrain loco-manipulation
    when both arms are occupied or additional contacts are required beyond their reach. Supernumerary robotic limbs (SRLs)
    offer a way to extend these ...
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
- supernumerary_limbs
- humanoid_robots
- loco_manipulation
- reinforcement_learning
- trajectory_optimization
- diffusion_policy
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-10-26'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-10-26). Bibliographic metadata from arXiv API (2610.25628);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2610.25628 Humanoid SRL: Augmenting Humanoids with Supernumerary Limbs for Coordinated Loco-Manipulation'
  url: https://arxiv.org/abs/2610.25628
  date: '2026-10-19'
  accessed_at: '2026-10-26'
---

## 概述

人形机器人的双臂构型虽能覆盖大量日常任务，但当双臂被占用或需要超出臂展的额外接触时，其移动操作能力会受到限制。本文通过在一台人形平台上开发并集成一条额外手臂，研究形态增强对可行动作空间的重塑作用。控制方面，作者利用基于模型的轨迹优化生成动态可行的运动，为目标条件强化学习控制器提供训练支撑；控制器在仿真中训练后以零样本方式迁移到真实硬件，实现接触丰富的三臂移动操作全身协调技能。研究还在部分任务上使用由硬件示教数据训练的扩散策略，实现了视觉引导的自主执行。结论指出，人形机器人的形态不必局限于类人外形，而可被视为可扩展的机器人增强设计空间。

## 核心内容

### 问题背景
人形机器人凭借拟人形态被期望完成多样化的人类级别任务，其双臂配置支持广泛的日常动作。但与人类类似，当双臂均被占用，或需要臂展之外的额外接触点时，这种形态会限制移动操作（loco-manipulation）能力。超数机器人肢体（supernumerary robotic limbs, SRLs）可扩展此类能力，但其集成要求新增肢体与全身运动及平衡相协调。

### 方法
- 在一台人形机器人平台上开发并集成一条超数手臂，用以研究形态增强如何重塑可行动作空间。
- 采用基于模型的轨迹优化（trajectory optimization, TO）为目条件强化学习（RL）控制器生成动态可行的运动。
- RL 控制器在仿真中训练，并以零样本（zero-shot）方式迁移到硬件，从而获得接触丰富的三臂移动操作全身协调技能。
- 在部分选定任务上，使用由硬件示教数据训练的扩散策略（diffusion policies）实现视觉引导的自主执行。

### 实验设置
研究通过定量分析与硬件实验，在两种构型（two configurations）下评估额外肢体的作用。

### 关键结果
- 定量分析与硬件实验表明，额外肢体扩展了全身交互能力，使操作与支撑能够在原生双臂构型的约束之外协同进行。
- 仿真训练的控制器可零样本迁移至硬件，支撑接触丰富的三臂移动操作。
- 扩散策略在选定任务上实现了视觉引导的自主执行。

### 结论
研究结果表明，人形机器人的形态不必局限于类人形式，而可以被重新构想为机器人增强的可扩展设计空间。

## Overview

Humanoid robots are envisioned to perform diverse human-level tasks through their anthropomorphic morphology. Their dual-arm configuration enables a broad range of everyday actions. Yet, as in humans, this morphology can constrain loco-manipulation when both arms are occupied or additional contacts are required beyond their reach. Supernumerary robotic limbs (SRLs) offer a way to extend these capabilities, but their integration requires the added limb to be coordinated with whole-body motion and balance. In this study, we develop and integrate a supernumerary arm into a humanoid platform to investigate how morphological augmentation reshapes its feasible action space. Through quantitative analysis and hardware experiments across two configurations, we show how the additional limb expands whole-body interaction capabilities by enabling manipulation and support to be coordinated beyond the constraints of the native dual-arm configuration. To control this augmented morphology, we leverage model-based trajectory optimization (TO) to generate dynamically feasible motions for goal-conditioned reinforcement learning (RL) controllers. The controllers are trained in simulation and transferred to hardware in a zero-shot manner, enabling coordinated whole-body skills for contact-rich tri-arm loco-manipulation. We further show vision-guided autonomous execution on selected tasks using diffusion policies trained from hardware demonstrations. Our findings suggest that humanoid morphology need not be restricted to human-like forms, but can be reimagined as an extensible design space for robotic augmentation.

## 参考
- https://arxiv.org/abs/2610.25628
