---
$id: ent_paper_shi_hi_robot_open_ended_instructio_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Hi Robot: Open-Ended Instruction Following with Hierarchical Vision-Language-Action Models'
  zh: Hi Robot
  ko: 'Hi Robot: Open-Ended Instruction Following with Hierarchical Vision-Language-Action Models'
summary:
  en: 'Hi Robot: Open-Ended Instruction Following with Hierarchical Vision-Language-Action Models (Hi Robot), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Physical Intelligence, Stanford University, University
    of California, Berkeley, and published at ICML25.'
  zh: 'Hi Robot: Open-Ended Instruction Following with Hierarchical Vision-Language-Action Models (Hi Robot), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Physical Intelligence, Stanford University, University
    of California, Berkeley, and published at ICML25.'
  ko: 'Hi Robot: Open-Ended Instruction Following with Hierarchical Vision-Language-Action Models (Hi Robot), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Physical Intelligence, Stanford University, University
    of California, Berkeley, and published at ICML25.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- hi_robot
- large_vla_model
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2502.19417v2.
sources:
- id: src_001
  type: paper
  title: Hi Robot source
  url: https://openreview.net/forum?id=lNVHg9npif
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Generalist robots that can perform a range of different tasks in open-world settings must be able to not only reason about the steps needed to accomplish their goals, but also process complex instructions, prompts, and even feedback during task execution. Intricate instructions (e.g., "Could you make me a vegetarian sandwich?" or "I don't like that one") require not just the ability to physically perform the individual steps, but the ability to situate complex commands and feedback in the physical world. In this work, we describe a system that uses vision-language models in a hierarchical structure, first reasoning over complex prompts and user feedback to deduce the most appropriate next step to fulfill the task, and then performing that step with low-level actions. In contrast to direct instruction following methods that can fulfill simple commands ("pick up the cup"), our system can reason through complex prompts and incorporate situated feedback during task execution ("that's not trash"). We evaluate our system across three robotic platforms, including single-arm, dual-arm, and dual-arm mobile robots, demonstrating its ability to handle tasks such as cleaning messy tables, making sandwiches, and grocery shopping. Videos are available at https://www.pi.website/research/hirobot

## 核心内容
Generalist robots that can perform a range of different tasks in open-world settings must be able to not only reason about the steps needed to accomplish their goals, but also process complex instructions, prompts, and even feedback during task execution. Intricate instructions (e.g., "Could you make me a vegetarian sandwich?" or "I don't like that one") require not just the ability to physically perform the individual steps, but the ability to situate complex commands and feedback in the physical world. In this work, we describe a system that uses vision-language models in a hierarchical structure, first reasoning over complex prompts and user feedback to deduce the most appropriate next step to fulfill the task, and then performing that step with low-level actions. In contrast to direct instruction following methods that can fulfill simple commands ("pick up the cup"), our system can reason through complex prompts and incorporate situated feedback during task execution ("that's not trash"). We evaluate our system across three robotic platforms, including single-arm, dual-arm, and dual-arm mobile robots, demonstrating its ability to handle tasks such as cleaning messy tables, making sandwiches, and grocery shopping. Videos are available at https://www.pi.website/research/hirobot

## 参考
- http://arxiv.org/abs/2502.19417v2

## Overview
Generalist robots that can perform a range of different tasks in open-world settings must be able to not only reason about the steps needed to accomplish their goals, but also process complex instructions, prompts, and even feedback during task execution. Intricate instructions (e.g., "Could you make me a vegetarian sandwich?" or "I don't like that one") require not just the ability to physically perform the individual steps, but the ability to situate complex commands and feedback in the physical world. In this work, we describe a system that uses vision-language models in a hierarchical structure, first reasoning over complex prompts and user feedback to deduce the most appropriate next step to fulfill the task, and then performing that step with low-level actions. In contrast to direct instruction following methods that can fulfill simple commands ("pick up the cup"), our system can reason through complex prompts and incorporate situated feedback during task execution ("that's not trash"). We evaluate our system across three robotic platforms, including single-arm, dual-arm, and dual-arm mobile robots, demonstrating its ability to handle tasks such as cleaning messy tables, making sandwiches, and grocery shopping. Videos are available at https://www.pi.website/research/hirobot

