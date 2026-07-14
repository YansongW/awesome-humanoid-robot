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

