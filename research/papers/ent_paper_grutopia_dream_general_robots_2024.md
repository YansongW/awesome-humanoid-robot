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
  zh: 'GRUtopia: Dream General Robots in a City at Scale is a 2024 work on simulation benchmark for humanoid robots.'
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2407.10943v1.
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
Recent works have been exploring the scaling laws in the field of Embodied AI. Given the prohibitive costs of collecting real-world data, we believe the Simulation-to-Real (Sim2Real) paradigm is a crucial step for scaling the learning of embodied models. This paper introduces project GRUtopia, the first simulated interactive 3D society designed for various robots. It features several advancements: (a) The scene dataset, GRScenes, includes 100k interactive, finely annotated scenes, which can be freely combined into city-scale environments. In contrast to previous works mainly focusing on home, GRScenes covers 89 diverse scene categories, bridging the gap of service-oriented environments where general robots would be initially deployed. (b) GRResidents, a Large Language Model (LLM) driven Non-Player Character (NPC) system that is responsible for social interaction, task generation, and task assignment, thus simulating social scenarios for embodied AI applications. (c) The benchmark, GRBench, supports various robots but focuses on legged robots as primary agents and poses moderately challenging tasks involving Object Loco-Navigation, Social Loco-Navigation, and Loco-Manipulation. We hope that this work can alleviate the scarcity of high-quality data in this field and provide a more comprehensive assessment of Embodied AI research. The project is available at https://github.com/OpenRobotLab/GRUtopia.

## 核心内容
Recent works have been exploring the scaling laws in the field of Embodied AI. Given the prohibitive costs of collecting real-world data, we believe the Simulation-to-Real (Sim2Real) paradigm is a crucial step for scaling the learning of embodied models. This paper introduces project GRUtopia, the first simulated interactive 3D society designed for various robots. It features several advancements: (a) The scene dataset, GRScenes, includes 100k interactive, finely annotated scenes, which can be freely combined into city-scale environments. In contrast to previous works mainly focusing on home, GRScenes covers 89 diverse scene categories, bridging the gap of service-oriented environments where general robots would be initially deployed. (b) GRResidents, a Large Language Model (LLM) driven Non-Player Character (NPC) system that is responsible for social interaction, task generation, and task assignment, thus simulating social scenarios for embodied AI applications. (c) The benchmark, GRBench, supports various robots but focuses on legged robots as primary agents and poses moderately challenging tasks involving Object Loco-Navigation, Social Loco-Navigation, and Loco-Manipulation. We hope that this work can alleviate the scarcity of high-quality data in this field and provide a more comprehensive assessment of Embodied AI research. The project is available at https://github.com/OpenRobotLab/GRUtopia.

## 参考
- http://arxiv.org/abs/2407.10943v1

## Overview
Recent works have been exploring the scaling laws in the field of Embodied AI. Given the prohibitive costs of collecting real-world data, we believe the Simulation-to-Real (Sim2Real) paradigm is a crucial step for scaling the learning of embodied models. This paper introduces project GRUtopia, the first simulated interactive 3D society designed for various robots. It features several advancements: (a) The scene dataset, GRScenes, includes 100k interactive, finely annotated scenes, which can be freely combined into city-scale environments. In contrast to previous works mainly focusing on home, GRScenes covers 89 diverse scene categories, bridging the gap of service-oriented environments where general robots would be initially deployed. (b) GRResidents, a Large Language Model (LLM) driven Non-Player Character (NPC) system that is responsible for social interaction, task generation, and task assignment, thus simulating social scenarios for embodied AI applications. (c) The benchmark, GRBench, supports various robots but focuses on legged robots as primary agents and poses moderately challenging tasks involving Object Loco-Navigation, Social Loco-Navigation, and Loco-Manipulation. We hope that this work can alleviate the scarcity of high-quality data in this field and provide a more comprehensive assessment of Embodied AI research. The project is available at https://github.com/OpenRobotLab/GRUtopia.

## Content
Recent works have been exploring the scaling laws in the field of Embodied AI. Given the prohibitive costs of collecting real-world data, we believe the Simulation-to-Real (Sim2Real) paradigm is a crucial step for scaling the learning of embodied models. This paper introduces project GRUtopia, the first simulated interactive 3D society designed for various robots. It features several advancements: (a) The scene dataset, GRScenes, includes 100k interactive, finely annotated scenes, which can be freely combined into city-scale environments. In contrast to previous works mainly focusing on home, GRScenes covers 89 diverse scene categories, bridging the gap of service-oriented environments where general robots would be initially deployed. (b) GRResidents, a Large Language Model (LLM) driven Non-Player Character (NPC) system that is responsible for social interaction, task generation, and task assignment, thus simulating social scenarios for embodied AI applications. (c) The benchmark, GRBench, supports various robots but focuses on legged robots as primary agents and poses moderately challenging tasks involving Object Loco-Navigation, Social Loco-Navigation, and Loco-Manipulation. We hope that this work can alleviate the scarcity of high-quality data in this field and provide a more comprehensive assessment of Embodied AI research. The project is available at https://github.com/OpenRobotLab/GRUtopia.

