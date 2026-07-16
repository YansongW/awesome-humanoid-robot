---
$id: ent_paper_egoactor_grounding_task_planni_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'EgoActor: Grounding Task Planning into Spatial-aware Egocentric Actions for Humanoid Robots via Visual-Language Models'
  zh: 'EgoActor: Grounding Task Planning into Spatial-aware Egocentric Actions for Humanoid Robots via Visual-Language Models'
  ko: 'EgoActor: Grounding Task Planning into Spatial-aware Egocentric Actions for Humanoid Robots via Visual-Language Models'
summary:
  en: 'EgoActor: Grounding Task Planning into Spatial-aware Egocentric Actions for Humanoid Robots via Visual-Language Models
    is a 2026 work on navigation for humanoid robots.'
  zh: 'EgoActor: Grounding Task Planning into Spatial-aware Egocentric Actions for Humanoid Robots via Visual-Language Models
    is a 2026 work on navigation for humanoid robots.'
  ko: 'EgoActor: Grounding Task Planning into Spatial-aware Egocentric Actions for Humanoid Robots via Visual-Language Models
    is a 2026 work on navigation for humanoid robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- egoactor
- humanoid
- navigation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.04515v1.
sources:
- id: src_001
  type: paper
  title: 'EgoActor: Grounding Task Planning into Spatial-aware Egocentric Actions for Humanoid Robots via Visual-Language
    Models (arXiv)'
  url: https://arxiv.org/abs/2602.04515
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Deploying humanoid robots in real-world settings is fundamentally challenging, as it demands tight integration of perception, locomotion, and manipulation under partial-information observations and dynamically changing environments. As well as transitioning robustly between sub-tasks of different types. Towards addressing these challenges, we propose a novel task - EgoActing, which requires directly grounding high-level instructions into various, precise, spatially aware humanoid actions. We further instantiate this task by introducing EgoActor, a unified and scalable vision-language model (VLM) that can predict locomotion primitives (e.g., walk, turn, move sideways, change height), head movements, manipulation commands, and human-robot interactions to coordinate perception and execution in real-time. We leverage broad supervision over egocentric RGB-only data from real-world demonstrations, spatial reasoning question-answering, and simulated environment demonstrations, enabling EgoActor to make robust, context-aware decisions and perform fluent action inference (under 1s) with both 8B and 4B parameter models. Extensive evaluations in both simulated and real-world environments demonstrate that EgoActor effectively bridges abstract task planning and concrete motor execution, while generalizing across diverse tasks and unseen environments.

## 核心内容
Deploying humanoid robots in real-world settings is fundamentally challenging, as it demands tight integration of perception, locomotion, and manipulation under partial-information observations and dynamically changing environments. As well as transitioning robustly between sub-tasks of different types. Towards addressing these challenges, we propose a novel task - EgoActing, which requires directly grounding high-level instructions into various, precise, spatially aware humanoid actions. We further instantiate this task by introducing EgoActor, a unified and scalable vision-language model (VLM) that can predict locomotion primitives (e.g., walk, turn, move sideways, change height), head movements, manipulation commands, and human-robot interactions to coordinate perception and execution in real-time. We leverage broad supervision over egocentric RGB-only data from real-world demonstrations, spatial reasoning question-answering, and simulated environment demonstrations, enabling EgoActor to make robust, context-aware decisions and perform fluent action inference (under 1s) with both 8B and 4B parameter models. Extensive evaluations in both simulated and real-world environments demonstrate that EgoActor effectively bridges abstract task planning and concrete motor execution, while generalizing across diverse tasks and unseen environments.

## 参考
- http://arxiv.org/abs/2602.04515v1

## Overview
Deploying humanoid robots in real-world settings is fundamentally challenging, as it demands tight integration of perception, locomotion, and manipulation under partial-information observations and dynamically changing environments, as well as transitioning robustly between sub-tasks of different types. Towards addressing these challenges, we propose a novel task - EgoActing, which requires directly grounding high-level instructions into various, precise, spatially aware humanoid actions. We further instantiate this task by introducing EgoActor, a unified and scalable vision-language model (VLM) that can predict locomotion primitives (e.g., walk, turn, move sideways, change height), head movements, manipulation commands, and human-robot interactions to coordinate perception and execution in real-time. We leverage broad supervision over egocentric RGB-only data from real-world demonstrations, spatial reasoning question-answering, and simulated environment demonstrations, enabling EgoActor to make robust, context-aware decisions and perform fluent action inference (under 1s) with both 8B and 4B parameter models. Extensive evaluations in both simulated and real-world environments demonstrate that EgoActor effectively bridges abstract task planning and concrete motor execution, while generalizing across diverse tasks and unseen environments.

