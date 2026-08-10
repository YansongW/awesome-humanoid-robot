---
$id: ent_paper_kimera_an_open_source_library_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Kimera: an Open-Source Library for Real-Time Metric-Semantic Localization and Mapping'
  zh: 'Kimera: an Open-Source Library for Real-Time Metric-Semantic Localization and Mapping'
  ko: 'Kimera: an Open-Source Library for Real-Time Metric-Semantic Localization and Mapping'
summary:
  en: 'Kimera: an Open-Source Library for Real-Time Metric-Semantic Localization and Mapping is a 2026 work on state estimation
    for humanoid robots.'
  zh: Kimera 是一个开源的 C++ 库，用于实时度量-语义视觉惯性同步定位与地图构建（SLAM）。该库由研究团队开发，核心贡献在于将 3D 网格重建与语义标注集成到 SLAM 系统中，超越了现有视觉 SLAM 库（如 ORB-SLAM、VINS-Mono）。关键参数包括在
    CPU 上实时运行，并支持模块化设计，可独立或组合使用四个核心组件。
  ko: 'Kimera: an Open-Source Library for Real-Time Metric-Semantic Localization and Mapping is a 2026 work on state estimation
    for humanoid robots.'
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
- kimera
- slam
- state_estimation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1910.02490v3. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (758 chars, DeepSeek).'
sources:
- id: src_001
  type: website
  title: 'Kimera: an Open-Source Library for Real-Time Metric-Semantic Localization and Mapping project page'
  url: https://github.com/MIT-SPARK/Kimera
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Kimera 是一个面向人形机器人状态估计的开源库，专注于实时度量-语义 SLAM。它通过四个模块实现功能：视觉惯性里程计（VIO）提供快速状态估计、鲁棒位姿图优化器用于全局轨迹估计、轻量级 3D 网格器实现快速网格重建，以及密集 3D 度量-语义重建模块。这些模块可独立运行或组合使用，使 Kimera 能灵活退化为纯 VIO 系统或完整 SLAM 系统。该库在 CPU 上实时运行，利用现代深度学习方法从语义标注图像生成 3D 度量-语义网格。

## 核心内容
### 方法
Kimera 采用模块化架构，包含四个核心组件：
- **视觉惯性里程计（VIO）模块**：基于 IMU 和视觉数据，实现快速且准确的状态估计。
- **鲁棒位姿图优化器**：用于全局轨迹估计，提升长期定位的稳定性。
- **轻量级 3D 网格器**：快速重建 3D 网格，支持实时处理。
- **密集 3D 度量-语义重建模块**：结合语义标签，生成带有语义信息的 3D 网格。

### 实验设置
- 运行环境：仅依赖 CPU，无需 GPU 加速。
- 输入数据：来自现代深度学习方法的语义标注图像。
- 对比基准：与 ORB-SLAM、VINS-Mono、OKVIS、ROVIO 等现有库进行性能比较。

### 关键数字
- 实时性：在 CPU 上实现实时运行，无需专用硬件。
- 模块化：四个组件可独立或组合使用，支持灵活配置。
- 输出：生成 3D 度量-语义网格，包含几何与语义信息。

### 结论
Kimera 通过开源库形式，为度量-语义 SLAM 和感知研究提供了灵活、高效且鲁棒的解决方案。其模块化设计允许研究人员在 VIO、SLAM、3D 重建和分割等领域快速原型化与基准测试，无需从零开始开发。

## Overview
We provide an open-source C++ library for real-time metric-semantic visual-inertial Simultaneous Localization And Mapping (SLAM). The library goes beyond existing visual and visual-inertial SLAM libraries (e.g., ORB-SLAM, VINS- Mono, OKVIS, ROVIO) by enabling mesh reconstruction and semantic labeling in 3D. Kimera is designed with modularity in mind and has four key components: a visual-inertial odometry (VIO) module for fast and accurate state estimation, a robust pose graph optimizer for global trajectory estimation, a lightweight 3D mesher module for fast mesh reconstruction, and a dense 3D metric-semantic reconstruction module. The modules can be run in isolation or in combination, hence Kimera can easily fall back to a state-of-the-art VIO or a full SLAM system. Kimera runs in real-time on a CPU and produces a 3D metric-semantic mesh from semantically labeled images, which can be obtained by modern deep learning methods. We hope that the flexibility, computational efficiency, robustness, and accuracy afforded by Kimera will build a solid basis for future metric-semantic SLAM and perception research, and will allow researchers across multiple areas (e.g., VIO, SLAM, 3D reconstruction, segmentation) to benchmark and prototype their own efforts without having to start from scratch.

