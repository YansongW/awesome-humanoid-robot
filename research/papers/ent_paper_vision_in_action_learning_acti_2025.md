---
$id: ent_paper_vision_in_action_learning_acti_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Vision in Action: Learning Active Perception from Human Demonstrations'
  zh: 'Vision in Action: Learning Active Perception from Human Demonstrations'
  ko: 'Vision in Action: Learning Active Perception from Human Demonstrations'
summary:
  en: 'Vision in Action: Learning Active Perception from Human Demonstrations is a 2025 work on manipulation for humanoid
    robots.'
  zh: Vision in Action (ViA) 是2025年提出的一种面向双臂机器人操作任务的主动感知系统。该系统通过人类演示学习任务相关的主动感知策略（如搜索、跟踪与聚焦），并采用6自由度机械颈实现类人头部运动。其核心贡献在于设计基于VR的遥操作界面，通过中间3D场景表示解决延迟导致的晕动症问题，最终在涉及视觉遮挡的多阶段双臂操作任务中显著超越基线系统。
  ko: 'Vision in Action: Learning Active Perception from Human Demonstrations is a 2025 work on manipulation for humanoid
    robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- manipulation
- vision_in_action
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2506.15666v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (861 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'Vision in Action: Learning Active Perception from Human Demonstrations (arXiv)'
  url: https://arxiv.org/abs/2506.15666
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
ViA系统通过人类演示直接学习主动感知策略，使机器人能像人类一样通过头部运动（搜索、跟踪、聚焦）辅助操作。硬件上采用6自由度机械颈实现灵活类人运动，软件层面则构建VR遥操作界面，通过共享观察空间捕捉人类感知策略。为解决机器人物理运动延迟引发的VR晕动症，系统引入中间3D场景表示，实现操作端实时视图渲染与机器人端异步场景更新。该设计在三个包含视觉遮挡的复杂多阶段双臂操作任务中，使视觉运动策略的鲁棒性显著优于基线方法。

## 核心内容
### 方法架构
ViA系统由三个核心组件构成：
- **主动感知策略学习**：通过人类演示数据直接学习任务相关的头部运动策略，包括搜索（searching）、跟踪（tracking）和聚焦（focusing）三类典型行为
- **硬件平台**：采用6自由度（6-DoF）机械颈，支持类人头部运动，为主动感知提供物理基础
- **VR遥操作界面**：构建人类操作员与机器人之间的共享观察空间，操作员通过VR设备控制机器人头部运动

### 关键技术突破
- **延迟缓解机制**：针对机器人物理运动延迟导致的VR晕动症，设计中间3D场景表示层。该层在操作员侧实现实时视图渲染，同时异步更新机器人最新观测数据，确保操作流畅性
- **共享观察空间**：通过VR界面将人类头部运动映射为机器人机械颈控制信号，使机器人能模仿人类在操作中的主动感知行为

### 实验设置与结果
- **任务场景**：三个包含视觉遮挡的复杂多阶段双臂操作任务
- **性能对比**：ViA系统在所有任务中均显著优于基线方法（baseline systems），具体表现为：
  - 在视觉遮挡条件下保持操作成功率
  - 多阶段任务衔接流畅度提升
  - 主动感知策略（如提前转头预判遮挡区域）的有效性验证

### 结论
ViA通过将人类主动感知策略直接迁移至机器人系统，证明了在复杂操作任务中，类人头部运动与VR遥操作结合的有效性。其延迟缓解机制为远程操作中的实时感知问题提供了可行解决方案。

## Overview
We present Vision in Action (ViA), an active perception system for bimanual robot manipulation. ViA learns task-relevant active perceptual strategies (e.g., searching, tracking, and focusing) directly from human demonstrations. On the hardware side, ViA employs a simple yet effective 6-DoF robotic neck to enable flexible, human-like head movements. To capture human active perception strategies, we design a VR-based teleoperation interface that creates a shared observation space between the robot and the human operator. To mitigate VR motion sickness caused by latency in the robot's physical movements, the interface uses an intermediate 3D scene representation, enabling real-time view rendering on the operator side while asynchronously updating the scene with the robot's latest observations. Together, these design elements enable the learning of robust visuomotor policies for three complex, multi-stage bimanual manipulation tasks involving visual occlusions, significantly outperforming baseline systems.

## 参考
- http://arxiv.org/abs/2506.15666v1

## 개요
ViA 시스템은 인간 시연을 통해 능동적 지각 전략을 직접 학습하여, 로봇이 인간처럼 머리 움직임(탐색, 추적, 초점)을 통해 조작을 보조할 수 있게 한다. 하드웨어는 6자유도 기계 목을 채택하여 유연한 인간형 움직임을 구현하고, 소프트웨어 측면에서는 VR 원격 조작 인터페이스를 구축하여 공유 관찰 공간을 통해 인간의 지각 전략을 포착한다. 로봇의 물리적 움직임 지연으로 인한 VR 멀미를 해결하기 위해, 시스템은 중간 3D 장면 표현을 도입하여 조작 측의 실시간 뷰 렌더링과 로봇 측의 비동기 장면 업데이트를 구현한다. 이 설계는 시각적 폐색을 포함한 세 가지 복잡한 다단계 양팔 조작 작업에서 시각 운동 정책의 견고성을 기준 방법보다 현저히 향상시켰다.

## 핵심 내용
### 방법 아키텍처
ViA 시스템은 세 가지 핵심 구성 요소로 이루어져 있다:
- **능동적 지각 전략 학습**: 인간 시연 데이터를 통해 작업 관련 머리 움직임 전략을 직접 학습하며, 탐색(searching), 추적(tracking), 초점(focusing)의 세 가지 전형적 행동을 포함한다.
- **하드웨어 플랫폼**: 6자유도(6-DoF) 기계 목을 채택하여 인간형 머리 움직임을 지원하며, 능동적 지각의 물리적 기반을 제공한다.
- **VR 원격 조작 인터페이스**: 인간 조작자와 로봇 간의 공유 관찰 공간을 구축하여, 조작자가 VR 장치를 통해 로봇의 머리 움직임을 제어한다.

### 핵심 기술 돌파
- **지연 완화 메커니즘**: 로봇의 물리적 움직임 지연으로 인한 VR 멀미를 해결하기 위해 중간 3D 장면 표현 계층을 설계한다. 이 계층은 조작자 측에서 실시간 뷰 렌더링을 구현하는 동시에 로봇의 최신 관측 데이터를 비동기적으로 업데이트하여 조작의 유연성을 보장한다.
- **공유 관찰 공간**: VR 인터페이스를 통해 인간의 머리 움직임을 로봇 기계 목 제어 신호로 매핑하여, 로봇이 조작 중 인간의 능동적 지각 행동을 모방할 수 있게 한다.

### 실험 설정 및 결과
- **작업 시나리오**: 시각적 폐색을 포함한 세 가지 복잡한 다단계 양팔 조작 작업.
- **성능 비교**: ViA 시스템은 모든 작업에서 기준 시스템(baseline systems)보다 현저히 우수했으며, 구체적으로는:
  - 시각적 폐색 조건에서도 조작 성공률 유지
  - 다단계 작업 전환의 유연성 향상
  - 능동적 지각 전략(예: 사전 고개 돌려 폐색 영역 예측)의 효과성 검증

### 결론
ViA는 인간의 능동적 지각 전략을 로봇 시스템에 직접 전이함으로써, 복잡한 조작 작업에서 인간형 머리 움직임과 VR 원격 조작의 결합 효과를 입증했다. 그 지연 완화 메커니즘은 원격 조작 중 실시간 지각 문제에 대한 실현 가능한 해결책을 제공한다.
