---
$id: ent_paper_semantic_co_speech_gesture_syn_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Semantic Co-Speech Gesture Synthesis and Real-Time Control for Humanoid Robots
  zh: Semantic Co-Speech Gesture Synthesis and Real-Time Control for Humanoid Robots
  ko: Semantic Co-Speech Gesture Synthesis and Real-Time Control for Humanoid Robots
summary:
  en: Semantic Co-Speech Gesture Synthesis and Real-Time Control for Humanoid Robots is a 2025 work on loco-manipulation and
    whole-body-control for humanoid robots.
  zh: 本文提出了一种面向人形机器人的端到端框架，用于合成语义丰富的共语手势并实现实时控制。该工作由研究团队完成，核心贡献在于将基于大语言模型和Motion-GPT的语义感知手势生成模块与高保真模仿学习控制策略MotionTracker相结合，使Unitree
    G1机器人能够动态执行复杂动作并保持平衡。
  ko: Semantic Co-Speech Gesture Synthesis and Real-Time Control for Humanoid Robots is a 2025 work on loco-manipulation and
    whole-body-control for humanoid robots.
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
- loco_manipulation
- semantic_co_speech_gesture_syn
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.17183v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (666 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Semantic Co-Speech Gesture Synthesis and Real-Time Control for Humanoid Robots (arXiv)
  url: https://arxiv.org/abs/2512.17183
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
该框架通过集成语义感知手势合成模块与高保真模仿学习控制策略，解决了人形机器人自然非语言交流的挑战。手势合成模块利用大语言模型和自回归Motion-GPT模型，从语音输入中生成具有语义的参考动作；而MotionTracker控制策略则使Unitree G1机器人能够动态执行这些复杂动作并维持平衡。为弥合人体运动数据与机器人平台之间的具身差异，系统采用了通用运动重定向方法。实验表明，该框架能生成语义恰当、节奏协调的手势，并由实体机器人精确跟踪执行。

## 核心内容
### 方法架构
- **语义感知手势合成模块**：基于大语言模型（LLMs）的生成检索机制与自回归Motion-GPT模型，从语音输入中提取语义特征并生成表达性参考动作。
- **高保真模仿学习控制策略（MotionTracker）**：使Unitree G1人形机器人能够动态执行复杂运动并保持平衡。
- **通用运动重定向（GMR）**：弥合人体运动数据与机器人平台之间的具身差异，确保动作可行性。

### 实验设置
- **机器人平台**：Unitree G1人形机器人。
- **评估指标**：语义恰当性、节奏连贯性、动作跟踪精度。

### 关键结果
- 系统生成的共语手势在语义上恰当且节奏上连贯。
- 实体机器人能够准确跟踪并执行这些手势。
- 该工作首次提供了从自动语义感知手势生成到同步实时物理部署的完整流水线。

### 结论
本文提出的端到端框架显著推进了人形机器人在真实场景中的通用应用，实现了自然、富有表现力的非语言交流。

## Overview
We present an innovative end-to-end framework for synthesizing semantically meaningful co-speech gestures and deploying them in real-time on a humanoid robot. This system addresses the challenge of creating natural, expressive non-verbal communication for robots by integrating advanced gesture generation techniques with robust physical control. Our core innovation lies in the meticulous integration of a semantics-aware gesture synthesis module, which derives expressive reference motions from speech input by leveraging a generative retrieval mechanism based on large language models (LLMs) and an autoregressive Motion-GPT model. This is coupled with a high-fidelity imitation learning control policy, the MotionTracker, which enables the Unitree G1 humanoid robot to execute these complex motions dynamically and maintain balance. To ensure feasibility, we employ a robust General Motion Retargeting (GMR) method to bridge the embodiment gap between human motion data and the robot platform. Through comprehensive evaluation, we demonstrate that our combined system produces semantically appropriate and rhythmically coherent gestures that are accurately tracked and executed by the physical robot. To our knowledge, this work represents a significant step toward general real-world use by providing a complete pipeline for automatic, semantic-aware, co-speech gesture generation and synchronized real-time physical deployment on a humanoid robot.

## 参考
- http://arxiv.org/abs/2512.17183v1

## 개요
이 프레임워크는 의미 인식 제스처 합성 모듈과 고충실도 모방 학습 제어 정책을 통합하여 휴머노이드 로봇의 자연스러운 비언어적 의사소통 문제를 해결합니다. 제스처 합성 모듈은 대규모 언어 모델과 자기회귀 Motion-GPT 모델을 활용하여 음성 입력에서 의미 있는 참조 동작을 생성하며, MotionTracker 제어 정책은 Unitree G1 로봇이 이러한 복잡한 동작을 동적으로 실행하고 균형을 유지할 수 있게 합니다. 인간 동작 데이터와 로봇 플랫폼 간의 구현 차이를 메우기 위해 시스템은 범용 동작 리타게팅 방법을 채택합니다. 실험 결과, 이 프레임워크는 의미적으로 적절하고 리듬이 조화로운 제스처를 생성하며, 실제 로봇이 이를 정밀하게 추적하여 실행할 수 있음을 보여줍니다.

## 핵심 내용
### 방법 아키텍처
- **의미 인식 제스처 합성 모듈**: 대규모 언어 모델(LLMs) 기반 생성-검색 메커니즘과 자기회귀 Motion-GPT 모델을 통해 음성 입력에서 의미 특징을 추출하고 표현력 있는 참조 동작을 생성합니다.
- **고충실도 모방 학습 제어 정책(MotionTracker)**: Unitree G1 휴머노이드 로봇이 복잡한 동작을 동적으로 실행하고 균형을 유지할 수 있게 합니다.
- **범용 동작 리타게팅(GMR)**: 인간 동작 데이터와 로봇 플랫폼 간의 구현 차이를 메우고 동작 실행 가능성을 보장합니다.

### 실험 설정
- **로봇 플랫폼**: Unitree G1 휴머노이드 로봇.
- **평가 지표**: 의미 적절성, 리듬 일관성, 동작 추적 정밀도.

### 주요 결과
- 시스템이 생성한 공동 발화 제스처는 의미적으로 적절하고 리듬적으로 일관됩니다.
- 실제 로봇이 이러한 제스처를 정확하게 추적하고 실행할 수 있습니다.
- 이 작업은 자동 의미 인식 제스처 생성부터 동기화된 실시간 물리적 배포까지의 완전한 파이프라인을 최초로 제공합니다.

### 결론
본 논문에서 제안한 엔드투엔드 프레임워크는 실제 시나리오에서 휴머노이드 로봇의 일반적 응용을 크게 발전시켜 자연스럽고 표현력 있는 비언어적 의사소통을 구현합니다.