## Content
Deploying humanoid robots in real-world settings is fundamentally challenging, as it demands tight integration of perception, locomotion, and manipulation under partial-information observations and dynamically changing environments, as well as transitioning robustly between sub-tasks of different types. Towards addressing these challenges, we propose a novel task - EgoActing, which requires directly grounding high-level instructions into various, precise, spatially aware humanoid actions. We further instantiate this task by introducing EgoActor, a unified and scalable vision-language model (VLM) that can predict locomotion primitives (e.g., walk, turn, move sideways, change height), head movements, manipulation commands, and human-robot interactions to coordinate perception and execution in real-time. We leverage broad supervision over egocentric RGB-only data from real-world demonstrations, spatial reasoning question-answering, and simulated environment demonstrations, enabling EgoActor to make robust, context-aware decisions and perform fluent action inference (under 1s) with both 8B and 4B parameter models. Extensive evaluations in both simulated and real-world environments demonstrate that EgoActor effectively bridges abstract task planning and concrete motor execution, while generalizing across diverse tasks and unseen environments.

## 개요
휴머노이드 로봇을 실제 환경에 배치하는 것은 근본적으로 어려운 과제입니다. 부분 정보 관측과 동적으로 변화하는 환경 속에서 인식, 보행, 조작의 긴밀한 통합이 요구되기 때문입니다. 또한 서로 다른 유형의 하위 작업 간 강건한 전환도 필요합니다. 이러한 과제를 해결하기 위해, 우리는 새로운 작업인 **EgoActing**을 제안합니다. 이 작업은 고수준 명령을 다양하고 정밀하며 공간 인식이 가능한 휴머노이드 동작에 직접적으로 기반하는 것을 요구합니다. 또한, 이 작업을 구체화하기 위해 **EgoActor**를 소개합니다. EgoActor는 통합적이고 확장 가능한 비전-언어 모델(VLM)로, 보행 기본 동작(예: 걷기, 회전, 측면 이동, 높이 변경), 머리 움직임, 조작 명령, 인간-로봇 상호작용을 예측하여 인식과 실행을 실시간으로 조정합니다. 우리는 실제 세계 시연에서 얻은 자아 중심 RGB 전용 데이터, 공간 추론 질의응답, 시뮬레이션 환경 시연에 대한 광범위한 감독을 활용하여, EgoActor가 강건하고 상황 인식적인 결정을 내리고 8B 및 4B 파라미터 모델로 유창한 동작 추론(1초 미만)을 수행할 수 있도록 합니다. 시뮬레이션 및 실제 환경에서의 광범위한 평가는 EgoActor가 추상적 작업 계획과 구체적 모터 실행을 효과적으로 연결하며, 다양한 작업과 보지 못한 환경에서 일반화됨을 보여줍니다.

## 핵심 내용
휴머노이드 로봇을 실제 환경에 배치하는 것은 근본적으로 어려운 과제입니다. 부분 정보 관측과 동적으로 변화하는 환경 속에서 인식, 보행, 조작의 긴밀한 통합이 요구되기 때문입니다. 또한 서로 다른 유형의 하위 작업 간 강건한 전환도 필요합니다. 이러한 과제를 해결하기 위해, 우리는 새로운 작업인 **EgoActing**을 제안합니다. 이 작업은 고수준 명령을 다양하고 정밀하며 공간 인식이 가능한 휴머노이드 동작에 직접적으로 기반하는 것을 요구합니다. 또한, 이 작업을 구체화하기 위해 **EgoActor**를 소개합니다. EgoActor는 통합적이고 확장 가능한 비전-언어 모델(VLM)로, 보행 기본 동작(예: 걷기, 회전, 측면 이동, 높이 변경), 머리 움직임, 조작 명령, 인간-로봇 상호작용을 예측하여 인식과 실행을 실시간으로 조정합니다. 우리는 실제 세계 시연에서 얻은 자아 중심 RGB 전용 데이터, 공간 추론 질의응답, 시뮬레이션 환경 시연에 대한 광범위한 감독을 활용하여, EgoActor가 강건하고 상황 인식적인 결정을 내리고 8B 및 4B 파라미터 모델로 유창한 동작 추론(1초 미만)을 수행할 수 있도록 합니다. 시뮬레이션 및 실제 환경에서의 광범위한 평가는 EgoActor가 추상적 작업 계획과 구체적 모터 실행을 효과적으로 연결하며, 다양한 작업과 보지 못한 환경에서 일반화됨을 보여줍니다.
