---
$id: ent_paper_walker_desiderata_for_planning_system_2019
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Desiderata for Planning Systems in General-Purpose Service Robots
  zh: 通用服务机器人规划系统的期望特性
  ko: 범용 서비스 로봇 계획 시스템을 위한 요구사항
summary:
  en: Proposes desiderata for planning and reasoning systems to support general-purpose service robots operating in homes
    and offices, emphasizing natural human interfaces and robust fallback methods.
  zh: 本文提出面向通用服务机器人的规划与推理系统设计准则，基于办公室与家庭环境的研究经验，强调支持自然的人机交互界面以及在交互失败时的稳健回退方法，旨在推动该领域形成统一视角。
  ko: 가정과 사무실에서 동작하는 범용 서비스 로봇을 지원하기 위한 계획 및 추론 시스템의 요구사항을 제안하며, 자연스러운 인간-로봇 상호작용과 강건한 폴백 방법을 강조한다.
domains:
- 07_ai_models_algorithms
- 11_applications_markets
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- service_robot_planning
- task_planning
- human_robot_interaction
- fallback_strategies
- knowledge_representation
- general_purpose_robotics
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1907.02300v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (526 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Desiderata for Planning Systems in General-Purpose Service Robots
  url: https://arxiv.org/abs/1907.02300
  date: '2019'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
---
## 概述
通用服务机器人需执行用户请求的广泛任务，但当前知识表示与规划系统缺乏统一的功能需求标准。本文作为立场论文，从办公室与家庭环境的研究经验出发，提出一套规划与推理系统的设计准则，重点涵盖自然的人机交互支持以及当人类或环境交互失败时的稳健回退机制，并梳理了相关已有工作。

## 核心内容
### 背景与动机
通用服务机器人需灵活应对家庭与办公室中的多样化任务，但现有规划与推理系统因对用户、环境及机器人系统的假设不同而进展受阻。本文旨在通过提出设计准则，促进该领域的统一发展。

### 核心设计准则
- **自然交互支持**：强调系统需能理解并响应自然语言指令，降低用户使用门槛。
- **稳健回退方法**：当与人类或环境的交互失败时（如指令模糊、传感器噪声），系统应具备自动降级或替代方案，确保任务不中断。
- **环境适应性**：基于办公室与家庭环境的实际需求（如动态障碍物、非结构化布局），系统需支持实时重规划与知识更新。

### 相关工作与结论
本文梳理了已有研究中对上述准则的探索，指出当前系统在交互鲁棒性与环境泛化性上的不足。作者认为，统一的设计准则将加速通用服务机器人的实用化进程，并呼吁社区关注自然交互与故障恢复的协同设计。

## Overview
General-purpose service robots are expected to undertake a broad range of tasks at the request of users. Knowledge representation and planning systems are essential to flexible autonomous robots, but the field lacks a unified perspective on which features are essential for general-purpose service robots. Progress towards planning and reasoning for general-purpose service robots is hindered by differing assumptions about users, the environment, and the overall robot system. In this position paper, we propose desiderata for planning and reasoning systems to promote general-purpose service robots. Each proposed item draws on our experience with research on service robots in the office and home and on the demands of these environments. Our desiderata emphasize support for natural human-interfaces as well as for robust fallback methods when interactions with humans and the environment fail. We highlight relevant work towards these goals.

## 参考
- http://arxiv.org/abs/1907.02300v1

## 개요
범용 서비스 로봇은 사용자가 요청하는 광범위한 작업을 수행해야 하지만, 현재 지식 표현 및 계획 시스템은 통일된 기능 요구사항 표준이 부족합니다. 본 논문은 입장 논문으로서, 사무실 및 가정 환경에서의 연구 경험을 바탕으로 계획 및 추론 시스템을 위한 설계 지침을 제안하며, 자연스러운 인간-로봇 상호작용 지원과 인간 또는 환경과의 상호작용 실패 시 강건한 복구 메커니즘을 중점적으로 다루고, 관련 기존 연구를 정리합니다.

## 핵심 내용
### 배경 및 동기
범용 서비스 로봇은 가정과 사무실에서의 다양한 작업에 유연하게 대응해야 하지만, 기존 계획 및 추론 시스템은 사용자, 환경 및 로봇 시스템에 대한 가정이 달라 발전이 저해되고 있습니다. 본 논문은 설계 지침을 제안함으로써 해당 분야의 통일된 발전을 촉진하는 것을 목표로 합니다.

### 핵심 설계 지침
- **자연스러운 상호작용 지원**: 시스템이 자연어 명령을 이해하고 응답할 수 있어야 하며, 사용자 사용 장벽을 낮추는 것을 강조합니다.
- **강건한 복구 방법**: 인간 또는 환경과의 상호작용이 실패할 때(예: 명령의 모호성, 센서 노이즈), 시스템은 자동으로 성능을 저하시키거나 대체 방안을 제공하여 작업이 중단되지 않도록 해야 합니다.
- **환경 적응성**: 사무실 및 가정 환경의 실제 요구사항(예: 동적 장애물, 비구조화된 배치)을 기반으로, 시스템은 실시간 재계획 및 지식 업데이트를 지원해야 합니다.

### 관련 연구 및 결론
본 논문은 기존 연구에서 위 지침에 대한 탐구를 정리하고, 현재 시스템이 상호작용 강건성과 환경 일반화 측면에서 부족함을 지적합니다. 저자는 통일된 설계 지침이 범용 서비스 로봇의 실용화를 가속화할 것이라고 주장하며, 자연스러운 상호작용과 오류 복구의 협력적 설계에 대한 커뮤니티의 관심을 촉구합니다.
