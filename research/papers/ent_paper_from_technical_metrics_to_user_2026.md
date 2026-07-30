---
$id: ent_paper_from_technical_metrics_to_user_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'From Technical Metrics to User Perception: A User Study of a Multimodal Human-Robot Interaction System for Object Detection
    and Grasping'
  zh: 'From Technical Metrics to User Perception: A User Study of a Multimodal Human-Robot Interaction System for Object Detection
    and Grasping'
  ko: 'From Technical Metrics to User Perception: A User Study of a Multimodal Human-Robot Interaction System for Object Detection
    and Grasping'
summary:
  en: 'arXiv:2607.00530v1 Announce Type: new Abstract: Improvements in the technical performance of human--robot interaction
    (HRI) systems do not automatically translate into differences that human users can detect during live interaction. This
    paper investigates whether a 15 percentage point gain in end-to-end task success (from 75% in a multimodal baseline system
    to 90% in an improved configuration identified through a prior ablation study) is sufficient to produce consistent and
    measurable differences in user perception. The baseline system combines Whisper for speech recognition, Florence-2 for
    open-vocabulary object detection, LLaMA 3.1 for action extraction, and an interval Type-2 fuzzy logic controller for motion
    execution. The improved configuration replaces the perception and language modules with Grounding DINO + SAM and Qwen
    3.5 9B, respectively, while retaining the same controller. A within-subject user study with 24 participants compared both
    systems on the same tabletop object-grasping task. After interacting with each configuration, participants rated perceived
    speed, reliability, and overall competence and fluency on a 7-point Likert scale. Results show that 17 out of 24 participants
    (70.83%) preferred the improved system (exact binomial test, p = 0.043, h = 0.43), and all three perceptual constructs
    were rated significantly higher for the improved configuration after Holm correction, with large to very large effect
    sizes (p < 0.001). These findings confirm that the identified technical improvements are perceptible to users in direct
    interaction and underscore the importance of complementing benchmark evaluation with user-centred evidence when assessing
    robotic manipulation pipelines.'
  zh: 本文研究多模态人机交互系统中技术性能提升是否可被用户感知。作者通过24人用户实验，对比基线系统（Whisper+Florence-2+LLaMA 3.1）与改进系统（Grounding DINO+SAM+Qwen 3.5 9B）在桌面抓取任务中的表现。结果显示70.83%用户偏好改进系统，且感知速度、可靠性、流畅性评分均显著提升（p<0.001），证实15%的任务成功率提升可被用户察觉。
  ko: 'arXiv:2607.00530v1 Announce Type: new Abstract: Improvements in the technical performance of human--robot interaction
    (HRI) systems do not automatically translate into differences that human users can detect during live interaction. This
    paper investigates whether a 15 percentage point gain in end-to-end task success (from 75% in a multimodal baseline system
    to 90% in an improved configuration identified through a prior ablation study) is sufficient to produce consistent and
    measurable differences in user perception. The baseline system combines Whisper for speech recognition, Florence-2 for
    open-vocabulary object detection, LLaMA 3.1 for action extraction, and an interval Type-2 fuzzy logic controller for motion
    execution. The improved configuration replaces the perception and language modules with Grounding DINO + SAM and Qwen
    3.5 9B, respectively, while retaining the same controller. A within-subject user study with 24 participants compared both
    systems on the same tabletop object-grasping task. After interacting with each configuration, participants rated perceived
    speed, reliability, and overall competence and fluency on a 7-point Likert scale. Results show that 17 out of 24 participants
    (70.83%) preferred the improved system (exact binomial test, p = 0.043, h = 0.43), and all three perceptual constructs
    were rated significantly higher for the improved configuration after Holm correction, with large to very large effect
    sizes (p < 0.001). These findings confirm that the identified technical improvements are perceptible to users in direct
    interaction and underscore the importance of complementing benchmark evaluation with user-centred evidence when assessing
    robotic manipulation pipelines.'
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
- robotics
- from_technical_metrics_to_user
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.00530v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'From Technical Metrics to User Perception: A User Study of a Multimodal Human-Robot Interaction System for Object
    Detection and Grasping (arXiv)'
  url: https://arxiv.org/abs/2607.00530
  date: '2026'
  accessed_at: '2026-07-03'
---
## 概述
该研究针对人机交互系统技术指标提升与用户实际体验之间的鸿沟展开。基线系统采用Whisper语音识别、Florence-2开放词汇检测、LLaMA 3.1动作提取及区间二型模糊逻辑控制器；改进系统将感知模块替换为Grounding DINO+SAM，语言模块替换为Qwen 3.5 9B。24名受试者在桌面物体抓取任务中依次体验两种配置，通过7点李克特量表评估感知速度、可靠性、整体能力与流畅性。统计结果表明，改进系统在三个感知维度均获得显著更高评分（效应量大至极大），且偏好比例达70.83%（精确二项检验p=0.043）。

## 核心内容
### 研究动机
- 技术性能提升（如任务成功率从75%升至90%）未必能转化为用户可感知的交互体验差异
- 需通过用户研究验证基准测试改进的实际可感知性

### 系统架构
- **基线系统**：Whisper（语音识别）+ Florence-2（开放词汇检测）+ LLaMA 3.1（动作提取）+ 区间二型模糊逻辑控制器（运动执行）
- **改进系统**：Grounding DINO + SAM（感知模块）+ Qwen 3.5 9B（语言模块），保留相同控制器

### 实验设计
- **受试者**：24名参与者（组内设计）
- **任务**：桌面物体抓取
- **评估指标**：7点李克特量表（1=非常不同意，7=非常同意），测量感知速度、可靠性、整体能力与流畅性
- **统计方法**：精确二项检验（偏好数据）、Holm校正（感知评分）

