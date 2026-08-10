---
$id: ent_paper_omnidp_beyond_fov_large_worksp_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'OmniDP: Beyond-FOV Large-Workspace Humanoid Manipulation with Omnidirectional 3D Perception'
  zh: OmniDP｜具有全方位3D感知的超视场大工作空间人形操控
  ko: 'OmniDP: Beyond-FOV Large-Workspace Humanoid Manipulation with Omnidirectional 3D Perception'
summary:
  en: The deployment of humanoid robots for dexterous manipulation in unstructured environments remains challenging due to
    perceptual limitations that constrain the effective workspace. In scenarios where physical constraints prevent the robot
    from repositioning itself, maintaining omnidirectional awareness becomes far more critical than color or semantic information.While
    recent advances in visuomotor policy learning have improved manipulation capabilities, conventional RGB-D solutions suffer
    from narrow fields of view (FOV) and self-occlusion, requiring frequent base movements that introduce motion uncertainty
    and safety risks. Existing approaches to expanding perception, including active vision systems and third-view cameras,
    introduce mechanical complexity, calibration dependencies, and late
  zh: OmniDP 是一种由 LiDAR 驱动的端到端 3D 视觉运动策略，旨在解决人形机器人在大工作空间中的灵巧操作难题。该工作通过全景点云处理和时间感知注意力池化机制，实现了 360 度感知，无需频繁移动机器人基座。实验表明，OmniDP
    在仿真和真实环境中均优于依赖传统 RGB-D 相机的基线方法。
  ko: OmniDP 主要解决数据闭环：用相机图像/多视角观测、本体状态与关节序列、遥操作/外骨骼数据采集人类操作和机器人状态，再通过策略网络和控制模块转成可训练、可复用的可执行动作命令。关键点是把策略网络和控制模块放在同一条训练/部署链路里，减少高层目标到低层动作之间的断点。
domains:
- 07_ai_models_algorithms
- 06_design_engineering
layers:
- intelligence
- midstream
functional_roles:
- knowledge
- intelligence
tags:
- mobile_manipulation
- omnidp
- scene_understanding
- vision_guided_control
- visual_perception
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: low
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from Semantic Scholar search: OmniDP: Beyond-FOV Large-Workspace
    Humanoid Manipulation with Omnidirectional 3D Perception. [2026-07-29] zh content backfilled from English abstract via
    scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10: ko body retranslated from zh deep-read (842 chars,
    DeepSeek).'
sources:
- id: src_001
  type: website
  title: 'OmniDP: Beyond-FOV Large-Workspace Humanoid Manipulation with Omnidirectional 3D Perception'
  url: ''
  date: '2026'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---
## 概述
人形机器人在非结构化环境中进行灵巧操作时，常因感知限制而受限于有效工作空间。传统 RGB-D 方案视野狭窄且易自遮挡，迫使机器人频繁移动基座，引入运动不确定性和安全风险。OmniDP 提出了一种基于 LiDAR 的端到端 3D 视觉运动策略，通过全景点云和时间感知注意力池化机制，高效编码稀疏 3D 数据并捕捉时间依赖关系，实现 360 度感知。该方法使机器人能在不频繁重新定位的情况下，与大面积区域内的物体交互。此外，研究团队还开发了一套全身遥操作系统，用于高效收集全身体协调数据。大量实验证明，OmniDP 在大工作空间和杂乱场景中均表现出鲁棒性能。

## 核心内容
### 方法
- **核心架构**：OmniDP 采用端到端 LiDAR 驱动的 3D 视觉运动策略，直接处理全景点云数据。
- **时间感知注意力池化（Time-Aware Attention Pooling）**：该机制高效编码稀疏 3D 点云，同时捕捉时间序列中的依赖关系，使策略能理解动态环境变化。
- **360 度感知**：通过 LiDAR 获取的全景点云，机器人无需频繁移动基座即可感知周围环境，克服了传统 RGB-D 相机视野狭窄和自遮挡的问题。

