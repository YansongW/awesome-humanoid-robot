---
$id: ent_paper_lee_harness_engineering_for_physic_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Harness Engineering for Physical AI: Robot Middleware Is the Harness Layer'
  zh: 物理人工智能的Harness工程：机器人中间件即Harness层
  ko: 'Physical AI를 위한 Harness Engineering: Robot Middleware가 Harness Layer이다'
summary:
  en: The paper argues that robot middleware should serve as the harness layer for Physical AI, hosting three co-located enforcement
    mechanisms—Projection, Isolation, and Transfer—to bound learned-model outputs, inference budgets, and operating regimes
    across control, computing, and communication.
  zh: 该论文提出机器人中间件应作为物理人工智能的Harness层，通过 Projection、Isolation 和 Transfer 三种协同执行机制，在学习模型输出、推理预算和运行范围上同时对控制、计算和通信进行约束。
  ko: 본 논문은 로봇 미들웨어가 Physical AI를 위한 하네스 레이어로 작동해야 하며, Projection, Isolation, Transfer의 세 가지 공존하는 강제 메커니즘을 통해 제어·컴퓨팅·통신 전반에
    걸쳐 학습 모델의 출력, 추론 예산 및 운영 영역을 제한해야 한다고 주장한다.
domains:
- 08_software_middleware
- 07_ai_models_algorithms
- 05_mass_production
- 11_applications_markets
layers:
- intelligence
- midstream
- validation_markets
functional_roles:
- knowledge
- intelligence
- system
tags:
- ros2
- dds
- zenoh
- robot_middleware
- physical_ai
- harness_layer
- vla
- learned_policies
- safety_enforcement
- real_time
- timing_guarantees
- network_guarantees
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.09416v1.
sources:
- id: src_001
  type: paper
  title: 'Harness Engineering for Physical AI: Robot Middleware Is the Harness Layer'
  url: https://arxiv.org/abs/2606.09416
  date: '2026'
  accessed_at: '2026-07-01'
theoretical_depth:
- method
---
## 概述
Robot middleware faces a new role in the era of Physical AI. Learned policies, planners, and vision-language-action (VLA) models now enter deployed robots as causal participants on the control path, but the layer that integrates them with timing, scheduling, and network has not been named. Recent language-agent work names this layer the harness, the external system that mediates tools, manages state, bounds resources, and records execution. The robotics community has not yet adopted this framing, and we propose that robot middleware is that harness. A Physical AI harness differs from a software harness in where it intervenes. A software harness mediates at tool-call boundaries. A Physical AI harness must mediate at control, computing, and communication simultaneously, because a learned policy's output crosses all three: its commands shift the trajectory, its inference time shifts the schedule, and its payload shifts the bandwidth. Robot middleware is the lowest robot-stack layer with mediating abstractions over all three, so it is best positioned to compose their enforcement. It already provides most of what a harness needs but lacks the enforcement for an AI model. We name this missing enforcement as three functions: Projection gates each output at emission, Isolation bounds the model's execution and transmission slot, and Transfer falls back to a verified baseline when checks fail. Each appears today as hand-built application code in deployed robot systems, built on surfaces robot middleware already provides. Robot middleware should host them not as the best single-axis enforcer but as the layer that composes all three. We sketch this as a ROS 2 Harness Profile, a deployment artifact that carries an AI model's declared output region, inference budget, and operating regime while the middleware enforces them across ROS 2, DDS, and Zenoh.

## 核心内容
Robot middleware faces a new role in the era of Physical AI. Learned policies, planners, and vision-language-action (VLA) models now enter deployed robots as causal participants on the control path, but the layer that integrates them with timing, scheduling, and network has not been named. Recent language-agent work names this layer the harness, the external system that mediates tools, manages state, bounds resources, and records execution. The robotics community has not yet adopted this framing, and we propose that robot middleware is that harness. A Physical AI harness differs from a software harness in where it intervenes. A software harness mediates at tool-call boundaries. A Physical AI harness must mediate at control, computing, and communication simultaneously, because a learned policy's output crosses all three: its commands shift the trajectory, its inference time shifts the schedule, and its payload shifts the bandwidth. Robot middleware is the lowest robot-stack layer with mediating abstractions over all three, so it is best positioned to compose their enforcement. It already provides most of what a harness needs but lacks the enforcement for an AI model. We name this missing enforcement as three functions: Projection gates each output at emission, Isolation bounds the model's execution and transmission slot, and Transfer falls back to a verified baseline when checks fail. Each appears today as hand-built application code in deployed robot systems, built on surfaces robot middleware already provides. Robot middleware should host them not as the best single-axis enforcer but as the layer that composes all three. We sketch this as a ROS 2 Harness Profile, a deployment artifact that carries an AI model's declared output region, inference budget, and operating regime while the middleware enforces them across ROS 2, DDS, and Zenoh.

