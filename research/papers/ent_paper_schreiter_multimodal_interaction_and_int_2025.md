---
$id: ent_paper_schreiter_multimodal_interaction_and_int_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Multimodal Interaction and Intention Communication for Industrial Robots
  zh: 工业机器人的多模态交互与意图通信
  ko: 산업용 로봇을 위한 다중모달 상호작용 및 의도 전달
summary:
  en: This paper presents methods to design, enhance, and evaluate expressive human-robot interaction for non-humanoid industrial
    robots, introducing the Anthropomorphic Robotic Mock Driver (ARMoD) as a small anthropomorphic proxy that communicates
    on behalf of a host robot using a multimodal, LLM-enhanced framework combining speech, gaze, and gestures, and quantifies
    effects with gaze tracking and motion capture in controlled lab studies.
  zh: 本文提出设计、增强和评估非人形工业机器人表达性人机交互的方法，引入拟人机器人模拟驾驶员（ARMoD）作为小型拟人化代理，代表宿主机器人通过结合语音、注视和手势的多模态、大语言模型增强框架进行沟通，并在受控实验室研究中用眼动追踪与动作捕捉量化其效果。
  ko: 본 논문은 비인간형 산업용 로봇을 위한 표현적 HRI를 설계, 강화, 평가하는 방법을 제시하며, 음성, 시선, 제스처를 결합한 다중모달 및 LLM 기반 프레임워크를 통해 호스트 로봇을 대신하여 의사소통하는 작은
    의인화된 ARMoD 개념을 소개하고, 통제된 실험실 연구에서 시선 추적과 모션 캡처를 사용하여 효과를 정량화한다.
domains:
- 07_ai_models_algorithms
- 11_applications_markets
- 08_software_middleware
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
- system
tags:
- human_robot_interaction
- multimodal_communication
- anthropomorphic_proxy
- armod
- large_language_models
- industrial_robots
- intention_communication
- gaze_tracking
- motion_capture
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2502.17971v1.
sources:
- id: src_001
  type: paper
  title: Multimodal Interaction and Intention Communication for Industrial Robots
  url: https://arxiv.org/abs/2502.17971
  date: '2025'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
Successful adoption of industrial robots will strongly depend on their ability to safely and efficiently operate in human environments, engage in natural communication, understand their users, and express intentions intuitively while avoiding unnecessary distractions. To achieve this advanced level of Human-Robot Interaction (HRI), robots need to acquire and incorporate knowledge of their users' tasks and environment and adopt multimodal communication approaches with expressive cues that combine speech, movement, gazes, and other modalities. This paper presents several methods to design, enhance, and evaluate expressive HRI systems for non-humanoid industrial robots. We present the concept of a small anthropomorphic robot communicating as a proxy for its non-humanoid host, such as a forklift. We developed a multimodal and LLM-enhanced communication framework for this robot and evaluated it in several lab experiments, using gaze tracking and motion capture to quantify how users perceive the robot and measure the task progress.

## 核心内容
Successful adoption of industrial robots will strongly depend on their ability to safely and efficiently operate in human environments, engage in natural communication, understand their users, and express intentions intuitively while avoiding unnecessary distractions. To achieve this advanced level of Human-Robot Interaction (HRI), robots need to acquire and incorporate knowledge of their users' tasks and environment and adopt multimodal communication approaches with expressive cues that combine speech, movement, gazes, and other modalities. This paper presents several methods to design, enhance, and evaluate expressive HRI systems for non-humanoid industrial robots. We present the concept of a small anthropomorphic robot communicating as a proxy for its non-humanoid host, such as a forklift. We developed a multimodal and LLM-enhanced communication framework for this robot and evaluated it in several lab experiments, using gaze tracking and motion capture to quantify how users perceive the robot and measure the task progress.

## 参考
- http://arxiv.org/abs/2502.17971v1