### 实验设置
- **数据收集**：开发了一套全身遥操作系统，用于高效收集全身体协调操作数据，支持策略学习。
- **环境**：在仿真环境和真实世界场景中进行了广泛实验，包括大工作空间和杂乱场景。

### 关键结果
- **性能对比**：OmniDP 在多种任务中均优于依赖自我中心深度相机的基线方法，展现出更强的鲁棒性。
- **优势**：在大工作空间和杂乱场景中，OmniDP 的 360 度感知能力显著减少了机器人基座移动次数，降低了运动不确定性和安全风险。

### 结论
OmniDP 通过 LiDAR 驱动的全景感知和时间注意力机制，有效扩展了人形机器人的有效工作空间，为在非结构化环境中实现可靠操作提供了新方案。

## Overview
The deployment of humanoid robots for dexterous manipulation in unstructured environments remains challenging due to perceptual limitations that constrain the effective workspace. In scenarios where physical constraints prevent the robot from repositioning itself, maintaining omnidirectional awareness becomes far more critical than color or semantic information.While recent advances in visuomotor policy learning have improved manipulation capabilities, conventional RGB-D solutions suffer from narrow fields of view (FOV) and self-occlusion, requiring frequent base movements that introduce motion uncertainty and safety risks. Existing approaches to expanding perception, including active vision systems and third-view cameras, introduce mechanical complexity, calibration dependencies, and latency that hinder reliable real-time performance. In this work, We propose OmniDP, an end-to-end LiDAR-driven 3D visuomotor policy that enables robust manipulation in large workspaces. Our method processes panoramic point clouds through a Time-Aware Attention Pooling mechanism, efficiently encoding sparse 3D data while capturing temporal dependencies. This 360{\deg} perception allows the robot to interact with objects across wide areas without frequent repositioning. To support policy learning, we develop a whole-body teleoperation system for efficient data collection on full-body coordination. Extensive experiments in simulation and real-world environments show that OmniDP achieves robust performance in large-workspace and cluttered scenarios, outperforming baselines that rely on egocentric depth cameras.

## Overview
The deployment of humanoid robots for dexterous manipulation in unstructured environments remains challenging due to perceptual limitations that constrain the effective workspace. In scenarios where physical constraints prevent the robot from repositioning itself, maintaining omnidirectional awareness becomes far more critical than color or semantic information. While recent advances in visuomotor policy learning have improved manipulation capabilities, conventional RGB-D solutions suffer from narrow fields of view (FOV) and self-occlusion, requiring frequent base movements that introduce motion uncertainty and safety risks. Existing approaches to expanding perception, including active vision systems and third-view cameras, introduce mechanical complexity, calibration dependencies, and latency that hinder reliable real-time performance. In this work, we propose OmniDP, an end-to-end LiDAR-driven 3D visuomotor policy that enables robust manipulation in large workspaces. Our method processes panoramic point clouds through a Time-Aware Attention Pooling mechanism, efficiently encoding sparse 3D data while capturing temporal dependencies. This 360° perception allows the robot to interact with objects across wide areas without frequent repositioning. To support policy learning, we develop a whole-body teleoperation system for efficient data collection on full-body coordination. Extensive experiments in simulation and real-world environments show that OmniDP achieves robust performance in large-workspace and cluttered scenarios, outperforming baselines that rely on egocentric depth cameras.

