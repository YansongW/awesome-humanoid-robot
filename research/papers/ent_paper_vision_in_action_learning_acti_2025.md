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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2506.15666v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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

## 개요
우리는 양팔 로봇 조작을 위한 능동 지각 시스템인 Vision in Action (ViA)을 제시합니다. ViA는 인간 시연으로부터 작업 관련 능동 지각 전략(예: 탐색, 추적, 집중)을 직접 학습합니다. 하드웨어 측면에서 ViA는 간단하면서도 효과적인 6자유도 로봇 목을 사용하여 유연하고 인간과 유사한 머리 움직임을 가능하게 합니다. 인간의 능동 지각 전략을 포착하기 위해, 우리는 로봇과 인간 조작자 간의 공유 관찰 공간을 생성하는 VR 기반 원격 조작 인터페이스를 설계했습니다. 로봇의 물리적 움직임 지연으로 인한 VR 멀미를 완화하기 위해, 인터페이스는 중간 3D 장면 표현을 사용하여 조작자 측에서 실시간 뷰 렌더링을 가능하게 하면서 비동기적으로 로봇의 최신 관찰로 장면을 업데이트합니다. 이러한 설계 요소들은 함께 시각적 폐색을 포함하는 세 가지 복잡한 다단계 양팔 조작 작업에 대해 강력한 시각-운동 정책 학습을 가능하게 하며, 기준 시스템을 크게 능가합니다.

## 핵심 내용
우리는 양팔 로봇 조작을 위한 능동 지각 시스템인 Vision in Action (ViA)을 제시합니다. ViA는 인간 시연으로부터 작업 관련 능동 지각 전략(예: 탐색, 추적, 집중)을 직접 학습합니다. 하드웨어 측면에서 ViA는 간단하면서도 효과적인 6자유도 로봇 목을 사용하여 유연하고 인간과 유사한 머리 움직임을 가능하게 합니다. 인간의 능동 지각 전략을 포착하기 위해, 우리는 로봇과 인간 조작자 간의 공유 관찰 공간을 생성하는 VR 기반 원격 조작 인터페이스를 설계했습니다. 로봇의 물리적 움직임 지연으로 인한 VR 멀미를 완화하기 위해, 인터페이스는 중간 3D 장면 표현을 사용하여 조작자 측에서 실시간 뷰 렌더링을 가능하게 하면서 비동기적으로 로봇의 최신 관찰로 장면을 업데이트합니다. 이러한 설계 요소들은 함께 시각적 폐색을 포함하는 세 가지 복잡한 다단계 양팔 조작 작업에 대해 강력한 시각-운동 정책 학습을 가능하게 하며, 기준 시스템을 크게 능가합니다.

## 参考
- http://arxiv.org/abs/2506.15666v1
