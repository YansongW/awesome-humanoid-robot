---
$id: ent_paper_grutopia_dream_general_robots_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'GRUtopia: Dream General Robots in a City at Scale'
  zh: 'GRUtopia: Dream General Robots in a City at Scale'
  ko: 'GRUtopia: Dream General Robots in a City at Scale'
summary:
  en: 'GRUtopia: Dream General Robots in a City at Scale is a 2024 work on simulation benchmark for humanoid robots.'
  zh: GRUtopia 是 2024 年提出的首个面向多种机器人的大规模交互式 3D 社会仿真基准。该项目由 OpenRobotLab 开发，核心贡献包括包含 10 万精细标注场景的 GRScenes 数据集、由大语言模型驱动的 NPC
    系统 GRResidents，以及针对腿足机器人的 GRBench 基准，旨在推动具身智能的 Sim2Real 研究。
  ko: 'GRUtopia: Dream General Robots in a City at Scale is a 2024 work on simulation benchmark for humanoid robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
- 10_evaluation_benchmarks
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- benchmark
- grutopia
- humanoid
- simulation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2407.10943v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (781 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'GRUtopia: Dream General Robots in a City at Scale (arXiv)'
  url: https://arxiv.org/abs/2407.10943
  date: '2024'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'GRUtopia: Dream General Robots in a City at Scale project page'
  url: https://github.com/OpenRobotLab/GRUtopia
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
GRUtopia 项目通过构建城市级仿真环境，解决了具身 AI 领域真实数据采集成本高昂的问题。其场景数据集 GRScenes 覆盖 89 种不同类别，远超以往仅聚焦家庭场景的工作，为通用机器人部署提供了更贴近服务场景的测试环境。项目还设计了由 LLM 驱动的 NPC 系统 GRResidents，负责社交互动与任务生成，并推出了包含物体定位导航、社交定位导航和定位操作三类任务的 GRBench 基准，重点评估腿足机器人的综合能力。

## 核心内容
### 项目背景与目标
GRUtopia 旨在通过 Sim2Real 范式降低具身模型学习成本，解决真实数据采集的高昂代价问题。项目构建了首个面向多种机器人的交互式 3D 社会仿真平台。

### 核心组件
- **GRScenes 数据集**：包含 10 万个精细标注的交互式场景，可自由组合成城市级环境。与以往仅覆盖家庭场景的工作不同，GRScenes 涵盖 89 种场景类别，填补了服务导向环境的空白。
- **GRResidents NPC 系统**：基于大语言模型驱动，负责社交互动、任务生成与分配，模拟具身 AI 应用所需的社会场景。
- **GRBench 基准**：支持多种机器人，但以腿足机器人为主要智能体。包含三类中等难度任务：
  - Object Loco-Navigation（物体定位导航）
  - Social Loco-Navigation（社交定位导航）
  - Loco-Manipulation（定位操作）

### 实验设置与结论
项目通过 GRBench 对腿足机器人在城市级环境中的导航与操作能力进行综合评估。实验表明，GRUtopia 能够有效缓解具身 AI 领域高质量数据稀缺的问题，并为研究提供更全面的评估框架。项目代码已开源在 GitHub。

## Overview
Recent works have been exploring the scaling laws in the field of Embodied AI. Given the prohibitive costs of collecting real-world data, we believe the Simulation-to-Real (Sim2Real) paradigm is a crucial step for scaling the learning of embodied models. This paper introduces project GRUtopia, the first simulated interactive 3D society designed for various robots. It features several advancements: (a) The scene dataset, GRScenes, includes 100k interactive, finely annotated scenes, which can be freely combined into city-scale environments. In contrast to previous works mainly focusing on home, GRScenes covers 89 diverse scene categories, bridging the gap of service-oriented environments where general robots would be initially deployed. (b) GRResidents, a Large Language Model (LLM) driven Non-Player Character (NPC) system that is responsible for social interaction, task generation, and task assignment, thus simulating social scenarios for embodied AI applications. (c) The benchmark, GRBench, supports various robots but focuses on legged robots as primary agents and poses moderately challenging tasks involving Object Loco-Navigation, Social Loco-Navigation, and Loco-Manipulation. We hope that this work can alleviate the scarcity of high-quality data in this field and provide a more comprehensive assessment of Embodied AI research. The project is available at https://github.com/OpenRobotLab/GRUtopia.

## 参考
- http://arxiv.org/abs/2407.10943v1

## 개요
GRUtopia 프로젝트는 도시 규모의 시뮬레이션 환경을 구축하여, 실제 데이터 수집 비용이 높은 임베디드 AI 분야의 문제를 해결합니다. 해당 시나리오 데이터셋 GRScenes는 89가지의 다양한 카테고리를 포함하며, 기존의 가정 환경에만 초점을 맞춘 연구를 훨씬 능가하여, 범용 로봇 배치에 더욱 서비스 지향적인 테스트 환경을 제공합니다. 프로젝트는 또한 LLM 기반의 NPC 시스템인 GRResidents를 설계하여 사회적 상호작용과 작업 생성을 담당하며, 객체 위치 탐색, 사회적 위치 탐색, 위치 조작의 세 가지 유형의 작업을 포함하는 GRBench 벤치마크를 출시하여, 주로 보행 로봇의 종합 능력을 평가합니다.

## 핵심 내용
### 프로젝트 배경 및 목표
GRUtopia는 Sim2Real 패러다임을 통해 임베디드 모델 학습 비용을 낮추고, 실제 데이터 수집의 높은 비용 문제를 해결하는 것을 목표로 합니다. 프로젝트는 다양한 로봇을 위한 최초의 상호작용형 3D 사회 시뮬레이션 플랫폼을 구축했습니다.

### 핵심 구성 요소
- **GRScenes 데이터셋**: 10만 개의 정밀하게 주석이 달린 상호작용형 시나리오를 포함하며, 자유롭게 조합하여 도시 규모의 환경을 만들 수 있습니다. 기존의 가정 환경만 다룬 연구와 달리, GRScenes는 89가지 시나리오 카테고리를 포함하여 서비스 지향 환경의 공백을 메웁니다.
- **GRResidents NPC 시스템**: 대규모 언어 모델 기반으로 구동되며, 사회적 상호작용, 작업 생성 및 할당을 담당하여 임베디드 AI 응용 프로그램에 필요한 사회적 시나리오를 시뮬레이션합니다.
- **GRBench 벤치마크**: 다양한 로봇을 지원하지만, 주로 보행 로봇을 주요 에이전트로 사용합니다. 세 가지 중간 난이도의 작업을 포함합니다:
  - Object Loco-Navigation (객체 위치 탐색)
  - Social Loco-Navigation (사회적 위치 탐색)
  - Loco-Manipulation (위치 조작)

### 실험 설정 및 결론
프로젝트는 GRBench를 통해 도시 규모 환경에서 보행 로봇의 탐색 및 조작 능력을 종합적으로 평가합니다. 실험 결과, GRUtopia는 임베디드 AI 분야의 고품질 데이터 부족 문제를 효과적으로 완화하고, 연구에 더 포괄적인 평가 프레임워크를 제공할 수 있음을 보여줍니다. 프로젝트 코드는 GitHub에 오픈소스로 공개되어 있습니다.
