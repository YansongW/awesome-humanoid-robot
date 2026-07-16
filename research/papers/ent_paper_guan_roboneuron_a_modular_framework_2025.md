---
$id: ent_paper_guan_roboneuron_a_modular_framework_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RoboNeuron: A Modular Framework Linking Foundation Models and ROS for Embodied AI'
  zh: RoboNeuron
  ko: 'RoboNeuron: A Modular Framework Linking Foundation Models and ROS for Embodied AI'
summary:
  en: 'RoboNeuron: A Modular Framework Linking Foundation Models and ROS for Embodied AI (RoboNeuron), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Institute of Automation, Chinese Academy of Sciences, University of Chinese
    Academy of Sciences, AiRiA, MICRO.'
  zh: 'RoboNeuron: A Modular Framework Linking Foundation Models and ROS for Embodied AI (RoboNeuron), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Institute of Automation, Chinese Academy of Sciences, University of Chinese
    Academy of Sciences, AiRiA, MICRO.'
  ko: 'RoboNeuron: A Modular Framework Linking Foundation Models and ROS for Embodied AI (RoboNeuron), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Institute of Automation, Chinese Academy of Sciences, University of Chinese
    Academy of Sciences, AiRiA, MICRO.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- large_vla_model
- roboneuron
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.10394v2.
sources:
- id: src_001
  type: paper
  title: 'RoboNeuron: A Modular Framework Linking Foundation Models and ROS for Embodied AI (arXiv)'
  url: https://arxiv.org/abs/2512.10394
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: RoboNeuron source
  url: https://doi.org/10.48550/arXiv.2512.10394
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-language-action (VLA) models and LLM agents have advanced rapidly, yet reliable deployment on physical robots is often hindered by an interface mismatch between agent tool APIs and robot middleware. Current implementations typically rely on ad-hoc wrappers that are difficult to reuse, and changes to the VLA backend or serving stack often necessitate extensive re-integration. We introduce RoboNeuron, a middleware layer that connects the Model Context Protocol (MCP) for LLM agents with robot middleware such as ROS2. RoboNeuron bridges these ecosystems by deriving agent-callable tools directly from ROS schemas, providing a unified execution abstraction that supports both direct commands and modular composition, and localizing backend, runtime, and acceleration-preset changes within a stable inference boundary. We evaluate RoboNeuron in simulation and on hardware through multi-platform base control, arm motion, and VLA-based grasping tasks, demonstrating that it enables modular system orchestration under a unified interface while supporting backend transitions without system rewiring. The full code implementation of this work is available at github repo: https://github.com/guanweifan/RoboNeuron

## 核心内容
Vision-language-action (VLA) models and LLM agents have advanced rapidly, yet reliable deployment on physical robots is often hindered by an interface mismatch between agent tool APIs and robot middleware. Current implementations typically rely on ad-hoc wrappers that are difficult to reuse, and changes to the VLA backend or serving stack often necessitate extensive re-integration. We introduce RoboNeuron, a middleware layer that connects the Model Context Protocol (MCP) for LLM agents with robot middleware such as ROS2. RoboNeuron bridges these ecosystems by deriving agent-callable tools directly from ROS schemas, providing a unified execution abstraction that supports both direct commands and modular composition, and localizing backend, runtime, and acceleration-preset changes within a stable inference boundary. We evaluate RoboNeuron in simulation and on hardware through multi-platform base control, arm motion, and VLA-based grasping tasks, demonstrating that it enables modular system orchestration under a unified interface while supporting backend transitions without system rewiring. The full code implementation of this work is available at github repo: https://github.com/guanweifan/RoboNeuron

## 参考
- http://arxiv.org/abs/2512.10394v2

## Overview
Vision-language-action (VLA) models and LLM agents have advanced rapidly, yet reliable deployment on physical robots is often hindered by an interface mismatch between agent tool APIs and robot middleware. Current implementations typically rely on ad-hoc wrappers that are difficult to reuse, and changes to the VLA backend or serving stack often necessitate extensive re-integration. We introduce RoboNeuron, a middleware layer that connects the Model Context Protocol (MCP) for LLM agents with robot middleware such as ROS2. RoboNeuron bridges these ecosystems by deriving agent-callable tools directly from ROS schemas, providing a unified execution abstraction that supports both direct commands and modular composition, and localizing backend, runtime, and acceleration-preset changes within a stable inference boundary. We evaluate RoboNeuron in simulation and on hardware through multi-platform base control, arm motion, and VLA-based grasping tasks, demonstrating that it enables modular system orchestration under a unified interface while supporting backend transitions without system rewiring. The full code implementation of this work is available at github repo: https://github.com/guanweifan/RoboNeuron

