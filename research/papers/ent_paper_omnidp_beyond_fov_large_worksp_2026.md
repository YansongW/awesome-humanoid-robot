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
  zh: OmniDP 主要解决数据闭环：用相机图像/多视角观测、本体状态与关节序列、遥操作/外骨骼数据采集人类操作和机器人状态，再通过策略网络和控制模块转成可训练、可复用的可执行动作命令。关键点是把策略网络和控制模块放在同一条训练/部署链路里，减少高层目标到低层动作之间的断点。
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
    Humanoid Manipulation with Omnidirectional 3D Perception.'
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
The deployment of humanoid robots for dexterous manipulation in unstructured environments remains challenging due to perceptual limitations that constrain the effective workspace. In scenarios where physical constraints prevent the robot from repositioning itself, maintaining omnidirectional awareness becomes far more critical than color or semantic information.While recent advances in visuomotor policy learning have improved manipulation capabilities, conventional RGB-D solutions suffer from narrow fields of view (FOV) and self-occlusion, requiring frequent base movements that introduce motion uncertainty and safety risks. Existing approaches to expanding perception, including active vision systems and third-view cameras, introduce mechanical complexity, calibration dependencies, and latency that hinder reliable real-time performance. In this work, We propose OmniDP, an end-to-end LiDAR-driven 3D visuomotor policy that enables robust manipulation in large workspaces. Our method processes panoramic point clouds through a Time-Aware Attention Pooling mechanism, efficiently encoding sparse 3D data while capturing temporal dependencies. This 360{\deg} perception allows the robot to interact with objects across wide areas without frequent repositioning. To support policy learning, we develop a whole-body teleoperation system for efficient data collection on full-body coordination. Extensive experiments in simulation and real-world environments show that OmniDP achieves robust performance in large-workspace and cluttered scenarios, outperforming baselines that rely on egocentric depth cameras.

## 核心内容
The deployment of humanoid robots for dexterous manipulation in unstructured environments remains challenging due to perceptual limitations that constrain the effective workspace. In scenarios where physical constraints prevent the robot from repositioning itself, maintaining omnidirectional awareness becomes far more critical than color or semantic information.While recent advances in visuomotor policy learning have improved manipulation capabilities, conventional RGB-D solutions suffer from narrow fields of view (FOV) and self-occlusion, requiring frequent base movements that introduce motion uncertainty and safety risks. Existing approaches to expanding perception, including active vision systems and third-view cameras, introduce mechanical complexity, calibration dependencies, and latency that hinder reliable real-time performance. In this work, We propose OmniDP, an end-to-end LiDAR-driven 3D visuomotor policy that enables robust manipulation in large workspaces. Our method processes panoramic point clouds through a Time-Aware Attention Pooling mechanism, efficiently encoding sparse 3D data while capturing temporal dependencies. This 360{\deg} perception allows the robot to interact with objects across wide areas without frequent repositioning. To support policy learning, we develop a whole-body teleoperation system for efficient data collection on full-body coordination. Extensive experiments in simulation and real-world environments show that OmniDP achieves robust performance in large-workspace and cluttered scenarios, outperforming baselines that rely on egocentric depth cameras.

## 参考
- Semantic Scholar search: OmniDP: Beyond-FOV Large-Workspace Humanoid Manipulation with Omnidirectional 3D Perception

## Overview
The deployment of humanoid robots for dexterous manipulation in unstructured environments remains challenging due to perceptual limitations that constrain the effective workspace. In scenarios where physical constraints prevent the robot from repositioning itself, maintaining omnidirectional awareness becomes far more critical than color or semantic information. While recent advances in visuomotor policy learning have improved manipulation capabilities, conventional RGB-D solutions suffer from narrow fields of view (FOV) and self-occlusion, requiring frequent base movements that introduce motion uncertainty and safety risks. Existing approaches to expanding perception, including active vision systems and third-view cameras, introduce mechanical complexity, calibration dependencies, and latency that hinder reliable real-time performance. In this work, we propose OmniDP, an end-to-end LiDAR-driven 3D visuomotor policy that enables robust manipulation in large workspaces. Our method processes panoramic point clouds through a Time-Aware Attention Pooling mechanism, efficiently encoding sparse 3D data while capturing temporal dependencies. This 360° perception allows the robot to interact with objects across wide areas without frequent repositioning. To support policy learning, we develop a whole-body teleoperation system for efficient data collection on full-body coordination. Extensive experiments in simulation and real-world environments show that OmniDP achieves robust performance in large-workspace and cluttered scenarios, outperforming baselines that rely on egocentric depth cameras.