## Overview
Successful adoption of industrial robots will strongly depend on their ability to safely and efficiently operate in human environments, engage in natural communication, understand their users, and express intentions intuitively while avoiding unnecessary distractions. To achieve this advanced level of Human-Robot Interaction (HRI), robots need to acquire and incorporate knowledge of their users' tasks and environment and adopt multimodal communication approaches with expressive cues that combine speech, movement, gazes, and other modalities. This paper presents several methods to design, enhance, and evaluate expressive HRI systems for non-humanoid industrial robots. We present the concept of a small anthropomorphic robot communicating as a proxy for its non-humanoid host, such as a forklift. We developed a multimodal and LLM-enhanced communication framework for this robot and evaluated it in several lab experiments, using gaze tracking and motion capture to quantify how users perceive the robot and measure the task progress.

## Content
Successful adoption of industrial robots will strongly depend on their ability to safely and efficiently operate in human environments, engage in natural communication, understand their users, and express intentions intuitively while avoiding unnecessary distractions. To achieve this advanced level of Human-Robot Interaction (HRI), robots need to acquire and incorporate knowledge of their users' tasks and environment and adopt multimodal communication approaches with expressive cues that combine speech, movement, gazes, and other modalities. This paper presents several methods to design, enhance, and evaluate expressive HRI systems for non-humanoid industrial robots. We present the concept of a small anthropomorphic robot communicating as a proxy for its non-humanoid host, such as a forklift. We developed a multimodal and LLM-enhanced communication framework for this robot and evaluated it in several lab experiments, using gaze tracking and motion capture to quantify how users perceive the robot and measure the task progress.

## 개요
산업용 로봇의 성공적인 도입은 인간 환경에서 안전하고 효율적으로 작동하며, 자연스러운 의사소통을 수행하고, 사용자를 이해하며, 불필요한 방해를 피하면서 직관적으로 의도를 표현하는 능력에 크게 의존할 것입니다. 이러한 고급 수준의 인간-로봇 상호작용(HRI)을 달성하기 위해 로봇은 사용자의 작업 및 환경에 대한 지식을 습득하고 통합해야 하며, 음성, 움직임, 시선 및 기타 양식을 결합한 표현적 단서를 갖춘 다중 모드 의사소통 접근 방식을 채택해야 합니다. 본 논문은 비인간형 산업용 로봇을 위한 표현적 HRI 시스템을 설계, 향상 및 평가하는 여러 방법을 제시합니다. 우리는 지게차와 같은 비인간형 호스트를 대신하여 의사소통하는 소형 의인화 로봇의 개념을 소개합니다. 이 로봇을 위해 다중 모드 및 LLM 강화 의사소통 프레임워크를 개발하고, 시선 추적 및 모션 캡처를 사용하여 사용자가 로봇을 어떻게 인식하는지 정량화하고 작업 진행 상황을 측정하는 여러 실험실 실험에서 이를 평가했습니다.

## 핵심 내용
산업용 로봇의 성공적인 도입은 인간 환경에서 안전하고 효율적으로 작동하며, 자연스러운 의사소통을 수행하고, 사용자를 이해하며, 불필요한 방해를 피하면서 직관적으로 의도를 표현하는 능력에 크게 의존할 것입니다. 이러한 고급 수준의 인간-로봇 상호작용(HRI)을 달성하기 위해 로봇은 사용자의 작업 및 환경에 대한 지식을 습득하고 통합해야 하며, 음성, 움직임, 시선 및 기타 양식을 결합한 표현적 단서를 갖춘 다중 모드 의사소통 접근 방식을 채택해야 합니다. 본 논문은 비인간형 산업용 로봇을 위한 표현적 HRI 시스템을 설계, 향상 및 평가하는 여러 방법을 제시합니다. 우리는 지게차와 같은 비인간형 호스트를 대신하여 의사소통하는 소형 의인화 로봇의 개념을 소개합니다. 이 로봇을 위해 다중 모드 및 LLM 강화 의사소통 프레임워크를 개발하고, 시선 추적 및 모션 캡처를 사용하여 사용자가 로봇을 어떻게 인식하는지 정량화하고 작업 진행 상황을 측정하는 여러 실험실 실험에서 이를 평가했습니다.
