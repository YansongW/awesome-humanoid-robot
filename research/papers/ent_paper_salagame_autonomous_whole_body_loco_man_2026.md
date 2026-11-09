---
$id: ent_paper_salagame_autonomous_whole_body_loco_man_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Autonomous Whole-body Loco-manipulation Using a Snake Robot
  zh: Autonomous Whole-body Loco-manipulation Using a Snake Robot
  ko: Autonomous Whole-body Loco-manipulation Using a Snake Robot
summary:
  en: Snake robots can leverage their hyper-redundant morphology for both locomotion and manipulation through distributed
    body contact but whole-body loco-manipulation is particularly challenging since the entire body serves simultaneously
    as propulsive mechanism and manipulation tool Prior work on wheeled legged and snake robot platforms has decoupled these
    functions through dedicated appendages body ...
  zh: 该论文研究蛇形机器人 COBRA 的自主全身移动-操作（loco-manipulation），让身体任意部位在侧向蜿蜒运动（sidewinding）中同时承担推进与操作功能，无需专用附肢或夹爪。作者建立了在 Moreau-Jean
    时间步进框架下统一机器人-地面、机器人-物体、物体-地面交互的接触隐式动力学模型，并在几何规划器与标称比例控制器引导下对全阶动力学进行轨迹优化，实现将物体自主推至目标位置。研究在硬件上跨多种构型验证了规划器与控制器，并给出简化轨迹优化的仿真结果。
  ko: Snake robots can leverage their hyper-redundant morphology for both locomotion and manipulation through distributed
    body contact but whole-body loco-manipulation is particularly challenging since the entire body serves simultaneously
    as propulsive mechanism and manipulation tool Prior work on wheeled legged and snake robot platforms has decoupled these
    functions through dedicated appendages body ...
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
- snake_robot
- loco_manipulation
- contact_implicit_dynamics
- trajectory_optimization
- sidewinding
- whole_body_control
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-11-09'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-11-09). Bibliographic metadata from arXiv API (2611.09777);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: arXiv:2611.09777 Autonomous Whole-body Loco-manipulation Using a Snake Robot
  url: https://arxiv.org/abs/2611.09777
  date: '2026-11-06'
  accessed_at: '2026-11-09'
---

## 概述

蛇形机器人凭借超冗余形态可通过分布式身体接触同时完成移动与操作，但全身移动-操作难度很大，因为整个身体既是推进机构又是操作工具。已有轮式、腿式与蛇形平台多通过专用附肢、身体分段或夹爪将两类功能解耦。本文提出不设这种区分的闭环移动-操作方案，使 COBRA 身体任意部位都可参与接触。作者构建了在 Moreau-Jean 时间步进框架内统一机器人-地面、机器人-物体与物体-地面交互的接触隐式动力学模型，并在几何规划器与标称比例控制器引导下对全阶动力学做轨迹优化，从而在侧向蜿蜒运动中自主将物体推向目标位置。规划器与控制器在硬件上跨多种构型得到验证，简化轨迹优化的仿真结果解决了机器人与物体、物体与地面的接触问题。

## 核心内容

### 问题背景
蛇形机器人具有超冗余形态，可通过分布式身体接触同时实现移动与操作。然而全身移动-操作（whole-body loco-manipulation）尤为困难：整个身体同时充当推进机构与操作工具。此前的轮式、腿式与蛇形机器人平台通常借助专用附肢、身体分段或夹爪将移动与操作功能解耦。本文则取消这种区分，允许身体任意部位发生接触，实现闭环移动-操作。

### 方法
- 建立接触隐式动力学模型，在 Moreau-Jean 时间步进框架内统一描述机器人-地面、机器人-物体与物体-地面三类交互。
- 对全阶动力学进行轨迹优化，并由几何规划器与标称比例控制器引导。
- 目标是在侧向蜿蜒运动（sidewinding）过程中自主将物体推至目标位置。

### 实验设置与结果
- 在硬件上跨多种构型验证了规划器与控制器。
- 给出简化轨迹优化的仿真结果，该优化处理机器人与物体、物体与地面的接触。

### 结论
所提方法无需专用操作附肢即可实现蛇形机器人的自主全身移动-操作，验证了接触隐式建模与规划控制方案在硬件多种构型下的可行性。

## Overview

Snake robots can leverage their hyper-redundant morphology for both locomotion and manipulation through distributed body contact but whole-body loco-manipulation is particularly challenging since the entire body serves simultaneously as propulsive mechanism and manipulation tool Prior work on wheeled legged and snake robot platforms has decoupled these functions through dedicated appendages body segmentation or grippers We present closed-loop loco-manipulation with our snake robot COBRA without this distinction such that any part of the body may make contact We develop a contact-implicit dynamic model unifying robot-ground robot-object and object-ground interactions within a Moreau-Jean time-stepping framework and formulate a trajectory optimization over the full-order dynamics guided by a geometric planner and nominal proportional controller to autonomously push an object to a goal location during sidewinding We validate the planner and controller on hardware across varied configurations and present simulation results for a simplified trajectory optimization that resolves robot-object and object-ground contacts

## 参考
- https://arxiv.org/abs/2611.09777
