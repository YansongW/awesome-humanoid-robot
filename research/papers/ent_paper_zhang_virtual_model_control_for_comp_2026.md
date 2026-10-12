---
$id: ent_paper_zhang_virtual_model_control_for_comp_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Virtual model control for compliant reaching under uncertainties
  zh: Virtual model control for compliant reaching under uncertainties
  ko: Virtual model control for compliant reaching under uncertainties
summary:
  en: Virtual Model Control (VMC) is an approach to design a controller for force-controlled robots in complex uncertain environments.
    While this method was primarily investigated for legged robot locomotion in the past, it can be more generally applicable
    to other types of robotic systems. This paper investigates the VMC framework for reaching tasks in a force-controlled
    robotic arm. We propose six ...
  zh: 本文研究将 Virtual Model Control（VMC）框架从足式机器人运动扩展到力控机械臂的 reaching 任务，作者为 Yi Zhang、Daniel Larby、Fumiya Iida 与 Fulvio Forni。他们提出六种虚拟模型设计方法，用于在有障碍与不确定性的环境中完成
    reaching，并在真实世界的力控 8 自由度人形机器人上验证。实验表明该方法虽需牺牲精度与轨迹最优性，但能以直观且可扩展的方式设计复杂 reaching 运动。
  ko: Virtual Model Control (VMC) is an approach to design a controller for force-controlled robots in complex uncertain environments.
    While this method was primarily investigated for legged robot locomotion in the past, it can be more generally applicable
    to other types of robotic systems. This paper investigates the VMC framework for reaching tasks in a force-controlled
    robotic arm. We propose six ...
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
- virtual_model_control
- compliant_reaching
- force_control
- humanoid_robot
- uncertain_environments
- reaching_tasks
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-10-12'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-10-12). Bibliographic metadata from arXiv API (2610.05695);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: arXiv:2610.05695 Virtual model control for compliant reaching under uncertainties
  url: https://arxiv.org/abs/2610.05695
  date: '2026-10-05'
  accessed_at: '2026-10-12'
---

## 概述

Virtual Model Control（VMC）是一种面向复杂不确定环境下力控机器人的控制器设计方法，过去主要用于足式机器人运动控制。本文将其推广到力控机械臂的 reaching 任务，提出六种不同的虚拟模型设计方式，以应对存在障碍与不确定性的环境。作者使用一台力控的 8 自由度人形机器人在真实世界中验证所提方法，并设计了三组实验，分别考察 VMC 控制器的可预测性、对外部力的敏感性，以及对已知与未知障碍的适应性。实验分析显示，该方法虽然需要牺牲一定的精度与轨迹最优性，但能够以直观且可扩展的方式设计不确定性条件下的复杂 reaching 运动。

## 核心内容

### 问题背景
Virtual Model Control（VMC）是一种为力控机器人在复杂不确定环境中设计控制器的方法。以往该方法主要针对足式机器人运动进行研究，但其适用范围可以更广。本文关注的是：能否将 VMC 框架用于力控机械臂的 reaching 任务。

### 方法
作者提出六种不同的虚拟模型设计方法，目标是在存在障碍与不确定性的环境中实现 reaching 任务。这些虚拟模型用于在力控框架下生成 reaching 运动。

### 实验设置
- 平台：一台力控的 8 自由度人形机器人，在真实世界中进行验证。
- 实验数量：共三组实验。
- 考察维度：VMC 控制器的可预测性、对外部力的敏感性，以及对已知与未知障碍的适应性。

### 关键结果
实验分析表明，所提方法需要牺牲精度与轨迹最优性，但能够在不确定性条件下设计复杂的 reaching 运动。

### 结论
VMC 框架可推广至力控机械臂的 reaching 任务，并且其虚拟模型设计方式具有直观性与可扩展性。

## Overview

Virtual Model Control (VMC) is an approach to design a controller for force-controlled robots in complex uncertain environments. While this method was primarily investigated for legged robot locomotion in the past, it can be more generally applicable to other types of robotic systems. This paper investigates the VMC framework for reaching tasks in a force-controlled robotic arm. We propose six different approaches to designing virtual models in order to achieve reaching tasks in environments with obstacles and uncertainties. A force-controlled 8 degree-of-freedom humanoid robot was used to validate the proposed approach in the real world. We conducted three experiments to test the performance of VMC controllers in terms of predictability, sensitivity to external force, and adaptability against known and unknown obstacles. Experimental analyses show that, even though the proposed approach needs to sacrifice accuracy and trajectory optimality, it enables us to design complex reaching motions under uncertainties, in an intuitive and extendable manner.

## 参考
- https://arxiv.org/abs/2610.05695