## Content
The deployment of humanoid robots for dexterous manipulation in unstructured environments remains challenging due to perceptual limitations that constrain the effective workspace. In scenarios where physical constraints prevent the robot from repositioning itself, maintaining omnidirectional awareness becomes far more critical than color or semantic information. While recent advances in visuomotor policy learning have improved manipulation capabilities, conventional RGB-D solutions suffer from narrow fields of view (FOV) and self-occlusion, requiring frequent base movements that introduce motion uncertainty and safety risks. Existing approaches to expanding perception, including active vision systems and third-view cameras, introduce mechanical complexity, calibration dependencies, and latency that hinder reliable real-time performance. In this work, we propose OmniDP, an end-to-end LiDAR-driven 3D visuomotor policy that enables robust manipulation in large workspaces. Our method processes panoramic point clouds through a Time-Aware Attention Pooling mechanism, efficiently encoding sparse 3D data while capturing temporal dependencies. This 360° perception allows the robot to interact with objects across wide areas without frequent repositioning. To support policy learning, we develop a whole-body teleoperation system for efficient data collection on full-body coordination. Extensive experiments in simulation and real-world environments show that OmniDP achieves robust performance in large-workspace and cluttered scenarios, outperforming baselines that rely on egocentric depth cameras.

## 개요
인간형 로봇의 비정형 환경에서의 정밀 조작 배치는 여전히 효과적인 작업 공간을 제한하는 인지적 한계로 인해 어려움을 겪고 있습니다. 물리적 제약으로 인해 로봇이 스스로 위치를 재조정할 수 없는 시나리오에서는 전방향 인식이 색상이나 의미 정보보다 훨씬 더 중요해집니다. 최근 시각-운동 정책 학습의 발전이 조작 능력을 향상시켰지만, 기존의 RGB-D 솔루션은 좁은 시야(FOV)와 자체 폐색으로 인해 잦은 베이스 이동이 필요하며, 이는 움직임 불확실성과 안전 위험을 초래합니다. 능동 시각 시스템 및 제3자 시점 카메라를 포함한 기존의 인식 확장 접근 방식은 기계적 복잡성, 캘리브레이션 의존성 및 지연 시간을 도입하여 신뢰할 수 있는 실시간 성능을 저해합니다. 본 연구에서는 대규모 작업 공간에서 강력한 조작을 가능하게 하는 엔드-투-엔드 LiDAR 기반 3D 시각-운동 정책인 OmniDP를 제안합니다. 우리의 방법은 시간 인식 어텐션 풀링(Time-Aware Attention Pooling) 메커니즘을 통해 파노라마 포인트 클라우드를 처리하여 시간적 종속성을 포착하면서 희소 3D 데이터를 효율적으로 인코딩합니다. 이 360° 인식을 통해 로봇은 잦은 위치 재조정 없이 넓은 영역에 걸쳐 객체와 상호작용할 수 있습니다. 정책 학습을 지원하기 위해 전신 협업에 대한 효율적인 데이터 수집을 위한 전신 원격 조작 시스템을 개발합니다. 시뮬레이션 및 실제 환경에서의 광범위한 실험을 통해 OmniDP가 대규모 작업 공간 및 혼잡한 시나리오에서 강력한 성능을 달성하며, 자아 중심 깊이 카메라에 의존하는 기준 모델을 능가함을 보여줍니다.

## 핵심 내용
인간형 로봇의 비정형 환경에서의 정밀 조작 배치는 여전히 효과적인 작업 공간을 제한하는 인지적 한계로 인해 어려움을 겪고 있습니다. 물리적 제약으로 인해 로봇이 스스로 위치를 재조정할 수 없는 시나리오에서는 전방향 인식이 색상이나 의미 정보보다 훨씬 더 중요해집니다. 최근 시각-운동 정책 학습의 발전이 조작 능력을 향상시켰지만, 기존의 RGB-D 솔루션은 좁은 시야(FOV)와 자체 폐색으로 인해 잦은 베이스 이동이 필요하며, 이는 움직임 불확실성과 안전 위험을 초래합니다. 능동 시각 시스템 및 제3자 시점 카메라를 포함한 기존의 인식 확장 접근 방식은 기계적 복잡성, 캘리브레이션 의존성 및 지연 시간을 도입하여 신뢰할 수 있는 실시간 성능을 저해합니다. 본 연구에서는 대규모 작업 공간에서 강력한 조작을 가능하게 하는 엔드-투-엔드 LiDAR 기반 3D 시각-운동 정책인 OmniDP를 제안합니다. 우리의 방법은 시간 인식 어텐션 풀링(Time-Aware Attention Pooling) 메커니즘을 통해 파노라마 포인트 클라우드를 처리하여 시간적 종속성을 포착하면서 희소 3D 데이터를 효율적으로 인코딩합니다. 이 360° 인식을 통해 로봇은 잦은 위치 재조정 없이 넓은 영역에 걸쳐 객체와 상호작용할 수 있습니다. 정책 학습을 지원하기 위해 전신 협업에 대한 효율적인 데이터 수집을 위한 전신 원격 조작 시스템을 개발합니다. 시뮬레이션 및 실제 환경에서의 광범위한 실험을 통해 OmniDP가 대규모 작업 공간 및 혼잡한 시나리오에서 강력한 성능을 달성하며, 자아 중심 깊이 카메라에 의존하는 기준 모델을 능가함을 보여줍니다.