## Content
Vision-language-action (VLA) models and LLM agents have advanced rapidly, yet reliable deployment on physical robots is often hindered by an interface mismatch between agent tool APIs and robot middleware. Current implementations typically rely on ad-hoc wrappers that are difficult to reuse, and changes to the VLA backend or serving stack often necessitate extensive re-integration. We introduce RoboNeuron, a middleware layer that connects the Model Context Protocol (MCP) for LLM agents with robot middleware such as ROS2. RoboNeuron bridges these ecosystems by deriving agent-callable tools directly from ROS schemas, providing a unified execution abstraction that supports both direct commands and modular composition, and localizing backend, runtime, and acceleration-preset changes within a stable inference boundary. We evaluate RoboNeuron in simulation and on hardware through multi-platform base control, arm motion, and VLA-based grasping tasks, demonstrating that it enables modular system orchestration under a unified interface while supporting backend transitions without system rewiring. The full code implementation of this work is available at github repo: https://github.com/guanweifan/RoboNeuron

## 개요
Vision-language-action (VLA) 모델과 LLM 에이전트는 빠르게 발전했지만, 물리적 로봇에 대한 신뢰할 수 있는 배포는 종종 에이전트 도구 API와 로봇 미들웨어 간의 인터페이스 불일치로 인해 방해를 받습니다. 현재 구현은 일반적으로 재사용이 어려운 임시 래퍼에 의존하며, VLA 백엔드나 서빙 스택의 변경은 종종 광범위한 재통합을 필요로 합니다. 우리는 LLM 에이전트를 위한 Model Context Protocol (MCP)과 ROS2와 같은 로봇 미들웨어를 연결하는 미들웨어 계층인 RoboNeuron을 소개합니다. RoboNeuron은 ROS 스키마에서 직접 에이전트 호출 가능 도구를 도출하고, 직접 명령과 모듈식 구성을 모두 지원하는 통합 실행 추상화를 제공하며, 안정적인 추론 경계 내에서 백엔드, 런타임 및 가속 프리셋 변경을 국소화함으로써 이러한 생태계를 연결합니다. 우리는 RoboNeuron을 시뮬레이션과 하드웨어에서 다중 플랫폼 베이스 제어, 암 모션, VLA 기반 파지 작업을 통해 평가하여, 시스템 재배선 없이 백엔드 전환을 지원하면서 통합 인터페이스 아래에서 모듈식 시스템 오케스트레이션을 가능하게 함을 입증합니다. 이 작업의 전체 코드 구현은 github 저장소에서 확인할 수 있습니다: https://github.com/guanweifan/RoboNeuron

## 핵심 내용
Vision-language-action (VLA) 모델과 LLM 에이전트는 빠르게 발전했지만, 물리적 로봇에 대한 신뢰할 수 있는 배포는 종종 에이전트 도구 API와 로봇 미들웨어 간의 인터페이스 불일치로 인해 방해를 받습니다. 현재 구현은 일반적으로 재사용이 어려운 임시 래퍼에 의존하며, VLA 백엔드나 서빙 스택의 변경은 종종 광범위한 재통합을 필요로 합니다. 우리는 LLM 에이전트를 위한 Model Context Protocol (MCP)과 ROS2와 같은 로봇 미들웨어를 연결하는 미들웨어 계층인 RoboNeuron을 소개합니다. RoboNeuron은 ROS 스키마에서 직접 에이전트 호출 가능 도구를 도출하고, 직접 명령과 모듈식 구성을 모두 지원하는 통합 실행 추상화를 제공하며, 안정적인 추론 경계 내에서 백엔드, 런타임 및 가속 프리셋 변경을 국소화함으로써 이러한 생태계를 연결합니다. 우리는 RoboNeuron을 시뮬레이션과 하드웨어에서 다중 플랫폼 베이스 제어, 암 모션, VLA 기반 파지 작업을 통해 평가하여, 시스템 재배선 없이 백엔드 전환을 지원하면서 통합 인터페이스 아래에서 모듈식 시스템 오케스트레이션을 가능하게 함을 입증합니다. 이 작업의 전체 코드 구현은 github 저장소에서 확인할 수 있습니다: https://github.com/guanweifan/RoboNeuron
