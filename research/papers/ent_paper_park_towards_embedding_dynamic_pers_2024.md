---
$id: ent_paper_park_towards_embedding_dynamic_pers_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Towards Embedding Dynamic Personas in Interactive Robots: Masquerading Animated Social Kinematic (MASK)'
  zh: 面向交互式机器人中动态人格嵌入：Masquerading Animated Social Kinematic (MASK)
  ko: '대화형 로봇에 동적 페르소나 임베딩을 향하여: Masquerading Animated Social Kinematic (MASK)'
summary:
  en: This paper proposes MASK, an interactive robotic system that embeds personality- and film-character-based personas into
    an anthropomorphic robot via non-verbal behaviors such as facial expressions and gestures, using an LLM-based persona
    infuser and finite-state-machine behavior selection to enable real-time autonomous interaction. User studies with 162
    participants showed that viewers could recognize the intended personality traits and fictional characters.
  zh: 本文提出了MASK交互式机器人系统，通过面部表情和手势等非言语行为，将基于人格和电影角色的动态角色形象嵌入类人机器人；该系统基于大语言模型的角色注入器和有限状态机行为选择实现实时自主交互，162名参与者的用户研究表明观众能够识别出目标人格特征和虚构角色。
  ko: 본 논문은 얼굴 표정과 제스처 등 비언어적 행동을 통해 개성 및 영화 캐릭터 기반의 페르소나를 의인화 로봇에 내재하는 MASK 대화형 로봇 시스템을 제안한다. 대규모 언어 모델 기반 페르소나 주입기와 유한 상태
    기계 행동 선택을 활용해 실시간 자율 상호작용을 가능하게 하며, 162명의 참가자를 대상으로 한 사용자 연구에서 시청자가 의도된 성격 특성과 허구 캐릭터를 인식할 수 있음을 보였다.
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
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2403.10041v2.
sources:
- id: src_001
  type: paper
  title: 'Towards Embedding Dynamic Personas in Interactive Robots: Masquerading Animated Social Kinematic (MASK)'
  url: https://arxiv.org/abs/2403.10041
  date: '2024'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
---
## 概述
This paper presents the design and development of an innovative interactive robotic system to enhance audience engagement using character-like personas. Built upon the foundations of persona-driven dialog agents, this work extends the agent's application to the physical realm, employing robots to provide a more captivating and interactive experience. The proposed system, named the Masquerading Animated Social Kinematic (MASK), leverages an anthropomorphic robot which interacts with guests using non-verbal interactions, including facial expressions and gestures. A behavior generation system based upon a finite-state machine structure effectively conditions robotic behavior to convey distinct personas. The MASK framework integrates a perception engine, a behavior selection engine, and a comprehensive action library to enable real-time, dynamic interactions with minimal human intervention in behavior design. Throughout the user subject studies, we examined whether the users could recognize the intended character in both personality- and film-character-based persona conditions. We conclude by discussing the role of personas in interactive agents and the factors to consider for creating an engaging user experience.

## 核心内容
This paper presents the design and development of an innovative interactive robotic system to enhance audience engagement using character-like personas. Built upon the foundations of persona-driven dialog agents, this work extends the agent's application to the physical realm, employing robots to provide a more captivating and interactive experience. The proposed system, named the Masquerading Animated Social Kinematic (MASK), leverages an anthropomorphic robot which interacts with guests using non-verbal interactions, including facial expressions and gestures. A behavior generation system based upon a finite-state machine structure effectively conditions robotic behavior to convey distinct personas. The MASK framework integrates a perception engine, a behavior selection engine, and a comprehensive action library to enable real-time, dynamic interactions with minimal human intervention in behavior design. Throughout the user subject studies, we examined whether the users could recognize the intended character in both personality- and film-character-based persona conditions. We conclude by discussing the role of personas in interactive agents and the factors to consider for creating an engaging user experience.

## 参考
- http://arxiv.org/abs/2403.10041v2

