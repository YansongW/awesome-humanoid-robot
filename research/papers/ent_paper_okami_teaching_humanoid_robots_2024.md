---
$id: ent_paper_okami_teaching_humanoid_robots_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'OKAMI: Teaching Humanoid Robots Manipulation Skills through Single Video Imitation'
  zh: 'OKAMI: Teaching Humanoid Robots Manipulation Skills through Single Video Imitation'
  ko: 'OKAMI: Teaching Humanoid Robots Manipulation Skills through Single Video Imitation'
summary:
  en: 'OKAMI: Teaching Humanoid Robots Manipulation Skills through Single Video Imitation is a 2024 work on manipulation for
    humanoid robots.'
  zh: OKAMI 是 2024 年提出的一种方法，用于通过单段 RGB-D 视频教会人形机器人模仿人类操作技能。其核心贡献在于物体感知重定向技术，能将视频中的人类动作适配到部署时不同的物体位置，并分别重定向身体运动和手部姿态。实验表明，OKAMI
    在开放世界模仿任务中优于现有基线，且其生成的轨迹可用于训练闭环视觉运动策略，平均成功率达 79.2%。
  ko: 'OKAMI: Teaching Humanoid Robots Manipulation Skills through Single Video Imitation is a 2024 work on manipulation for
    humanoid robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- manipulation
- okami
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2410.11792v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'OKAMI: Teaching Humanoid Robots Manipulation Skills through Single Video Imitation (arXiv)'
  url: https://arxiv.org/abs/2410.11792
  date: '2024'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'OKAMI: Teaching Humanoid Robots Manipulation Skills through Single Video Imitation project page'
  url: https://ut-austin-rpl.github.io/OKAMI/
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
OKAMI 方法旨在解决人形机器人通过单段视频演示学习操作技能的问题。它从单段 RGB-D 视频中生成操作计划，并推导出可执行的策略。该方法的核心是物体感知重定向，利用开放世界视觉模型识别任务相关物体，并分别重定向身体运动和手部姿态，使机器人能模仿人类动作的同时适应部署时物体位置的变化。实验结果显示，OKAMI 在多种视觉和空间条件下表现出强大的泛化能力，超越了开放世界模仿观察的现有基线。此外，OKAMI 生成的轨迹可用于训练闭环视觉运动策略，平均成功率达到 79.2%，无需繁重的遥操作。

## 核心内容
### 方法概述
OKAMI 从单段 RGB-D 视频中提取人类操作演示，并生成人形机器人可执行的策略。其核心流程包括：
- **物体感知重定向**：利用开放世界视觉模型（如 open-world vision models）识别视频中与任务相关的物体，并分别处理身体运动和手部姿态的重定向。
- **运动重定向**：将视频中的人类身体运动映射到人形机器人上，同时根据部署时物体位置的变化进行调整，确保机器人能适应不同的空间条件。
- **手部姿态重定向**：单独处理手部动作，使机器人能精确模仿抓取、操作等精细动作。

### 实验设置与结果
- **基线对比**：与 state-of-the-art baseline 在开放世界模仿观察任务上进行比较，OKAMI 在多种视觉和空间条件下均表现出更强的泛化能力。
- **闭环策略训练**：利用 OKAMI 生成的 rollout 轨迹训练闭环 visuomotor policies，无需遥操作即可实现高成功率。
- **关键数字**：闭环策略的平均成功率达到 79.2%，显著降低了训练成本。

### 结论
OKAMI 通过单段视频演示实现了人形机器人的操作技能学习，其物体感知重定向技术有效解决了模仿过程中物体位置变化的问题。该方法不仅提升了泛化能力，还通过闭环策略训练减少了人工干预，为机器人学习提供了高效方案。更多演示视频可访问项目网站 https://ut-austin-rpl.github.io/OKAMI/。

## Overview
We study the problem of teaching humanoid robots manipulation skills by imitating from single video demonstrations. We introduce OKAMI, a method that generates a manipulation plan from a single RGB-D video and derives a policy for execution. At the heart of our approach is object-aware retargeting, which enables the humanoid robot to mimic the human motions in an RGB-D video while adjusting to different object locations during deployment. OKAMI uses open-world vision models to identify task-relevant objects and retarget the body motions and hand poses separately. Our experiments show that OKAMI achieves strong generalizations across varying visual and spatial conditions, outperforming the state-of-the-art baseline on open-world imitation from observation. Furthermore, OKAMI rollout trajectories are leveraged to train closed-loop visuomotor policies, which achieve an average success rate of 79.2% without the need for labor-intensive teleoperation. More videos can be found on our website https://ut-austin-rpl.github.io/OKAMI/.

## 개요
본 연구는 단일 비디오 시연을 모방하여 휴머노이드 로봇의 조작 기술을 가르치는 문제를 다룹니다. 우리는 단일 RGB-D 비디오로부터 조작 계획을 생성하고 실행 정책을 도출하는 방법인 OKAMI를 소개합니다. 이 접근법의 핵심은 객체 인식 리타겟팅(object-aware retargeting)으로, 휴머노이드 로봇이 RGB-D 비디오 속 인간의 동작을 모방하면서도 배치 시 다른 객체 위치에 적응할 수 있게 합니다. OKAMI는 개방형 세계 비전 모델(open-world vision models)을 사용하여 작업 관련 객체를 식별하고, 신체 동작과 손 자세를 별도로 리타겟팅합니다. 실험 결과, OKAMI는 다양한 시각적 및 공간적 조건에서 강력한 일반화 능력을 보여주며, 관찰로부터의 개방형 세계 모방(open-world imitation from observation)에서 최첨단 기준선(state-of-the-art baseline)을 능가합니다. 또한, OKAMI 롤아웃 궤적을 활용하여 폐쇄 루프 시각운동 정책(closed-loop visuomotor policies)을 훈련하며, 이는 노동 집약적인 원격 조작 없이 평균 성공률 79.2%를 달성합니다. 더 많은 비디오는 당사 웹사이트 https://ut-austin-rpl.github.io/OKAMI/에서 확인할 수 있습니다.

## 핵심 내용
본 연구는 단일 비디오 시연을 모방하여 휴머노이드 로봇의 조작 기술을 가르치는 문제를 다룹니다. 우리는 단일 RGB-D 비디오로부터 조작 계획을 생성하고 실행 정책을 도출하는 방법인 OKAMI를 소개합니다. 이 접근법의 핵심은 객체 인식 리타겟팅(object-aware retargeting)으로, 휴머노이드 로봇이 RGB-D 비디오 속 인간의 동작을 모방하면서도 배치 시 다른 객체 위치에 적응할 수 있게 합니다. OKAMI는 개방형 세계 비전 모델(open-world vision models)을 사용하여 작업 관련 객체를 식별하고, 신체 동작과 손 자세를 별도로 리타겟팅합니다. 실험 결과, OKAMI는 다양한 시각적 및 공간적 조건에서 강력한 일반화 능력을 보여주며, 관찰로부터의 개방형 세계 모방(open-world imitation from observation)에서 최첨단 기준선(state-of-the-art baseline)을 능가합니다. 또한, OKAMI 롤아웃 궤적을 활용하여 폐쇄 루프 시각운동 정책(closed-loop visuomotor policies)을 훈련하며, 이는 노동 집약적인 원격 조작 없이 평균 성공률 79.2%를 달성합니다. 더 많은 비디오는 당사 웹사이트 https://ut-austin-rpl.github.io/OKAMI/에서 확인할 수 있습니다.

## 参考
- http://arxiv.org/abs/2410.11792v1
