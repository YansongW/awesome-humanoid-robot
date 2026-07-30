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
  zh: EgoActor 是 2026 年提出的一项面向人形机器人的新任务与模型。它通过视觉-语言模型（VLM）将高层指令直接转化为空间感知的自我中心动作，并能在 1 秒内完成推理。核心贡献在于统一了运动基元、头部运动、操控指令与人机交互的预测，实现了从抽象任务规划到具体运动执行的桥梁。
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.04515v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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
EgoActor 针对人形机器人在真实世界中部署时面临的感知、运动与操控紧密耦合的挑战，提出了 EgoActing 任务。该任务要求模型将高层指令直接映射为多种精确且具有空间意识的自我中心动作。为此，作者构建了 EgoActor 模型，这是一个统一的、可扩展的视觉-语言模型，能够同时预测行走、转身、侧移、高度变化等运动基元，以及头部运动、操控指令和人机交互。模型通过真实世界演示的自我中心 RGB 数据、空间推理问答和模拟环境演示进行广泛监督训练，实现了鲁棒的上下文感知决策和流畅的动作推理（推理时间低于 1 秒）。实验在模拟和真实环境中均验证了其有效性。

## 核心内容
### 方法概述
EgoActor 的核心是一个统一的视觉-语言模型（VLM），旨在解决人形机器人在部分观测和动态环境下的任务规划与执行问题。模型将高层指令直接“落地”为一系列空间感知的自我中心动作，即 EgoActing 任务。

### 架构与输入
- **输入**：模型仅依赖自我中心视角的 RGB 图像作为视觉输入。
- **输出**：模型预测多种动作基元，包括：
  - **运动基元**：行走、转身、侧移、改变高度。
  - **头部运动**：用于协调感知。
  - **操控指令**：用于物体操作。
  - **人机交互指令**：用于与人类协作。
- **推理速度**：在 8B 和 4B 参数规模的模型上，均能实现低于 1 秒的流畅动作推理。

### 训练数据与监督
EgoActor 通过三种数据源进行广泛监督训练：
1.  **真实世界演示**：采集自我中心 RGB 数据，用于学习真实环境中的动作模式。
2.  **空间推理问答**：通过问答形式增强模型的空间感知能力。
3.  **模拟环境演示**：在模拟器中生成大量演示数据，提升模型的泛化能力。

### 实验设置与结果
- **评估环境**：在模拟环境和真实世界环境中均进行了广泛评估。
- **关键结论**：
  - EgoActor 能够有效连接抽象的任务规划与具体的运动执行。
  - 模型展现出良好的泛化能力，能够适应多样化的任务和未见过的环境。
  - 通过统一预测多种动作类型（运动、头部、操控、交互），实现了感知与执行的实时协调。

## Overview
Deploying humanoid robots in real-world settings is fundamentally challenging, as it demands tight integration of perception, locomotion, and manipulation under partial-information observations and dynamically changing environments. As well as transitioning robustly between sub-tasks of different types. Towards addressing these challenges, we propose a novel task - EgoActing, which requires directly grounding high-level instructions into various, precise, spatially aware humanoid actions. We further instantiate this task by introducing EgoActor, a unified and scalable vision-language model (VLM) that can predict locomotion primitives (e.g., walk, turn, move sideways, change height), head movements, manipulation commands, and human-robot interactions to coordinate perception and execution in real-time. We leverage broad supervision over egocentric RGB-only data from real-world demonstrations, spatial reasoning question-answering, and simulated environment demonstrations, enabling EgoActor to make robust, context-aware decisions and perform fluent action inference (under 1s) with both 8B and 4B parameter models. Extensive evaluations in both simulated and real-world environments demonstrate that EgoActor effectively bridges abstract task planning and concrete motor execution, while generalizing across diverse tasks and unseen environments.

## Overview
Deploying humanoid robots in real-world settings is fundamentally challenging, as it demands tight integration of perception, locomotion, and manipulation under partial-information observations and dynamically changing environments, as well as transitioning robustly between sub-tasks of different types. Towards addressing these challenges, we propose a novel task - EgoActing, which requires directly grounding high-level instructions into various, precise, spatially aware humanoid actions. We further instantiate this task by introducing EgoActor, a unified and scalable vision-language model (VLM) that can predict locomotion primitives (e.g., walk, turn, move sideways, change height), head movements, manipulation commands, and human-robot interactions to coordinate perception and execution in real-time. We leverage broad supervision over egocentric RGB-only data from real-world demonstrations, spatial reasoning question-answering, and simulated environment demonstrations, enabling EgoActor to make robust, context-aware decisions and perform fluent action inference (under 1s) with both 8B and 4B parameter models. Extensive evaluations in both simulated and real-world environments demonstrate that EgoActor effectively bridges abstract task planning and concrete motor execution, while generalizing across diverse tasks and unseen environments.

