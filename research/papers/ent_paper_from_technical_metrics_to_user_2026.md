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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.00530v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (870 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2607.00530v1

## 개요
본 연구는 인간-로봇 상호작용 시스템의 기술적 지표 향상과 사용자 실제 경험 사이의 간극을 다룬다. 기준 시스템은 Whisper 음성 인식, Florence-2 개방형 어휘 검출, LLaMA 3.1 동작 추출 및 구간 2형 퍼지 논리 제어기를 사용한다. 개선 시스템은 지각 모듈을 Grounding DINO+SAM으로, 언어 모듈을 Qwen 3.5 9B로 교체한다. 24명의 피험자가 테이블 위 물체 잡기 과제에서 두 구성을 순차적으로 경험하며, 7점 리커트 척도로 지각 속도, 신뢰성, 전반적 능력 및 유창성을 평가한다. 통계 결과, 개선 시스템은 세 가지 지각 차원 모두에서 유의미하게 높은 점수를 얻었으며(효과 크기 큼~매우 큼), 선호 비율은 70.83%에 달했다(정확 이항 검정 p=0.043).

## 핵심 내용
### 연구 동기
- 기술적 성능 향상(예: 작업 성공률 75%에서 90%로 상승)이 반드시 사용자가 인지 가능한 상호작용 경험 차이로 이어지지는 않음
- 벤치마크 개선의 실제 인지 가능성을 사용자 연구를 통해 검증할 필요가 있음

### 시스템 아키텍처
- **기준 시스템**: Whisper(음성 인식) + Florence-2(개방형 어휘 검출) + LLaMA 3.1(동작 추출) + 구간 2형 퍼지 논리 제어기(운동 실행)
- **개선 시스템**: Grounding DINO + SAM(지각 모듈) + Qwen 3.5 9B(언어 모듈), 동일한 제어기 유지

### 실험 설계
- **피험자**: 24명의 참가자(피험자 내 설계)
- **과제**: 테이블 위 물체 잡기
- **평가 지표**: 7점 리커트 척도(1=매우 동의하지 않음, 7=매우 동의함), 지각 속도, 신뢰성, 전반적 능력 및 유창성 측정
- **통계 방법**: 정확 이항 검정(선호 데이터), Holm 보정(지각 점수)

### 주요 결과
- **선호 데이터**: 17/24(70.83%)가 개선 시스템을 선호함(p=0.043, 효과 크기 h=0.43)
- **지각 점수**: 개선 시스템은 세 가지 차원 모두에서 유의미하게 높음(p<0.001), 효과 크기 큼~매우 큼
- **결론**: 15%의 작업 성공률 향상은 사용자가 안정적으로 인지할 수 있으며, 기술 개선의 실제 가치를 검증함

### 연구 의의
- 로봇 조작 파이프라인 평가에서 벤치마크 테스트와 사용자 중심 증거를 결합해야 함을 강조
- 다중 모달 HRI 시스템의 사용자 지각 연구를 위한 정량적 방법론 참조를 제공함