## Overview
This paper presents the design and development of an innovative interactive robotic system to enhance audience engagement using character-like personas. Built upon the foundations of persona-driven dialog agents, this work extends the agent's application to the physical realm, employing robots to provide a more captivating and interactive experience. The proposed system, named the Masquerading Animated Social Kinematic (MASK), leverages an anthropomorphic robot which interacts with guests using non-verbal interactions, including facial expressions and gestures. A behavior generation system based upon a finite-state machine structure effectively conditions robotic behavior to convey distinct personas. The MASK framework integrates a perception engine, a behavior selection engine, and a comprehensive action library to enable real-time, dynamic interactions with minimal human intervention in behavior design. Throughout the user subject studies, we examined whether the users could recognize the intended character in both personality- and film-character-based persona conditions. We conclude by discussing the role of personas in interactive agents and the factors to consider for creating an engaging user experience.

## Content
This paper presents the design and development of an innovative interactive robotic system to enhance audience engagement using character-like personas. Built upon the foundations of persona-driven dialog agents, this work extends the agent's application to the physical realm, employing robots to provide a more captivating and interactive experience. The proposed system, named the Masquerading Animated Social Kinematic (MASK), leverages an anthropomorphic robot which interacts with guests using non-verbal interactions, including facial expressions and gestures. A behavior generation system based upon a finite-state machine structure effectively conditions robotic behavior to convey distinct personas. The MASK framework integrates a perception engine, a behavior selection engine, and a comprehensive action library to enable real-time, dynamic interactions with minimal human intervention in behavior design. Throughout the user subject studies, we examined whether the users could recognize the intended character in both personality- and film-character-based persona conditions. We conclude by discussing the role of personas in interactive agents and the factors to consider for creating an engaging user experience.

## 개요
본 논문은 캐릭터와 같은 페르소나를 활용하여 관객의 참여를 향상시키는 혁신적인 대화형 로봇 시스템의 설계 및 개발을 제시합니다. 페르소나 기반 대화 에이전트의 기초 위에 구축된 이 연구는 에이전트의 적용을 물리적 영역으로 확장하여 로봇을 사용해 더욱 매력적이고 상호작용적인 경험을 제공합니다. 제안된 시스템인 MASK(Masquerading Animated Social Kinematic)는 인간형 로봇을 활용하여 표정과 제스처를 포함한 비언어적 상호작용으로 손님과 소통합니다. 유한 상태 기계 구조에 기반한 행동 생성 시스템은 로봇의 행동을 효과적으로 조절하여 뚜렷한 페르소나를 전달합니다. MASK 프레임워크는 인식 엔진, 행동 선택 엔진 및 포괄적인 동작 라이브러리를 통합하여 행동 설계에 최소한의 인간 개입으로 실시간 동적 상호작용을 가능하게 합니다. 사용자 주제 연구를 통해 우리는 사용자가 성격 기반 및 영화 캐릭터 기반 페르소나 조건 모두에서 의도된 캐릭터를 인식할 수 있는지 조사했습니다. 결론적으로 대화형 에이전트에서 페르소나의 역할과 매력적인 사용자 경험을 창출하기 위해 고려해야 할 요소에 대해 논의합니다.

## 핵심 내용
본 논문은 캐릭터와 같은 페르소나를 활용하여 관객의 참여를 향상시키는 혁신적인 대화형 로봇 시스템의 설계 및 개발을 제시합니다. 페르소나 기반 대화 에이전트의 기초 위에 구축된 이 연구는 에이전트의 적용을 물리적 영역으로 확장하여 로봇을 사용해 더욱 매력적이고 상호작용적인 경험을 제공합니다. 제안된 시스템인 MASK(Masquerading Animated Social Kinematic)는 인간형 로봇을 활용하여 표정과 제스처를 포함한 비언어적 상호작용으로 손님과 소통합니다. 유한 상태 기계 구조에 기반한 행동 생성 시스템은 로봇의 행동을 효과적으로 조절하여 뚜렷한 페르소나를 전달합니다. MASK 프레임워크는 인식 엔진, 행동 선택 엔진 및 포괄적인 동작 라이브러리를 통합하여 행동 설계에 최소한의 인간 개입으로 실시간 동적 상호작용을 가능하게 합니다. 사용자 주제 연구를 통해 우리는 사용자가 성격 기반 및 영화 캐릭터 기반 페르소나 조건 모두에서 의도된 캐릭터를 인식할 수 있는지 조사했습니다. 결론적으로 대화형 에이전트에서 페르소나의 역할과 매력적인 사용자 경험을 창출하기 위해 고려해야 할 요소에 대해 논의합니다.