## Content
Deploying humanoid robots in real-world settings is fundamentally challenging, as it demands tight integration of perception, locomotion, and manipulation under partial-information observations and dynamically changing environments, as well as transitioning robustly between sub-tasks of different types. Towards addressing these challenges, we propose a novel task - EgoActing, which requires directly grounding high-level instructions into various, precise, spatially aware humanoid actions. We further instantiate this task by introducing EgoActor, a unified and scalable vision-language model (VLM) that can predict locomotion primitives (e.g., walk, turn, move sideways, change height), head movements, manipulation commands, and human-robot interactions to coordinate perception and execution in real-time. We leverage broad supervision over egocentric RGB-only data from real-world demonstrations, spatial reasoning question-answering, and simulated environment demonstrations, enabling EgoActor to make robust, context-aware decisions and perform fluent action inference (under 1s) with both 8B and 4B parameter models. Extensive evaluations in both simulated and real-world environments demonstrate that EgoActor effectively bridges abstract task planning and concrete motor execution, while generalizing across diverse tasks and unseen environments.

## 개요
휴머노이드 로봇을 실제 환경에 배치하는 것은 근본적으로 어려운 과제입니다. 부분 정보 관측과 동적으로 변화하는 환경 속에서 인식, 보행, 조작의 긴밀한 통합이 요구되기 때문입니다. 또한 서로 다른 유형의 하위 작업 간 강건한 전환도 필요합니다. 이러한 과제를 해결하기 위해, 우리는 새로운 작업인 **EgoActing**을 제안합니다. 이 작업은 고수준 명령을 다양하고 정밀하며 공간 인식이 가능한 휴머노이드 동작에 직접적으로 기반하는 것을 요구합니다. 또한, 이 작업을 구체화하기 위해 **EgoActor**를 소개합니다. EgoActor는 통합적이고 확장 가능한 비전-언어 모델(VLM)로, 보행 기본 동작(예: 걷기, 회전, 측면 이동, 높이 변경), 머리 움직임, 조작 명령, 인간-로봇 상호작용을 예측하여 인식과 실행을 실시간으로 조정합니다. 우리는 실제 세계 시연에서 얻은 자아 중심 RGB 전용 데이터, 공간 추론 질의응답, 시뮬레이션 환경 시연에 대한 광범위한 감독을 활용하여, EgoActor가 강건하고 상황 인식적인 결정을 내리고 8B 및 4B 파라미터 모델로 유창한 동작 추론(1초 미만)을 수행할 수 있도록 합니다. 시뮬레이션 및 실제 환경에서의 광범위한 평가는 EgoActor가 추상적 작업 계획과 구체적 모터 실행을 효과적으로 연결하며, 다양한 작업과 보지 못한 환경에서 일반화됨을 보여줍니다.

## 핵심 내용
휴머노이드 로봇을 실제 환경에 배치하는 것은 근본적으로 어려운 과제입니다. 부분 정보 관측과 동적으로 변화하는 환경 속에서 인식, 보행, 조작의 긴밀한 통합이 요구되기 때문입니다. 또한 서로 다른 유형의 하위 작업 간 강건한 전환도 필요합니다. 이러한 과제를 해결하기 위해, 우리는 새로운 작업인 **EgoActing**을 제안합니다. 이 작업은 고수준 명령을 다양하고 정밀하며 공간 인식이 가능한 휴머노이드 동작에 직접적으로 기반하는 것을 요구합니다. 또한, 이 작업을 구체화하기 위해 **EgoActor**를 소개합니다. EgoActor는 통합적이고 확장 가능한 비전-언어 모델(VLM)로, 보행 기본 동작(예: 걷기, 회전, 측면 이동, 높이 변경), 머리 움직임, 조작 명령, 인간-로봇 상호작용을 예측하여 인식과 실행을 실시간으로 조정합니다. 우리는 실제 세계 시연에서 얻은 자아 중심 RGB 전용 데이터, 공간 추론 질의응답, 시뮬레이션 환경 시연에 대한 광범위한 감독을 활용하여, EgoActor가 강건하고 상황 인식적인 결정을 내리고 8B 및 4B 파라미터 모델로 유창한 동작 추론(1초 미만)을 수행할 수 있도록 합니다. 시뮬레이션 및 실제 환경에서의 광범위한 평가는 EgoActor가 추상적 작업 계획과 구체적 모터 실행을 효과적으로 연결하며, 다양한 작업과 보지 못한 환경에서 일반화됨을 보여줍니다.

## 参考
- http://arxiv.org/abs/2602.04515v1
