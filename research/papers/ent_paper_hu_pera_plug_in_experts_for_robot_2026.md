---
$id: ent_paper_hu_pera_plug_in_experts_for_robot_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'PERA: Plug-in Experts for Robotic Actions in Continual Whole-Body Control'
  zh: 'PERA: Plug-in Experts for Robotic Actions in Continual Whole-Body Control'
  ko: 'PERA: Plug-in Experts for Robotic Actions in Continual Whole-Body Control'
summary:
  en: Motion imitation enables humanoid robots to acquire whole-body skills such as walking and dancing. However, fine-tuning
    an entire policy for a new skill can affect existing behaviors, while training a separate policy for each skill increases
    training and maintenance costs. We present PERA, a method for learning new skills by reusing existing motion capabilities.
    PERA freezes a pretrained ...
  zh: PERA 是一种面向人形机器人全身控制的持续学习新方法，由 Shangchao Hu、Yadan Sun、Xibo Yu、Wei Huang 提出。该方法冻结预训练的混合专家策略，仅新增一个任务专家及其路由分数，从而在复用已有运动能力的基础上学习新技能。在
    Unitree G1 仿真中，每个新增任务模块的参数量约为基础 actor 的 1.03%，成功完成全部十项新任务，且禁用该专家后基础策略仍能完整执行原有的 126 个动作。
  ko: Motion imitation enables humanoid robots to acquire whole-body skills such as walking and dancing. However, fine-tuning
    an entire policy for a new skill can affect existing behaviors, while training a separate policy for each skill increases
    training and maintenance costs. We present PERA, a method for learning new skills by reusing existing motion capabilities.
    PERA freezes a pretrained ...
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
- humanoid_robot
- whole_body_control
- continual_learning
- mixture_of_experts
- motion_imitation
- unitree_g1
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-11-16'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-11-16). Bibliographic metadata from arXiv API (2611.16188);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2611.16188 PERA: Plug-in Experts for Robotic Actions in Continual Whole-Body Control'
  url: https://arxiv.org/abs/2611.16188
  date: '2026-11-12'
  accessed_at: '2026-11-16'
---

## 概述

PERA 针对人形机器人运动模仿中的持续学习难题：若对整个策略进行微调，容易破坏已有行为；若为每个新技能单独训练策略，又会推高训练与维护成本。为此，作者提出复用已有运动能力来学习新技能，具体做法是冻结预训练的混合专家策略，并利用任务奖励或教师动作监督，额外训练一个任务专家及其路由分数。在 Unitree G1 仿真环境中，每个新增任务模块的参数量约为基础 actor 的 1.03%，基于预训练策略成功完成全部十项新任务。禁用该专家后，基础策略恢复原有计算路径，仍能完整执行全部 126 个原始动作；启用该专家还能改善部分未参与该专家训练的舞蹈动作，说明其收益超出训练动作本身。在 HoloMotion 上的实验进一步表明，PERA 可适用于不同的基础策略。

## 核心内容

### 问题背景

运动模仿使人形机器人能够获得行走、跳舞等全身技能。但持续学习新技能时存在两难：微调整个策略会影响已有行为，而为每个技能单独训练策略则增加训练与维护成本。

### 方法

PERA 的核心思路是复用已有运动能力来学习新技能：

- 冻结一个预训练的混合专家（mixture-of-experts）策略；
- 额外训练一个任务专家及其路由分数；
- 训练信号可采用任务奖励或教师动作监督。

### 实验设置

- 仿真平台：Unitree G1；
- 基础策略：作者预训练的混合专家策略；
- 新增模块规模：每个任务模块约为基础 actor 参数量的 1.03%；
- 额外验证：在 HoloMotion 上进行实验，以检验方法对不同基础策略的适用性。

### 关键结果

- 基于预训练策略，PERA 成功完成全部十项新任务；
- 禁用新增专家后，基础策略恢复原有计算路径，仍能完整执行全部 126 个原始动作；
- 启用专家还能改善部分未用于训练该专家的舞蹈动作，表明其收益不局限于训练动作；
- HoloMotion 实验表明 PERA 可适用于不同的基础策略。

### 结论

PERA 通过冻结基础混合专家策略并仅添加轻量任务专家与路由分数，在保持原有运动能力的同时高效扩展新技能，且具备跨基础策略的适用性。

## Overview

Motion imitation enables humanoid robots to acquire whole-body skills such as walking and dancing. However, fine-tuning an entire policy for a new skill can affect existing behaviors, while training a separate policy for each skill increases training and maintenance costs. We present PERA, a method for learning new skills by reusing existing motion capabilities. PERA freezes a pretrained mixture-of-experts policy and trains an additional task expert and its routing score using task rewards or teacher-action supervision. In Unitree G1 simulation, each added task module contains approximately 1.03% of the parameters of the base actor. Built on our pretrained policy, PERA successfully completes all ten new tasks. Disabling the expert restores the original computation path of the base policy, which still fully executes all 126 original motions. Enabling the expert also improves the execution of some dance motions not used to train that expert, indicating that its benefits extend beyond its training motions. Experiments with HoloMotion further demonstrate the applicability of PERA to different base policies.

## 参考
- https://arxiv.org/abs/2611.16188
