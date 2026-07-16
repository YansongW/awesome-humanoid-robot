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
  zh: Semantic Co-Speech Gesture Synthesis and Real-Time Control for Humanoid Robots is a 2025 work on loco-manipulation and
    whole-body-control for humanoid robots.
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.17183v1.
sources:
- id: src_001
  type: paper
  title: Semantic Co-Speech Gesture Synthesis and Real-Time Control for Humanoid Robots (arXiv)
  url: https://arxiv.org/abs/2512.17183
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
We present an innovative end-to-end framework for synthesizing semantically meaningful co-speech gestures and deploying them in real-time on a humanoid robot. This system addresses the challenge of creating natural, expressive non-verbal communication for robots by integrating advanced gesture generation techniques with robust physical control. Our core innovation lies in the meticulous integration of a semantics-aware gesture synthesis module, which derives expressive reference motions from speech input by leveraging a generative retrieval mechanism based on large language models (LLMs) and an autoregressive Motion-GPT model. This is coupled with a high-fidelity imitation learning control policy, the MotionTracker, which enables the Unitree G1 humanoid robot to execute these complex motions dynamically and maintain balance. To ensure feasibility, we employ a robust General Motion Retargeting (GMR) method to bridge the embodiment gap between human motion data and the robot platform. Through comprehensive evaluation, we demonstrate that our combined system produces semantically appropriate and rhythmically coherent gestures that are accurately tracked and executed by the physical robot. To our knowledge, this work represents a significant step toward general real-world use by providing a complete pipeline for automatic, semantic-aware, co-speech gesture generation and synchronized real-time physical deployment on a humanoid robot.

## 核心内容
We present an innovative end-to-end framework for synthesizing semantically meaningful co-speech gestures and deploying them in real-time on a humanoid robot. This system addresses the challenge of creating natural, expressive non-verbal communication for robots by integrating advanced gesture generation techniques with robust physical control. Our core innovation lies in the meticulous integration of a semantics-aware gesture synthesis module, which derives expressive reference motions from speech input by leveraging a generative retrieval mechanism based on large language models (LLMs) and an autoregressive Motion-GPT model. This is coupled with a high-fidelity imitation learning control policy, the MotionTracker, which enables the Unitree G1 humanoid robot to execute these complex motions dynamically and maintain balance. To ensure feasibility, we employ a robust General Motion Retargeting (GMR) method to bridge the embodiment gap between human motion data and the robot platform. Through comprehensive evaluation, we demonstrate that our combined system produces semantically appropriate and rhythmically coherent gestures that are accurately tracked and executed by the physical robot. To our knowledge, this work represents a significant step toward general real-world use by providing a complete pipeline for automatic, semantic-aware, co-speech gesture generation and synchronized real-time physical deployment on a humanoid robot.

## 参考
- http://arxiv.org/abs/2512.17183v1

## Overview
We present an innovative end-to-end framework for synthesizing semantically meaningful co-speech gestures and deploying them in real-time on a humanoid robot. This system addresses the challenge of creating natural, expressive non-verbal communication for robots by integrating advanced gesture generation techniques with robust physical control. Our core innovation lies in the meticulous integration of a semantics-aware gesture synthesis module, which derives expressive reference motions from speech input by leveraging a generative retrieval mechanism based on large language models (LLMs) and an autoregressive Motion-GPT model. This is coupled with a high-fidelity imitation learning control policy, the MotionTracker, which enables the Unitree G1 humanoid robot to execute these complex motions dynamically and maintain balance. To ensure feasibility, we employ a robust General Motion Retargeting (GMR) method to bridge the embodiment gap between human motion data and the robot platform. Through comprehensive evaluation, we demonstrate that our combined system produces semantically appropriate and rhythmically coherent gestures that are accurately tracked and executed by the physical robot. To our knowledge, this work represents a significant step toward general real-world use by providing a complete pipeline for automatic, semantic-aware, co-speech gesture generation and synchronized real-time physical deployment on a humanoid robot.