## 개요
최근 연구들은 체화된 인공지능(Embodied AI) 분야에서 스케일링 법칙을 탐구하고 있습니다. 실제 세계 데이터 수집의 엄청난 비용을 고려할 때, 시뮬레이션-현실(Sim2Real) 패러다임은 체화된 모델의 학습을 확장하는 데 중요한 단계라고 믿습니다. 본 논문은 다양한 로봇을 위해 설계된 최초의 시뮬레이션된 상호작용형 3D 사회인 GRUtopia 프로젝트를 소개합니다. 이 프로젝트는 다음과 같은 여러 발전 사항을 특징으로 합니다: (a) 장면 데이터셋인 GRScenes는 10만 개의 상호작용 가능하고 정밀하게 주석이 달린 장면을 포함하며, 이를 자유롭게 결합하여 도시 규모의 환경을 만들 수 있습니다. 주로 가정에 초점을 맞춘 이전 연구들과 달리, GRScenes는 89개의 다양한 장면 범주를 다루어 일반 로봇이 초기에 배치될 서비스 지향 환경의 격차를 해소합니다. (b) GRResidents는 대규모 언어 모델(LLM) 기반의 비플레이어 캐릭터(NPC) 시스템으로, 사회적 상호작용, 작업 생성 및 작업 할당을 담당하여 체화된 AI 응용을 위한 사회적 시나리오를 시뮬레이션합니다. (c) 벤치마크인 GRBench는 다양한 로봇을 지원하지만, 주요 에이전트로 보행 로봇에 초점을 맞추며 객체 위치-내비게이션(Object Loco-Navigation), 사회적 위치-내비게이션(Social Loco-Navigation), 위치-조작(Loco-Manipulation)을 포함하는 중간 수준의 도전적인 작업을 제시합니다. 이 연구가 해당 분야의 고품질 데이터 부족을 완화하고 체화된 AI 연구에 대한 더 포괄적인 평가를 제공할 수 있기를 바랍니다. 프로젝트는 https://github.com/OpenRobotLab/GRUtopia에서 확인할 수 있습니다.

## 핵심 내용
최근 연구들은 체화된 인공지능(Embodied AI) 분야에서 스케일링 법칙을 탐구하고 있습니다. 실제 세계 데이터 수집의 엄청난 비용을 고려할 때, 시뮬레이션-현실(Sim2Real) 패러다임은 체화된 모델의 학습을 확장하는 데 중요한 단계라고 믿습니다. 본 논문은 다양한 로봇을 위해 설계된 최초의 시뮬레이션된 상호작용형 3D 사회인 GRUtopia 프로젝트를 소개합니다. 이 프로젝트는 다음과 같은 여러 발전 사항을 특징으로 합니다: (a) 장면 데이터셋인 GRScenes는 10만 개의 상호작용 가능하고 정밀하게 주석이 달린 장면을 포함하며, 이를 자유롭게 결합하여 도시 규모의 환경을 만들 수 있습니다. 주로 가정에 초점을 맞춘 이전 연구들과 달리, GRScenes는 89개의 다양한 장면 범주를 다루어 일반 로봇이 초기에 배치될 서비스 지향 환경의 격차를 해소합니다. (b) GRResidents는 대규모 언어 모델(LLM) 기반의 비플레이어 캐릭터(NPC) 시스템으로, 사회적 상호작용, 작업 생성 및 작업 할당을 담당하여 체화된 AI 응용을 위한 사회적 시나리오를 시뮬레이션합니다. (c) 벤치마크인 GRBench는 다양한 로봇을 지원하지만, 주요 에이전트로 보행 로봇에 초점을 맞추며 객체 위치-내비게이션(Object Loco-Navigation), 사회적 위치-내비게이션(Social Loco-Navigation), 위치-조작(Loco-Manipulation)을 포함하는 중간 수준의 도전적인 작업을 제시합니다. 이 연구가 해당 분야의 고품질 데이터 부족을 완화하고 체화된 AI 연구에 대한 더 포괄적인 평가를 제공할 수 있기를 바랍니다. 프로젝트는 https://github.com/OpenRobotLab/GRUtopia에서 확인할 수 있습니다.
