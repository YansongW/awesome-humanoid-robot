---
$id: ent_paper_yang_a_robust_single_sensing_elemen_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: A robust single-sensing-element tactile sensor for concurrent pressure and tackiness detection with real-time signal
    decoupling capability
  zh: A robust single-sensing-element tactile sensor for concurrent pressure and tackiness detection with real-time signal
    decoupling capability
  ko: A robust single-sensing-element tactile sensor for concurrent pressure and tackiness detection with real-time signal
    decoupling capability
summary:
  en: Integrating tackiness sensation into the artificial skin of humanoid robots significantly enhances their cognitive and
    operational capabilities. However existing tactile sensors face challenges in decoupling of the multimodal signal and
    stability. Here we present a surface-soft tactile sensor that incorporates a Hall effect sensor and a soft magnetic composite
    within a robust elastic framework. ...
  zh: 该研究提出一种表面柔软的触觉传感器，将霍尔效应传感器与软磁复合材料集成于稳健的弹性框架中，用单一传感元件同时检测压力与粘附性。当表面受压时凹陷、脱离粘性表面时明显凸起，从而动态改变霍尔传感器与磁体之间的距离，产生全程可追踪且基线分离的信号，实现压力与拉脱力的实时区分。该设计在同一接触点实现双模态感知并消除应力串扰，兼具可靠性与信号基线稳定性。
  ko: Integrating tackiness sensation into the artificial skin of humanoid robots significantly enhances their cognitive and
    operational capabilities. However existing tactile sensors face challenges in decoupling of the multimodal signal and
    stability. Here we present a surface-soft tactile sensor that incorporates a Hall effect sensor and a soft magnetic composite
    within a robust elastic framework. ...
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
- tactile_sensing
- multimodal_sensor
- hall_effect_sensor
- signal_decoupling
- soft_robotics
- humanoid_robot_skin
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-10-05'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-10-05). Bibliographic metadata from arXiv API (2609.36558);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: arXiv:2609.36558 A robust single-sensing-element tactile sensor for concurrent pressure and tackiness detection with
    real-time signal decoupling capability
  url: https://arxiv.org/abs/2609.36558
  date: '2026-09-29'
  accessed_at: '2026-10-05'
---

## 概述

该工作面向人形机器人人工皮肤中粘附感（tackiness）感知的需求，针对现有多模态触觉传感器信号解耦困难与稳定性不足的问题，提出一种表面柔软的触觉传感器。其结构将霍尔效应传感器与软磁复合材料嵌入稳健的弹性框架，利用受压凹陷与脱离粘性表面时凸起这两种形变来改变霍尔传感器与磁体之间的距离。由此产生的信号具有全程可追踪、基线分离的特点，可在实时条件下区分压力与拉脱力。单一传感元件的设计使同一接触点即可完成双模态感知，并消除应力串扰，提升精度与灵敏度。稳健框架与磁-机械传感机制的融合赋予传感器出色的可靠性与优良的信号基线稳定性，在评估粘附特性、监测橡胶老化、精细操作轻质物体以及认知自然物体表面特征等方面具有应用潜力。

## 核心内容

### 问题背景
将粘附感（tackiness）集成到人形机器人的人工皮肤中，可显著提升其认知与操作能力。然而，现有触觉传感器在多模态信号解耦和稳定性方面仍面临挑战。

### 方法
- 提出一种表面柔软的触觉传感器，在稳健的弹性框架内集成霍尔效应传感器（Hall effect sensor）与软磁复合材料（soft magnetic composite）。
- 传感机制：传感器表面在受压时凹陷，在从粘性表面脱离时明显凸起，这两种形变会动态改变霍尔传感器与磁体之间的距离。
- 由此产生全程可追踪（whole-process-traceable）且基线分离（baseline-separated）的信号，实现压力与拉脱力（pull-off force）的实时区分。
- 单一传感元件设计：在同一接触点实现双模态感知，同时消除应力串扰（stress cross-talk），提升精度与灵敏度。

### 关键结果
- 稳健框架与磁-机械传感机制的融合，使传感器具备出色的可靠性与优良的信号基线稳定性。
- 该设计在同一接触点完成压力与粘附性的并发检测，并具备实时信号解耦能力。

### 结论
该触觉传感器在提升机器人能力方面具有显著潜力，包括评估粘附特性、监测橡胶老化、精细操作轻质物体，以及认知自然物体的表面特征。

## Overview

Integrating tackiness sensation into the artificial skin of humanoid robots significantly enhances their cognitive and operational capabilities. However existing tactile sensors face challenges in decoupling of the multimodal signal and stability. Here we present a surface-soft tactile sensor that incorporates a Hall effect sensor and a soft magnetic composite within a robust elastic framework. The sensor surface indents under pressure and bulges prominently when retracted from sticky surfaces dynamically altering the Hall sensor-magnet distance. This generates whole-process-traceable and baseline-separated signals enabling real-time differentiation between pressure and pull-off force. This single-sensing-element design facilitates bimodal sensing at the same contact spot while eliminate stress cross-talk enhancing both accuracy and sensitivity. The fusion of a robust framework and magneto-mechanical sensing mechanism equips the sensor with exceptional reliability and excellent signal baseline stability. This tactile sensor holds substantial potential for advancing robotic capabilities in evaluating adhesive properties monitoring rubber aging precisely handling lightweight objects and cognizing natural objects surface characteristics.

## 参考
- https://arxiv.org/abs/2609.36558