## Content
The deployment of humanoid robots for dexterous manipulation in unstructured environments remains challenging due to perceptual limitations that constrain the effective workspace. In scenarios where physical constraints prevent the robot from repositioning itself, maintaining omnidirectional awareness becomes far more critical than color or semantic information. While recent advances in visuomotor policy learning have improved manipulation capabilities, conventional RGB-D solutions suffer from narrow fields of view (FOV) and self-occlusion, requiring frequent base movements that introduce motion uncertainty and safety risks. Existing approaches to expanding perception, including active vision systems and third-view cameras, introduce mechanical complexity, calibration dependencies, and latency that hinder reliable real-time performance. In this work, we propose OmniDP, an end-to-end LiDAR-driven 3D visuomotor policy that enables robust manipulation in large workspaces. Our method processes panoramic point clouds through a Time-Aware Attention Pooling mechanism, efficiently encoding sparse 3D data while capturing temporal dependencies. This 360° perception allows the robot to interact with objects across wide areas without frequent repositioning. To support policy learning, we develop a whole-body teleoperation system for efficient data collection on full-body coordination. Extensive experiments in simulation and real-world environments show that OmniDP achieves robust performance in large-workspace and cluttered scenarios, outperforming baselines that rely on egocentric depth cameras.

## 参考
- Semantic Scholar search: OmniDP: Beyond-FOV Large-Workspace Humanoid Manipulation with Omnidirectional 3D Perception

## 개요
휴머노이드 로봇이 비구조화 환경에서 정밀한 조작을 수행할 때, 종종 인식 제한으로 인해 유효 작업 공간이 제한됩니다. 기존 RGB-D 방식은 시야가 좁고 자체 가림이 발생하기 쉬워, 로봇이 잦은 베이스 이동을 해야 하며, 이는 운동 불확실성과 안전 위험을 초래합니다. OmniDP는 LiDAR 기반의 엔드투엔드 3D 시각 운동 정책을 제안하며, 전방위 포인트 클라우드와 시간 인식 어텐션 풀링 메커니즘을 통해 희소 3D 데이터를 효율적으로 인코딩하고 시간적 의존성을 포착하여 360도 인식을 구현합니다. 이 방법은 로봇이 빈번한 재배치 없이 넓은 영역의 객체와 상호작용할 수 있게 합니다. 또한, 연구팀은 전신 조정 데이터를 효율적으로 수집하기 위한 전신 원격 조작 시스템을 개발했습니다. 광범위한 실험을 통해 OmniDP는 넓은 작업 공간과 복잡한 환경에서 강건한 성능을 보임을 입증했습니다.

## 핵심 내용
### 방법
- **핵심 아키텍처**: OmniDP는 엔드투엔드 LiDAR 기반 3D 시각 운동 정책을 채택하여 전방위 포인트 클라우드 데이터를 직접 처리합니다.
- **시간 인식 어텐션 풀링(Time-Aware Attention Pooling)**: 이 메커니즘은 희소 3D 포인트 클라우드를 효율적으로 인코딩하면서 시간 시퀀스의 의존성을 포착하여, 정책이 동적 환경 변화를 이해할 수 있게 합니다.
- **360도 인식**: LiDAR로 획득한 전방위 포인트 클라우드를 통해 로봇은 빈번한 베이스 이동 없이 주변 환경을 인식할 수 있으며, 기존 RGB-D 카메라의 좁은 시야와 자체 가림 문제를 극복합니다.

### 실험 설정
- **데이터 수집**: 전신 원격 조작 시스템을 개발하여 전신 조정 조작 데이터를 효율적으로 수집하고 정책 학습을 지원합니다.
- **환경**: 시뮬레이션 환경과 실제 세계 시나리오에서 넓은 작업 공간과 복잡한 환경을 포함한 광범위한 실험을 수행했습니다.

### 주요 결과
- **성능 비교**: OmniDP는 다양한 작업에서 자아 중심 깊이 카메라에 의존하는 기준 방법보다 우수한 성능을 보이며, 더 강력한 견고성을 입증했습니다.
- **장점**: 넓은 작업 공간과 복잡한 환경에서 OmniDP의 360도 인식 능력은 로봇 베이스 이동 횟수를 크게 줄여 운동 불확실성과 안전 위험을 낮춥니다.

### 결론
OmniDP는 LiDAR 기반의 전방위 인식과 시간 어텐션 메커니즘을 통해 휴머노이드 로봇의 유효 작업 공간을 효과적으로 확장하며, 비구조화 환경에서 신뢰할 수 있는 조작을 위한 새로운 솔루션을 제공합니다.
