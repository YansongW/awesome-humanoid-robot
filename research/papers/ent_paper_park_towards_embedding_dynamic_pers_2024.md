---
$id: ent_paper_park_towards_embedding_dynamic_pers_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Towards Embedding Dynamic Personas in Interactive Robots: Masquerading Animated
    Social Kinematic (MASK)'
  zh: 面向交互式机器人中动态人格嵌入：Masquerading Animated Social Kinematic (MASK)
  ko: '대화형 로봇에 동적 페르소나 임베딩을 향하여: Masquerading Animated Social Kinematic (MASK)'
summary:
  en: This paper proposes MASK, an interactive robotic system that embeds personality-
    and film-character-based personas into an anthropomorphic robot via non-verbal
    behaviors such as facial expressions and gestures, using an LLM-based persona
    infuser and finite-state-machine behavior selection to enable real-time autonomous
    interaction. User studies with 162 participants showed that viewers could recognize
    the intended personality traits and fictional characters.
  zh: 本文提出了MASK交互式机器人系统，通过面部表情和手势等非言语行为，将基于人格和电影角色的动态角色形象嵌入类人机器人；该系统基于大语言模型的角色注入器和有限状态机行为选择实现实时自主交互，162名参与者的用户研究表明观众能够识别出目标人格特征和虚构角色。
  ko: 본 논문은 얼굴 표정과 제스처 등 비언어적 행동을 통해 개성 및 영화 캐릭터 기반의 페르소나를 의인화 로봇에 내재하는 MASK 대화형 로봇
    시스템을 제안한다. 대규모 언어 모델 기반 페르소나 주입기와 유한 상태 기계 행동 선택을 활용해 실시간 자율 상호작용을 가능하게 하며, 162명의
    참가자를 대상으로 한 사용자 연구에서 시청자가 의도된 성격 특성과 허구 캐릭터를 인식할 수 있음을 보였다.
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
tags:
- mask
- persona
- non_verbal_interaction
- behavior_generation
- finite_state_machine
- large_language_model
- anthropomorphic_robot
- social_robotics
- audience_engagement
- interactive_robot
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-28'
  confidence: medium
  notes: AI-extracted from supplied metadata and abstract; full-text verification
    and human review are required before promotion to verified.
sources:
- id: src_001
  type: paper
  title: 'Towards Embedding Dynamic Personas in Interactive Robots: Masquerading Animated
    Social Kinematic (MASK)'
  url: https://arxiv.org/abs/2403.10041
  date: '2024'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
---

## Overview

MASK (Masquerading Animated Social Kinematic) is an interactive robotic system designed to make anthropomorphic robots engaging by endowing them with dynamic, character-like personas. It moves beyond purely dialog-based persona agents by expressing personas through physical non-verbal behaviors, including facial expressions rendered on a head-mounted display and upper-body gestures executed by the Ambidex robot. The architecture couples a perception engine, a behavior-selection engine based on a finite-state machine, and a retargetable action library so that the robot can interact with guests in real time with limited hand-authored behavior design.

A central novelty is the LLM-based persona infuser. Given a short textual description of a persona, the infuser generates a matching motion set, facial-expression pairings, and FSM state transitions. This automation reduces the manual effort normally required to map a personality or fictional character onto concrete robot behaviors. The perception module estimates 3D body pose via a ZED 2i RGB-D camera and computes a curiosity score that guides turn-taking and behavior selection.

## Key Contributions

- Proposed MASK, an interactive robotic system that embeds personality- and film-character-based personas via non-verbal behavior.
- Introduced an LLM-based persona infuser that automates finite-state-machine transition generation, reducing manual behavior design.
- Integrated perception, behavior selection, and action-library modules for real-time autonomous interaction.
- Demonstrated through user studies with 162 participants that viewers can recognize both personality traits and fictional characters.

## Relevance to Humanoid Robotics

MASK is directly relevant to humanoid robotics because it addresses real-time, autonomous generation of socially expressive non-verbal behavior on an anthropomorphic platform. By automating persona-to-motion mapping with an LLM and structuring behavior selection with an FSM, the work provides a scalable software blueprint for deploying interactive humanoids in entertainment, service, and public-engagement settings. Its limitations—repetition over long interactions, coarse turn-taking, and appearance-motion mismatch—also highlight open engineering challenges for the field.
