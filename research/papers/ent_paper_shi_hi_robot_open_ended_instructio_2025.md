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
  zh: Hi Robot 是 2025 年由 Physical Intelligence、Stanford University、University of California, Berkeley 联合提出的分层视觉-语言-动作模型，发表于
    ICML25。其核心贡献在于通过分层架构让机器人不仅能执行简单指令，还能理解复杂开放式指令并在执行中融入用户反馈，从而完成多步骤操作任务。
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2502.19417v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (830 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Hi Robot source
  url: https://openreview.net/forum?id=lNVHg9npif
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Hi Robot 系统采用分层视觉-语言模型结构，首先利用高层模型对复杂提示和用户反馈进行推理，确定完成当前任务最合适的下一步骤，再由低层模型执行具体动作。与只能处理“拿起杯子”这类简单指令的直接指令跟随方法不同，该系统能够理解“能帮我做个素食三明治吗？”或“我不喜欢那个”等复杂指令，并在任务执行过程中融入情境化反馈（如“那不是垃圾”）。研究团队在单臂、双臂和双臂移动机器人三种平台上进行了评估，展示了系统在清理杂乱桌面、制作三明治和杂货购物等任务中的能力。

## 核心内容
### 方法架构
- 采用分层视觉-语言-动作模型（Vision-Language-Action Models）结构，将任务执行分为两个层次：
  - **高层推理**：利用视觉-语言模型对复杂指令和用户反馈进行语义理解与推理，从任务步骤序列中选出当前最合适的下一步操作
  - **低层执行**：将高层选定的步骤转化为具体的机器人动作指令，完成物理操作
- 与直接指令跟随方法（仅能处理“pick up the cup”这类简单命令）形成对比，Hi Robot 能够处理包含条件判断和用户反馈的开放式指令

### 实验设置
- 在三种机器人平台上进行验证：
  - 单臂机器人
  - 双臂机器人
  - 双臂移动机器人
- 测试任务涵盖多种真实场景：
  - 清理杂乱桌面（需区分垃圾与非垃圾物品）
  - 制作三明治（需理解“素食”等复杂要求）
  - 杂货购物（需在动态环境中执行多步骤操作）

### 关键能力
- 能够理解并处理“that's not trash”这类执行过程中的情境化反馈，实时调整后续动作
- 支持开放式指令跟随，无需预设任务步骤序列
- 在多个机器人平台上均展现出泛化能力

### 结论
Hi Robot 通过分层架构有效解决了机器人对复杂指令和实时反馈的理解与执行问题，为通用型机器人在开放世界中的多步骤操作任务提供了可行方案。

## Overview
Generalist robots that can perform a range of different tasks in open-world settings must be able to not only reason about the steps needed to accomplish their goals, but also process complex instructions, prompts, and even feedback during task execution. Intricate instructions (e.g., "Could you make me a vegetarian sandwich?" or "I don't like that one") require not just the ability to physically perform the individual steps, but the ability to situate complex commands and feedback in the physical world. In this work, we describe a system that uses vision-language models in a hierarchical structure, first reasoning over complex prompts and user feedback to deduce the most appropriate next step to fulfill the task, and then performing that step with low-level actions. In contrast to direct instruction following methods that can fulfill simple commands ("pick up the cup"), our system can reason through complex prompts and incorporate situated feedback during task execution ("that's not trash"). We evaluate our system across three robotic platforms, including single-arm, dual-arm, and dual-arm mobile robots, demonstrating its ability to handle tasks such as cleaning messy tables, making sandwiches, and grocery shopping. Videos are available at https://www.pi.website/research/hirobot

## 参考
- http://arxiv.org/abs/2502.19417v2

## 개요
Hi Robot 시스템은 계층적 비전-언어 모델 구조를 채택하며, 먼저 상위 수준 모델이 복잡한 프롬프트와 사용자 피드백을 추론하여 현재 작업을 완료하는 데 가장 적합한 다음 단계를 결정하고, 하위 수준 모델이 구체적인 동작을 실행합니다. "컵 집기"와 같은 단순한 명령만 처리할 수 있는 직접 명령 추종 방식과 달리, 이 시스템은 "채식 샌드위치 만들어 줄 수 있어?" 또는 "그건 마음에 안 들어"와 같은 복잡한 명령을 이해하고, 작업 실행 중에 "그건 쓰레기가 아니야"와 같은 상황적 피드백을 통합할 수 있습니다. 연구팀은 단일 팔, 이중 팔, 이중 팔 이동 로봇의 세 가지 플랫폼에서 시스템을 평가하여 어수선한 책상 정리, 샌드위치 만들기, 식료품 쇼핑 등의 작업에서의 능력을 입증했습니다.

## 핵심 내용
### 방법 아키텍처
- 계층적 비전-언어-행동 모델(Vision-Language-Action Models) 구조를 채택하여 작업 실행을 두 수준으로 나눕니다:
  - **상위 수준 추론**: 비전-언어 모델을 활용하여 복잡한 명령과 사용자 피드백에 대한 의미론적 이해와 추론을 수행하고, 작업 단계 시퀀스에서 현재 가장 적합한 다음 작업을 선택합니다
  - **하위 수준 실행**: 상위 수준에서 선택된 단계를 구체적인 로봇 동작 명령으로 변환하여 물리적 조작을 완료합니다
- 직접 명령 추종 방식(단순한 "pick up the cup"과 같은 명령만 처리 가능)과 대조적으로, Hi Robot은 조건 판단과 사용자 피드백을 포함한 개방형 명령을 처리할 수 있습니다

### 실험 설정
- 세 가지 로봇 플랫폼에서 검증:
  - 단일 팔 로봇
  - 이중 팔 로봇
  - 이중 팔 이동 로봇
- 테스트 작업은 다양한 실제 시나리오를 포함:
  - 어수선한 책상 정리(쓰레기와 비쓰레기 물건 구분 필요)
  - 샌드위치 만들기("채식"과 같은 복잡한 요구 이해 필요)
  - 식료품 쇼핑(동적 환경에서 다단계 작업 실행 필요)

### 핵심 능력
- "that's not trash"와 같은 실행 중 상황적 피드백을 이해하고 처리하여 후속 동작을 실시간으로 조정할 수 있습니다
- 사전 정의된 작업 단계 시퀀스 없이 개방형 명령 추종을 지원합니다
- 여러 로봇 플랫폼에서 일반화 능력을 입증했습니다

### 결론
Hi Robot은 계층적 아키텍처를 통해 복잡한 명령과 실시간 피드백에 대한 로봇의 이해 및 실행 문제를 효과적으로 해결하며, 개방형 세계에서의 다단계 조작 작업을 위한 범용 로봇의 실현 가능한 솔루션을 제공합니다.