## 参考
- http://arxiv.org/abs/2606.09416v1

## Overview
Robot middleware faces a new role in the era of Physical AI. Learned policies, planners, and vision-language-action (VLA) models now enter deployed robots as causal participants on the control path, but the layer that integrates them with timing, scheduling, and network has not been named. Recent language-agent work names this layer the harness, the external system that mediates tools, manages state, bounds resources, and records execution. The robotics community has not yet adopted this framing, and we propose that robot middleware is that harness. A Physical AI harness differs from a software harness in where it intervenes. A software harness mediates at tool-call boundaries. A Physical AI harness must mediate at control, computing, and communication simultaneously, because a learned policy's output crosses all three: its commands shift the trajectory, its inference time shifts the schedule, and its payload shifts the bandwidth. Robot middleware is the lowest robot-stack layer with mediating abstractions over all three, so it is best positioned to compose their enforcement. It already provides most of what a harness needs but lacks the enforcement for an AI model. We name this missing enforcement as three functions: Projection gates each output at emission, Isolation bounds the model's execution and transmission slot, and Transfer falls back to a verified baseline when checks fail. Each appears today as hand-built application code in deployed robot systems, built on surfaces robot middleware already provides. Robot middleware should host them not as the best single-axis enforcer but as the layer that composes all three. We sketch this as a ROS 2 Harness Profile, a deployment artifact that carries an AI model's declared output region, inference budget, and operating regime while the middleware enforces them across ROS 2, DDS, and Zenoh.

## Content
Robot middleware faces a new role in the era of Physical AI. Learned policies, planners, and vision-language-action (VLA) models now enter deployed robots as causal participants on the control path, but the layer that integrates them with timing, scheduling, and network has not been named. Recent language-agent work names this layer the harness, the external system that mediates tools, manages state, bounds resources, and records execution. The robotics community has not yet adopted this framing, and we propose that robot middleware is that harness. A Physical AI harness differs from a software harness in where it intervenes. A software harness mediates at tool-call boundaries. A Physical AI harness must mediate at control, computing, and communication simultaneously, because a learned policy's output crosses all three: its commands shift the trajectory, its inference time shifts the schedule, and its payload shifts the bandwidth. Robot middleware is the lowest robot-stack layer with mediating abstractions over all three, so it is best positioned to compose their enforcement. It already provides most of what a harness needs but lacks the enforcement for an AI model. We name this missing enforcement as three functions: Projection gates each output at emission, Isolation bounds the model's execution and transmission slot, and Transfer falls back to a verified baseline when checks fail. Each appears today as hand-built application code in deployed robot systems, built on surfaces robot middleware already provides. Robot middleware should host them not as the best single-axis enforcer but as the layer that composes all three. We sketch this as a ROS 2 Harness Profile, a deployment artifact that carries an AI model's declared output region, inference budget, and operating regime while the middleware enforces them across ROS 2, DDS, and Zenoh.

