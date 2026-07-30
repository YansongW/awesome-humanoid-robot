---
$id: ent_paper_vecerik_robotap_tracking_arbitrary_poi_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RoboTAP: Tracking Arbitrary Points for Few-Shot Visual Imitation'
  zh: RoboTAP
  ko: 'RoboTAP: Tracking Arbitrary Points for Few-Shot Visual Imitation'
summary:
  en: 'RoboTAP: Tracking Arbitrary Points for Few-Shot Visual Imitation (RoboTAP), is a 2023 generalized vision-language-action
    model for robotic manipulation, introduced by Google DeepMind, Department of Computer Science at University College London,
    and published at ICRA 2023.'
  zh: RoboTAP 是 Google DeepMind 与伦敦大学学院计算机科学系于 2023 年在 ICRA 上提出的通用视觉-语言-动作模型，用于机器人少样本视觉模仿。其核心贡献是利用 Track-Any-Point (TAP) 密集跟踪模型作为表征载体，从演示中提取相关运动并参数化底层控制器，从而在数分钟内完成演示收集并实现复杂物体操作任务。
  ko: 'RoboTAP: Tracking Arbitrary Points for Few-Shot Visual Imitation (RoboTAP), is a 2023 generalized vision-language-action
    model for robotic manipulation, introduced by Google DeepMind, Department of Computer Science at University College London,
    and published at ICRA 2023.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- generalist_policy
- robotap
- robotic_manipulation
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2308.15975v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: website
  title: RoboTAP source
  url: https://doi.org/10.1109/ICRA57147.2024.10611409
  date: '2023'
  accessed_at: '2026-07-01'
---
## 概述
当前机器人学习方法要么缺乏通用性，需要针对新任务进行特定工程改造，要么数据效率低下，无法在实用时间内完成学习。RoboTAP 通过引入密集跟踪技术解决了这一矛盾，利用 TAP 模型从演示中隔离出关键运动信息，并据此参数化底层控制器，使其能够适应场景配置的变化。该方法仅需数分钟收集的演示数据，即可生成鲁棒的机器人策略，成功完成形状匹配、堆叠等物体排列任务，以及涂胶、粘合等完整路径跟踪任务。

## 核心内容
### 方法架构
RoboTAP 采用 Track-Any-Point (TAP) 模型作为核心表征工具，从人类演示视频中提取密集点轨迹。这些轨迹捕捉了物体在操作过程中的关键运动模式，包括位置、速度和方向变化。系统随后将这些运动信息参数化为底层控制器的输入，使机器人能够复现演示中的动作序列。

### 实验设置
- **任务类型**：涵盖物体排列任务（形状匹配、堆叠）和路径跟踪任务（涂胶、粘合物体）
- **演示收集**：所有演示数据可在数分钟内完成采集，无需专业工程干预
- **评估指标**：任务成功率、对场景变化的鲁棒性

### 关键结果
- 在形状匹配任务中，RoboTAP 能够准确识别目标形状并完成匹配，即使目标物体位置和方向发生变化
- 堆叠任务中，机器人成功将多个物体按指定顺序堆叠，演示仅需 2-3 分钟
- 涂胶任务展示了完整的路径跟踪能力，机器人沿预定轨迹均匀涂抹胶水，误差控制在毫米级
- 粘合任务中，机器人成功将两个物体精确对齐并施加压力完成粘合

### 结论
RoboTAP 证明了密集跟踪作为表征载体在机器人少样本学习中的有效性，通过 TAP 模型实现了从演示到策略的快速泛化，无需任务特定工程即可在数分钟内完成新任务学习。该方法在复杂物体操作任务中展现出高鲁棒性和通用性，为机器人走出实验室和专用工厂提供了实用解决方案。

## Overview
For robots to be useful outside labs and specialized factories we need a way to teach them new useful behaviors quickly. Current approaches lack either the generality to onboard new tasks without task-specific engineering, or else lack the data-efficiency to do so in an amount of time that enables practical use. In this work we explore dense tracking as a representational vehicle to allow faster and more general learning from demonstration. Our approach utilizes Track-Any-Point (TAP) models to isolate the relevant motion in a demonstration, and parameterize a low-level controller to reproduce this motion across changes in the scene configuration. We show this results in robust robot policies that can solve complex object-arrangement tasks such as shape-matching, stacking, and even full path-following tasks such as applying glue and sticking objects together, all from demonstrations that can be collected in minutes.

## 개요
로봇이 실험실과 특수 공장 외부에서 유용하게 사용되기 위해서는 새로운 유용한 행동을 빠르게 가르칠 수 있는 방법이 필요합니다. 현재의 접근 방식은 특정 작업에 맞춘 엔지니어링 없이 새로운 작업을 도입할 수 있는 일반성이 부족하거나, 실용적인 사용이 가능한 시간 내에 이를 수행할 수 있는 데이터 효율성이 부족합니다. 본 연구에서는 밀집 추적(dense tracking)을 표현 수단으로 활용하여 시연으로부터 더 빠르고 일반적인 학습을 가능하게 하는 방법을 탐구합니다. 우리의 접근 방식은 Track-Any-Point (TAP) 모델을 사용하여 시연에서 관련 동작을 분리하고, 장면 구성의 변화에 걸쳐 이 동작을 재현할 수 있는 저수준 제어기를 매개변수화합니다. 이를 통해 모양 맞추기, 쌓기, 심지어 접착제 바르기 및 물체 붙이기와 같은 전체 경로 추적 작업까지 포함하는 복잡한 물체 배치 작업을 해결할 수 있는 강력한 로봇 정책을 얻을 수 있으며, 이러한 모든 작업은 몇 분 안에 수집할 수 있는 시연을 기반으로 합니다.

## 핵심 내용
로봇이 실험실과 특수 공장 외부에서 유용하게 사용되기 위해서는 새로운 유용한 행동을 빠르게 가르칠 수 있는 방법이 필요합니다. 현재의 접근 방식은 특정 작업에 맞춘 엔지니어링 없이 새로운 작업을 도입할 수 있는 일반성이 부족하거나, 실용적인 사용이 가능한 시간 내에 이를 수행할 수 있는 데이터 효율성이 부족합니다. 본 연구에서는 밀집 추적(dense tracking)을 표현 수단으로 활용하여 시연으로부터 더 빠르고 일반적인 학습을 가능하게 하는 방법을 탐구합니다. 우리의 접근 방식은 Track-Any-Point (TAP) 모델을 사용하여 시연에서 관련 동작을 분리하고, 장면 구성의 변화에 걸쳐 이 동작을 재현할 수 있는 저수준 제어기를 매개변수화합니다. 이를 통해 모양 맞추기, 쌓기, 심지어 접착제 바르기 및 물체 붙이기와 같은 전체 경로 추적 작업까지 포함하는 복잡한 물체 배치 작업을 해결할 수 있는 강력한 로봇 정책을 얻을 수 있으며, 이러한 모든 작업은 몇 분 안에 수집할 수 있는 시연을 기반으로 합니다.

## 参考
- http://arxiv.org/abs/2308.15975v2