## Overview
We provide an open-source C++ library for real-time metric-semantic visual-inertial Simultaneous Localization And Mapping (SLAM). The library goes beyond existing visual and visual-inertial SLAM libraries (e.g., ORB-SLAM, VINS-Mono, OKVIS, ROVIO) by enabling mesh reconstruction and semantic labeling in 3D. Kimera is designed with modularity in mind and has four key components: a visual-inertial odometry (VIO) module for fast and accurate state estimation, a robust pose graph optimizer for global trajectory estimation, a lightweight 3D mesher module for fast mesh reconstruction, and a dense 3D metric-semantic reconstruction module. The modules can be run in isolation or in combination, hence Kimera can easily fall back to a state-of-the-art VIO or a full SLAM system. Kimera runs in real-time on a CPU and produces a 3D metric-semantic mesh from semantically labeled images, which can be obtained by modern deep learning methods. We hope that the flexibility, computational efficiency, robustness, and accuracy afforded by Kimera will build a solid basis for future metric-semantic SLAM and perception research, and will allow researchers across multiple areas (e.g., VIO, SLAM, 3D reconstruction, segmentation) to benchmark and prototype their own efforts without having to start from scratch.

## Content
We provide an open-source C++ library for real-time metric-semantic visual-inertial Simultaneous Localization And Mapping (SLAM). The library goes beyond existing visual and visual-inertial SLAM libraries (e.g., ORB-SLAM, VINS-Mono, OKVIS, ROVIO) by enabling mesh reconstruction and semantic labeling in 3D. Kimera is designed with modularity in mind and has four key components: a visual-inertial odometry (VIO) module for fast and accurate state estimation, a robust pose graph optimizer for global trajectory estimation, a lightweight 3D mesher module for fast mesh reconstruction, and a dense 3D metric-semantic reconstruction module. The modules can be run in isolation or in combination, hence Kimera can easily fall back to a state-of-the-art VIO or a full SLAM system. Kimera runs in real-time on a CPU and produces a 3D metric-semantic mesh from semantically labeled images, which can be obtained by modern deep learning methods. We hope that the flexibility, computational efficiency, robustness, and accuracy afforded by Kimera will build a solid basis for future metric-semantic SLAM and perception research, and will allow researchers across multiple areas (e.g., VIO, SLAM, 3D reconstruction, segmentation) to benchmark and prototype their own efforts without having to start from scratch.

## 参考
- http://arxiv.org/abs/1910.02490v3

## 개요
Kimera는 휴머노이드 로봇 상태 추정을 위한 오픈소스 라이브러리로, 실시간 메트릭-시맨틱 SLAM에 중점을 둡니다. 네 가지 모듈을 통해 기능을 구현합니다: 시각-관성 주행계(VIO)는 빠른 상태 추정을 제공하고, 강건한 포즈 그래프 최적화기는 전역 궤적 추정을 담당하며, 경량 3D 메셔는 빠른 메시 재구성을 가능하게 하고, 밀집 3D 메트릭-시맨틱 재구성 모듈이 포함됩니다. 이러한 모듈은 독립적으로 실행되거나 결합되어 사용될 수 있어, Kimera는 순수 VIO 시스템 또는 완전한 SLAM 시스템으로 유연하게 축소될 수 있습니다. 이 라이브러리는 CPU에서 실시간으로 실행되며, 현대 딥러닝 방법을 활용하여 시맨틱 주석 이미지에서 3D 메트릭-시맨틱 메시를 생성합니다.

## 핵심 내용
### 방법
Kimera는 모듈형 아키텍처를 채택하며, 네 가지 핵심 구성 요소를 포함합니다:
- **시각-관성 주행계(VIO) 모듈**: IMU와 시각 데이터를 기반으로 빠르고 정확한 상태 추정을 구현합니다.
- **강건한 포즈 그래프 최적화기**: 전역 궤적 추정에 사용되어 장기 위치 추정의 안정성을 향상시킵니다.
- **경량 3D 메셔**: 3D 메시를 빠르게 재구성하여 실시간 처리를 지원합니다.
- **밀집 3D 메트릭-시맨틱 재구성 모듈**: 시맨틱 레이블을 결합하여 의미 정보가 포함된 3D 메시를 생성합니다.

### 실험 설정
- 실행 환경: CPU에만 의존하며 GPU 가속이 필요 없습니다.
- 입력 데이터: 현대 딥러닝 방법에서 생성된 시맨틱 주석 이미지.
- 비교 기준: ORB-SLAM, VINS-Mono, OKVIS, ROVIO 등 기존 라이브러리와 성능을 비교합니다.

### 주요 수치
- 실시간성: CPU에서 실시간 실행을 구현하며 전용 하드웨어가 필요 없습니다.
- 모듈성: 네 가지 구성 요소를 독립적으로 또는 결합하여 사용할 수 있어 유연한 구성을 지원합니다.
- 출력: 기하학적 및 시맨틱 정보를 포함한 3D 메트릭-시맨틱 메시를 생성합니다.

### 결론
Kimera는 오픈소스 라이브러리 형태로 메트릭-시맨틱 SLAM 및 인식 연구에 유연하고 효율적이며 강건한 솔루션을 제공합니다. 모듈형 설계 덕분에 연구자들은 VIO, SLAM, 3D 재구성 및 분할 분야에서 처음부터 개발하지 않고도 빠르게 프로토타이핑하고 벤치마킹할 수 있습니다.