## 개요
로봇 미들웨어는 물리적 AI 시대에 새로운 역할을 마주하고 있습니다. 학습된 정책, 플래너, 비전-언어-행동(VLA) 모델이 이제 배치된 로봇에 제어 경로 상의 인과적 참여자로 진입하지만, 이들을 타이밍, 스케줄링, 네트워크와 통합하는 계층은 아직 명명되지 않았습니다. 최근 언어 에이전트 연구는 이 계층을 하네스(harness)라고 명명하며, 이는 도구를 중재하고, 상태를 관리하며, 자원을 제한하고, 실행을 기록하는 외부 시스템입니다. 로봇 공학 커뮤니티는 아직 이 프레임워크를 채택하지 않았으며, 우리는 로봇 미들웨어가 바로 그 하네스라고 제안합니다. 물리적 AI 하네스는 개입하는 지점에서 소프트웨어 하네스와 다릅니다. 소프트웨어 하네스는 도구 호출 경계에서 중재합니다. 물리적 AI 하네스는 제어, 컴퓨팅, 통신을 동시에 중재해야 합니다. 학습된 정책의 출력이 이 세 가지를 모두 넘나들기 때문입니다. 명령은 궤적을 변경하고, 추론 시간은 스케줄을 변경하며, 페이로드는 대역폭을 변경합니다. 로봇 미들웨어는 이 세 가지 모두에 대한 중재 추상화를 제공하는 가장 낮은 로봇 스택 계층이므로, 이들의 집행을 구성하기에 가장 적합한 위치에 있습니다. 이미 하네스에 필요한 대부분을 제공하지만 AI 모델에 대한 집행 기능이 부족합니다. 우리는 이 누락된 집행 기능을 세 가지로 명명합니다: 투영(Projection)은 각 출력을 방출 시 게이트하고, 격리(Isolation)는 모델의 실행 및 전송 슬롯을 제한하며, 전환(Transfer)은 검사 실패 시 검증된 기준선으로 대체합니다. 각각은 현재 배치된 로봇 시스템에서 수작업으로 구축된 애플리케이션 코드로 나타나며, 로봇 미들웨어가 이미 제공하는 표면 위에 구축됩니다. 로봇 미들웨어는 이들을 최고의 단일 축 집행자로 호스팅하는 것이 아니라, 세 가지를 모두 구성하는 계층으로 호스팅해야 합니다. 우리는 이를 ROS 2 하네스 프로필(ROS 2 Harness Profile)로 스케치하며, 이는 AI 모델의 선언된 출력 영역, 추론 예산, 운영 체제를 전달하는 배치 아티팩트로, 미들웨어가 ROS 2, DDS, Zenoh 전반에서 이를 집행합니다.

## 핵심 내용
로봇 미들웨어는 물리적 AI 시대에 새로운 역할을 마주하고 있습니다. 학습된 정책, 플래너, 비전-언어-행동(VLA) 모델이 이제 배치된 로봇에 제어 경로 상의 인과적 참여자로 진입하지만, 이들을 타이밍, 스케줄링, 네트워크와 통합하는 계층은 아직 명명되지 않았습니다. 최근 언어 에이전트 연구는 이 계층을 하네스(harness)라고 명명하며, 이는 도구를 중재하고, 상태를 관리하며, 자원을 제한하고, 실행을 기록하는 외부 시스템입니다. 로봇 공학 커뮤니티는 아직 이 프레임워크를 채택하지 않았으며, 우리는 로봇 미들웨어가 바로 그 하네스라고 제안합니다. 물리적 AI 하네스는 개입하는 지점에서 소프트웨어 하네스와 다릅니다. 소프트웨어 하네스는 도구 호출 경계에서 중재합니다. 물리적 AI 하네스는 제어, 컴퓨팅, 통신을 동시에 중재해야 합니다. 학습된 정책의 출력이 이 세 가지를 모두 넘나들기 때문입니다. 명령은 궤적을 변경하고, 추론 시간은 스케줄을 변경하며, 페이로드는 대역폭을 변경합니다. 로봇 미들웨어는 이 세 가지 모두에 대한 중재 추상화를 제공하는 가장 낮은 로봇 스택 계층이므로, 이들의 집행을 구성하기에 가장 적합한 위치에 있습니다. 이미 하네스에 필요한 대부분을 제공하지만 AI 모델에 대한 집행 기능이 부족합니다. 우리는 이 누락된 집행 기능을 세 가지로 명명합니다: 투영(Projection)은 각 출력을 방출 시 게이트하고, 격리(Isolation)는 모델의 실행 및 전송 슬롯을 제한하며, 전환(Transfer)은 검사 실패 시 검증된 기준선으로 대체합니다. 각각은 현재 배치된 로봇 시스템에서 수작업으로 구축된 애플리케이션 코드로 나타나며, 로봇 미들웨어가 이미 제공하는 표면 위에 구축됩니다. 로봇 미들웨어는 이들을 최고의 단일 축 집행자로 호스팅하는 것이 아니라, 세 가지를 모두 구성하는 계층으로 호스팅해야 합니다. 우리는 이를 ROS 2 하네스 프로필(ROS 2 Harness Profile)로 스케치하며, 이는 AI 모델의 선언된 출력 영역, 추론 예산, 운영 체제를 전달하는 배치 아티팩트로, 미들웨어가 ROS 2, DDS, Zenoh 전반에서 이를 집행합니다.
