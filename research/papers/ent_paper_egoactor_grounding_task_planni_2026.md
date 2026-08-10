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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.04515v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (958 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2602.04515v1

## 개요
EgoActor는 휴머노이드 로봇이 실제 세계에 배치될 때 직면하는 인식, 운동, 조작의 긴밀한 결합 문제를 해결하기 위해 EgoActing 작업을 제안합니다. 이 작업은 모델이 높은 수준의 지시를 다양한 정밀하고 공간 인식이 가능한 자아 중심 동작으로 직접 매핑하도록 요구합니다. 이를 위해 저자는 EgoActor 모델을 구축했으며, 이는 걷기, 회전, 측면 이동, 높이 변화와 같은 운동 기본 요소와 머리 움직임, 조작 지시, 인간-로봇 상호작용을 동시에 예측할 수 있는 통합적이고 확장 가능한 비전-언어 모델입니다. 모델은 실제 세계 시연의 자아 중심 RGB 데이터, 공간 추론 질의응답, 시뮬레이션 환경 시연을 통해 광범위하게 지도 학습되어 강력한 상황 인식 의사 결정과 원활한 동작 추론(추론 시간 1초 미만)을 구현합니다. 실험은 시뮬레이션 및 실제 환경 모두에서 그 효과를 검증했습니다.

## 핵심 내용
### 방법 개요
EgoActor의 핵심은 부분 관측 및 동적 환경에서 휴머노이드 로봇의 작업 계획 및 실행 문제를 해결하기 위한 통합 비전-언어 모델(VLM)입니다. 모델은 높은 수준의 지시를 일련의 공간 인식 자아 중심 동작, 즉 EgoActing 작업으로 직접 "구체화"합니다.

### 아키텍처 및 입력
- **입력**: 모델은 자아 중심 시점의 RGB 이미지만을 시각적 입력으로 사용합니다.
- **출력**: 모델은 여러 동작 기본 요소를 예측합니다:
  - **운동 기본 요소**: 걷기, 회전, 측면 이동, 높이 변경.
  - **머리 움직임**: 인식 조정에 사용.
  - **조작 지시**: 물체 조작에 사용.
  - **인간-로봇 상호작용 지시**: 인간과의 협업에 사용.
- **추론 속도**: 8B 및 4B 매개변수 규모의 모델에서 모두 1초 미만의 원활한 동작 추론을 달성합니다.

### 훈련 데이터 및 지도
EgoActor는 세 가지 데이터 소스를 통해 광범위한 지도 학습을 수행합니다:
1.  **실제 세계 시연**: 실제 환경에서의 동작 패턴을 학습하기 위해 자아 중심 RGB 데이터를 수집합니다.
2.  **공간 추론 질의응답**: 질의응답 형식을 통해 모델의 공간 인식 능력을 강화합니다.
3.  **시뮬레이션 환경 시연**: 시뮬레이터에서 대량의 시연 데이터를 생성하여 모델의 일반화 능력을 향상시킵니다.

### 실험 설정 및 결과
- **평가 환경**: 시뮬레이션 환경과 실제 세계 환경 모두에서 광범위하게 평가되었습니다.
- **핵심 결론**:
  - EgoActor는 추상적인 작업 계획과 구체적인 운동 실행을 효과적으로 연결할 수 있습니다.
  - 모델은 다양한 작업과 보지 못한 환경에 적응할 수 있는 우수한 일반화 능력을 보여줍니다.
  - 여러 동작 유형(운동, 머리, 조작, 상호작용)을 통합적으로 예측하여 인식과 실행의 실시간 조정을 구현합니다.