## Content
We present an innovative end-to-end framework for synthesizing semantically meaningful co-speech gestures and deploying them in real-time on a humanoid robot. This system addresses the challenge of creating natural, expressive non-verbal communication for robots by integrating advanced gesture generation techniques with robust physical control. Our core innovation lies in the meticulous integration of a semantics-aware gesture synthesis module, which derives expressive reference motions from speech input by leveraging a generative retrieval mechanism based on large language models (LLMs) and an autoregressive Motion-GPT model. This is coupled with a high-fidelity imitation learning control policy, the MotionTracker, which enables the Unitree G1 humanoid robot to execute these complex motions dynamically and maintain balance. To ensure feasibility, we employ a robust General Motion Retargeting (GMR) method to bridge the embodiment gap between human motion data and the robot platform. Through comprehensive evaluation, we demonstrate that our combined system produces semantically appropriate and rhythmically coherent gestures that are accurately tracked and executed by the physical robot. To our knowledge, this work represents a significant step toward general real-world use by providing a complete pipeline for automatic, semantic-aware, co-speech gesture generation and synchronized real-time physical deployment on a humanoid robot.

## 개요
본 논문에서는 의미적으로 의미 있는 공동 발화 제스처를 합성하고 이를 휴머노이드 로봇에서 실시간으로 배포하기 위한 혁신적인 엔드투엔드 프레임워크를 제시합니다. 이 시스템은 고급 제스처 생성 기술과 강력한 물리적 제어를 통합하여 로봇을 위한 자연스럽고 표현력 있는 비언어적 의사소통을 창출하는 과제를 해결합니다. 핵심 혁신은 대규모 언어 모델(LLM) 기반의 생성적 검색 메커니즘과 자기회귀 Motion-GPT 모델을 활용하여 음성 입력에서 표현력 있는 참조 동작을 도출하는 의미 인식 제스처 합성 모듈의 세심한 통합에 있습니다. 이는 고충실도 모방 학습 제어 정책인 MotionTracker와 결합되어 Unitree G1 휴머노이드 로봇이 이러한 복잡한 동작을 동적으로 실행하고 균형을 유지할 수 있도록 합니다. 실현 가능성을 보장하기 위해, 인간 동작 데이터와 로봇 플랫폼 간의 구현 격차를 해소하는 강력한 일반 동작 리타겟팅(GMR) 방법을 사용합니다. 포괄적인 평가를 통해, 우리의 통합 시스템이 의미적으로 적절하고 리듬적으로 일관된 제스처를 생성하며, 이를 물리적 로봇이 정확하게 추적하고 실행함을 입증합니다. 본 연구는 자동적이고 의미 인식적인 공동 발화 제스처 생성과 휴머노이드 로봇에서의 동기화된 실시간 물리적 배포를 위한 완전한 파이프라인을 제공함으로써, 일반적인 실제 사용을 향한 중요한 진전을 나타냅니다.

## 핵심 내용
본 논문에서는 의미적으로 의미 있는 공동 발화 제스처를 합성하고 이를 휴머노이드 로봇에서 실시간으로 배포하기 위한 혁신적인 엔드투엔드 프레임워크를 제시합니다. 이 시스템은 고급 제스처 생성 기술과 강력한 물리적 제어를 통합하여 로봇을 위한 자연스럽고 표현력 있는 비언어적 의사소통을 창출하는 과제를 해결합니다. 핵심 혁신은 대규모 언어 모델(LLM) 기반의 생성적 검색 메커니즘과 자기회귀 Motion-GPT 모델을 활용하여 음성 입력에서 표현력 있는 참조 동작을 도출하는 의미 인식 제스처 합성 모듈의 세심한 통합에 있습니다. 이는 고충실도 모방 학습 제어 정책인 MotionTracker와 결합되어 Unitree G1 휴머노이드 로봇이 이러한 복잡한 동작을 동적으로 실행하고 균형을 유지할 수 있도록 합니다. 실현 가능성을 보장하기 위해, 인간 동작 데이터와 로봇 플랫폼 간의 구현 격차를 해소하는 강력한 일반 동작 리타겟팅(GMR) 방법을 사용합니다. 포괄적인 평가를 통해, 우리의 통합 시스템이 의미적으로 적절하고 리듬적으로 일관된 제스처를 생성하며, 이를 물리적 로봇이 정확하게 추적하고 실행함을 입증합니다. 본 연구는 자동적이고 의미 인식적인 공동 발화 제스처 생성과 휴머노이드 로봇에서의 동기화된 실시간 물리적 배포를 위한 완전한 파이프라인을 제공함으로써, 일반적인 실제 사용을 향한 중요한 진전을 나타냅니다.