### 关键结果
- **偏好数据**：17/24（70.83%）偏好改进系统（p=0.043，效应量h=0.43）
- **感知评分**：改进系统在三个维度均显著更高（p<0.001），效应量大至极大
- **结论**：15%的任务成功率提升可被用户可靠感知，验证了技术改进的实际价值

### 研究意义
- 强调在机器人操作流水线评估中，需将基准测试与用户中心证据相结合
- 为多模态HRI系统的用户感知研究提供了量化方法论参考

## Overview
Improvements in the technical performance of human--robot interaction (HRI) systems do not automatically translate into differences that human users can detect during live interaction. This paper investigates whether a 15 percentage point gain in end-to-end task success (from 75% in a multimodal baseline system to 90% in an improved configuration identified through a prior ablation study) is sufficient to produce consistent and measurable differences in user perception. The baseline system combines Whisper for speech recognition, Florence-2 for open-vocabulary object detection, LLaMA 3.1 for action extraction, and an interval Type-2 fuzzy logic controller for motion execution. The improved configuration replaces the perception and language modules with Grounding DINO + SAM and Qwen 3.5 9B, respectively, while retaining the same controller. A within-subject user study with 24 participants compared both systems on the same tabletop object-grasping task. After interacting with each configuration, participants rated perceived speed, reliability, and overall competence and fluency on a 7-point Likert scale. Results show that 17 out of 24 participants (70.83%) preferred the improved system (exact binomial test, p = 0.043, h = 0.43), and all three perceptual constructs were rated significantly higher for the improved configuration after Holm correction, with large to very large effect sizes (p < 0.001). These findings confirm that the identified technical improvements are perceptible to users in direct interaction and underscore the importance of complementing benchmark evaluation with user-centred evidence when assessing robotic manipulation pipelines.

## 개요
인간-로봇 상호작용(HRI) 시스템의 기술적 성능 향상이 실제 상호작용 중 인간 사용자가 감지할 수 있는 차이로 자동 이어지지는 않습니다. 본 논문은 종단 간 작업 성공률에서 15% 포인트 향상(이전 절제 연구를 통해 확인된 개선 구성에서 90%, 다중 모달 기준 시스템에서 75%)이 사용자 인식에서 일관되고 측정 가능한 차이를 만들어내기에 충분한지 조사합니다. 기준 시스템은 음성 인식을 위한 Whisper, 개방형 어휘 객체 탐지를 위한 Florence-2, 행동 추출을 위한 LLaMA 3.1, 동작 실행을 위한 구간 Type-2 퍼지 논리 제어기를 결합합니다. 개선 구성은 인식 및 언어 모듈을 각각 Grounding DINO + SAM과 Qwen 3.5 9B로 대체하고 동일한 제어기를 유지합니다. 24명의 참가자를 대상으로 한 피험자 내 사용자 연구는 동일한 탁상 객체 잡기 작업에서 두 시스템을 비교했습니다. 각 구성과 상호작용한 후, 참가자들은 인지된 속도, 신뢰성, 전반적인 능숙도 및 유창성을 7점 리커트 척도로 평가했습니다. 결과는 24명 중 17명(70.83%)의 참가자가 개선 시스템을 선호했으며(정확 이항 검정, p = 0.043, h = 0.43), Holm 보정 후 세 가지 인식 구성 모두 개선 구성에서 유의미하게 높게 평가되었고, 크거나 매우 큰 효과 크기를 보였습니다(p < 0.001). 이러한 발견은 확인된 기술적 개선이 직접 상호작용에서 사용자에게 인지 가능함을 확인하며, 로봇 조작 파이프라인을 평가할 때 벤치마크 평가를 사용자 중심 증거로 보완하는 중요성을 강조합니다.

## 핵심 내용
인간-로봇 상호작용(HRI) 시스템의 기술적 성능 향상이 실제 상호작용 중 인간 사용자가 감지할 수 있는 차이로 자동 이어지지는 않습니다. 본 논문은 종단 간 작업 성공률에서 15% 포인트 향상(이전 절제 연구를 통해 확인된 개선 구성에서 90%, 다중 모달 기준 시스템에서 75%)이 사용자 인식에서 일관되고 측정 가능한 차이를 만들어내기에 충분한지 조사합니다. 기준 시스템은 음성 인식을 위한 Whisper, 개방형 어휘 객체 탐지를 위한 Florence-2, 행동 추출을 위한 LLaMA 3.1, 동작 실행을 위한 구간 Type-2 퍼지 논리 제어기를 결합합니다. 개선 구성은 인식 및 언어 모듈을 각각 Grounding DINO + SAM과 Qwen 3.5 9B로 대체하고 동일한 제어기를 유지합니다. 24명의 참가자를 대상으로 한 피험자 내 사용자 연구는 동일한 탁상 객체 잡기 작업에서 두 시스템을 비교했습니다. 각 구성과 상호작용한 후, 참가자들은 인지된 속도, 신뢰성, 전반적인 능숙도 및 유창성을 7점 리커트 척도로 평가했습니다. 결과는 24명 중 17명(70.83%)의 참가자가 개선 시스템을 선호했으며(정확 이항 검정, p = 0.043, h = 0.43), Holm 보정 후 세 가지 인식 구성 모두 개선 구성에서 유의미하게 높게 평가되었고, 크거나 매우 큰 효과 크기를 보였습니다(p < 0.001). 이러한 발견은 확인된 기술적 개선이 직접 상호작용에서 사용자에게 인지 가능함을 확인하며, 로봇 조작 파이프라인을 평가할 때 벤치마크 평가를 사용자 중심 증거로 보완하는 중요성을 강조합니다.

## 参考
- http://arxiv.org/abs/2607.00530v1