## Content
Generalist robots that can perform a range of different tasks in open-world settings must be able to not only reason about the steps needed to accomplish their goals, but also process complex instructions, prompts, and even feedback during task execution. Intricate instructions (e.g., "Could you make me a vegetarian sandwich?" or "I don't like that one") require not just the ability to physically perform the individual steps, but the ability to situate complex commands and feedback in the physical world. In this work, we describe a system that uses vision-language models in a hierarchical structure, first reasoning over complex prompts and user feedback to deduce the most appropriate next step to fulfill the task, and then performing that step with low-level actions. In contrast to direct instruction following methods that can fulfill simple commands ("pick up the cup"), our system can reason through complex prompts and incorporate situated feedback during task execution ("that's not trash"). We evaluate our system across three robotic platforms, including single-arm, dual-arm, and dual-arm mobile robots, demonstrating its ability to handle tasks such as cleaning messy tables, making sandwiches, and grocery shopping. Videos are available at https://www.pi.website/research/hirobot

## 개요
개방형 환경에서 다양한 작업을 수행할 수 있는 제너럴리스트 로봇은 목표 달성에 필요한 단계를 추론할 수 있을 뿐만 아니라, 작업 실행 중 복잡한 지시, 프롬프트, 심지어 피드백까지 처리할 수 있어야 합니다. 복잡한 지시(예: "채식 샌드위치를 만들어 줄래요?" 또는 "그건 마음에 안 들어요")는 개별 단계를 물리적으로 수행하는 능력뿐만 아니라, 복잡한 명령과 피드백을 물리적 세계에 적절히 배치하는 능력을 요구합니다. 본 연구에서는 계층적 구조로 비전-언어 모델을 사용하는 시스템을 설명합니다. 이 시스템은 먼저 복잡한 프롬프트와 사용자 피드백을 추론하여 작업을 완료하기 위한 가장 적절한 다음 단계를 도출한 후, 저수준 동작으로 해당 단계를 수행합니다. 간단한 명령("컵을 집어 들어")을 수행할 수 있는 직접적인 지시 수행 방법과 달리, 우리 시스템은 복잡한 프롬프트를 추론하고 작업 실행 중 상황에 맞는 피드백("그건 쓰레기가 아니에요")을 통합할 수 있습니다. 우리는 단일 암, 이중 암, 이중 암 모바일 로봇을 포함한 세 가지 로봇 플랫폼에서 시스템을 평가하여, 지저분한 테이블 청소, 샌드위치 만들기, 식료품 쇼핑과 같은 작업을 처리하는 능력을 입증했습니다. 비디오는 https://www.pi.website/research/hirobot 에서 확인할 수 있습니다.

## 핵심 내용
개방형 환경에서 다양한 작업을 수행할 수 있는 제너럴리스트 로봇은 목표 달성에 필요한 단계를 추론할 수 있을 뿐만 아니라, 작업 실행 중 복잡한 지시, 프롬프트, 심지어 피드백까지 처리할 수 있어야 합니다. 복잡한 지시(예: "채식 샌드위치를 만들어 줄래요?" 또는 "그건 마음에 안 들어요")는 개별 단계를 물리적으로 수행하는 능력뿐만 아니라, 복잡한 명령과 피드백을 물리적 세계에 적절히 배치하는 능력을 요구합니다. 본 연구에서는 계층적 구조로 비전-언어 모델을 사용하는 시스템을 설명합니다. 이 시스템은 먼저 복잡한 프롬프트와 사용자 피드백을 추론하여 작업을 완료하기 위한 가장 적절한 다음 단계를 도출한 후, 저수준 동작으로 해당 단계를 수행합니다. 간단한 명령("컵을 집어 들어")을 수행할 수 있는 직접적인 지시 수행 방법과 달리, 우리 시스템은 복잡한 프롬프트를 추론하고 작업 실행 중 상황에 맞는 피드백("그건 쓰레기가 아니에요")을 통합할 수 있습니다. 우리는 단일 암, 이중 암, 이중 암 모바일 로봇을 포함한 세 가지 로봇 플랫폼에서 시스템을 평가하여, 지저분한 테이블 청소, 샌드위치 만들기, 식료품 쇼핑과 같은 작업을 처리하는 능력을 입증했습니다. 비디오는 https://www.pi.website/research/hirobot 에서 확인할 수 있습니다.
