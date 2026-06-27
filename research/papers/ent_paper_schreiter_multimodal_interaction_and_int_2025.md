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
  en: This paper presents methods to design, enhance, and evaluate expressive human-robot
    interaction for non-humanoid industrial robots, introducing the Anthropomorphic
    Robotic Mock Driver (ARMoD) as a small anthropomorphic proxy that communicates
    on behalf of a host robot using a multimodal, LLM-enhanced framework combining
    speech, gaze, and gestures, and quantifies effects with gaze tracking and motion
    capture in controlled lab studies.
  zh: 本文提出设计、增强和评估非人形工业机器人表达性人机交互的方法，引入拟人机器人模拟驾驶员（ARMoD）作为小型拟人化代理，代表宿主机器人通过结合语音、注视和手势的多模态、大语言模型增强框架进行沟通，并在受控实验室研究中用眼动追踪与动作捕捉量化其效果。
  ko: 본 논문은 비인간형 산업용 로봇을 위한 표현적 HRI를 설계, 강화, 평가하는 방법을 제시하며, 음성, 시선, 제스처를 결합한 다중모달
    및 LLM 기반 프레임워크를 통해 호스트 로봇을 대신하여 의사소통하는 작은 의인화된 ARMoD 개념을 소개하고, 통제된 실험실 연구에서 시선
    추적과 모션 캡처를 사용하여 효과를 정량화한다.
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
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from the arXiv full-text PDF; named methods, datasets, and results
    are quoted from the paper, but exact model details and demographic data were not
    present in the extracted text and require human review.
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

## Overview

Industrial robots are increasingly deployed in shared human environments, yet their function-driven, non-humanoid designs often lack the expressive modalities needed for intuitive communication. This paper addresses that gap by developing methods to design, enhance, and evaluate expressive human-robot interaction (HRI) for non-humanoid industrial platforms. The authors introduce the Anthropomorphic Robotic Mock Driver (ARMoD), a small anthropomorphic robot that acts as a communication proxy for a host machine such as a forklift, translating the host's intentions into human-readable social signals.

The proposed multimodal communication framework combines speech, gaze, and referential gestures, and is further extended with Large Language Models (LLMs) to enable real-time context interpretation and natural-language response generation. To assess the impact of these behaviors, the authors integrate gaze tracking and motion capture, using eye movements and head rotations as objective measures of attention, intention, and task progress. The work was carried out within the EU project DARKO, and the experiments include both scripted object-handling scenarios and spontaneous navigation interactions.

The reported lab studies compare verbal-only, multimodal, scripted, and LLM-enhanced interaction styles. The results indicate that users react faster and focus more on the robot when multimodal cues are present, but no significant efficiency gain was observed for LLM-enhanced responses over fully scripted ones, nor between differential and omnidirectional robot motion in the THÖR-MAGNI dataset.

## Key Contributions

- ARMoD concept: a small anthropomorphic proxy robot that communicates on behalf of non-humanoid host platforms such as forklifts.
- Multimodal and LLM-enhanced communication framework using speech, gaze, and referential gestures.
- Objective quantification of HRI effectiveness through gaze tracking and motion capture.
- Controlled lab studies comparing verbal-only, multimodal, scripted, and LLM-enhanced interaction styles.

## Relevance to Humanoid Robotics

Although the paper targets non-humanoid industrial robots, its core relevance to humanoid robotics lies in the use of a small anthropomorphic proxy to generate human-like expressive cues. The ARMoD concept demonstrates how anthropomorphic form factors, multimodal signaling, and LLM-based natural-language adaptation can improve user attention, task understanding, and coordination in human-robot teams.

The findings are transferable to humanoid platforms, which already possess many of the required expressive modalities. The combination of gaze, gesture, speech, and contextual language generation, together with objective gaze- and motion-capture evaluation, provides a methodological reference for designing more natural and legible intention communication in humanoid robots deployed in industrial or service settings.
